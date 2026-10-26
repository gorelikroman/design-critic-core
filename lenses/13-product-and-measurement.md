# 13 — Product and measurement

Checks the product layer after the screen lenses: whether the change was defined with a metric, whether it is measured on real users, whether it is fast, and whether approval rests on evidence. Order: metric and baseline → telemetry → performance (real-user monitoring) → the gate → the cleanup pass.
Pre-tests: ask for the brief's five items; open the real-user monitoring dashboard; scan the approval thread for taste words.
Static designs prove none of the performance or telemetry rows; mark them not-reviewed.

## Evidence, measurement and performance

### Define the metric before the work
- **Rule:** Every UX change defines, before work starts: success KPIs (what improves, by how much), a baseline, a validation method (A/B, fake door, usability test, cohort, phased rollout), an instrumentation plan, and a post-launch monitoring window with a rollback trigger.
- **Why:** [feedback loop] — a change with no metric closes no loop: hypotheses over opinions, observed behaviour over "what users will do"; no KPI, no claim.
- **Check:** Ask for the five items; any missing → the change is not approvable. Typical KPIs: completion rate, conversion, drop-off at step X, error rate and recovery rate, time-to-complete, support contact rate after launch, performance distributions (p50/p90/p95).
- **Severity:** blocking
- **Tells:** a brief with goals but no baseline; "we'll see how it goes"; a KPI with no target number.

### Evidence, not taste
- **Rule:** A decision that affects task effectiveness — hierarchy, flow, copy, controls, states — needs evidence, not taste: "looks good", "I have a good eye", "users will understand", "this is obvious", "the platform vendor does it" and "competitors do it" are not arguments without context and outcome data, and a decision that rests on taste alone is blocking. A purely stylistic choice that does not affect effectiveness — a corner radius, a shade within the palette, an illustration style — may be accepted on taste and is not a finding. Perceived quality is admissible only as measured evidence — rated ease, preference or first-impression tests, satisfaction after use — never as the reviewer's opinion. An unreadable hierarchy (no single dominant, no nameable route, the dominant lost in grayscale) is blocking, the same as a functional failure; a nuance-level hierarchy or dominance issue remains a `warning`.
- **Why:** [aesthetic–usability] — attractive interfaces are rated easier and forgiven more, which makes perceived quality a real outcome worth measuring and an unreliable proxy when merely asserted; an unreadable hierarchy blocks the task exactly as a functional failure does, while a taste call with no effect on the task costs nothing to allow.
- **Check:** Scan the review thread for the phrases above; for a claim that bears on effectiveness ask for the measurement, for a purely stylistic claim ask nothing more. When grading findings: an unreadable hierarchy (no dominant, no nameable route, dominant lost in grayscale) is `blocking`; a nuance-level hierarchy or dominance issue is `warning`; a functional failure (accessibility floor, clipping, colour-only meaning) is `blocking`.
- **Severity:** blocking
- **Tells:** an approval comment of taste words only on a hierarchy, flow or control decision; "premium feel" with no test; a finding argued from the reviewer's preference on something that affects the task; a radius or illustration-style debate escalated as if it blocked the task.

### Track only what answers a question
- **Rule:** Every tracked event is tied to a UX question, hypothesis or decision; unused events are removed; tracking never degrades performance or privacy. Minimum: screen views and flow steps, completion, drop-off, categorised errors, time-to-complete, search events; on mobile also retries, latency distributions on real devices, and ANRs or freezes.
- **Why:** an unobserved funnel cannot be improved, and an event that supports no decision is cost without evidence.
- **Check:** For each event: which dashboard reads it, and which decision does it feed? Static design cannot prove instrumentation; check the tracking plan or mark not-reviewed.
- **Severity:** warning
- **Tells:** a "track everything" plan; errors with no category; no mobile latency samples.

Minimum telemetry schema (recommended):

```
screen_view(screen_id, platform, locale, user_type)
flow_step(flow_id, step_id, result, reason)
action(action_id, component_id, input_method)
error_shown(error_id, category, recovery_available)
perf_sample(FMP, TTI, input_latency, blank_ms, jank_flag)
search_query(query_len, results_count, time_to_results_ms, clicked_result)
```

### Gradual rollout
- **Rule:** Critical flows ship by staged exposure with monitoring dashboards, rollback ability and explicit stop conditions that halt the rollout.
- **Why:** [layered defences] — release is part of UX safety; a rollout that cannot be rolled back has no last line of defence.
- **Check:** Is there a percentage ramp and a named stop threshold? Who watches the dashboard during the window?
- **Severity:** warning
- **Tells:** big-bang release of a critical flow; a rollback that needs a new build.

### Performance targets
- **Rule:** The numbers in the table are approval thresholds, measured with real-user monitoring at p90; synthetic measurement alone is not enough. Any visible jank, layout shift after interaction or freeze fails regardless of averages.
- **Why:** [feedback loop] — the user does not separate speed from UX; when the user wonders "is this working?", the loop is broken and the screen is bad UX.
- **Check:** Real-user p90 against the table per platform; watch lists and charts scroll on a mid-range device. Static design cannot prove any row; mark not-reviewed. Press feedback timing: lens 09 · Feedback within 100 ms, regardless of processing time; skeletons and shift: lens 05 · Loading preserves layout and names the outcome. Device targets: lens 14 · Device performance targets.
- **Severity:** blocking
- **Tells:** spinner with no skeleton; button with no pressed state; content jumping after load.

| Platform | Metric | Target |
|---|---|---|
| Desktop / web | First Meaningful Paint | ≤ 1.5 s |
| Desktop / web | Time to Interactive | ≤ 2.5 s |
| Desktop / web | Click → visual feedback | ≤ 100 ms |
| Desktop / web | Blank / empty UI | ≤ 300 ms |
| Desktop / web | Visible jank, layout shift after interaction, freezes | 0 |
| Mobile | First Meaningful Paint | ≤ 2.0 s |
| Mobile | Time to Interactive | ≤ 3.0 s |
| Mobile | Tap → feedback | ≤ 100 ms |
| Mobile | Blank / empty UI | ≤ 300 ms |
| Mobile | ANRs / freezes / visible jank (lists, charts) | 0 |
| Search (all) | Keystroke → UI feedback | ≤ 100 ms |
| Search (all) | Input → results update | ≤ 300 ms |
| Search (all) | Input → final result set | ≤ 500 ms |

### Search quality KPIs
- **Rule:** Where search exists: zero-result rate ≤ 5 %, reformulation rate ≤ 20 %, search click-through ≥ 60 %, search abandonment ≤ 15 %.
- **Why:** a user who searches more than twice for one thing was not understood the first time.
- **Check:** A dashboard for the four KPIs exists and is read. Matching behaviour: lens 11 · Search is full-text.
- **Severity:** warning
- **Tells:** search with no telemetry at all; a reformulation rate that rises after a redesign.

## Unified approval gate (one failure → no-go)

Applies to new products, major redesigns, third-party deliverables inside the product, and any change to a critical flow. No UX approval → no go-live. Each item names the entry that defines it.

**A. Intent and structure**
- [ ] One clear user intent (lens 04 · One intent per screen)
- [ ] One clear primary action; no competing CTAs (lens 04 · The primary action is the screen's verb)

**B. Defaults and simplicity**
- [ ] Defaults work; no mandatory configuration to proceed (lens 06 · Defaults must work)
- [ ] Advanced options behind progressive disclosure only (lens 06 · Simplicity over configuration; lens 04 · Layered UX)

**C. Navigation and IA**
- [ ] Primary navigation visible: tabs for 2–5 primary sections; a drawer only for six or more sections, content-heavy products or secondary destinations (lens 11 · Tabs over hamburger for primary navigation; lens 12 · Bottom tab bar or drawer)

**D. Colour discipline**
- [ ] Palette followed; defined roles only; no ad-hoc colours; colour never replaces hierarchy or stands alone as meaning (lens 03 · Defined roles only)

**E. Screen states**
- [ ] Loading · empty · error · success/confirmation — all designed (lens 05 · Required states present)

**F. Errors and recovery**
- [ ] No generic error messages; each explains what / why / next; a recovery path exists (lens 05 · Error copy answers four questions)

**G. Performance**
- [ ] Desktop, mobile and (if present) search meet the targets, measured by real-user monitoring (this lens · Performance targets)

**H. Interaction mechanics**
- [ ] Desktop: focus lands in the first field on load, never on phone widths (lens 08 · Autofocus on desktop, never on phones) · dropdowns: arrows + Enter, type-to-confirm, autocomplete (lens 11 · Dropdowns and selection) · × clears fields; password component with live requirements (lens 08 · Password fields show rules live and accept managers) · radio/checkbox: the whole row or frame is clickable (lens 11, checkbox and radio family)
- [ ] Mobile: thumb-first placement (lens 12 · Thumb reach) · safe areas respected (lens 12 · Safe areas and system bars) · charts: finger slide with pop-up values (lens 12 · Touch gets a hover equivalent) · numeric keypad for numeric fields (lens 12 · Numeric keypad for numeric input) · flow progresses top to bottom (lens 12 · Flow direction follows scroll)

**I. Formats**
- [ ] One format per product for decimals, thousands, currency, percent, date and time — locale-aware by default; a fixed house format only as a recorded project decision; no mixed formats on one screen (lens 07 · One number format per product; lens 07 · One date and time format per product)

**J. Input forgiveness and sensitive data**
- [ ] Case-insensitive; tolerates whitespace, separators, paste artifacts; intent clear ⇒ input accepted (lens 08 · Forgiving inputs)
- [ ] Sensitive input masked, minimised, never echoed in errors or confirmations (lens 07 · Sensitive data during input)

**K. Layout and platform verification**
- [ ] Adapts to all supported sizes; nothing clipped, no hidden actions; resize and rotation do not change the primary action (lens 01 · Layout adapts to the viewport; lens 12 · A critical action is never clipped)
- [ ] Desktop tested on resize and zoom; mobile on orientation change and safe areas (lens 12 · Hold structure until it breaks; lens 12 · Orientation is not locked; lens 12 · Safe areas and system bars)

**L. Measurement and approval discipline**
- [ ] KPIs, baseline, validation method, monitoring window and rollback trigger defined (this lens · Define the metric before the work)
- [ ] Approval is evidence-based; "looks good" not used (this lens · Evidence, not taste)

Global rejection triggers (any one → rejected): performance below benchmark · missing KPIs or validation plan · a generic error message exists · approval justified by taste · a key state not designed · search not full-text by default.

## Cleanup pass

Surgical, diff-scoped, behaviour-preserving. Run it on generated or hastily built UI after the lenses, never instead of them.

**Pass 1 — squint the render**, ranked by how much each gives the game away:
1. No focal point → make the one thing the user came for dominate; demote the rest (lens 01).
2. Flat hierarchy → tiers from weight plus a short colour ramp, not size alone (lens 02).
3. Monotone layout → vary density by zone, group by proximity, differentiate cards by role (lens 01).
4. Timid colour (five low-commitment tints, or one accent smeared everywhere) → one accent at about 10 %, structural neutrals elsewhere (lens 03).
5. Borders doing the work of space → spacing and surface steps; keep lines only where separation needs one (lens 01).

**Pass 2 — scan the diff** for line-level tells:
- Colour names: generic names (a numbered grey, a numbered surface, an inline hex) → semantic names; competing accents → one; decorative gradients or tints → remove, or make them mean status or action; a different hue per surface → one hue, lightness shifts.
- Typography: a defaulted face where a direction exists → the chosen face; size-only hierarchy → add weight and colour; slack heading tracking → tighten; proportional figures on updating numbers → tabular figures.
- Surfaces: harsh 1 px solid → low-opacity line or shadow; dramatic elevation → a few percent per step; off-canvas sidebar colour → same canvas plus a border; mixed depth → one strategy; equal nested radii → concentric.
- States and motion: missing hover / focus / active / disabled → add; transition-all → exact properties (lens 09 · Transition only what changes); ease-in or the default curve → an ease-out under 300 ms; no press feedback → a press state (lens 09 · Every pressable element has a press state); animation on keyboard-repeated actions → remove (lens 09 · Keyboard-initiated actions never animate); hit areas under the platform floor → extend (lens 10 · Target size). A wholly absent empty, loading or error state is build work — note it, do not patch it.
- Spacing and structure: off-grid values (17, 23 on a 4/8 base) → snap; unmotivated asymmetric padding → symmetrical; structural hacks → the clean layout.
- Reinvention: a clickable div → a button or a link; a hand-rolled overlay → an accessible primitive or the project's component; sprayed class names → a component or variant; literals → named values.

**Not slop, leave it:** a bold or unusual choice that is clearly motivated; an intentional deviation with a reason; anything outside the diff; anything a linter owns; anything the project's decisions log ratifies. Generated UI does not become good by defaulting harder: when unsure, treat it as a decision and note it.

## Glossary

- **FMP** — First Meaningful Paint: when meaningful content appears; a UX moment, not just a metric.
- **TTI** — Time to Interactive: when the UI reliably responds.
- **Jank** — visible stutter during motion or scroll. Zero tolerated.
- **Perceived freeze** — the user cannot tell whether the system is working. Zero tolerated.
- **ANR** — Application Not Responding: the Android freeze dialog. Zero tolerated.
- **RUM** — Real User Monitoring: real users, devices, networks. Required for performance approval.
- **Fake door** — a demand test run before building.
- **Gradual rollout** — staged release with monitoring, stop conditions and rollback.
- **Layered UX** — core task first, options later, configuration last; each layer optional (lens 04 · Layered UX).
- **Transactional surface** — where friction or delay directly costs revenue or trust (payments; lens 14).
