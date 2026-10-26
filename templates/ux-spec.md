# UX spec — `<story / flow name>` · `<date>`

> Spec mode (`method/spec-method.md`). What the user must be able to do, in which situations,
> with which states, measured how. No layout, no colours, no components: those are design's.
> The build brief inherits §1–§2; the test plan starts from §2–§3.
>
> Author: `<name / role>` · Story / PRD: `<link>` · Platform: `<…>` ·
> Project log: `<design-decisions.md version or "none yet">`

## 1. Problem and outcome

- Who, in what state: `<…>`
- Screens and their verbs: `<screen — verb>`, …
- Business outcome: `<…>`
- Metric: KPI `<…>` · baseline `<…>` · validation `<A/B | before-after | fake door>` ·
  monitoring window `<…>` · rollback trigger `<…>`
- Out of scope: `<…>`

## 2. Scenario model

| Dimension | Values | Risk |
|---|---|---|
| persona | | |
| session | | |
| data | 0 / 1 / many / corrupted | |
| environment | viewport, offline, slow network | |
| flow | earlier choices | |

Constraints: `<exclude / require rule — reason>`

| # | Scenario | Priority | Values (one per dimension) | Path (screen → state) | Outcome |
|---|---|---|---|---|---|
| S1 | happy path | critical | | | completed |
| S2 | | | | | blocked / recoverable_error |

Flow invariants: `<"the full price is always visible", …>`

State matrix:

| Screen | loading | empty | validation_error | server_error | success | permission_denied | custom (named) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 3. Acceptance criteria

<!-- Observable, one rule each. Severity comes from the rule; priority is the PM's. -->

| # | Scenario | Given | When | Then | Rule | Severity | Priority |
|---|---|---|---|---|---|---|---|
| AC1 | S1 | | | | `<catalog ID / lens NN · entry>` | blocking | |

## 4. Release gates

- [ ] Metric, baseline and validation plan defined (lens 13 · Define the metric before the work)
- [ ] Gradual rollout with stop conditions; rollback without a new build
- [ ] Performance target: `<…>` (transactional or data-heavy flows)
- [ ] Every key state designed; no generic error message
- [ ] Approval on evidence, not taste (lens 13 · Evidence, not taste)

## 5. Open decisions

| Decision | Options | Owner | Blocks design by |
|---|---|---|---|
| | | | |

## 6. Pre-flight

- [ ] Every screen has a verb and a required-state list
- [ ] Every `critical` value appears in a scenario
- [ ] Every failing outcome ends on a next step
- [ ] Every criterion is observable and cites a rule
- [ ] Nothing here prescribes layout, colour or components
