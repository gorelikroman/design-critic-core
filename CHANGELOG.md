# Changelog

Versions follow `.claude-plugin/plugin.json`. Plugin installs stay on a version until it is
bumped here and in the manifest.

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
