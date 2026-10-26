# Review — `<slug>` · `<date>`

<!-- Chat version: paste the Verdict, Top findings, Not reviewed, Links and Next step
     sections only. File version (reviews/<date>-<slug>/README.md): everything. -->

## Verdict

`<N>` screens in `<K>` clusters · `<a>` match · `<b>` deviate (`<c>` blocking, `<d>` warning) ·
`<e>` decision-needed (the project owner's call, not defects) · `<f>` rule-candidates.

<!-- One sentence on the overall state. What kind of work is this: mostly consistent with
     debt, or structurally two systems, or new patterns worth logging. -->

## Top findings

<!-- The three most consequential, not the three most frequent. Location + rule + severity +
     confidence. Observation, interpretation and recommendation as three sentences. -->

1. **`<title>`** — `<location>` · rule `<lens · entry | catalog ID | log row>` ·
   `<blocking|warning|note>` · `<fail|partial>` · confidence `<high|medium|low>`
   `<Observation.>` `<Interpretation.>` `<Recommendation.>`
2. **`<title>`** — …
3. **`<title>`** — …

## Decision-needed (project owner)

<!-- Do not resolve these. State the two ways and the score. -->

- `<question>` — A `<n>` : B `<m>` · hypothesis `<…>`

## Not reviewed

<!-- Lenses loaded (method §2b) and what the input could not prove — so silence is not
     mistaken for a pass. -->

- Lenses loaded: `<01, 04, 05, 07, …>`
- Could not be proved by this input: `<runtime | keyboard | screen reader | network | motion | …>`

## Links

- Decision board: `<url>` — omit this line only when the review found nothing to decide
  (say so instead: "no debt or decision-needed items; no board built").

## Paths

- `reviews/<date>-<slug>/00-method.md` — plan, lenses loaded, changes on the way
- `reviews/<date>-<slug>/NN-cluster-*.md` — cards, finding blocks, cluster patterns
- `reviews/<date>-<slug>/debt.md` — `<n>` rows (`<c>` blocking); fix priority unassigned
- `reviews/<date>-<slug>/decisions-delta.md` — `<n>` proposed rows, `<m>` status changes
- `reviews/<date>-<slug>/coverage.md` — scenario coverage (flows only) and the not-reviewed list

## Coverage (flows only)

| Scenario | Priority | Screens / states | Covered |
|---|---|---|---|
| | | | |

Gaps: `<list, each with a suggestion>`

## Next step

`<what>` — model: `<Opus | Sonnet | Haiku | script>`, because `<one line>`.
