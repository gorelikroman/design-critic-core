# The build method — designing and coding with the rules as constraints

> How the same body of rules is used while a screen, a flow or a component is being made,
> not judged. The review method asks "does this work, and why not"; the build method asks
> "what must be true before anything is drawn, and what did we decide". The inputs are a
> task and the project's context; the outputs are the artifact itself and a build note that
> says which rules shaped it, which conflicts were resolved and what still needs a review.
>
> The procedure is the same whether the artifact is a design file, code, or a written spec;
> only the medium step (§6) changes. The rules are not restated here: this file routes to
> the lenses, the catalog and the project's `design-decisions.md`.

---

## 0. What build mode is, and what it is not

- **It is** the skill consulted while designing or coding: the brief is written first, the
  lens pack becomes a set of constraints, the screen is composed in a fixed order, and a
  pre-flight self-check runs before the artifact is handed over.
- **It is not a review.** The builder's self-check catches what the builder can see; it
  issues no verdicts, fills no debt table and never marks its own work `pass`. The review is
  a separate pass (`method/review-method.md`), ideally in a fresh session or by another
  person, on the finished artifact. Building and judging the same artifact in one pass is
  how defaults pass as decisions.
- **It edits only what it was asked to make.** A new frame, a new file, a new branch, or the
  one artifact the requester named. It never edits an artifact that is under review, never
  edits the project's `design-decisions.md` (it proposes rows, §7), and never changes the
  project's library or tokens as a side effect.

### Who comes in through this mode

| Role | Typical request | Starts at |
|---|---|---|
| Designer | "design the subscription screen", "make three directions for onboarding" | §1 brief → §5 compose in the design tool |
| Developer | "build this component to our rules", "implement the checkout step" | §1 brief (often from the ticket) → §6 code |
| Product manager | "what states does this story need", "write the design brief for the redesign" | §1 brief + §2 scenario model; stops before composition |
| Anyone, after feedback | "make it cleaner", "less loud", "it has no air" | §8 iterate |

A request can stop at any step: a brief alone (§1–§3) is a complete deliverable for a PM or
for a designer before a kickoff.

---

## 1. The brief — the screen card, written before the screen

The seven-field card of the review (`method/review-method.md` §3) is the brief of the build.
Written first, it forces the decisions the review would otherwise find missing. Template:
`templates/design-brief.md`.

| # | Card field | In the brief it becomes |
|---|---|---|
| 1 | User task | the one verb (find / buy / read / glance / choose / decide / recover), the user's state (hurrying, anxious, comparing), and what "done" looks like for them |
| 2 | Business task | the outcome to move and how it will be measured (lens 13 · Define the metric before the work) |
| 3 | Anatomy | the planned zones, top to bottom, with the project's components named where they exist |
| 4 | Devices | the techniques chosen from the device vocabulary (review method §3) and from the project's log, with a reason for each |
| 5 | Hierarchy and attention | the intended dominant, the route (first, second, third fixation), the number of levels, the reading mode (analytical or exploratory) |
| 6 | Rule fit | the constraints: the lens pack (§3) and the project's confirmed rows that apply |
| 7 | Portability | what should become a reusable pattern, what is unique to this screen |

Rules of the brief:

- **Read what exists first.** The product layer (`products/<slug>/product.md` or the
  repository's `.design-critic/product.md`: design system sources, components, patterns,
  hard rules), the project's `design-decisions.md`, the neighbouring screens of the same
  section, and any references the requester gave. A spec (`templates/ux-spec.md`), when there
  is one, already answers §1 and §2. The project's confirmed rows are defaults; its `decision-needed` rows are
  followed the way the neighbouring screens follow them, and flagged (never a third variant).
- **Ask only what the inputs cannot answer.** Usually the verb, the audience's state and the
  target platform. A ticket, a PRD or a user story usually answers fields 1 and 2; say where
  each answer came from.
- **Profile the verb.** Lens 04's task profiles fix the size steps, the accent axis, the rail
  and the gap ladder for the verb before any layout (lens 04 · Task profiles at a glance).
- **References are patterns, not identities.** Port the pattern the references share, keep
  the project's own components and colours (review method §8, the last row of the feedback
  table).
- **No log yet.** Build against the universal rules only. Every project-specific choice made
  along the way (a component, a colour role, a spacing ladder) is a `rule-candidate` in the
  build note, never a rule.

---

## 2. The scenario model and the state matrix — before the layout

States are designed, not discovered at review. Before composing, write the scenario model
from lens 05 (§1 Scenario coverage) at the size the job needs:

1. **Dimensions** that change the interface (persona, session, data 0 / 1 / many / corrupted,
   environment, earlier choices in the flow, local outcomes), each with a risk level
   (lens 05 · Scenario dimensions).
2. **Constraints** that remove impossible combinations (lens 05 · Scenario constraints).
3. **The state matrix**: per screen, which of the eight states in the shared vocabulary are
   required (lens 05 · State vocabulary, Required states present). Every screen that loads
   data gets `loading`, `empty`, `server_error`; every screen that accepts input gets
   `validation_error` and `success`; a screen behind a permission gets `permission_denied`.
4. **Component states** for anything new: hover, focus, active, disabled, loading, selected,
   empty, error, narrow width (lens 05 · Every component ships every state).
5. **The minimum stress set** planned per text-bearing component: longest realistic string,
   unbreakable string, zero items, 320 px width, 200 % zoom; RTL where the product localises
   (lens 05 · The reviewer's minimum stress set).

For a single component, one line per axis is enough; for a flow, the full model with
scenario cases is the deliverable a PM can hand to design and QA alike. The matrix lives in
the brief (`templates/design-brief.md`) and is carried unchanged into the build note.

---

## 3. The lens pack as constraints

Route exactly as a review does (`method/review-method.md` §2b, the table in `SKILL.md`), by
screen type and by medium, then read each loaded rule as a constraint:

| Severity of the rule | In build mode |
|---|---|
| `blocking` | a hard constraint. The artifact is not handed over while it is violated. Accessibility floors (contrast, target size, zoom, reflow, flash rate), a visible label on every input, exactly one dominant, required states present, no dead ends, honest money. |
| `warning` | a default. Follow it unless the task gives a reason not to; when deviating, write the reason in the build note (it becomes `context` at review, not `debt`). |
| `note` | a consideration. Apply where it helps; no record needed. |
| project row, `confirmed` | a default that outranks a universal `warning` or `note`, never a universal `blocking` (precedence in `SKILL.md`). |
| project row, `decision-needed` | follow the neighbouring screens; list it in the build note as an open decision. |

When two rules conflict, resolve by the precedence order in `SKILL.md` and write the
conflict and the resolution into the build note; never pick silently. For a handoff-bound
build, also walk the REQUIRED rows of the catalog sections the screen touches
(`catalog/rules-catalog.md`) and treat them as constraints.

---

## 4. Directions — when to make more than one

- **The direction is fixed** (a confirmed log, an existing section, a component to match):
  make one version.
- **The direction is open** (a new product, a redesign, "make it stylish"): make two or three
  directions that differ on **one named axis each**, and name it: where the dominant sits,
  density (the outer-to-inner gap ratio, lens 01 · The outer-to-inner ratio is a mood dial),
  reading mode, the colour budget, the motion register (lens 09 · Name the register before
  the first finding). Directions that differ on everything at once cannot be chosen between;
  they can only be liked.
- Every direction still satisfies every `blocking` constraint. A direction is a choice among
  compliant options, never a compliant one and a pretty one.
- An open choice between directions is the owner's call, presented like a `decision-needed`
  item: the options, what each optimises, the builder's hypothesis. The decision board
  (`board/`) can carry it when the options are rendered.

---

## 5. Compose — in a fixed order

Each step settles one thing before the next can blur it. Skipping ahead is how three equal
dominants and a spacing soup appear.

1. **The verb and the dominant.** Make the one thing the user came for the most contrasting
   element on the screen; decide the primary action as the screen's verb (lens 01 · Single
   dominant; lens 04 · The primary action is the screen's verb).
2. **The route.** Order zones by importance along the reading mode; plan the first, second
   and third fixation (lens 01 · Route in 0.3 s, no attention tearing; Choose the reading
   mode first).
3. **Grouping by space.** Build the spacing cascade from the project's ladder: inter-group gap
   at least 1.5× the intra-group gap; space first, surfaces second, lines last (lens 01 · The
   spacing cascade).
4. **Type levels.** As many size steps as the verb profile needs, no more; one title style
   per screen; hierarchy by weight and colour as well as size (lens 02).
5. **Colour budget.** Neutrals do the structure; one accent spent once; status colours
   consistent with the neighbouring screens; red reserved for the destructive
   (lens 03; lens 05 · Red is reserved).
6. **States and feedback.** Draw or code every state in the matrix (§2): empty with a next
   step, error with a recovery, loading that keeps the layout and names the outcome
   (lens 05).
7. **Copy.** Title is an action or a promise; the CTA names the next step; one format for
   numbers, dates and currency; real strings, never lorem ipsum (lens 07).
8. **Motion and interaction.** Only where the medium carries it: appear and disappear have a
   transition, except frequent or keyboard-driven actions; the register fits the product
   (lens 09).

Throughout, **the cheapest move first**: delete → use the platform → reuse an existing
pattern or component → correct a value → add something new (precedence rule 6 in
`SKILL.md`). **Hierarchy tools in order**: contrast → space → size → weight → colour; lines
and boxes last.

---

## 6. Per medium

### Design file (Figma or equivalent)

- Build from the project's library: its components, variables and text styles. A raw value
  where a token exists is debt the builder creates; name it in the build note if it cannot be
  avoided.
- Every state in the matrix is a frame or a variant, named with the state vocabulary
  (`<screen> · empty`, `<screen> · server_error`), placed next to the default.
- Draw the minimum stress set on real content where it can break the layout: the longest
  string, zero items, the narrowest width.
- Name frames with stable keys so the later review can cite them.
- When a design-tool integration is used (for example the Figma MCP server), follow that
  tool's own instructions for writing to the file; this method decides what to build, not
  how the tool writes it.

### Code (a component, a screen, a branch)

- Use the project's components and tokens; a literal where a token exists is the code form of
  a raw fill. Native elements first: a button is a `button`, a link is an `a`
  (catalog A-14).
- States are real branches or props, each reachable: loading, empty, errors, success,
  disabled with a reason (lens 05).
- Accessibility is written, not added later: a label for every input, focus visible,
  keyboard reachability, names and roles, target sizes, reduced motion honoured (lens 10).
- Transitions animate only what changes, with the project's durations and an ease-out;
  keyboard-repeated actions do not animate (lens 09).
- On generated or hurried UI, run the cleanup pass on the diff after the lenses, never
  instead of them (lens 13 · Cleanup pass). `scripts/ui_tells.py` lists the line-level tells
  in the changed files, each with its rule; every hit is looked at, none is a verdict.
- Render it (a dev server, a component workshop) and look at it before handing over: the
  dominant cannot be judged from code.

### A written spec (no design tool, no code)

- Deliver the brief (§1), the scenario model and the state matrix (§2), a zone-by-zone
  layout description with the dominant and the route, the copy for every state, and the
  constraint list (§3). This is the form a PM hands to design and development, and the form
  QA derives test cases from.

---

## 7. Pre-flight self-check and the build note

Before handing over, the builder runs the checks it can run on its own work. They catch
omissions; they are not a verdict.

- **The three pre-tests** of lens 01 on a render: blur (exactly one zone of highest
  contrast), grayscale (hierarchy survives without hue), name the route (first, second, third
  fixation).
- **Every `blocking` constraint** from §3, one by one: satisfied, or the artifact is not
  handed over.
- **The state matrix** from §2: every required state exists in the artifact.
- **The stress set**: which of the five cases were rendered; the rest are listed.
- **Twins**: the same string styled the same on the mobile and desktop (or variant) twins.

Then write the **build note** (`templates/build-note.md`), next to the artifact or in the
pull request description:

- the brief (or a link to it);
- the rules applied: the lens pack, the project rows followed, the catalog IDs walked;
- conflicts and how they were resolved, citing the precedence order;
- deviations from `warning` rules, each with its reason (a review reads these as `context`);
- open decisions: `decision-needed` rows followed, and direction choices for the owner;
- **needs review**: what the builder could not check (runtime, keyboard, screen reader,
  network, real content) and every rule not loaded;
- rule-candidates: project-specific choices proposed as rows for `design-decisions.md`. The
  builder never writes them into the log; the owner does.

The build note ends with the next step: a review in review mode, which input it should use
(the design file, the branch, the staging URL) and which lenses it should load.

---

## 8. Iterate on feedback

- **Translate the feedback into an axis** before touching the artifact: "cleaner" is
  redundant signals, "no air" is the outer-to-inner ratio, "a Christmas tree" is the colour
  budget (review method §8, Translating vague feedback into a named axis). Say the axis back
  to the requester in one line.
- **Change one axis per iteration**, so the result can be attributed. Re-run the pre-flight
  (§7) after each.
- **Keep the old version** next to the new one; compare by content, not by position
  (review method §9).
- **After a review**, fix what the owner marked `fix` on the decision board, in the order of
  the fix priority the owner set; a `blocking` finding is fixed regardless. Re-test on the
  same evidence that opened the finding.

---

## 9. Guardrails

- The builder does not review its own work; the self-check is a checklist, not a verdict.
- Do not invent a design system. Without the project's library or log, use neutral,
  platform-default values and mark every project-specific choice as a rule-candidate.
- Do not invent requirements. A state, a field or a flow step the brief does not justify is
  asked about, not added.
- `blocking` constraints are never traded for a direction, a deadline or a reference.
- Do not cross platforms: mobile conventions on desktop, or the reverse, only after checking
  the target (lens 12, lens 14).
- Real content, not placeholders. Placeholder copy at handoff is `blocking` when the review is
  a handoff gate.
