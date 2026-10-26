# design-critic — unification spec (v1, 2026-09-25)

This spec turns fourteen source digests (references/01…14, notes/) into ONE system. Every
merge agent follows it exactly. Anything not covered here: keep the content, ask nothing,
note the doubt at the end of your reply.

## 1. What the skill is

`design-critic` is a portable Claude Code skill that reviews any interface (design file,
screenshots, code, live URL, kiosk) against a single body of universal design knowledge, and
leaves the project with its own decisions log. It is design-system-agnostic: no fonts, hexes,
tokens, component names or brand rules. Project specifics accrue in the project's own
`design-decisions.md`, never in the skill.

Final layout:

```
design-critic/
  SKILL.md                      front door: triggers, method in brief, routing, severity, precedence
  SOURCES.md                    the only place origins and licences are named
  method/
    review-method.md            the reproducible procedure (from 06 + notes/catalog-review-protocol)
  foundations/
    perception-and-cognition.md the WHY: mechanisms, evidence levels, myths (from 01 §1 + 11)
  lenses/                       the WHAT, one file per review lens, single entry format
    01-hierarchy-and-composition.md
    02-typography.md
    03-colour-and-surfaces.md
    04-task-fit.md
    05-states-flows-and-errors.md
    06-choice-trust-and-ethics.md
    07-copy-and-formats.md
    08-forms-and-inputs.md
    09-motion-and-interaction.md
    10-accessibility-and-input.md
    11-components.md
    12-mobile-and-responsive.md
    13-product-and-measurement.md
    14-devices-kiosk-handheld.md   (optional module)
  catalog/
    rules-catalog.md            the 266 testable rules by ID (from 10), the flat checklist index
  templates/
    screen-card.md  design-decisions.md  report.md  finding.md
  scripts/
    figma-fingerprint.js        optional capture script for design-file input
```

## 2. Voice and attribution

- English. Second person is never used; the reader is "the critic" or "the reviewer".
- **No author names anywhere except SOURCES.md.** Not in headings, not in entries, not in
  "Sources" sections at the end of files (delete those sections). Names to purge: Emil,
  Kowalski, Jakub, Krehel, Jhey, Tompkins, Zantos, Akinleye, Vercel, LottieFiles, Lottie,
  rastian, Apple / WWDC (say "platform guidelines"), "the UX Book", "the catalog author",
  a product name, "the owner's" (say "the project's").
- No "lens by X". Where a source gave two numbers for the same thing (press scale 0.95–0.98
  vs 0.96; stagger 30–80 ms vs ~100 ms), give ONE range and say "range; pick per product".
- Write rules, not commentary. No "this file covers…" longer than 5 lines. No apologies.

## 3. The single entry format

Every rule in every lens file uses exactly this block. Nothing else counts as a rule.

```
### <Name in sentence case, unique across the whole skill>
- **Rule:** one or two sentences, imperative.
- **Why:** the mechanism, one clause; cite the foundation by name in square brackets when
  one applies, e.g. [crowding], [single dominant], [change blindness]. Only names that exist
  in foundations/perception-and-cognition.md.
- **Check:** how the critic verifies it: what to look at, count, measure, blur, tab through.
  Measurable when possible. Say what input types can prove it ("static design cannot prove
  this; mark not-reviewed").
- **Severity:** blocking | warning | note
- **Tells:** 1–3 symptoms, semicolon-separated.
- **Catalog:** comma-separated rule IDs from catalog/rules-catalog.md when they overlap
  (e.g. `A-03, D-07`). Omit the line when none.
```

Kebab-case ids (file 04) become sentence-case names. Names must not collide: before naming,
check the other lens files' H3s if they already exist in the folder; if a collision is
unavoidable, qualify ("Single dominant" vs "Single dominant on mobile").

Tables are allowed for numeric references (formats, targets, duration ranges) but every
table sits under an entry or under an H2 "Reference tables" at the end of the file.

## 4. Severity — one model

| Level | Meaning | Maps from |
|---|---|---|
| `blocking` | the work is not accepted until fixed; always tagged `debt` | catalog REQUIRED at priority 1; book "mandatory / forbidden"; any a11y minimum; data loss; dark pattern; dead end |
| `warning` | listed; a human accepts or rejects | catalog REQUIRED priority 2–3 and RECOMMENDED; book "guideline"; the doctrine's hierarchy rules; motion audit "Important" |
| `note` | worth knowing; no action required | catalog CONTEXT-DEPENDENT; taste; "nice-to-have"; rule-candidates |

Numeric thresholds (durations, px, ratios, percentages) are **tells to look closer**, not
verdicts — EXCEPT accessibility minimums (contrast, target size, zoom, flash rate), which are
floors and blocking. State this once in SKILL.md; entries do not repeat it.

## 5. Result and tag vocabulary (method only, not in lens entries)

- Per rule checked: **pass / partial / fail / not-applicable / not-reviewed**. `not-reviewed`
  when the input cannot prove it (static design → runtime, keyboard, screen reader, network).
- Per observation: **ok / debt / context / decision-needed / rule-candidate**.
- A `fail` or `partial` on a confirmed rule → `debt`, unless the task justifies it →
  `context` with the reason. A `blocking` fail is always `debt`.
- Every finding: location + rule name (or catalog ID) + observation / interpretation /
  recommendation as three separate sentences + severity + result + confidence (high / medium /
  low). Template: templates/finding.md.

## 6. Lens contents — what merges where

Read every listed source section in full before writing. Merge duplicates into ONE entry
(keep the strongest Rule, union the Checks and Tells, one Why). Keep everything that is
not a duplicate. Do not invent rules.

| Lens | Sources to merge |
|---|---|
| 01 hierarchy-and-composition | 01 §2 dominant & route, §3 levels, §4 reading modes · 02 §1 composition and layout · 03 §3 density axis, §4 tension axis, §5 axis hierarchy, §6 counter-form · 07 §6 layout · 12 "whole-screen questions" and "consistency beats perfection" · 08 "Visual calm and cognitive load", "Information hierarchy and density", "Layout adapts to the viewport" |
| 02 typography | 02 §2 typography · 07 §3 typography rendering · 01 "Reading eye movements", "Letters, not word shapes", "Critical print size", "Thin needs more contrast" · 03 "Caps + tracking = the utility layer's single voice", "Letter-spacing and case are tone" · 10 L (type-related rows referenced by ID, not copied) |
| 03 colour-and-surfaces | 02 §3 colour · 07 §1 surfaces and radius, §4 colour system craft · 01 "Luminance carries form", "Optical over geometric" · 08 "Colour discipline" · 12 design-direction vocabulary table (as "naming the project's direction") |
| 04 task-fit | 03 §1 task verbs, §2 six cross-cutting laws, §7 comparison and choice · 01 "Choose the reading mode first", "Rhyme" (cross-reference to 01, do not duplicate) · 08 "One intent per screen", "Layered UX", "One primary action per screen" (merge with single dominant: one entry, cross-ref) |
| 05 states-flows-and-errors | 04 §1 scenario coverage, §2 state vocabulary, §4 destructive, §5 error copy and behaviour, §6 flow structure, §7 status and feedback · 07 §8 loading and state polish, §9 stress test · 08 "Explicit screen states", "Errors and recovery", "Error visibility on submit", "Mobile states" · 03 "Forgiving design for risky and irreversible actions", "Helpful error, empty and failure messages" · 10 E, F (by ID) |
| 06 choice-trust-and-ethics | 04 §3 choice and consequence, §8 trust devices, §10 ethics · 03 §8 "Affordances are perceived", "Mental models", "Choice-architecture ethics", "No UX folklore" · 01 "Banner blindness", "Expertise reversal", "Recognition over recall", "Serial position", "Working memory", "Chunking", "Cognitive load" (these are cognition-driven UX rules; the mechanism itself stays in foundations) · 08 "Defaults must work", "Simplicity over configuration", "Consistency over creativity" · 10 M trust rows (by ID) |
| 07 copy-and-formats | 04 §9 copy · 07 §7 product writing · 08 §2 formats (both tables), "Sensitive data during input" · 10 M (by ID) |
| 08 forms-and-inputs | 08 §3 inputs and forms (all except errors, which went to 05) · 07 "Labels, autocomplete, keyboards" · 05 §9 "Never block paste, typing or zoom", "Submit stays enabled" · 10 C, D (by ID; copy the numeric rows) |
| 09 motion-and-interaction | 05 §1–8, §10–12 · 12 three motion lenses (rewrite as "three motion registers: restrained / production / playful", chosen by product type and moment, no names), Jhey entries, motion audit checklist, anti-slop tells · 13 (all) · 03 "Functional animation" · 10 N (by ID) · 08 performance targets stay in lens 13 |
| 10 accessibility-and-input | 07 §5 WCAG 2.2 essentials · 05 §9 hit areas · 01 "Fitts's law" · 10 A, J, K, L (by ID; copy the numeric floors) · 14 accessibility rows |
| 11 components | 05 §10 overlay conventions (toasts, sheets, popovers, modals, materials) · 07 §2 icons · 08 "Dropdowns and selection", "Tables and charts expose values", "Search is full-text", "Tabs over hamburger" · 10 B, C, G, H, I (by ID; one entry per component family summarising the REQUIRED rows) · 14 component rows |
| 12 mobile-and-responsive | 08 §4 mobile mechanics · 05 §11 mobile-native tells · 02 §4 responsive and longread · 07 "Breathing room, insets, bleeds, safe areas", "Hold structure until it breaks" · 10 L responsive rows (by ID) |
| 13 product-and-measurement | 08 §5 evidence and rollout, §6 performance, §7 approval gate, §8 glossary (trim) · 12 "deslop pass" (as a cleanup checklist) |
| 14 devices-kiosk-handheld | 09 as is, reformatted; header says optional |

Cross-references between lenses: `(see lens 05 · Empty state shape)` — lens number + entry
name. Never duplicate an entry across lenses; reference it.

## 7. Foundations file

`foundations/perception-and-cognition.md` merges 01 §1 mechanisms with 11 (How We See).
Structure: H2 per system (Optics and the retina · Attention and eye movements · Grouping,
figure and hierarchy · Reading · Colour · Depth and motion · Memory and load · Mental models
and expectation · Choice, risk and bias · Error and recovery · Aesthetics and first
impression · Consciousness and awareness). Each mechanism:

```
### <Mechanism name>
- **Claim:** what is known.
- **Evidence:** established | qualified | contested | myth  (from the book's own rating; "not rated" if none)
- **Design consequence:** one or two sentences; name the lens entries it drives, e.g. (lens 01 · Single dominant).
- **Myth it corrects:** if the book names one.
```

End with "## Myths and oversimplifications" (one table: Myth | What is known | What the critic does instead) and "## Glossary". The foundations file is the only place that carries citations to research; lens entries cite mechanism names, not papers.

## 7b. Canonical mechanism names (the only names allowed in [brackets])

Lens entries cite these exact names; the foundations file uses them as its H3 headings.

predictive brain · focal vs peripheral vision · gestalt grouping · gist first · pre-attentive
pop-out · faces win · optical vs geometric · crowding · luminance carries form · contrast
sensitivity · reading eye movements · working memory · cognitive load · processing fluency ·
recognition over recall · critical print size · letter recognition · Fitts's law · Hick–Hyman
law · serial position · banner blindness · expertise reversal · chunking · change blindness ·
inattentional blindness · attentional capture · habituation · vigilance · saccadic suppression
· scene gist · ensemble perception · figure–ground · depth cues · motion perception · colour
opponency · colour constancy · colour vision deficiency · metamerism · mental models · schemas
and scripts · affordance and signifier · conventions · mapping · feedback loop · forgetting
curve · spacing and retrieval · loss aversion · reference point · anchoring · availability ·
framing · defaults · choice overload · slips lapses mistakes · layered defences · warning
habituation · aesthetic–usability · first impression · symmetry and curvature · attention
networks · covert attention · load theory · cortical magnification · efficient coding ·
object constancy (added 2026-09-26 with the usability-motion techniques).

If a Why needs a mechanism not on this list, write it in plain words without brackets and
list it under "doubts" in your reply.

## 8. Precedence when sources disagree

Stated once in SKILL.md §"Precedence"; lens entries apply it silently. Order:

1. Safety, legality, accessibility minimums, data loss, honesty about money → blocking floor; nothing overrides.
2. Task fit: can the user do the screen's verb (lens 04) → over hierarchy polish.
3. Hierarchy and route (lens 01): one dominant by contrast → over craft numbers.
4. The project's confirmed decisions (its log) → over universal `warning` and `note`, never over `blocking`.
5. Craft numbers (radius, stagger, px grids, ratios) are tells; perception decides.
6. Cheapest fix first: delete → use the platform → reuse an existing pattern → correct the value → add something new.
7. Consistency beats perfection: a coherent system with imperfect values outranks scattered "correct" values, but consistency never protects a blocker.

Specific resolutions to bake in (write them as entries or as notes on entries):

- Labels: a visible label — floating or static above the field, either is fine — is the rule; a label that disappears, or a floating label that becomes unreadable once moved (below the body-size or contrast floor), is blocking.
- Autofocus on load: lands in the first field on desktop; never on phone widths, where it summons a keyboard or moves a screen-reader user unexpectedly.
- Number and date formats: locale-aware by default; a fixed house format is a project decision recorded in the log; either way, ONE format per product.
- Primary navigation: tabs when 2–5 top-level sections; a drawer is not a defect for 6+ sections or content-heavy products; the count is a tell.
- One dominant vs "one filled action": the dominant is the most contrasting element; a filled button is one way to make it; recolouring controls is never the fix when the project has another emphasis mechanism.
- Motion gaps: any element that appears or disappears with no transition is `blocking`, except a snap on a frequent (100+/day) or keyboard-driven action, which is correct, not a gap.
- Motion registers: default restrained; production polish for SaaS/tools; playful only for rare moments (onboarding, empty state, success) or products whose register is play. Bounce on a utility action is always a warning.
- Distinctiveness: a signature element must BE the dominant or sit outside its zone; it never competes with the entry point.
- Hierarchy tools order: contrast (lightness) → space → size → weight → colour; lines and boxes last.
- Density rule of thumb: inter-group gap ≥ 1.5× intra-group gap is the structural floor; the project's ladder supplies the values.
- "Evidence, not taste": a decision affecting task effectiveness (hierarchy, flow, copy, controls, states) needs evidence, blocking when it rests on taste alone; a purely stylistic choice with no effect on effectiveness (radius, a shade within the palette, illustration style) may be accepted on taste. An unreadable hierarchy (no dominant, no nameable route, dominant lost in grayscale) is `blocking`, like a functional failure (a11y, clipping, colour-only meaning); a nuance-level hierarchy or dominance issue remains `warning`.
- Blur on enter: the production-polish register's own recipe pairs opacity with a small translate and a small blur (never on body text); in the restrained register, only as a bridge when a crossfade visibly overlaps.
- Exit easing: exits use an accelerating (ease-in family) curve in every register; entrances stay ease-out.
- Hover: every hoverable element has a visible hover state; in lists, grids and groups use colour/opacity/background, never scale or movement; a single standalone element may scale slightly.

## 9. Quality bar for every merged file

- 5-line intro max: what the lens checks, in what order, with which pre-tests.
- H2 sections group entries by sub-topic; 4–12 entries per H2.
- No entry duplicated from another lens (grep the folder).
- No author names (grep the purge list in §2).
- No design-system specifics (grep: `#[0-9a-f]{6}`, font names, `token`, `--space`, `node id`).
- Every Why that names a mechanism uses a name present in foundations.
- Reply with: path, line count, entry count, severity counts, list of merged duplicates
  (which source entries became which single entry), and any doubt.
