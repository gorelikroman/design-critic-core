# Evals

Two kinds of check keep the skill from quietly getting worse as rules and modes change.

## 1. Integrity — every commit

`python3 scripts/check_skill.py` checks what a model cannot be trusted to notice:

- `SKILL.md` frontmatter parses, has `name` and `description`, and the description fits
  1024 characters;
- every `lens NN · <entry>` citation in the method, templates, products and the front door
  resolves to a real lens heading;
- every catalog ID cited outside the catalog exists in it;
- every path listed in the `SKILL.md` Files block exists;
- `.claude-plugin/plugin.json` and `marketplace.json` parse and agree on the plugin name;
- the repository text is English only.

It exits non-zero on any failure, so it can gate a pull request.

## 2. Routing — before each release

`evals/routing.json` lists prompts from every role (one asks for the answer in another language), plus prompts that
must not trigger the skill. Review cases carry an artifact from `evals/fixtures/` (a checkout
screen with deliberate defects); without one the model correctly asks for the artifact before
loading the skill.

```bash
python3 evals/run_routing.py            # all cases; needs the claude CLI, signed in
python3 evals/run_routing.py R01 R13    # selected cases
```

Each case runs in a fresh temporary folder with its fixtures (and a git branch or a product
layer when `setup` asks for one). It passes when the skill triggers (or, for
`trigger: false`, does not), the expected mode's method file is read (a review may run from `SKILL.md` straight into the
lenses, which counts), and, for
`product_layer: true`, the product layer is read. `expect` notes are for a human reading the
transcripts (`--keep out/`).

Keep the results next to the release in `CHANGELOG.md` (pass count and the failing IDs).
When a case fails, fix the cause (the description's triggers, the mode table, the routing)
rather than the case.

## 3. Quality — per product, over time

The strongest eval is a set of real screens with known answers: for each product, a few
screens with the findings the product owner agreed on in a past review. Re-run the review
on them after rule changes and compare findings by rule ID. Put them in
`evals/<product>/` with the screenshots and the agreed findings; they are product data and
stay private with the product layer.
