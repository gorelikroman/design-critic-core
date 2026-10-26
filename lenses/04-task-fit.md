# Lens 04 — Task fit

Checks that the user can do the screen's verb. The critic extracts the task verb (find, buy, read, glance, choose) from the brief or the screen's evident purpose, then checks the measured profile — size gamut, accent axis, rails, gap steps — against it; then one intent, one primary action serving it, and layering; then comparison cost. Run it after lens 01's pre-tests; when task fit and hierarchy polish disagree, the verb wins.
Reading modes and rhyme are checked in lens 01 (Choose the reading mode first; Rhyme: uniformity for recognition, variety for content) and the utility layer's voice in lens 02 (Caps + tracking = the utility layer's single voice); neither is repeated here.

## One screen, one verb

### One intent per screen
- **Rule:** A screen answers one question — what is the user here to do — with supporting information allowed and competing intents not. When tasks mix, the dominant verb sets the size gamut and the accent mechanism and the secondary verb adds only its rail or its pause (a catalog with purchase = the modular ladder from *choose* plus the pre-CTA pause from *buy*), never a second hierarchy.
- **Why:** Two intents split attention and double the decisions before the first action; two full profiles on one screen mean two accents and two gamuts, a broken single dominant [cognitive load], [Hick–Hyman law].
- **Check:** State the screen's purpose in one clause; if a full sentence is needed, the screen does too much. Name the dominant verb; confirm the accent is made with that verb's axis and that the secondary verb contributed one element, not a second hierarchy.
- **Severity:** warning
- **Tells:** Two headline tasks side by side; a "dashboard" that also collects input; a settings panel embedded in a task flow; a catalog with a buy-page price spike on every card.

### The primary action is the screen's verb
- **Rule:** The one primary action performs the intent's verb; every other action is visually and cognitively subordinate, and no cluster of equal actions forces the user to decide what matters. The visual side — one dominant by contrast — is checked in lens 01 · Single dominant.
- **Why:** If two actions feel equally important, the screen is doing too much; each extra peer action is a decision added before the first one [Hick–Hyman law].
- **Check:** Name the verb, then name the action that performs it; do they match, and is it the one with primary styling? Look for clusters of three or more equal-weight buttons and for two commands that differ only in scope ("Save" / "Save & continue").
- **Severity:** warning
- **Tells:** "Save" and "Save & continue" both prominent; a toolbar of equal buttons above the content; the verb's action hidden in an overflow menu while a secondary one is filled.
- **Catalog:** B-01, B-02, B-04, G-07

### Layered UX
- **Rule:** Core task and progress first; secondary actions and options later; configuration, optimisation and edge cases last — and every layer is optional unless strictly required to complete the task.
- **Why:** Complexity must be earned, not required; users who meet complexity before value leave, and scaffolding that helps a novice is load for everyone else [cognitive load], [expertise reversal].
- **Check:** Can a first-time user finish the core task without opening any option, setting or advanced section? Count required steps before the first value. Common-case defaults and disclosure of rare options: see lens 06 · Simplicity over configuration.
- **Severity:** warning
- **Tells:** Setup wizard before first value; advanced fields inline with required ones; toggles the user cannot skip.
- **Catalog:** D-32, I-07, H-14

### One accent per screen, made with the task's axis
- **Rule:** One accent per screen, and the axis that makes it is a function of the task, not of taste: position (find) · size (glance) · size + position (buy) · size + a pause after it (read) · breaking the rhyme (choose).
- **Why:** The accent axis is what the task's reading pattern can absorb without tearing — a size accent in a flat settings table shouts, a positional accent in a dense catalog has nowhere to go [pre-attentive pop-out].
- **Check:** Name the accent and the axis that makes it; compare with the verb's row in the reference table. A second accent, or an accent on the wrong axis, is a violation; a colour accent where the task called for position is the commonest form.
- **Severity:** warning
- **Tells:** A colour accent when the task called for position; a featured catalog item made with colour instead of a rhyme break; a red badge as the only way to spot the row that needs attention.
- **Catalog:** B-04

## The five task profiles

### Find and edit: settings, tables, admin
- **Rule:** A flat size gamut of ~3 steps (meta / body / one title) — nothing shouts except navigation — with the accent made BY POSITION: broken out into a zone that is empty in every other row. A left rail (labels on one vertical, values starting on another) and no right-hand rail because values are read one at a time; few, widely spaced gap steps; the utility layer in caps + mild tracking.
- **Why:** The user already knows what they are looking for, so every extra contrast is a distraction from the scan, and a positional accent needs neither size nor weight when the counter-form gives it a place [attentional capture].
- **Check:** Count distinct type sizes (≤ 3–4). Is the "needs attention" accent placed in an otherwise empty column, or coloured / enlarged? Do labels and values each sit on one vertical?
- **Severity:** warning
- **Tells:** A settings page with a hero number; a red badge as the only way to spot the row that needs attention; values on a right rail as if compared.

### Buy: product page, plan page, checkout
- **Rule:** The widest gamut (~7 steps) — an expensive decision gets maximum dramaturgy — with the accent made by SIZE + POSITION: a diagonal reading path from the name (top-left) to the price (right-top spot), then a full pause before the single CTA. A left reading rail plus a right-top spot for the price; specs compressed into one fixation; tracking used as tone (price slightly tightened, CTA slightly loosened), not as a rail.
- **Why:** The user must be led through name → evidence → price → action in one predictable route, and a wide gamut lets every role in that route own a step [predictive brain].
- **Check:** Count size steps (5–7 expected). Trace the route: does the eye land on name, then price, then CTA? Is there an enlarged pause before the CTA, and is the CTA centred on that pause (lens 01 · A positional accent needs a counter-form)?
- **Severity:** warning
- **Tells:** Price at body size; specs spaced like benefits; a CTA glued to the last content line; two prices competing.

### Read: article, help page, longread
- **Rule:** A flat body plus a pull-quote step plus one title (~3 steps), with the accent made by SIZE + A PAUSE AFTER IT; a single column; the kicker or descriptor line carries strong caps tracking to cut through running prose. Gap steps: paragraph, inter-paragraph, section, and a full-width pause strip after the header — a counter-form with its own height.
- **Why:** Analytical reading is focal and sequential, so the body must be neutral and uninterrupted, and tempo is set by pauses, not by extra accents [reading eye movements].
- **Check:** Characters per line 40–70; one column; is the header followed by a real pause (a strip, not a gap)? Any accent inside the body beyond the pull-quote?
- **Severity:** warning
- **Tells:** Two columns of prose; coloured callouts every paragraph; no air between the title block and the first paragraph.
- **Catalog:** L-08, L-09

### Glance: home, balance, status
- **Rule:** One spike — a single hero value at roughly ×3 the body size, everything else flat — with the accent made by PURE SIZE; a right-hand rail with every number on one right edge so they can be compared, the empty run to the left of the hero number setting the reading direction toward that rail. A short, tight ladder of small gaps; feeds compressed into one fixation each.
- **Why:** The user wants one answer in one fixation and the option to compare a few numbers without reading; the two-role gamut (spike + everything else) is the fastest possible hierarchy [pre-attentive pop-out].
- **Check:** Exactly one spike? Ratio to body ~×3 (not ×1.5, not ×6)? All numbers on one right edge? Is the feed compressed below the line height of its own text?
- **Severity:** warning
- **Tells:** Three "hero" numbers of equal size; numbers left-aligned with ragged ends; a feed spaced like a form.
- **Catalog:** I-14

### Choose among similar items: catalog, plan comparison, list of options
- **Rule:** A modular ladder — sizes in a geometric progression (each step ~×1.3–1.4 the previous) so the steps RHYME — with the accent made by BREAKING THE RHYME: the featured item keeps the same skeleton and moves one step up. A right rail for the comparable numbers (price, rating); the utility layer carries the strongest caps tracking because it must cut through the noisiest content; gap steps: intra-module, between modules, between groups, a pause before the action.
- **Why:** Exploratory reading needs modules that rhyme so the eye can skip; a featured item that changes shape breaks the comparison, and the rhyme extends to sizes, not only structure [focal vs peripheral vision], [predictive brain].
- **Check:** Overlay two modules: same skeleton (lens 01 · Rhyme: uniformity for recognition, variety for content)? Is the featured item the same skeleton one step up, or a different design? Do prices / ratings share one right edge? Are sizes in a consistent ratio?
- **Severity:** warning
- **Tells:** The featured plan as a different card; prices at different x positions; type sizes with no ratio between them.
- **Catalog:** I-05, I-14

## Laws across the verbs, and comparison

### Size steps equal the roles to distinguish
- **Rule:** The number of type-size steps equals the number of ROLES the task must distinguish, not the volume of content: glance = 2, find = 3, read = 3, choose = a rhyming ladder of ~4, buy = up to 7.
- **Why:** Each step answers "what is the first / second / third fixation"; a step with no role is noise, and a missing step merges two roles.
- **Check:** List the roles the task needs; count the size steps; they should match within one.
- **Severity:** warning
- **Tells:** Seven sizes on a settings page; two sizes on a product page.

### A comparison rail appears exactly where numbers are compared
- **Rule:** A right-hand rail (all values on one right edge) appears where numbers must be COMPARED — balances, prices, ratings — and is absent where values are read one at a time (settings, details), which sit on the left rail.
- **Why:** Aligned right edges let the eye compare magnitudes without reading; a rail where nothing is compared is a false invitation [pre-attentive pop-out].
- **Check:** Are there ≥ 2 numbers the user would compare? Then one right edge. Otherwise values on the left rail.
- **Severity:** warning
- **Tells:** Prices staggered by label length; a right-aligned column of unrelated text values.
- **Catalog:** I-14

### Compression lowers priority
- **Rule:** A clumped mass reads as ONE fixation: lower the priority of specs, meta or a transaction feed by compressing their gaps below the line height of their own text. Compression is a cheaper demotion than shrinking the type.
- **Why:** Proximity groups before size is read, so a compressed block is skipped as one unit and re-entered only on demand [gestalt grouping].
- **Check:** Secondary blocks: is the inter-line gap ≤ the text's line height, or are they spaced like primary content?
- **Severity:** note
- **Tells:** Spec rows spaced like benefit bullets; a feed that reads as a list of equally important items.

### Quarantine for the irreversible
- **Rule:** An irreversible or destructive action lives in a quarantined zone: an enlarged gap before it (~×1.6 the inter-section gap), the utility layer stripped of its usual voice (a label without caps or tracking speaks in a different voice), and full-width text that cannot be scanned, only read. Friction is part of the composition; the behavioural safeguards (undo, confirmation, focus) are in lens 05 · Destructive safeguard and lens 05 · Reversible is undo first.
- **Why:** The change of rhythm and voice breaks the automatic scan and forces the deep processing route exactly where a slip would be costly [slips lapses mistakes], [habituation].
- **Check:** Find delete / cancel / close-account: is the gap before it the largest on the screen? Is its label styled unlike the other labels? Is its explanation set as a readable paragraph, not a scannable row?
- **Severity:** warning
- **Tells:** "Delete account" as one more row in a settings list; a destructive button styled and spaced like the primary.
- **Catalog:** B-07, E-14

### Comparison cost, not count of options
- **Rule:** Do not amputate functionality to hit a "magic number" of options; structure the choice instead — group options into meaningful sections (30 items in 5 groups cuts choice time with the same count), make key attributes directly comparable side by side, provide filters, sorting and search, state the trade-offs, show a sensible starting set while keeping the full range reachable, and push rare options to secondary levels.
- **Why:** Choice time grows with the log of equiprobable alternatives, but the average choice-overload effect across many studies is ≈ zero; what costs the user is the difficulty of COMPARING (task complexity, comparability, preference uncertainty, best-vs-good-enough goal), so three badly explained plans are harder than ten transparent ones [Hick–Hyman law], [choice overload], [working memory].
- **Check:** For a long list: grouped? Attributes aligned so they can be compared without holding them in memory? Filters and sort present? Trade-offs stated? Was anything removed "to simplify"?
- **Severity:** warning
- **Tells:** A flat list of 20 plans; plans whose attributes are in prose so the user must remember them; a "simplified" set that hides the option the user needs.
- **Catalog:** D-23, D-24, G-13, H-13, I-11

### Side-by-side comparisons stay at most four columns
- **Rule:** Compare at most four items side by side; beyond that, paginate, filter or compare in pairs.
- **Why:** Working memory holds ~4 chunks, so a fifth column forces the user to re-read [working memory].
- **Check:** Count comparison columns on the widest breakpoint.
- **Severity:** warning
- **Tells:** A six-plan comparison table; a carousel of comparable cards with no way to fix two of them.

## Reference tables

### Task profiles at a glance

| Verb | Typical screens | Size steps | Accent axis | Rail | Gap ladder |
|---|---|---|---|---|---|
| Find (and edit) | settings, tables, admin | ~3 | position: an empty zone in every other row | left — labels on one vertical, values on another; no right rail | few, widely spaced steps |
| Buy | product, plan, checkout | ~5–7 | size + position: name top-left → price right-top → pause → CTA | left reading rail + right-top price spot | specs compressed; full pause before the CTA |
| Read | article, help, longread | ~3 | size + a pause after it | single column | paragraph · inter-paragraph · section · pause strip after the header |
| Glance | home, balance, status | 2 | pure size: one spike at ~×3 body | right — all numbers on one right edge | short, tight ladder; feeds compressed to one fixation |
| Choose | catalog, plan comparison, options | ~4, geometric (~×1.3–1.4) | breaking the rhyme: same skeleton, one step up | right rail for comparable numbers | intra-module · between modules · between groups · pause before the action |
