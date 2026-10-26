#!/usr/bin/env python3
"""Integrity checks for the skill: run before every commit (evals/README.md §1).

- SKILL.md frontmatter parses, has name and description, description <= 1024 characters
- every `lens NN · <entry>` citation resolves to a lens heading
- every catalog ID cited outside the catalog exists in it
- every path in the SKILL.md Files block exists
- .claude-plugin/plugin.json and marketplace.json parse and agree on the plugin name
- the repository text is English only (no Cyrillic)

Standard library only (PyYAML is used for the frontmatter when installed). Exit 1 on failure.
"""
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def check_frontmatter():
    text = read("SKILL.md")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md: no frontmatter")
        return
    block = m.group(1)
    try:
        import yaml
        data = yaml.safe_load(block)
    except ImportError:
        data = {}
        for line in block.splitlines():
            key, sep, value = line.partition(": ")
            if not sep:
                errors.append(f"SKILL.md frontmatter: cannot parse line {line[:40]!r}")
                continue
            if ": " in value and not value.startswith(("'", '"')):
                errors.append(f"SKILL.md frontmatter: '{key}' has ': ' inside an unquoted value (invalid YAML)")
            data[key] = value
    except Exception as e:  # yaml.YAMLError
        errors.append(f"SKILL.md frontmatter: invalid YAML ({str(e).splitlines()[0]})")
        return
    for key in ("name", "description"):
        if not data.get(key):
            errors.append(f"SKILL.md frontmatter: missing {key}")
    desc = str(data.get("description", ""))
    if len(desc) > 1024:
        errors.append(f"SKILL.md description is {len(desc)} characters (max 1024)")
    return data


def lens_headings():
    heads = {}
    for path in glob.glob(os.path.join(ROOT, "lenses", "*.md")):
        n = os.path.basename(path)[:2]
        with open(path, encoding="utf-8") as f:
            heads[n] = {re.sub(r"^#+\s*(\d+\.\s*)?", "", l).strip() for l in f if l.startswith("#")}
    return heads


def doc_files():
    pats = ["SKILL.md", "README.md", "method/*.md", "templates/*.md", "products/**/*.md", "evals/*.md"]
    seen = []
    for p in pats:
        for f in glob.glob(os.path.join(ROOT, p), recursive=True):
            if f not in seen:
                seen.append(f)
    return seen


def check_citations():
    heads = lens_headings()
    cite = re.compile(r"lens (\d\d) · ([^;),|\n`>]+?)(?=[;),|`>]|$| \(| —|\.\s)")
    for f in doc_files():
        with open(f, encoding="utf-8") as fh:
            text = re.sub(r"\s*\n\s*", " ", fh.read())
        for n, name in cite.findall(text):
            name = name.strip().rstrip(".")
            if n not in heads:
                errors.append(f"{os.path.relpath(f, ROOT)}: lens {n} does not exist")
            elif not any(h == name or h.startswith(name) for h in heads[n]):
                errors.append(f"{os.path.relpath(f, ROOT)}: 'lens {n} · {name}' matches no heading")


def check_catalog_ids():
    ids = set(re.findall(r"^\| ([A-N]-\d\d) \|", read("catalog/rules-catalog.md"), re.M))
    files = doc_files() + glob.glob(os.path.join(ROOT, "lenses", "*.md")) + glob.glob(os.path.join(ROOT, "scripts", "*.py"))
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for rid in set(re.findall(r"(?:catalog |Catalog:\*\*[^\n]*?|\b)([A-N]-\d\d)\b", text)):
            if rid not in ids:
                errors.append(f"{os.path.relpath(f, ROOT)}: catalog ID {rid} does not exist")


def check_files_block():
    text = read("SKILL.md")
    m = re.search(r"## Files\s*```\n(.*?)```", text, re.S)
    if not m:
        errors.append("SKILL.md: no Files block")
        return
    for line in m.group(1).splitlines():
        base = ""
        for part in line.split("  ")[0].split("·"):
            part = part.strip().split(" ")[0] if part.strip() else ""
            if not part or "…" in part:
                continue
            if "/" in part:
                base = os.path.dirname(part)
            elif base:
                part = os.path.join(base, part)  # "templates/a.md · b.md" → templates/b.md
            if not os.path.exists(os.path.join(ROOT, part.rstrip("/"))):
                errors.append(f"SKILL.md Files block: {part} does not exist")


def check_plugin(skill_name):
    try:
        plugin = json.loads(read(".claude-plugin/plugin.json"))
        market = json.loads(read(".claude-plugin/marketplace.json"))
    except (OSError, ValueError) as e:
        errors.append(f".claude-plugin: {e}")
        return
    names = {p.get("name") for p in market.get("plugins", [])}
    if plugin.get("name") not in names:
        errors.append(".claude-plugin: plugin.json name is not listed in marketplace.json")
    if skill_name and plugin.get("name") != skill_name:
        errors.append(f".claude-plugin: plugin name {plugin.get('name')!r} differs from skill name {skill_name!r}")
    for key in ("name", "owner", "plugins"):
        if key not in market:
            errors.append(f".claude-plugin/marketplace.json: missing {key}")


def repository_files():
    """Files the repository would ship: tracked plus untracked, minus .gitignore'd ones
    (local reports and builds are not repository text). Falls back to a walk outside git."""
    try:
        out = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                             cwd=ROOT, capture_output=True, check=True).stdout.decode()
        return [os.path.join(ROOT, p) for p in out.split("\0") if p and os.path.isfile(os.path.join(ROOT, p))]
    except (OSError, subprocess.CalledProcessError):
        files = []
        for dirpath, dirnames, names in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
            files += [os.path.join(dirpath, n) for n in names]
        return files


def check_english_only():
    cyrillic = re.compile("[\u0400-\u04FF]")
    for path in repository_files():
        if not path.endswith((".md", ".json", ".py", ".js", ".html", ".yml", ".yaml", ".txt", ".css")):
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for n, line in enumerate(f, 1):
                if cyrillic.search(line):
                    errors.append(f"{os.path.relpath(path, ROOT)}:{n}: non-English (Cyrillic) text")
                    break


def main():
    data = check_frontmatter() or {}
    check_citations()
    check_catalog_ids()
    check_files_block()
    check_plugin(data.get("name"))
    check_english_only()
    if errors:
        print("\n".join(f"FAIL {e}" for e in errors))
        print(f"\n{len(errors)} problem(s)")
        sys.exit(1)
    print("OK — frontmatter, lens citations, catalog IDs, Files block, plugin manifests, English only")


if __name__ == "__main__":
    main()
