# Design brief — `<key>` `<screen | flow | component name>`

> The screen card, written before the screen (`method/build-method.md` §1–§3). Fill what the
> inputs answer, say where each answer came from, ask only for the rest. A brief alone is a
> complete deliverable: a PM can hand it to design, a designer to development, QA can derive
> test cases from §5 and §6.
>
> Requested by: `<name / role>` · Date: `<date>` · Medium: `<design file | code | written spec>` ·
> Platform: `<desktop web | mobile web | iOS | Android | kiosk / POS / handheld>` ·
> Sources: `<ticket, PRD, story, references, design-decisions.md version>`

## 1. User task

<!-- One verb: find / buy / read / glance / choose / decide / recover. The user's state
     (hurrying? anxious? comparing?). What "done" looks like for them. -->

- Verb:
- User's state:
- Done means:

## 2. Business task

<!-- The outcome to move and how it is measured (lens 13 · Define the metric before the work). -->

- Outcome:
- Metric and baseline:

## 3. Planned anatomy

<!-- Zones top to bottom; the project's components named where they exist. -->

| Zone | Content | Component (project library) | Notes |
|---|---|---|---|
| header | | | |
| title | | | |
| blocks | | | |
| CTA | | | |
| footer | | | |

## 4. Devices chosen

<!-- From the device vocabulary (method/review-method.md §3) and the project's log. One reason each. -->

| Device | Why here | Source (vocabulary / log row) |
|---|---|---|
| | | |

## 5. Hierarchy and attention

- Verb profile (lens 04 · Task profiles at a glance): `<size steps · accent axis · rail · gap ladder>`
- Dominant: `<the one most contrasting element>`
- Route: 1 `<…>` → 2 `<…>` → 3 `<…>`
- Levels: `<n>` · Reading mode: `<analytical | exploratory>`

## 6. Scenario model and state matrix

<!-- lens 05 §1–§2. For a single component one line per axis is enough. -->

| Dimension | Values | Risk (`critical` / `standard`) |
|---|---|---|
| persona | | |
| session | | |
| data | 0 / 1 / many / corrupted | |
| environment | viewport, offline, slow network | |
| flow | earlier choices | |

Constraints (impossible combinations): `<exclude / require rules, each with its reason>`

| Screen / component | default | loading | empty | validation_error | server_error | success | permission_denied | custom (named) |
|---|---|---|---|---|---|---|---|---|
| | required | | | | | | | |

Stress set per text-bearing component: longest string · unbreakable string · zero items ·
320 px · 200 % zoom · RTL `<if localised>`.

## 7. Constraints

- Lens pack: `<01, 04, 05, 07, …>` (method/review-method.md §2b)
- `blocking` constraints that matter most here: `<list, each with lens · entry or catalog ID>`
- Project rows followed (`confirmed`): `<archetype · decision>`
- `decision-needed` rows met (follow the neighbours): `<row · which way the neighbours go>`
- Catalog sections walked for a handoff-bound build: `<A–N>`

## 8. Directions

<!-- One version when the direction is fixed; two or three when open, each differing on ONE
     named axis (method/build-method.md §4). -->

| Direction | Axis it varies | What it optimises |
|---|---|---|
| A | | |

## 9. Portability

- Reusable pattern for other sections: `<…>`
- Unique to this screen: `<…>`

## Open questions for the requester

- `<only what the inputs could not answer>`
