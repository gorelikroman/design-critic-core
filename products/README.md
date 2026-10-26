# Product layers

The skill's core is design-system-agnostic. A **product layer** adds one product's design
system, patterns, voice and decisions on top of it, so building and reviewing that product
use its real components and its own rules.

```
universal rules      lenses/, catalog/, foundations/          — this skill, never product-specific
company layer        products/_company/product.md             — optional: what all products share
product layer        product.md                               — the product's design system and patterns
                     design-decisions.md                      — the product's decisions log, grown by reviews
```

The core ships no product layer. A layer lives in one of three places:

| Where | Who gets it | When to use |
|---|---|---|
| A **product pack** — a separate plugin, `design-critic-<slug>` | whoever installs the pack | the usual way: teams install only the products they work on, and the core stays shareable |
| The product repository's `.design-critic/` | anyone working in that repository | developers and QA inside the product's code |
| `products/<slug>/` in a private copy of this skill | everyone with that copy | a single-product team that keeps its own fork |

## How a layer is loaded

1. **By name.** The request names the product; the name is matched against the title and
   the `Names` line of every layer — installed packs (an available skill named
   `design-critic-<slug>:product-layer`), this folder, and the working repository's
   `.design-critic/product.md` (list every name people actually use: the official one,
   localized ones, the repo slug).
2. **By repository.** No name in the request, and the working repository has
   `.design-critic/product.md` (a product repo can keep its layer there instead of in this
   folder) → that layer. If a named product and the repository's layer disagree, the name
   wins and the mismatch is pointed out.
3. **Otherwise** universal rules only — a product is never guessed. The first line of the
   deliverable says so and lists the available layers, so the requester can name one.
4. The skill loads `products/_company/product.md` if it exists, then the product's
   `product.md` and `design-decisions.md`. The product wins over the company where they
   differ.

Switching is per request: "now the same screen in Beta" loads Beta's layer and drops
Alpha's. Every deliverable starts with the active layer ("Product: Alpha"), so a report can
never be read as the wrong product's.

## Precedence

A product layer is "the project's confirmed decisions" in the precedence order of
`SKILL.md`: it outranks universal `warning` and `note` rules, never a universal `blocking`
one. The **hard rules** section of `product.md` is the project's hard rules of the review
method (§4.5): breaking one is `debt` with no `context` exception.

## Creating a layer for a product

1. `cp -R products/_template products/<slug>`: it holds `product.md` and an empty
   `design-decisions.md` (the same file as `templates/design-decisions.md`).
2. Fill `product.md` §1–§3 by hand: what the product is, the design system's sources (library
   link, token source, component docs), the voice. Leave §4–§6 mostly empty.
3. Run a review in **learn mode** on the product's most recent, most trusted screens
   (`method/review-method.md` §0, §5 "Bootstrapping a new project"). Its decisions delta and
   component inventory become the first rows of `design-decisions.md` and §4–§5 of
   `product.md`, once the product owner accepts them.
4. From then on, reviews grow the log and builds use the components and patterns listed here.

Only the product owner edits a product layer. Builds and reviews propose changes; they do not
write them.

## Packaging a layer as a product pack

The quickest way is `/design-critic:new-product` (the whole procedure, `method/product-method.md`)
or the scaffold alone, `python3 scripts/new_pack.py <pack-repo> --product "<Name>" --names
"<names>"`. The structure it writes:

A pack is a plugin with one skill that holds the layer's files. Keep packs in a private
repository of your own that doubles as a marketplace:

```
<your-product-packs>/
  .claude-plugin/marketplace.json            lists the packs
  plugins/design-critic-<slug>/
    .claude-plugin/plugin.json               name: design-critic-<slug>, version
    skills/product-layer/SKILL.md            the product's names; points at the two files
    skills/product-layer/product.md          the layer (from products/_template/)
    skills/product-layer/design-decisions.md the decisions log
```

`skills/product-layer/SKILL.md`:

```markdown
---
name: product-layer
description: Alpha product layer for design-critic (design system, patterns, voice, hard rules, decisions log). Names - Alpha, Alpha app, alpha-app. Load only when a design-critic request names Alpha.
---

# Alpha — product layer for design-critic

Data, not a procedure. design-critic reads `product.md` and `design-decisions.md` in this
folder as the Alpha layer (design-critic `SKILL.md` · Product layers).
```

`.claude-plugin/marketplace.json` at the repository root:

```json
{
  "name": "<your-product-packs>",
  "owner": { "name": "<your-team>" },
  "plugins": [
    { "name": "design-critic-alpha", "source": "./plugins/design-critic-alpha",
      "description": "Alpha product layer for design-critic" }
  ]
}
```

Install next to the core:

```bash
claude plugin marketplace add <your-org>/<your-product-packs>
claude plugin install design-critic-alpha@<your-product-packs>
```

Updating a layer is a commit to the pack and a version bump in its `plugin.json`; teammates
run `claude plugin update design-critic-alpha@<your-product-packs>`. To give a whole product
repository's team the pack automatically, list the marketplace and the plugin in that
repository's `.claude/settings.json` (`extraKnownMarketplaces`, `enabledPlugins`), as in the
main README.
