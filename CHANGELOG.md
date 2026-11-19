# Changelog

Versions follow `.claude-plugin/plugin.json`. Plugin installs stay on a version until it is
bumped here and in the manifest.

## 2.1.0 — 2026-11-19

What building two real product packs taught the product method:

- **Layer template** (`products/_template/product.md`): a `Not this product` line for sibling
  products with similar names; a reading order per mode; the "summary layer" first line when the
  sources cannot be read; §0 Source of truth for a product that already keeps a handbook; radius
  and elevation token roles; "States every flow draws"; §8 Tolerated exceptions, §9 Working in
  the design file, §10 Known drift and open questions.
- **Decisions log template**: rows confirmed directly by the owner, stable row IDs, answered
  questions kept and struck through, hard rules reviewed rule by rule (demoted ones become product
  warnings), and a Superseded decisions section.
- **Product method** §5: decision rounds — how each round of the owner's answers updates the log,
  the hard rules, the exceptions, §10 and the pack version; refreshing a summary layer.
- **`scripts/new_pack.py --not-for`** writes the `Not this product` line and adds "Not for …" to
  the pack's skill description.

## 2.0.0 — 2026-11-19

- **Renamed: design-critic is now Roman in your Pocket.** The plugin, its marketplace and its
  skill are `roman-in-your-pocket` (install `roman-in-your-pocket@roman-in-your-pocket` from
  `gorelikroman/roman-in-your-pocket`); the commands are `/roman-in-your-pocket:roman-in-your-pocket`
  and `/roman-in-your-pocket:new-product`; product packs are `roman-in-your-pocket-<product>`.
  Breaking: reinstall under the new name. A product repository's layer folder is now
  `.roman-in-your-pocket/`; the older `.design-critic/` is still read. `live-checks.js` exposes
  `window.romanChecks`, with `window.designCriticChecks` kept as an alias.
- **Called by name:** "Roman, review this" (in any language) starts the critic. Evals: R20.

## 1.4.0 — 2026-11-01

- **Perceptual contrast (APCA) next to WCAG 2.** Lens 03 · Contrast floors now reports the
  APCA lightness contrast (Lc) for text beside the WCAG 2 ratio: Lc 75 body text (90 preferred),
  Lc 60 other content text, Lc 45 above 36 px. The WCAG 2 ratio stays the blocking floor,
  because accessibility law references it and APCA is in no adopted standard; text that passes
  the ratio but falls below its APCA level is a warning (typically grey text on dark surfaces),
  and a pair that fails the ratio but meets APCA stays blocking with the APCA value recorded.
- `scripts/live-checks.js` computes both on every text pair it can resolve to a solid
  background (`apca` warning, `apcaOnly` note); the formula matches the APCA-W3 reference
  values. APCA's licence covers web content only, so native app screens get the ratio alone.
- Foundations (text–background polarity) and `SOURCES.md` record what APCA models, its
  evidence and licence.

## 1.3.0 — 2026-10-26

- **Connect a product** without help: `/design-critic:new-product` (or "connect our product")
  runs the new product method (`method/product-method.md`) — ask for the inputs, scaffold a
  pack, fill the layer from the design system's own sources and a learn-mode review of shipped
  screens, hand it to the owner with publish and install commands. No special design-system
  format is required.
- `scripts/new_pack.py` scaffolds a product pack repository: marketplace, plugin, the skill
  that carries the layer, and the layer from the template; a second run adds another product.
- Evals: R19 (connecting a product).

## 1.2.0 — 2026-10-26

- **Product-neutral core.** The skill names no product and no company. Product layers ship as
  separate **product packs**: a plugin `design-critic-<product>` with one skill,
  `product-layer`, holding the product's `product.md` and `design-decisions.md`. The lookup in
  `SKILL.md` collects installed packs first, then `products/*/`, then the working repository's
  `.design-critic/`. How to build a pack: `products/README.md`.
- **Live layout checks** (`scripts/live-checks.js`): a read-only inspector for a rendered page —
  overlapping targets, target sizes, clipped and spilling text, sideways scroll, overlapping
  text — with axe-core results mapped to catalog IDs. `method/test-method.md` §3 says how
  unattended checks and screenshot regression fit a test run.
- `check_skill.py` checks repository files only (tracked, or untracked and not ignored), so
  local reports and builds no longer fail the English-only check.
- Evals: R14 and R18 no longer depend on a bundled product layer.

## 1.1.0 — 2026-09-27

- **Product lookup never guesses:** with no product named and no `.design-critic/` layer in
  the repository, the skill uses universal rules and lists the available layers in the first
  line (before, a single existing layer was applied to every request).
- Evals: R14 updated, R18 added (a named product); the runner counts skill files read through
  the shell.

## 1.0.0 — 2026-09-27

First packaged release: one core for designers, PMs, QA and developers.

- **Modes.** Review (existing), plus build (`method/build-method.md`), spec
  (`method/spec-method.md`) and test (`method/test-method.md`), with their templates: design
  brief, build note, UX spec, test plan, bug report.
- **Product layers** (`products/`): a product's design system sources, components, patterns,
  voice and hard rules on top of the universal rules; a blank template; loading order and
  precedence in `SKILL.md`.
- **Language.** Output in the language of the request; counting tokens stay English
  (`method/language.md`). The repository itself is English only; `check_skill.py` enforces it.
- **Scripts.** `catalog_to_tests.py` (catalog → test cases CSV / Markdown, severity from the
  lenses), `ui_tells.py` (line-level tells in UI code, each with its rule),
  `check_skill.py` (integrity checks).
- **Distribution.** Plugin manifest and marketplace (`.claude-plugin/`); CLAUDE.md snippet for
  product repositories; routing evals (`evals/`).
- Routing evals (`python3 evals/run_routing.py`, 2026-09-27): **17/17 passed** on the English
  suite: every mode triggers and reads its method file, the `.design-critic/` product layer is
  loaded when the request names the product, both negative prompts stay silent. The trigger
  list is English only; a separate set of 11 Russian prompts still triggered the skill 11/11
  and picked the right mode 11/11, answering in Russian. Fixed on the way: a named product was
  looked up only in `products/` and missed the repository's layer; a review could run from the
  summary without opening the lenses; without an artifact a review or test prompt asks for one
  first (correct, so those cases carry `evals/fixtures/`); in `claude -p` the skill's files
  need `--add-dir`. The runner stops at 14 turns, so it measures routing, not finished
  deliverables.

## 0.1 — 2026-09-26

Review-only skill: lenses 01–14, catalog, foundations, review method, decision board.
