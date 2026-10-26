#!/usr/bin/env python3
"""Scaffold a product pack: the plugin that carries one product's layer for design-critic.

A pack repository is a Claude Code marketplace holding one plugin per product:

    <repo>/.claude-plugin/marketplace.json
    <repo>/plugins/design-critic-<slug>/.claude-plugin/plugin.json
    <repo>/plugins/design-critic-<slug>/skills/product-layer/SKILL.md
    <repo>/plugins/design-critic-<slug>/skills/product-layer/product.md
    <repo>/plugins/design-critic-<slug>/skills/product-layer/design-decisions.md

The script writes the structure and the manifests, and fills in the parts of the blank layer it
knows (name, names, owners, date). Everything else in product.md stays a placeholder for the
product method (method/product-method.md) or a person to fill. Run it again with another
product to add a second pack to the same repository.

    python3 scripts/new_pack.py ../my-product-packs --product "Alpha" \\
        --names "Alpha, Alpha app, alpha-app" --owner "Design team"
"""
import argparse
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "products", "_template")


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if not slug:
        sys.exit("cannot derive a slug from the product name; pass --slug")
    return slug


def write(path, text, force):
    if os.path.exists(path) and not force:
        sys.exit(f"{path} exists; pass --force to overwrite")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser(description="Scaffold a design-critic product pack.")
    ap.add_argument("repo", help="pack repository folder (created if missing; may already hold other packs)")
    ap.add_argument("--product", required=True, help='official product name, e.g. "Alpha"')
    ap.add_argument("--names", help="comma-separated names people use in requests (default: the product name)")
    ap.add_argument("--slug", help="plugin slug (default: from the product name)")
    ap.add_argument("--owner", default="<product owner>", help="product owner, a person or a team")
    ap.add_argument("--ds-owner", default="<design system owner>", help="design system owner")
    ap.add_argument("--marketplace", help="marketplace name for a new repository (default: the folder name)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing pack of the same slug")
    args = ap.parse_args()

    names = [n.strip() for n in (args.names or args.product).split(",") if n.strip()]
    if args.product not in names:
        names.insert(0, args.product)
    for n in [args.product, *names]:
        if ":" in n or "\n" in n:
            sys.exit(f"a name cannot contain ':' or a line break: {n!r}")
    slug = args.slug or slugify(args.product)
    plugin = f"design-critic-{slug}"
    repo = os.path.abspath(args.repo)
    pack = os.path.join(repo, "plugins", plugin)
    layer = os.path.join(pack, "skills", "product-layer")
    today = datetime.date.today().isoformat()

    # Manifests.
    write(os.path.join(pack, ".claude-plugin", "plugin.json"), json.dumps({
        "name": plugin,
        "version": "0.1.0",
        "description": f"{args.product} product layer for design-critic: design system sources, "
                       "patterns, voice, hard rules and the decisions log.",
        "author": {"name": args.owner},
    }, indent=2, ensure_ascii=False) + "\n", args.force)

    market_path = os.path.join(repo, ".claude-plugin", "marketplace.json")
    if os.path.exists(market_path):
        with open(market_path, encoding="utf-8") as f:
            market = json.load(f)
    else:
        market = {"name": args.marketplace or slugify(os.path.basename(repo)),
                  "owner": {"name": args.owner},
                  "description": "Product packs for design-critic: one plugin per product.",
                  "plugins": []}
    market["plugins"] = [p for p in market.get("plugins", []) if p.get("name") != plugin]
    market["plugins"].append({"name": plugin, "source": f"./plugins/{plugin}",
                              "description": f"{args.product} product layer for design-critic"})
    os.makedirs(os.path.dirname(market_path), exist_ok=True)
    with open(market_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(market, indent=2, ensure_ascii=False) + "\n")

    # The skill that carries the layer. Its description is how design-critic finds the pack.
    write(os.path.join(layer, "SKILL.md"), f"""---
name: product-layer
description: {args.product} product layer for design-critic (design system, components, patterns, voice, hard rules, decisions log). Names - {", ".join(names)}. Load only when a design-critic request names {args.product}.
---

# {args.product} — product layer for design-critic

Data, not a procedure. design-critic reads the two files in this folder as the {args.product}
layer (design-critic `SKILL.md` · Product layers):

- `product.md` — design system sources, components, patterns, voice, hard rules
- `design-decisions.md` — the decisions log, grown by reviews
""", args.force)

    # The layer itself, from the blank template.
    with open(os.path.join(TEMPLATE, "product.md"), encoding="utf-8") as f:
        product = f.read()
    product = product.replace("# Product layer — `<product name>`", f"# Product layer — {args.product}")
    product = product.replace("(`products/README.md`)", "(design-critic `products/README.md`)")
    product = re.sub(r"> \*\*Names:\*\* .*?— every name people use for\n> this product in requests;",
                     "> **Names:** " + " · ".join(names) + " — every name people use for\n> this product in requests;",
                     product, flags=re.S)
    product = product.replace("Product owner: `<name>` · Design system owner: `<name>` · Last updated: `<date>`",
                              f"Product owner: {args.owner} · Design system owner: {args.ds_owner} · Last updated: {today}")
    write(os.path.join(layer, "product.md"), product, args.force)

    with open(os.path.join(TEMPLATE, "design-decisions.md"), encoding="utf-8") as f:
        log = f.read()
    log = log.replace("# Design decisions log — `<project>`", f"# Design decisions log — {args.product}")
    log = log.replace("Created: `<date>` · Project owner: `<name>`", f"Created: {today} · Project owner: {args.owner}")
    write(os.path.join(layer, "design-decisions.md"), log, args.force)

    readme = os.path.join(repo, "README.md")
    if not os.path.exists(readme):
        write(readme, f"""# {market["name"]}

Product packs for [design-critic](https://github.com/gorelikroman/design-critic-core): each
plugin in `plugins/` carries one product's layer — its design system sources, patterns, voice,
hard rules and decisions log. Install the critic once, then the packs of the products you
work on:

```bash
claude plugin marketplace add <owner>/{os.path.basename(repo)}
claude plugin install <pack>@{market["name"]}
```

Name the product in a request ("review the checkout in {args.product}") and the critic loads
its pack. Add a product: `/design-critic:new-product` in Claude Code, or
`python3 scripts/new_pack.py` from the design-critic repository. Update a pack: commit, bump
`version` in its `plugin.json`, and teammates run `claude plugin update <pack>@{market["name"]}`.
""", False)

    rel = lambda p: os.path.relpath(p, repo)
    print(f"Pack {plugin} in {repo}")
    for p in [market_path, os.path.join(pack, ".claude-plugin", "plugin.json"),
              os.path.join(layer, "SKILL.md"), os.path.join(layer, "product.md"),
              os.path.join(layer, "design-decisions.md")]:
        print("  " + rel(p))
    print(f"\nNext: fill product.md §1–§7 and the decisions log (method/product-method.md), push the "
          f"repository, then:\n  claude plugin marketplace add <owner>/{os.path.basename(repo)}\n"
          f"  claude plugin install {plugin}@{market['name']}")


if __name__ == "__main__":
    main()
