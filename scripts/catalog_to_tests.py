#!/usr/bin/env python3
"""Export catalog rules as UX test cases (CSV or Markdown).

Reads catalog/rules-catalog.md and the lenses, filters rows by section, platform and
level, and writes one test case per rule: the catalog's Check column becomes the steps,
its Rule column the expected result, and the severity comes from the lens entries that
cite the rule (the highest one; the lens entry decides which applies to a failure).

    python3 scripts/catalog_to_tests.py --sections A,B,D,E,K,L --platform web --level REQ -o cases.csv
    python3 scripts/catalog_to_tests.py --sections H --format md

Standard library only. Method: method/test-method.md §2.
"""
import argparse
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "catalog", "rules-catalog.md")
LENSES = os.path.join(ROOT, "lenses", "*.md")

SEVERITY_ORDER = {"blocking": 3, "warning": 2, "note": 1}
LEVELS = {"REQ", "REC", "CTX"}
# A requested platform matches a row whose Platform cell names any of these tokens.
PLATFORM_MATCH = {
    "web": {"all", "web"},
    "desktop": {"all", "desktop"},
    "mobile": {"all", "mobile", "ios", "android"},
    "ios": {"all", "mobile", "ios"},
    "android": {"all", "mobile", "android"},
}
ROW = re.compile(r"^\| ([A-N]-\d\d) \| (\w+) \| ([^|]+) \| (.+?) \| (.+?) \|\s*$")
SECTION = re.compile(r"^## ([A-N])\. (.+?) \(\d+\)\s*$")


def read_catalog():
    rows, section = [], None
    with open(CATALOG, encoding="utf-8") as f:
        for line in f:
            m = SECTION.match(line)
            if m:
                section = f"{m.group(1)}. {m.group(2)}"
                continue
            m = ROW.match(line)
            if m:
                rid, level, platform, rule, check = (g.strip() for g in m.groups())
                rows.append({"id": rid, "section": section, "level": level,
                             "platform": platform, "rule": rule, "check": check})
    return rows


def read_lens_map():
    """Catalog ID -> list of (lens number, entry heading, severity)."""
    mapping = {}
    for path in sorted(glob.glob(LENSES)):
        lens = os.path.basename(path)[:2]
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for entry in re.split(r"\n### ", text)[1:]:
            heading = entry.split("\n", 1)[0].strip()
            cat = re.search(r"\*\*Catalog:\*\*\s*([^\n]+)", entry)
            if not cat:
                continue
            sev = re.search(r"\*\*Severity:\*\*\s*(\w+)", entry)
            severity = sev.group(1).lower() if sev else ""
            for rid in re.findall(r"[A-N]-\d\d", cat.group(1)):
                mapping.setdefault(rid, []).append((lens, heading, severity))
    return mapping


def platform_ok(cell, wanted):
    if not wanted:
        return True
    tokens = {t.strip().lower() for t in cell.split(",")}
    return bool(tokens & PLATFORM_MATCH[wanted])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--sections", help="comma-separated section letters, e.g. A,B,D (default: all)")
    ap.add_argument("--platform", choices=sorted(PLATFORM_MATCH), help="keep rows for this platform (rows marked All always match)")
    ap.add_argument("--level", default="REQ,REC,CTX", help="comma-separated levels: REQ, REC, CTX (default: all)")
    ap.add_argument("--prefix", default="TC", help="test case ID prefix, e.g. CHECKOUT-TC (default: TC)")
    ap.add_argument("--format", choices=("csv", "md"), default="csv")
    ap.add_argument("-o", "--output", help="output file (default: stdout)")
    args = ap.parse_args()

    sections = {s.strip().upper() for s in args.sections.split(",")} if args.sections else None
    levels = {s.strip().upper() for s in args.level.split(",")}
    if not levels <= LEVELS:
        ap.error(f"unknown level(s): {', '.join(sorted(levels - LEVELS))}")

    lens_map = read_lens_map()
    cases = []
    for row in read_catalog():
        if sections and row["id"][0] not in sections:
            continue
        if row["level"] not in levels or not platform_ok(row["platform"], args.platform):
            continue
        entries = lens_map.get(row["id"], [])
        severities = [e[2] for e in entries if e[2] in SEVERITY_ORDER]
        severity = max(severities, key=SEVERITY_ORDER.get) if severities else ""
        cases.append({
            "Case ID": f"{args.prefix}-{len(cases) + 1:03d}",
            "Rule ID": row["id"],
            "Section": row["section"],
            "Level": row["level"],
            "Platform": row["platform"],
            "Title": row["rule"],
            "Steps": row["check"],
            "Expected": row["rule"],
            "Severity if failed (highest)": severity,
            "Lens entries": "; ".join(f"lens {l} · {h} ({s})" for l, h, s in entries),
            "Result": "",
            "Evidence": "",
        })

    out = open(args.output, "w", newline="", encoding="utf-8") if args.output else sys.stdout
    try:
        fields = list(cases[0]) if cases else ["Case ID"]
        if args.format == "csv":
            w = csv.DictWriter(out, fieldnames=fields)
            w.writeheader()
            w.writerows(cases)
        else:
            out.write("| " + " | ".join(fields) + " |\n")
            out.write("|" + "---|" * len(fields) + "\n")
            for c in cases:
                out.write("| " + " | ".join(str(c[k]).replace("|", "\\|") for k in fields) + " |\n")
    finally:
        if args.output:
            out.close()
    print(f"{len(cases)} cases", file=sys.stderr)


if __name__ == "__main__":
    main()
