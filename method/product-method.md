# The product method — connecting a product to the critic

> How a team turns its product into a **product layer** the critic can use: who gives what,
> what the critic fills itself, and how the layer ships as a **product pack**. Requests:
> "connect our product", "set up a product layer for Alpha", "teach the critic our design
> system", `/design-critic:new-product`. The layer format: `products/README.md`; the blank
> layer: `products/_template/`.

---

## 0. What a layer is, and what it is not

- **It is a passport, not a design system.** The design system stays where it lives — the
  design library, the token source, the component code and docs. The layer points to them and
  records what the product decided: names, voice, which component when, patterns, hard rules,
  the motion register, and the decisions log.
- **No special format is required from the design system.** Tokens in any form (CSS variables,
  a tokens JSON, design-tool variables), components in any library. The layer names roles
  ("primary action → `Button/Primary`") and links to the source of truth.
- **It never invents.** A row without a source or a reference screen does not exist; an unknown
  value stays a placeholder and is listed as open.

## 1. Ask for the inputs

Ask once, in one message, and say which are required. Never guess a missing one.

| Input | Required | Used for |
|---|---|---|
| Official product name, and every name people use in requests | yes | the `Names` line, pack slug |
| Product owner and design-system owner (people or teams) | yes | who accepts the layer |
| Where the layer will live: a **product pack** (default), the product repository's `.design-critic/`, or a fork's `products/<slug>/` | yes | §2 |
| Design library link (Figma or equivalent) | yes | §2 sources, §4 components |
| Token source: repository path, package or design-tool variables | yes | §2 token roles |
| Component code and docs (package, Storybook) | if they exist | §2, §4 |
| 10–20 of the most recent, most trusted shipped screens (links or screenshots), across the product's main flows | strongly recommended | learn mode → decisions log, §4, §5 |
| Voice: a few real texts, terms the product insists on, words it never uses | if known | §3 |
| Platforms, locales, house formats for dates, numbers, money | yes | §1 |

## 2. Scaffold

- **Product pack** (default): `python3 scripts/new_pack.py <pack-repo> --product "<Name>"
  --names "<Name>, <other names>" --owner "<owner>"`. It writes the marketplace, the plugin, the
  skill that carries the layer, and `product.md` / `design-decisions.md` from the template with
  the name, names, owners and date filled in. A second product goes into the same repository.
- **Product repository:** copy `products/_template/` to `<repo>/.design-critic/`.
- **Fork:** copy `products/_template/` to `products/<slug>/`.

## 3. Fill the passport

Work section by section in `product.md`; mark each value with its source.

1. **§1 The product** and **§3 Voice and terms** — from the requester's answers.
2. **§2 Design system sources** — the links as given. Token roles: read the token source (or
   the design tool through its integration, read-only) and map roles to token names; values
   stay in the source.
3. **§4 Components** and **§5 Patterns** — from the library and from the learn-mode review below.
4. **§6 Hard rules** — only what the owner states as non-negotiable. A rule the critic merely
   observed is a `candidate` row in the log, not a hard rule.
5. **§7 Motion register** — from the product's motion if it can be observed, otherwise ask
   (lens 09 · Name the register before the first finding).

## 4. Learn the product from its screens

Run a review in **learn mode** on the shipped screens (`method/review-method.md` §0 and §5 ·
Bootstrapping a new project): cluster by user task, judge against the universal rules only,
and record every device that recurs as a `candidate` row of `design-decisions.md` with its
reference screen. The component inventory and recurring patterns feed §4 and §5. Deviations from
universal `blocking` rules are listed as debt, never written into the layer as product rules.

## 5. Hand over for the owner's decision

The layer is a proposal until the owner accepts it. Deliver, in the language of the request:

- the files written, as a tree;
- per section of `product.md`: filled from a source / proposed from screens / still open;
- the decisions log: number of `candidate` rows by cluster, and the open questions;
- conflicts found: product decisions that break a universal `blocking` rule;
- how to publish and install it (§6).

Only the owner edits the layer afterwards; reviews and builds propose rows.

## 6. Publish

- **Pack:** commit and push the pack repository (private if the product is not public), then
  every teammate who works on the product runs
  `claude plugin marketplace add <owner>/<pack-repo>` and
  `claude plugin install design-critic-<slug>@<marketplace>`. A product repository's team gets it
  automatically from `extraKnownMarketplaces` and `enabledPlugins` in that repository's
  `.claude/settings.json`.
- **Updates:** a commit plus a `version` bump in the pack's `plugin.json`; teammates run
  `claude plugin update`.
- **Check:** in a fresh session, "review <a screen> in <Name>" must open the pack and start the
  answer with "Product: <Name>".
