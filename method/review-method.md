# The review method — reproducible, input-agnostic

> How a design review is run so that two reviewers, or the same reviewer twice, produce the
> same findings. Not "pretty / not pretty" but **task → device → why it works**: every screen
> through the same seven-field card, every rule checked to one result on one scale, every
> finding with a location and a rule, then patterns counted across screens. The output is
> visual (pins on screenshots), the verdict is short, and the rules a project accrues live in
> the project's own log, not in the reviewer's head.
>
> Inputs can be a design file, screenshots, code, a live URL, or a device build. The
> procedure is the same; only the capture step (§2) and the lens pack (§2b) change.

---

## 0. Inputs, scaling, and when to ask

### Two purposes

1. **Check new work against the style.** Mockups, a branch, a staging URL — before handoff or
   merge. Verdict per screen: matches / deviates (where, which rule) / debt. The yardstick is
   the project's `design-decisions.md` plus the universal rules in this skill.
2. **Learn the style from existing screens.** No log exists, or it is thin. The review's job
   is to derive candidate rules from what is already shipped, so the project has a yardstick
   next time. The output is a decisions delta, not a list of defects.

### Three stages of evidence — what the input can prove

Whatever the purpose, load the product layer first when there is one (`SKILL.md` · Product
layers): its hard rules and confirmed decisions are the project's yardstick. The input fixes
what a result may claim:

- **Design-stage review** (design file, screenshots, a clickable prototype). Rules that are
  checkable statically: hierarchy, layout, type, colour, copy, declared states, labels,
  target sizes on the canvas. A static design cannot prove runtime, keyboard, screen-reader
  or network behaviour: those rules are `not-reviewed`, never `fail`.
- **Implementation review** (a URL, the DOM or code, a working build). The rules that need
  behaviour: focus order, announcements, timing, network states, motion. Test with mouse,
  keyboard, touch and screen reader where the rule's Check requires it. Visual presence of an
  element is not proof that its behaviour is correct; a finding needs observable evidence.
- **Build-time use** (the skill consulted while designing or coding, not reviewing). Select
  the lens pack first (§2b). `blocking` rules are constraints; `warning` and `note` rules are
  applied per product context. When two rules conflict, state the conflict and the resolution
  (precedence order in `SKILL.md`). End by listing the rules applied and the rules that still
  need a manual review. This is build mode, with its own procedure: `method/build-method.md`.
  When a review follows a build, read the build note first: its deviations with reasons are
  `context` candidates, its "needs review" list is where to start.

### When to ask

Ask which purpose applies only if it is not obvious from the request. "Review my screens"
with no context → ask what the screens are for (new feature / redesign / just a check). A
link to a whole file without a page or folder → ask which. No input at all → ask for it.
Otherwise start; do not front-load questions the artifact can answer.

### Scale the job

| Size | Screens | Do |
|---|---|---|
| small | 1–8 | one pass, one cluster, one visual page |
| medium | 9–30 | 2–4 clusters, one pass per cluster, one visual page |
| large | > 30 | cluster first, then one agent per cluster in parallel (same prompt, different screen ids); assemble the pages centrally; split visual pages at about 40 screens each |

One sitting = one cluster (4–8 screens). After each cluster, write the cluster file and update
the decisions delta; do not rewrite anything project-wide until the review is finished.

### Model tiers (when the run is delegated)

Card wording, judging, and the decisions delta are reasoning work: the strongest model. Capture
(screenshots, fingerprints, DOM dumps, box coordinates) is mechanical: a cheaper model or a
script. Never let the mechanical agent write the verdicts.

### The workflow in one line

Register the target → choose the lens pack (§2b) → capture (§2) → judge: one result per rule,
one tag per observation (§4) → record findings with evidence (§6) → a human reviews the
findings and assigns fix priorities (§8) → re-test after remediation, and keep the evidence.

---

## 1. Collect and cluster

1. List every top-level screen: name, id or path, size, source. From a design file that is
   the page's top-level frames; from code it is the routes or the story list; from a live
   product it is the sitemap of the flow; from screenshots it is the files.
2. Group into **clusters by user task**, not by section name or by file order: "account:
   manage subscriptions", "onboarding: choose a plan", "checkout and sign-in",
   "survey step". 4–8 screens per cluster. A cluster is what one sitting can hold in
   its head and compare.
3. Order the clusters: the project owner's most recent work first (it holds the current
   decisions, not history), then the anxious or high-stakes contexts, then the rest, then a
   mop-up cluster.
4. Write the plan table into the review's `00-method.md`:

| # | Cluster | Screens (ids) | Why in this order |
|---|---|---|---|

The plan is allowed to change on the way. When it does, record the change in the same file
(a cluster turned out to be something else; a rule was disproved mid-review).

---

## 2. Capture, per input type

The capture step produces two things per screen: **an image** to look at and **a structure**
to measure. Where an input type cannot give one of them, the card says so explicitly.

The rule, whatever the input: **numbers come from the structure, the dominant comes from the
screenshot, line length is counted.** Never read a size, a gap or a colour off the image by
eye when the structure can be read.

### Design file (Figma or equivalent)

- Screenshot at a size where 12 px text is legible → `shots/<key>-<slug>.png`. Look at it.
- Structural fingerprint, read-only, to depth 3–4: node type, name, size, component for
  instances, text style + first ~45 characters + family/weight/size for text, fill
  (**bound to a design token** vs **raw value** — raw is debt), layout (direction, gap,
  padding, bound or not), radius, stroke. Keep each read small (2–4 screens per call); long
  payloads truncate mid-stream. `scripts/figma-fingerprint.js` is the optional capture script.
- The reviewer never writes to the file. Every call is a read.
- Rules that need behaviour (focus order, announcements, timing, network, motion) are
  `not-reviewed` unless the prototype demonstrates them.

### Screenshots only

- Visual only. The card records what **cannot** be measured: exact sizes, whether colours are
  tokens, whether text uses a named style, gap values. Say "estimated" on every number, and
  keep estimated numbers out of rule-making.
- What can still be judged: the dominant, hierarchy, grouping, states shown, copy, colour
  budget, line length (count characters), consistency between twin screenshots.

### Code (a component tree, a branch, a story)

- Read the component tree of each screen; list the components used and whether they are the
  project's own or native elements.
- Read the design tokens: which colours, spacings, radii and type styles are referenced by
  token and which are literals (a literal is the code equivalent of a raw fill).
- Read the states: which variants and branches exist (loading, empty, error, success,
  disabled), which required ones are missing.
- Read the transitions: which state changes animate, with what properties, duration and
  easing, and whether reduced motion is honoured (lens 09).
- `scripts/ui_tells.py <paths>` lists line-level tells (transition-all, removed outlines,
  clickable divs, blocked zoom, literal colours, …) with the rule each points to: a list of
  places to look, not findings.
- Render if possible (a component workshop, a dev server) and screenshot; otherwise say the
  review is structural only and the dominant could not be judged.

### Live URL

- With browser tools: screenshot at desktop 1x and at a phone width; read the DOM
  (accessibility tree) for headings, buttons, labels, and state; read computed styles for the
  numbers where the tools allow it.
- Walk the flow, not just the page: reach the empty, error and success states where the
  product allows it; say which states were observed and which were not reachable.
- Test with the input the rule requires: mouse, keyboard (tab through), touch, screen reader.
  A button that is visible is not proof that it is reachable or announced.
- Note what only a live product shows: focus order, toast timing, what a refresh does to
  progress, what a back button does.

### Device build (kiosk / POS / handheld)

- Capture as for a live URL or code, at the device's native resolution.
- Name the device category (generic / unattended / handheld) in every card; a verdict that
  does not name it is incomplete (lens 14).

### What every capture records, regardless of input

- Which states were **seen**, which were **declared but not seen**, which are **required but
  absent** (vocabulary in `lenses/05-states-flows-and-errors.md` · State vocabulary).
- Which rules the input **cannot prove** — the `not-reviewed` list for the card.
- Every text string that looks like a placeholder or a leftover.
- Twin screens (mobile/desktop, variant A/B) paired by name for later diffing.

---

## 2b. Which lenses to load

Review the relevant lens pack, not every lens every time. Lenses are numbered 01–14 in
`lenses/`. Load the core pack for every screen, add by screen type, then add or drop by
input type. The catalog is the flat checklist, not a lens: it is walked by ID at handoff and
merge gates.

**Core pack, every review:** `01-hierarchy-and-composition` · `04-task-fit` ·
`05-states-flows-and-errors` · `07-copy-and-formats`.

| Screen type | Add |
|---|---|
| form, step, data entry, sign-in, checkout | `08-forms-and-inputs` · `06-choice-trust-and-ethics` · `10-accessibility-and-input` |
| choice, plan, pricing, comparison, offer | `06-choice-trust-and-ethics` · `02-typography` · `03-colour-and-surfaces` |
| list, table, catalog, detail, dashboard | `02-typography` · `03-colour-and-surfaces` · `11-components` |
| overlay: modal, sheet, drawer, popover, toast | `11-components` · `09-motion-and-interaction` (only if motion is present or the input is code) |
| empty, error, loading, confirmation, success | core pack is enough; `03-colour-and-surfaces` when status colour is involved |
| landing, longread, marketing, onboarding | `02-typography` · `03-colour-and-surfaces` · `06-choice-trust-and-ethics` |
| any screen with a phone-width twin or a mobile target | `12-mobile-and-responsive` |
| kiosk, POS, handheld terminal | `14-devices-kiosk-handheld` (only here; a device rule wins over a mobile convention) |

| Input type | Adjust |
|---|---|
| design file, screenshots | `10` static rows only (contrast, target size, labels, colour-only meaning); `09` only when the prototype shows motion; `13-product-and-measurement` only its approval-gate items; everything behavioural is `not-reviewed` |
| code | add `09-motion-and-interaction` (code proves transitions); `10` in full (keyboard, semantics, reduced motion); `11` component rows; `13` performance targets |
| live URL | add `09`, `10` in full including screen reader, `12` at phone width, `13` measurement and performance |
| device build | add `14` whatever the screen type; `12` only where the device rule does not override it |
| handoff or merge gate, any input | walk `catalog/rules-catalog.md`: the acceptance checklist and the REQUIRED rows of the sections the screen touches (A–N), cited by ID |

Pre-tests that come with the core pack: the squint test for the dominant (lens 01), the
count of styles and levels (lens 02), the states list against the scenario table (lens 05).

---

## 3. The card — seven fields, always all seven

| # | Field | What to write |
|---|---|---|
| 1 | **User task** | what the person does here and in what state (hurrying? anxious? comparing?). One verb: find / buy / read / glance / choose / decide / recover |
| 2 | **Business task** | what must happen: conversion, retention, fewer support contacts, legal cover, data quality |
| 3 | **Anatomy** | zones top to bottom with real sizes and components: header → title → blocks → CTA → footer. From the structure, not by eye |
| 4 | **Devices** | which techniques solve the task — tick from the vocabulary below so frequency can be counted later |
| 5 | **Hierarchy and attention** | where the dominant is (squint test on the screenshot), the eye route, how many levels, what recedes. Reading mode: analytical (one axis, forms, steps) or exploratory (rhyming modules, catalogs) |
| 6 | **Rule fit** | every rule checked gets a result (pass / partial / fail / not-applicable / not-reviewed); every observation gets a tag (`ok` / `debt` / `context` / `decision-needed` / `rule-candidate`). A deviation is not automatically an error (§4) |
| 7 | **Portability** | what on the screen is a reusable pattern for other sections, what is unique to this one |

The identical form is the only way to later spot a pattern: when five cards agree in field 4,
that is a rule; when one does, that is a decision for its context, or a deviation.

Template: `templates/screen-card.md`. Each row of field 6 that is more than `ok` is written
out as a finding block: `templates/finding.md`.

### Device vocabulary (field 4)

Tick what is present. Every device here exists in any product; a project extends the list in
its own log with its named components.

**Structure:** card container · row list with an action · section divider · sticky CTA ·
hero header · "breadcrumb + title" header · overlay instead of a page (popup / sheet / drawer)
· accordion · tabs · step timeline · empty state · one centered column · sticky summary bar.

**Hierarchy:** one title per screen · title centered (flow, promise) vs left (question, list)
· eyebrow / kicker above a block · hero number · price as the second hero · one primary button
· secondary as outline / ghost / text link · receding lighter and thinner · nuance inside a
module, contrast between modules · label/value inversion (small label, big answer).

**Grouping:** container as its own canvas (spacing restarts inside) · key–value stacked / row
· spec strip · benefit list with icons · chunking of long data · rhyming modules · grouping
by time · divider between "what" and "details".

**Colour:** one accent, spent once · feedback triad (surface / fill / text) · semantic status
colours consistent across screens · colour proportional to severity · danger colour reserved ·
inversion (a dark block on a light page) marking a chapter or a must-do · image dimmed to a
texture behind text · neutrals from one temperature.

**Type:** one title style per screen · lead under the title · section heading · block heading
· in-container heading · caps kicker (short labels only) · label above a value · caption for
meta and the words around a price · legal size only for legal text · the same string styled
the same on twin screens · emphasis in a paragraph by weight, not colour · line length within
range.

**States & feedback:** selected via border + tint · disabled dimmed, not hidden · status dot
→ badge → border · alert / toast · helper under a field · success helper · empty state ·
skeleton · waiting screen naming the outcome · progress (segmented rhythm or "N of M").

**Trust & anxiety:** lead-in sentence under the title · "what happens next" timeline ·
third-party trust marks · privacy sentence at the field · a named human · explicit price and
what is charged today · the cancel path next to the commitment · a number linked to its
source · addressing the user by name · context card before an action.

**Copy:** title = action or promise, not a section name · subtitle does not repeat the
breadcrumb · CTA names the next step or the reward · one currency / number / date format ·
placeholder text flagged · "(optional)" in the label, no asterisks · consequence caption on
every option.

---

## 4. Judging

### 4.1 Archetype and zones

For every screen, name its archetype (the closest entry in the project log, or the generic
type: list, detail, form, step, choice, checkout, confirmation, overlay, empty, error) and
compare zone by zone against the loaded lenses (§2b) and the project log.

### 4.2 One result per rule checked

| Result | When |
|---|---|
| `pass` | the target complies; the evidence is in the capture |
| `partial` | complies in part — some instances, some states, some breakpoints — say which |
| `fail` | does not comply; the evidence is in the capture |
| `not-applicable` | the rule's subject is not on this screen; no finding is written |
| `not-reviewed` | the input cannot prove it (static design → runtime, keyboard, screen reader, network); listed, never a verdict |

Evidence missing → `not-reviewed`, never `fail`. A rule that is contested, or whose result
depends on a choice the project has not made, keeps its observed result and is tagged
`decision-needed` (4.3). Do not confuse a rule's editorial status (accepted into the catalog
or the log) with the audit result (this target complies).

### 4.3 One tag per observation

| Tag | When | What it means for the project owner |
|---|---|---|
| `ok` | matches a rule (project or universal); say which | nothing to do |
| `debt` | deviates from a **confirmed** rule with no justification; raw values; wrong style; leftovers; placeholder copy | fix; goes to the debt table |
| `context` | deviates from a rule, and the deviation is justified by this screen's task; say why | keep; the "why" is recorded so the next reviewer does not flag it again |
| `decision-needed` | the product does the same thing two ways, or the point is already open in the log, or the rule is contested and the project has not chosen | do not judge; record which way this screen uses and add to the count. The project owner decides |
| `rule-candidate` | not in the log at all, and the device looks deliberate; describe it and where else it recurs | a proposed row for the decisions log |

### 4.4 Result → tag

| Result | Tag |
|---|---|
| `pass` | `ok` |
| `fail` or `partial` on a confirmed rule (project log) or a universal rule | `debt` — unless the screen's task justifies the deviation → `context`, with the reason written out. A `blocking` fail is always `debt`; no `context` exception |
| `fail` or `partial` where the log says `decision-needed`, or the product does it two ways, or the rule is contested | `decision-needed` — record the way this screen uses; never resolve it in the review |
| any result on a rule that is neither in the log nor universal, and the device looks deliberate | `rule-candidate` — the result is against nothing yet; describe the device and where it recurs |
| `not-applicable` | no observation is written |
| `not-reviewed` | no tag; the rule goes on the card's "not reviewed" line and into `coverage.md`; it is never `debt` |

### 4.5 Rules of judging

- **Blocking is always `debt`.** Anything at `blocking` severity in the universal rules (the
  lens entries, the catalog's REQUIRED rows at priority 1) and in the project's hard rules is
  debt with no `context` exception. Typical universal blockers: a dead end, a dark pattern, an
  undisclosed charge, wrong arithmetic in a total, a destructive action with no safeguard, an
  input with no label, a native control where the project's hard rules forbid it.
- **Every finding cites a location and a rule.** Location = node id, file path + line,
  route + selector, or screenshot + pin. Rule = a lens entry (lens number + entry name), a
  catalog ID, or a row in the project log (including its hard rules). A finding without both
  is an opinion; leave it out or mark it as one.
- **Observation, interpretation, recommendation — three separate sentences.** What is there
  (measured or seen), what it means against the rule, what to do. Never fused into one claim.
- **A recommendation is not a requirement.** Present the fix as a proposal at the finding's
  severity; only `blocking` findings state what must change. Never present a `warning` or
  `note` recommendation as normative.
- **One screen never makes a rule.** One screen = `context` or `rule-candidate`, never a new
  rule and never a `debt` against a rule that does not yet exist.
- **Where the log says `decision-needed`, follow the neighbouring screens** of the same section
  in the report and say so; never invent a third variant.
- **When two rules conflict, state the conflict and the resolution** by the precedence order
  in `SKILL.md`; never pick silently.
- **The review never edits the reviewed artifact.** No fixes in the file, no commits to the
  branch, no changes on the live product. Fixing is a separate task with its own brief.
- **Count, don't eyeball.** "Too many styles" is a count of styles; "no air" is a ratio of
  outer to inner gaps; "muddy hierarchy" is the list of levels and the contrast between them.

### 4.6 Guardrails

- **Do not invent states.** Only states visible in the design or reachable in the
  implementation are judged; a state that should exist and does not is a `required but
  absent` row, not an imagined defect in an imagined state.
- **Do not cross platforms.** Mobile conventions are not applied to desktop, nor desktop
  conventions to mobile, nor mobile-app conventions to a kiosk, without checking the target
  platform first (lens 12, lens 14).
- **Respect documented exceptions.** A lens entry's Check and Tells, a catalog card's
  exceptions, and a `context` row in the project log are part of the rule; a finding that
  ignores them is wrong.
- **Evidence missing → `not-reviewed`**, never `fail`, never `partial`.
- **One problem, one finding.** A finding may cite several rules; the same problem is never
  written twice under two rules. Identical problems across screens are one finding with
  examples (§6, the debt table).
- **Minimal repro for important violations.** Every `blocking` finding, and every `warning`
  that a human might contest, carries the shortest scenario that reproduces it: start state →
  action → what is observed.
- **Confidence is stated.** `high` when the structure or a measurement proves it; `medium`
  when read from a screenshot or inferred from code without a render; `low` when it rests on
  an assumption about the task or the platform. Estimated numbers never carry `high`.
- **The lens pack, not the whole skill.** Load what §2b routes to; a rule that was not
  loaded is `not-reviewed`, and the report says which lenses were loaded.

Severity model, and rule priority versus fix priority: §8.

---

## 5. The project rule lifecycle

The skill carries the universal laws. Everything project-specific — the archetypes, the
named components, the colour and type roles, the tolerated exceptions — accrues in the
project's own `design-decisions.md`. This is what makes the method portable: the reviewer
arrives with the method and leaves the project with a yardstick.

### The decisions log

One table per archetype (or per section, if the project has no archetype vocabulary yet):

| Decision | Why | Reference | Violations | Status |
|---|---|---|---|---|

- **Decision** — the device, stated as a rule ("status is a dot and a word; a badge only when
  there are three or more states").
- **Why** — the mechanism, one clause ("colour is spent in proportion to severity").
- **Reference** — where it is done right (ids, paths, screenshot names).
- **Violations** — where it is not.
- **Status** — `candidate` (seen in one cluster) · `confirmed` (seen on ≥ 3 screens across
  ≥ 2 clusters, and the project owner has not objected) · `decision-needed` (the product does
  it two ways; the project owner must choose).

A separate **Open questions** list at the end holds the `decision-needed` items with the
options, the score (how many screens do it each way), and, if the reviewer has one, a
hypothesis.

Template: `templates/design-decisions.md`.

### Promotion and demotion

- A `candidate` becomes `confirmed` only with **3+ screens across 2+ clusters**. Not before,
  however convincing one screen is.
- **Counter-evidence downgrades.** If a later cluster contradicts a candidate (score 2:2),
  the row moves to `decision-needed` and the open questions list gets the entry. A rule the
  project owner once pointed at is not immune: if it contradicts the confirmed rules, the
  rules win and the reference screen is listed as a violation.
- **Only the project owner promotes** rows into the project's hard rules or its handbook. The
  reviewer writes a **decisions delta** (`decisions-delta.md`): proposed new rows, proposed
  status changes with the evidence, counter-evidence to existing rows, new open questions. The
  reviewer does not edit `design-decisions.md` unless the requester is the project owner and
  asks.
- Owner confirmation is recorded in the log header with a date ("Owner confirmation
  <date>: cluster A observations correct; candidates from A are considered confirmed and
  await other clusters").

### Bootstrapping a new project

When the project has no `design-decisions.md`:

1. Copy `templates/design-decisions.md` to the project (root, `docs/`, or wherever the
   project keeps design documents) with an empty table and the status legend.
2. Run the first review in **learn mode** (§0) on the project owner's most recent, most
   trusted screens first. Every device that recurs on that first cluster is a `candidate` row.
3. Judge that first review against the universal rules only; do not manufacture project
   rules to judge against. Deviations from universals are `debt`; everything else is
   `rule-candidate` or `context`.
4. Deliver the decisions delta as the proposed first content of the log. The project owner
   accepts rows; those become the yardstick for the second review.
5. From the second review on, the project log is the primary yardstick and the universal rules
   are the floor.

The log grows by reviews, never by speculation: a row without a reference screen does not
exist.

---

## 6. Outputs

Review folder: `reviews/<YYYY-MM-DD>-<slug>/` at the project root (or wherever the project
keeps review artifacts). Contents:

| File | What |
|---|---|
| `00-method.md` | the plan table (§1), the lenses loaded (§2b), the changes made on the way |
| `NN-cluster-<X>-<slug>.md` | the cards of the cluster + the finding blocks (`templates/finding.md`) + "patterns of the cluster" (what repeats on ≥ 3 screens) + the cluster's debt table (location → what → fix) |
| `debt.md` | all debt rows in one table, sortable by cluster, with severity and fix priority |
| `decisions-delta.md` | proposed additions and changes to `design-decisions.md` (§5) |
| `coverage.md` | the scenario coverage table when the input is a flow (`lenses/05-states-flows-and-errors.md` · Scenario coverage): scenario → screens/states → covered?; plus the `not-reviewed` list per screen |
| `shots/` | screenshots, named `<key>-<slug>.png` |
| `pins.json` + the decision board | see below |

### The decision board (the default visual and decision output)

A review is not finished at a text report. Every review that finds at least one `debt` or
`decision-needed` item ends in a published decision board — not a separate optional layer,
the way findings and proposed decisions reach the project owner. The board ships with the
skill (`board/`): every screen shows its image with numbered pins linked to numbered items,
each item carries three verdict buttons (ok / fix / skip) and a comment field, each
`decision-needed` row becomes clickable options, and a sticky button exports every verdict as
JSON. The board is presentation only — the findings, their wording and severity still come
from this method (§4, §8); building it never changes a verdict.

Build it:

1. **Convert the cluster cards into `review.json`** — schema and a filled example at
   `board/examples/review.example.json`; a blank, commented skeleton showing the mapping from
   a finding's fields to the board's fields is at `templates/decision-board.review.json`.
   One item per debt row, grouped exactly as the debt table groups them (below); a
   `decision-needed` row becomes a `decisions` entry with the two (or more) ways as options
   and, when the review has one, the hypothesis as `why`. Screens keep the card's location and
   title.
2. **Images and coordinates.** Reuse `shots/` for images. Reuse `pins.json` for coordinates: a
   pin's `x`/`y`/`w`/`h` becomes the item's `boxes`. An item with no coordinate still gets a
   number, just no pin.
3. **Build:** `python3 board/scripts/build.py review.json OUT_DIR`. It prints screens / items
   / pinned / unpinned — check `unpinned` and fix coordinates or `match` prefixes before
   publishing.
4. **Publish** with the Artifact tool (load `artifact-design` first): `file_path:
   OUT_DIR/index.html`, `files` from `OUT_DIR/files-map.json`, `root: OUT_DIR`,
   `capabilities: {"db": {}, "downloads": true}`, a short distinctive title. Give the link in
   the chat report (§7).
5. **Read verdicts back** when the project owner has answered: `read_db`, `list`, collection
   `verdicts`. Apply the `fix` items and whatever the comments ask, then mark each one
   `applied: true` with a pinned `write_db batch` write.
6. **A later iteration** appends a new section with new screen ids; never reorder, delete or
   renumber a screen or an item once verdicts exist against it.

Skip the board only when the review found nothing to decide — every observation is `ok`,
`context`, or a lone `rule-candidate` with no companion pattern — and say so in the report
instead of publishing an empty page.

Two execution rules, learned the hard way:

- **Show whole screens, not abstract rule cards.** A project owner who is shown a
  generalised card cannot tell why the same thing is asked twice; the same pattern shown as
  before and after on complete screens is answered immediately.
- **Render from the real artifact, never as a mock-up.** When a finding proposes a
  change, the "after" is a real render (a clone in the design file, a branch build, a
  browser with the style patched), not a drawing of what it might look like.

### The debt table

| # | Cluster | Location | What | Rule | Severity | Fix priority | Fix |
|---|---|---|---|---|---|---|---|

One row per finding, not per screen. Identical fixes across screens are grouped in one row
with examples ("…and 4 more"). Severity comes from the rule (§8); fix priority is assigned by
a human from product context and stays empty until then.

---

## 7. The chat report

Lead with the verdict, then the three findings that matter most, then the links, then the
paths. Template: `templates/report.md`.

- **Verdict first:** how many screens, how many match, how many deviate, how many
  `decision-needed`. One sentence on the overall state.
- **Top three findings**, each with location, rule and severity. Consequential, not frequent:
  a dead end outranks twelve raw fills.
- **Link** to the decision board (§6); say in one line if the review found nothing to decide
  and so no board was built.
- **Decision-needed items are flagged as the project owner's call**, not as defects for the
  team to fix.
- **What was not reviewed:** the lenses loaded and the rules the input could not prove, in
  one line, so nobody mistakes silence for a pass.
- **Paths** to the review folder files.
- **Do not list every pin in chat.** The page holds them.
- End with the next step and the model tier it needs.

---

## 8. Severity, priorities, and the feedback → diagnosis table

### Severity

| Level | Meaning | Examples (universal) |
|---|---|---|
| `blocking` | the work is not accepted until fixed; always `debt` | dead end · dark pattern · undisclosed charge · totals that do not add up · destructive action without a safeguard · input without a label · an accessibility floor missed (contrast, target size, zoom, flash) · placeholder copy at handoff (when the review is a handoff gate) · more than one primary · more than one title · a competing dominant · an element that appears or disappears with no transition (unless keyboard-initiated or top-frequency-tier) |
| `warning` | listed by the reviewer, accepted or rejected by a human | inner gap ≥ outer gap ratio between 1 and 1.5× · required state missing · colour drift for the same status · line length outside range · red spent on the non-destructive · same string styled two ways on twins · a centered element hanging in nothing |
| `note` | worth knowing, no action required | a rule-candidate · a portability observation · a quieter alternative · folklore in a "why" |

Numeric thresholds are tells to look closer, not verdicts — except accessibility minimums,
which are floors and blocking (stated once in `SKILL.md`).

### Rule priority is not fix priority

Two different numbers; never conflate them.

- **Rule priority** is editorial and travels with the rule. In the catalog: **1** critical and
  foundational (accessibility, error prevention, data loss, task completion); **2** a
  noticeable effect on clarity, speed or ease; **3** polish, rarely blocks the task. It maps
  onto severity: REQUIRED at priority 1 → `blocking`; REQUIRED at 2–3 and RECOMMENDED →
  `warning`; CONTEXT-DEPENDENT → `note`. Lens entries carry their severity directly.
- **Fix priority** is assigned per finding, by a human, from product context: traffic on the
  screen, cost of the error, what ships next, what the fix touches. A `warning` on the
  checkout can outrank a `blocking` on an admin page nobody reaches this quarter — in the fix
  queue, never in the verdict. The reviewer proposes an order in the debt table; the project
  owner sets it.
- A finding's severity never changes to match its fix priority, and a fix priority is never
  derived from severity alone.

### Translating vague feedback into a named axis

Project owners rarely speak in rules. The reviewer's job is to translate the feedback into
the axis it is about and check that axis by count. Worked pairs from a real iteration
history:

| Feedback, as said | Diagnosis, as named |
|---|---|
| "Cleaner, more minimal, more modern" | **redundant signals**: border + badge + coloured text all saying the same thing; keep one signal per fact, separate modules by surface contrast rather than borders |
| "Go further from cards — solve hierarchy with air and typography" | **spacing-contrast** and **type steps**: remove container surfaces, then carry hierarchy with outer:inner gap ratio and a real size step between levels |
| "Contrast only on the H1, everything after gets muddy, and there's still no air" | **contrast zone** wrong for between-module levels (middle levels sat at 30–50 % "nuance" instead of 70–100 % "contrast") and **outer:inner ratio** too low; fix with a declared editorial zone (outer ≈ 2.5–4 × inner) and a size step per level |
| "Keep the alert, but less loud — maybe just a red dot" | **one status mark, three scales**: the alert strip duplicated the typographic hero at full volume; one dot before the hero, echoed in the list and the timeline |
| "The list looks like a Christmas tree of coloured pills" | **colour budget** and **status escalation**: background states as dot + quiet label, colour only on the rows that need action; and **semantic drift** — the same status was two colours on two screens |
| "The mockups are cool but there's no design — needs something stylish" | **form character**: the build sat at the pure-neutral pole; spend the budget on ONE coordinated system (one accent, one art treatment) instead of decorating several unrelated elements; choose the contour register (curvature vs angularity) for the domain |
| Four reference screenshots, no brief | **read the pattern, not the identity**: the references shared a label/value inversion (tiny caption, big answer); port the pattern, keep the project's own components and colours |

The diagnosis always names an axis that can be counted or a rule that can be cited. "Make it
nicer" is never the diagnosis.

---

## 9. Execution lessons

Recorded from reviews that cost time. Each one will cost it again if forgotten.

- **Show whole screens before/after.** Generalised rule cards get rejected; complete screens
  get decided (§6).
- **Render from the real file.** Every open question carries two real renders, cloned from the
  artifact, so the choice is made on the real thing (§6).
- **A rule keyed on a word must be scoped.** A rule written against text ("as needed",
  "weekly") will match answer chips, filter tabs and values elsewhere. Value words need a
  screen list.
- **Audit after every batch, by count.** Heuristic matching silently skips sibling layers (the
  second half of a breadcrumb in its own node). Count what changed against what should have.
- **Do not compare before/after by position.** Once styles change, text moves. Match by
  content, or read the old value from an inventory taken first.
- **Verify delegated results by grep, never by the report.** A delegated agent once spawned
  another agent, reported "started", and touched nothing. Check the files.
- **Keep tool responses small.** Long payloads truncate mid-stream. Batch about ten screens at
  a time; return counts, not samples.
- **Re-read relied-on state in a separate call.** Overrides and bindings that were set earlier
  can silently revert over a long chain of edits; before calling a screen done, read the value
  back.
- **A reference screen is not evidence against a rule.** If the project owner's reference
  screen contradicts the confirmed rules, the rules win and the screen joins the violations
  list.
- **Log gaps, don't drop them.** A pairwise gap, an uncovered scenario or a `not-reviewed`
  rule is a row with a suggestion, never a silent omission.
- **Re-test after remediation, on the same evidence.** A fix is closed by the same capture
  and the same rule that opened it, with the new screenshot or render kept next to the old.
