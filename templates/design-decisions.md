# Design decisions log — `<project>`

> The project's own yardstick, accrued from reviews. The `roman-in-your-pocket` skill carries the
> universal rules (lenses 01–14 and the catalog); everything specific to this product —
> archetypes, named components, colour and type roles, tolerated exceptions — lives here.
> A row without a reference screen does not exist. Lifecycle: `method/review-method.md` §5.
>
> Created: `<date>` · Project owner: `<name>` · Last review: `<reviews/<date>-<slug>/>`

## Status legend

| Status | Meaning |
|---|---|
| `candidate` | seen in one cluster; the project owner has not objected |
| `confirmed` | seen on **3+ screens across 2+ clusters**, the project owner has not objected — or decided by the owner directly, written `confirmed (owner, <date> · <round or item>)` |
| `decision-needed` | the product does it two ways, or counter-evidence appeared; listed under Open questions; the project owner decides |

Status is editorial (is this row a rule of the project). It is not an audit result: a
`confirmed` row is checked on every screen and gets `pass` / `partial` / `fail` there.

## Promotion rule

- `candidate` → `confirmed`: 3+ screens across 2+ clusters, or an owner answer in a decision
  round. Never from one screen, however convincing.
- Counter-evidence downgrades: a contradiction in a later cluster moves a row to
  `decision-needed` with the score (how many screens each way).
- Only the project owner promotes rows into hard rules or the handbook, and only the project
  owner edits this file. Reviewers propose changes in `decisions-delta.md` inside their
  review folder.
- A reference screen that contradicts a confirmed rule is a violation, not evidence.
- A later owner answer replaces an earlier one; the old row moves to Superseded decisions.
- Rows keep a stable ID (`<AREA>-<n>`, e.g. `COL-3`); hard rules, exceptions and answers cite it.
- A confirmed row outranks a universal `warning` or `note` (a deviation from the universal
  becomes `context`, citing the row). It never outranks a universal `blocking`.

## Owner confirmations

<!-- One line per review or decision round, newest last:
     "<date> — cluster <X>: observations correct; candidates from <X> considered confirmed,
     await other clusters."
     "<date> — round <n> (<board or chat>, <N> items): <what was decided>; Q<a>–Q<b> answered." -->

---

## 1. `<Archetype or section>`

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| | | | | | |

## 2. `<Archetype or section>`

| # | Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|---|
| | | | | | |

---

## Open questions for the project owner

<!-- One per decision-needed row: the two (or more) ways, the score, the reviewer's
     hypothesis if any. Numbered; numbers are never reused. An answered question stays listed,
     struck through, with the date and the row it became:
     "3. ~~<question>~~ — answered <date>: <answer> (<ID>)." -->

1. `<question>` — A: `<way, N screens>` · B: `<way, M screens>` · hypothesis: `<…>`

## Tolerated exceptions

<!-- `context` verdicts the project owner has accepted as permanent: screen or archetype,
     the universal rule it deviates from (lens + entry, or catalog ID), the reason. A reviewer
     who meets the same deviation on the listed screens tags it `context`, not `debt`. -->

| Where | Deviates from | Why it is allowed | Since |
|---|---|---|---|
| | | | |

## Hard rules (owner-promoted, blocking)

<!-- Rules the project owner has promoted from confirmed rows. Reviewers treat these as
     blocking severity: always debt, no context exception. Keep the list in step with
     `product.md` §6, cite row IDs, and have the owner review it rule by rule; a rule the owner
     demotes is listed below as a product warning ("the critic reports it, a human decides"). -->

1.

---

## Superseded decisions (history — do not apply)

<!-- A decision a later owner answer replaced. Kept so an old screen or an old review is read
     correctly; never a rule. -->

| Was | Replaced by | When |
|---|---|---|
| | | |
