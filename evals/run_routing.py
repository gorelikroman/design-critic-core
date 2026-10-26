#!/usr/bin/env python3
"""Run the routing evals in evals/routing.json against the skill in this repository.

For each case: a fresh temporary folder with the case's fixture files (and, if asked, a git
branch or a product layer), then `claude -p <prompt> --plugin-dir <repo> --add-dir <repo>`
(the skill's own files must be readable). A case passes
when the skill triggers (or, for `trigger: false`, does not) and the expected mode's method
file is read successfully (review also counts when lenses are read with no other method file);
`product_layer: true` also requires `.design-critic/product.md` to be read; a string names the
layer file that must be read (e.g. `products/<slug>/product.md`).
`expect` notes are printed for a human to check in the transcripts.

    python3 evals/run_routing.py                 # all cases, 4 in parallel
    python3 evals/run_routing.py R01 R13 -j 2    # selected cases
    python3 evals/run_routing.py --keep out/     # keep transcripts in out/
    python3 evals/run_routing.py --rescore out/  # score kept transcripts again, no new runs

Needs the claude CLI, signed in. Costs one short session per case.
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GIT = ["git", "-c", "user.email=eval@example.com", "-c", "user.name=eval"]


def prepare(case, wd):
    for rel in case.get("files", []):
        shutil.copy(os.path.join(HERE, rel), wd)
    setup = case.get("setup")
    if setup == "git-branch":
        # a base commit, then a feature branch that removes a focus outline and adds transition: all
        run = lambda *a: subprocess.run(a, cwd=wd, check=True, capture_output=True)
        run("git", "init", "-q", "-b", "main")
        run("git", "add", "-A")
        run(*GIT, "commit", "-qm", "base")
        run("git", "checkout", "-qb", "feature")
        for name in os.listdir(wd):
            if name.endswith(".html"):
                path = os.path.join(wd, name)
                text = open(path, encoding="utf-8").read().replace("</style>", ".btn{transition:all .2s}</style>")
                open(path, "w", encoding="utf-8").write(text)
        run(*GIT, "commit", "-qam", "Restyle checkout buttons")
    elif setup == "product-layer":
        os.makedirs(os.path.join(wd, ".design-critic"))
        with open(os.path.join(wd, ".design-critic", "product.md"), "w", encoding="utf-8") as f:
            f.write("# Product layer — Alpha\n\n> **Names:** Alpha · Alpha app · alpha-app\n\n## 6. Hard rules\n\n"
                    "- The primary action is always the product Button, never a styled div.\n")


def run_case(case, keep):
    wd = tempfile.mkdtemp(prefix=f"eval-{case['id']}-")
    try:
        prepare(case, wd)
        proc = subprocess.run(
            ["claude", "-p", case["prompt"], "--plugin-dir", ROOT, "--add-dir", ROOT, "--output-format", "stream-json",
             "--verbose", "--max-turns", "14"],
            cwd=wd, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=900)
        lines = proc.stdout.splitlines()
        if keep:
            os.makedirs(keep, exist_ok=True)
            with open(os.path.join(keep, f"{case['id']}.jsonl"), "w", encoding="utf-8") as f:
                f.write(proc.stdout)
    except subprocess.TimeoutExpired:
        lines = []
    finally:
        shutil.rmtree(wd, ignore_errors=True)
    return score(case, lines)


def score(case, lines):
    triggered, pending, reads, denied = False, {}, [], 0
    for line in lines:
        try:
            event = json.loads(line)
        except ValueError:
            continue
        message = event.get("message") if isinstance(event, dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                if block["name"] == "Skill" and "design-critic" in block["input"].get("skill", ""):
                    triggered = True
                if block["name"] == "Read":
                    pending[block["id"]] = block["input"].get("file_path", "")
                if block["name"] == "Bash":
                    command = block["input"].get("command", "")
                    if ".design-critic/product.md" in command:
                        pending[block["id"]] = ".design-critic/product.md"  # read with cat / head
                    else:
                        # skill files read with cat / sed / grep count like a Read
                        shell_reads = re.findall(r"[\w./-]*(?:method/\w+-method\.md|lenses/[\w-]+\.md|products/[\w-]+/product\.md)", command)
                        if shell_reads:
                            pending[block["id"]] = shell_reads
            elif block.get("type") == "tool_result" and block.get("tool_use_id") in pending:
                path = pending.pop(block["tool_use_id"])
                if isinstance(path, list):
                    if str(block.get("content")).strip():
                        reads.extend(path)
                elif path == ".design-critic/product.md" and "Product layer" in str(block.get("content")):
                    reads.append(path)  # a shell read counts when the layer's text came back
                elif block.get("is_error"):
                    denied += 1  # a read the session was not allowed to make does not count
                else:
                    reads.append(path)
    modes = [m for m in ("review", "build", "spec", "test", "product")
             if any(r.endswith(f"method/{m}-method.md") for r in reads)]
    if not modes and any("/lenses/" in r for r in reads):
        # review often runs from SKILL.md's one-screen summary straight into the lenses
        modes = ["review"]
    layer = case.get("product_layer")
    target = layer if isinstance(layer, str) else ".design-critic/product.md"
    product = any(r.endswith(target) for r in reads)

    ok = triggered == case.get("trigger", True)
    if ok and case.get("trigger", True) and case.get("mode"):
        ok = case["mode"] in modes
    if ok and case.get("product_layer"):
        ok = product
    return case, ok, triggered, modes, product, denied


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("ids", nargs="*", help="case IDs to run (default: all)")
    ap.add_argument("-j", "--jobs", type=int, default=4)
    ap.add_argument("--keep", help="folder to keep the transcripts in")
    ap.add_argument("--rescore", help="score transcripts kept earlier in this folder instead of running")
    ap.add_argument("--cases", default=os.path.join(HERE, "routing.json"), help="cases file (default: evals/routing.json)")
    args = ap.parse_args()

    cases = json.load(open(args.cases, encoding="utf-8"))["cases"]
    if args.ids:
        cases = [c for c in cases if c["id"] in set(args.ids)]
    passed = 0
    if args.rescore:
        def job(c):
            path = os.path.join(args.rescore, f"{c['id']}.jsonl")
            lines = open(path, encoding="utf-8").read().splitlines() if os.path.exists(path) else []
            return score(c, lines)
    else:
        def job(c):
            return run_case(c, args.keep)
    with cf.ThreadPoolExecutor(args.jobs) as ex:
        for case, ok, trig, modes, product, denied in ex.map(job, cases):
            passed += ok
            note = f" · check: {case['expect']}" if case.get("expect") else ""
            print(f"{'PASS' if ok else 'FAIL'} {case['id']} [{case['lang']}/{case['role']}] "
                  f"trigger {case.get('trigger', True)}→{trig} · mode {case.get('mode', '—')}→{','.join(modes) or '—'}"
                  f"{' · product layer read' if product else ''}"
                  f"{f' · {denied} failed reads' if denied else ''}{note}")
            sys.stdout.flush()
    print(f"\n{passed}/{len(cases)} passed")
    sys.exit(0 if passed == len(cases) else 1)


if __name__ == "__main__":
    main()
