#!/usr/bin/env python3
"""Scan UI code for line-level tells: places a reviewer or a developer should look at.

Each hit names the rule it points to. A hit is a tell, not a verdict: the rule's Check
decides (a hex inside a token file is correct, an outline removed next to a :focus-visible
style is fine). Use it on a diff or a component folder before a review, or in build mode
before handing over (method/build-method.md §6, Code).

    python3 scripts/ui_tells.py src/components
    git diff --name-only main | python3 scripts/ui_tells.py --stdin
    python3 scripts/ui_tells.py src --format md > tells.md

Standard library only. Exit code 0 always: tells never fail a build on their own.
"""
import argparse
import os
import re
import sys

EXTENSIONS = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts",
              ".tsx", ".vue", ".svelte", ".astro", ".swift", ".kt", ".dart"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "out", "coverage", "vendor"}
TOKEN_FILE = re.compile(r"(token|theme|palette|colou?rs?|variables|vars)\.", re.I)

# (id, pattern, rule, note). Patterns are matched per line, case-insensitive.
LINE_TELLS = [
    ("transition-all", r"transition(-property)?\s*:\s*all\b|\btransition-all\b|transition:\s*['\"]all",
     "lens 09 · Transition only what changes",
     "animate the properties that change, not all"),
    ("ease-in-entrance", r"\bease-in\b(?!-out)|cubic-bezier\(\s*0?\.4\s*,\s*0\s*,\s*1\s*,\s*1\s*\)",
     "lens 09 · Ease-out for entrances; never ease-in on an entrance",
     "ease-in is for exits only; check what this animates"),
    ("outline-removed", r"outline\s*:\s*(none|0)\b|\boutline-none\b",
     "lens 10 · Visible focus indicator",
     "a removed outline needs a visible :focus-visible replacement"),
    ("clickable-div", r"<(div|span|li|td|img)\b[^>]*\b(onClick|@click|v-on:click|on:click|\(click\))\s*=",
     "catalog A-14 · lens 10 · Every control exposes name, role and state",
     "use a button or a link, or supply role, tabindex and key handlers"),
    ("positive-tabindex", r"tabindex\s*=\s*[\"'{]?\s*[1-9]",
     "catalog K-05 · lens 10 · Tab order follows meaning",
     "fix the DOM order instead of a positive tabindex"),
    ("zoom-blocked", r"user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b",
     "catalog L-04 · lens 10 · Structure is navigation; zoom and reflow",
     "never block pinch zoom"),
    ("img-no-alt", r"<img\b(?![^>]*\balt\s*=)[^>]*>",
     "catalog K-08 · lens 10 · Images and icons: alt by purpose",
     "meaningful images need alt text; decorative ones alt=\"\""),
    ("autofocus", r"\bautofocus\b|\bautoFocus\b",
     "lens 08 · Autofocus on desktop, never on phones",
     "first field on desktop only; never on phone widths"),
    ("placeholder-copy", r"lorem ipsum|\bTBD\b|\bplaceholder text\b|\bJohn Doe\b|\btest(ing)? 123\b",
     "lens 07 · Placeholder copy is flagged",
     "draft copy must not reach handoff unmarked"),
    ("raw-colour", r"(?<![\w-])#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3}(?:[0-9a-fA-F]{2})?)?\b|\brgba?\(\s*\d",
     "lens 13 · Cleanup pass (literals → named values)",
     "a literal colour where the project has a token"),
]
# File-level: motion without a reduced-motion branch anywhere in the same file.
MOTION = re.compile(r"@keyframes|\banimation\s*:|\banimate\(|framer-motion|motion\.", re.I)
REDUCED = re.compile(r"prefers-reduced-motion|useReducedMotion|reduceMotion|reducedMotion", re.I)


def files_from(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for n in names:
                    yield os.path.join(root, n)


def scan(path):
    hits = []
    if os.path.splitext(path)[1].lower() not in EXTENSIONS:
        return hits
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return hits
    token_file = bool(TOKEN_FILE.search(os.path.basename(path)))
    for i, line in enumerate(lines, 1):
        for tid, pat, rule, note in LINE_TELLS:
            subject = line
            if tid == "raw-colour":
                if token_file:
                    continue  # token files are where literals belong
                subject = re.sub(r"--[\w-]+\s*:[^;}]*", "", line)  # so are custom-property definitions
            if re.search(pat, subject, re.I if tid != "autofocus" else 0):
                hits.append((path, i, tid, rule, note, line.strip()[:120]))
    text = "\n".join(lines)
    if MOTION.search(text) and not REDUCED.search(text):
        line_no = next(i for i, l in enumerate(lines, 1) if MOTION.search(l))
        hits.append((path, line_no, "no-reduced-motion",
                     "lens 09 · Reduced motion means gentler, not none",
                     "motion in this file, no reduced-motion branch in it (check a global one)",
                     lines[line_no - 1].strip()[:120]))
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*", help="files or folders to scan")
    ap.add_argument("--stdin", action="store_true", help="read file paths from stdin (e.g. git diff --name-only)")
    ap.add_argument("--format", choices=("text", "md"), default="text")
    ap.add_argument("--only", help="comma-separated tell ids to keep")
    args = ap.parse_args()

    paths = list(args.paths)
    if args.stdin:
        paths += [l.strip() for l in sys.stdin if l.strip()]
    if not paths:
        ap.error("give paths or --stdin")
    only = set(args.only.split(",")) if args.only else None

    hits = []
    for f in files_from(paths):
        hits += [h for h in scan(f) if not only or h[2] in only]

    if args.format == "md":
        print("| Location | Tell | Rule | Look at | Line |")
        print("|---|---|---|---|---|")
        for path, n, tid, rule, note, line in hits:
            cell = line.replace("|", "\\|")
            print(f"| `{path}:{n}` | {tid} | {rule} | {note} | `{cell}` |")
    else:
        for path, n, tid, rule, note, line in hits:
            print(f"{path}:{n}: [{tid}] {note} — {rule}\n    {line}")
    counts = {}
    for h in hits:
        counts[h[2]] = counts.get(h[2], 0) + 1
    summary = ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none"
    print(f"\n{len(hits)} tells: {summary}", file=sys.stderr)


if __name__ == "__main__":
    main()
