# The spec method — UX requirements a team can build and test against

> How a product manager (or anyone writing the requirement) turns a story, a PRD or a
> feature idea into UX requirements that design can build from, development can implement
> and QA can test, before anything is drawn. The rules are not restated here: this file
> routes to the build method's brief, lens 05's scenario model, the catalog and lens 13's
> product gates.
>
> Output: one UX spec per story or flow (`templates/ux-spec.md`). It is the input of the
> build (`method/build-method.md`) and of the test plan (`method/test-method.md`).

---

## 0. What spec mode is, and what it is not

- **It is** the step before design: what the user must be able to do, in which situations,
  with which states, measured how, and released how.
- **It is not a design.** It names the dominant action and the states, never the layout,
  the colours or the components. A spec that draws the screen takes the designer's job and
  loses the reasons.
- **It is not a review.** A spec is judged by whether design and QA can work from it
  without asking; the pre-flight in §6 checks exactly that.

---

## 1. The problem and the outcome

From the story or the PRD, write down, each with its source:

- **Who and in what state** (a returning customer in a hurry, a first-time admin, an anxious
  payer) and **the one verb** of each screen in the flow: find / buy / read / glance / choose /
  decide / recover (lens 04 · One intent per screen).
- **The business outcome** and **the metric**: KPI, baseline, how it will be validated, the
  monitoring window, the rollback trigger (lens 13 · Define the metric before the work).
- **Out of scope**, explicitly. What is not in the story is not silently designed.

Ask only what the story does not answer; usually the user's state, the platform and the
metric's baseline.

---

## 2. The scenario model

Write the model of lens 05 §1 at the size of the flow (the same model the build method's §2
uses, so design inherits it unchanged):

1. **Dimensions** with values and risk (`critical` when it can block the user or money):
   persona and permissions, session, data (0 / 1 / many / corrupted), environment (viewport,
   offline, slow network), earlier choices, local outcomes (lens 05 · Scenario dimensions).
2. **Constraints**: impossible combinations, each with its reason (lens 05 · Scenario
   constraints).
3. **Scenario cases**: a name, a priority, one value on every dimension, the path through the
   screens and the outcome `completed` / `blocked` / `recoverable_error` (lens 05 · Scenario
   cases). At least: the happy path, every `critical` value, every way to fail that costs the
   user money or data.
4. **Flow invariants**: what stays true along the whole path ("the full price is always
   visible", "progress is never lost") (lens 05 · Scenario coverage rules, check 5).
5. **The state matrix**: per screen, which of `default · loading · empty · validation_error ·
   server_error · success · permission_denied · custom` are required (lens 05 · Required
   states present).

---

## 3. Acceptance criteria

Each criterion is observable, cites the rule it enforces, and says which scenario it
belongs to. Turn a wish into a criterion the way the catalog does (catalog, the paragraph
after the acceptance checklist): replace "the card should be easy to use" with what can be
clicked, what opens, what is announced.

Format, one per line in the spec's table:

> **Given** `<scenario / state>` **when** `<action>` **then** `<observable result>` —
> rule `<catalog ID | lens NN · entry>` · `<blocking | warning>`

Sources, in this order:

1. **The flow's own logic**: every scenario case in §2 ends in the outcome it declares;
   every `blocked` or `recoverable_error` ends on a screen with an explicit next step
   (lens 05 · No dead ends).
2. **The required states**: each state in the matrix has a criterion for what the user sees
   and can do there (an empty state with a next step, an error with a recovery that keeps
   the input).
3. **The catalog's REQUIRED rows** of the sections the flow touches (A–N): forms → D and E,
   lists and tables → I, dialogs → H, navigation → G, and K and L for every flow. Pick the
   rows that apply; do not paste the whole section.
4. **The floor**: accessibility minimums, honesty about money, destructive safeguards
   (precedence rule 1 in `SKILL.md`). These are always `blocking`.
5. **The project's confirmed rows** in `design-decisions.md` that the flow meets.

Severity comes from the rule (a lens entry's Severity, or `blocking` for the floor), never
from how much the PM wants it. Priority between criteria is a separate column, set by the
PM (review method §8, "Rule priority is not fix priority").

---

## 4. Release and approval gates

From lens 13, only what the release needs:

- the metric and its validation plan (§1);
- the rollout: gradual release, stop conditions, rollback that does not need a new build
  (lens 13);
- performance targets where the flow is transactional or data-heavy (lens 13);
- approval on evidence, never on taste (lens 13 · Evidence, not taste).

Lens 13's global rejection triggers are the gate's red lines: a generic error message, a key
state not designed, missing KPIs or validation plan.

---

## 5. Open decisions

Everything the spec deliberately does not decide goes into one list with the options and
the owner: a product choice (one step or two), a `decision-needed` row from the project's
log the flow runs into (follow the neighbouring screens until the owner decides; never a
third variant), a question for legal or support. Each has a date by which it blocks design.

---

## 6. Pre-flight: can design and QA work from this?

- Every screen has a verb and a required-state list.
- Every `critical` dimension value appears in at least one scenario case.
- Every scenario case has an outcome, and every failing outcome has a next step.
- Every acceptance criterion is observable (no "easy", "intuitive", "clean") and cites a rule.
- The metric has a baseline and a rollback trigger, or the gap is an open decision.
- Nothing in the spec prescribes layout, colour or components.

Then the next step: a build (`method/build-method.md`), whose brief inherits §1–§2 of the
spec, and a test plan (`method/test-method.md`), whose cases start from §2–§3.
