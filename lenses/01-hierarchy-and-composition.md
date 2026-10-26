# Lens 01 — Hierarchy and composition

Checks that the screen has one entry point, an obvious route, readable levels, a spacing cascade that groups before anyone reads, and a reading mode it holds. The critic runs three pre-tests first — blur / squint (exactly one zone of highest contrast?), grayscale (does the hierarchy survive without hue? see lens 03 · Salience survives grayscale), name-the-route (first, second, third fixation; would two reviewers agree?) — then the sections below in order: the dominant and the route, axes and alignment, levels, the spacing cascade, reading mode and rhythm, whole-screen coherence.
Findings are measured against the screen's declared intent and density (a dense tool is not failing for being dense) and the project's own decisions, never a generic ideal; under every entry the question is whether the author decided or defaulted.

## The dominant and the route

### Single dominant
- **Rule:** Exactly one entry point per screen — the single most contrasting element — so at most one solid-primary action and one top-level title, everything else stepping down in a clear hierarchy with no simultaneous emphasis. The dominant is defined by contrast, not by component: a filled button is one way to make it, and recolouring controls is never the fix when the project has another emphasis mechanism.
- **Why:** Attention lands where contrast is highest and the entry point is decided in ~0.3 s, before reading; two equal dominants tear attention [pre-attentive pop-out].
- **Check:** Squint or blur: exactly one zone of highest contrast, and nothing jumping out harshly? Count primary-styled buttons and top-level titles; look for clusters of three or more equal-weight actions. The one legitimate exception: a hero number and its phrase that read as one sentence. A static design proves this fully. The task side of the primary action is in lens 04 · The primary action is the screen's verb.
- **Severity:** blocking — for two filled primary actions, for two top-level titles, and for any other competing dominant
- **Tells:** Two filled buttons, or "Save" and "Save & continue" both prominent; a hero image, badge or banner louder than the title or CTA; badges, banners and filled buttons all shouting at once; a toolbar of equal buttons above the content.
- **Catalog:** B-04

### Hierarchy tools in order
- **Rule:** Build emphasis in this order and stop at the first rung that works: contrast (lightness) → space (isolation) → size → weight → colour, with lines and boxes last. Promote by demoting — secondary actions ghosted, metadata muted; promotion without demotion is not hierarchy.
- **Why:** Hierarchy is read from lightness patches before objects are recognised, so lightness and isolation cost nothing while colour, lines and boxes add figures that compete [luminance carries form], [gist first].
- **Check:** Name the focal element and the one tool that makes it win (contrast, isolation, size, weight, colour). List what was demoted. Can primary, secondary and metadata be told apart without reading the words? Count colours, lines and boxes doing hierarchy work that lightness or space could do.
- **Severity:** warning
- **Tells:** Size-only tiers (15 / 16 / 17 mush); colour used to separate sections instead of spacing; bold everywhere; every card with a coloured header; a flat screen where nothing was demoted.

### Contrast and air before size
- **Rule:** Make the entry point the most contrasting element, not necessarily the largest; to make an element read bigger, reduce its surroundings and add air rather than inflating it until it merges with its neighbours. Do not oversize type and elements so they read on a zoomed-out canvas — restrained type with a few small satellites reads as more elegant.
- **Why:** A small high-contrast element beats a large low-contrast one; perceived size is relative, and an inflated element loses the air that isolates it as a figure [figure–ground].
- **Check:** For the intended dominant, name its contrast to its surroundings (lightness, isolation, weight); if it relies on size alone, verify it does not merge with its neighbours. Does the dominant have more air around it than anything else, or is it merely bigger? Is the type sized for the viewing distance or for the designer's zoom level? Is there anything small on the screen at all?
- **Severity:** warning
- **Tells:** Everything enlarged, nothing stands out; huge pale hero text touching the edges; a full-bleed CTA with no breathing room; oversized body on a phone.

### Route in 0.3 s, no attention tearing
- **Rule:** The layout presents an obvious route — entry, second, third — with no two elements competing as equals; then each block either HOLDS attention (closed composition: frames, return verticals, loops) or PASSES it on (open composition: a line, diagonal, cropped image or air pushing beyond the block). Dense is fine; chaotic is not.
- **Why:** The periphery decides where the eye jumps next and the user judges the route before content; open composition leads to a next section, closed keeps the user on one block [focal vs peripheral vision].
- **Check:** Name what is seen first, second and third; are they the right three, and would two reviewers agree? Shrink the screen to a thumbnail: can the first and second landing still be named? Mark each block open or closed; is that the intent? If the main point takes two scans to find, hierarchy failed.
- **Severity:** blocking when no route can be named or attention visibly tears between two or more equal elements; warning for a weaker ambiguity (the route exists but is slow to read)
- **Tells:** Six equal cards ("dashboard soup"); the eye hops between layers; nobody can say what comes second; a closed frame around a block that should hand off to the next.

### Distinctiveness sits outside the entry point's zone
- **Rule:** A signature element (illustration, brand device, display type, a face) must either BE the dominant or sit outside the dominant's zone; it never competes with the entry point. Spend character on a second layer — illustration, type, voice, rhythm — over a fluent skeleton, never on the function of a control.
- **Why:** Novelty is felt as character only when the function already reads instantly; a face or a strong device fires before the intended dominant and steals the first fixation [processing fluency], [faces win].
- **Check:** Does the screen look like this product rather than every other one? Then: where does the eye go first — the signature element or the intended dominant? Is any face, illustration or brand device inside the zone of the primary action or title? List every departure from the genre; each must sit in character, not in function (how to close, where the primary action is).
- **Severity:** warning
- **Tells:** A hero portrait beside a CTA nobody sees; a "clever" close or navigation; an interchangeable dashboard with nothing to notice at all.

### Order by importance; do not overload the entry point
- **Rule:** The most important content sits near the top and the leading edge; within a row, identifying content leads and metadata and actions trail; the one number the user came for is never buried under secondary detail. The first screenful is a table of contents, not the whole book — secondary actions go behind a menu once they exceed two or three, a short view that links deeper beats a long view that shows everything at level one, and each control sits near what it affects with controls arranged to mirror what they change.
- **Why:** If everything is prominent nothing is; proximity implies relationship, and a control whose position mirrors its effect needs no label [gestalt grouping], [mapping].
- **Check:** Cover the screen and reveal it top-down: is the first thing seen the thing the user came for? Count peers at level one. For each control, measure its distance from what it changes; if a label is needed to explain the control, the mapping is weak. Layering of the task itself: see lens 04 · Layered UX.
- **Severity:** warning
- **Tells:** The balance in small text below account metadata; five equally weighted actions in a header; a toggle far from the thing it toggles.
- **Catalog:** I-04, I-07, B-17

### Direction devices
- **Rule:** A diagonal or triangle drives the eye DOWN; a corner (horizontal + vertical) sets a vector; an extra vertical axis pulls the eye back up and closes the block; a cropped image or a line running off the edge opens it. Down is more natural than up.
- **Why:** Force lines and vectors are read before objects are recognised; the cultural scan runs left to right, top to bottom, and a "flying" object reads as falling [gist first].
- **Check:** For each device present, does it point where the flow wants to go? Any diagonal aimed away from the next section? Any hero subject looking off-screen, away from the content?
- **Severity:** note
- **Tells:** A hero subject looking away from the content; diagonals running up and out.

### Image leads, text follows
- **Rule:** In an image + text pair the image is the entry point; text goes after it on the scan path — below or to the right — never above or to the left.
- **Why:** Images are read faster and grab attention first, and the scan runs left to right, top to bottom, so text placed before the image is skipped [gist first].
- **Check:** For each pair, where is the text relative to the image?
- **Severity:** warning
- **Tells:** A caption above a photo; a text column to the left of a large image in a card.

### Prototypical layout, moderate colour, low incidental complexity
- **Rule:** The layout looks like its genre; colourfulness is moderate; what is minimised is INCIDENTAL complexity — heterogeneity, weak grouping, competing accents, irregular alignment, no repeating structure — never the content itself.
- **Why:** Appeal is judged in ~50–500 ms from colourfulness, visual complexity and prototypicality; ten aligned rows are simpler than three unrelated blocks [first impression], [processing fluency].
- **Check:** Count distinct alignment systems, accents and block types on the screen. Does it look like its category (a checkout looks like a checkout; see lens 06 · Conventional things in conventional places)?
- **Severity:** warning
- **Tells:** A sparse but chaotic screen; a screen stripped "to look clean" while its three blocks still don't relate; a rainbow, or dead grey.

## Axes and alignment

### Force lines and the central axis
- **Rule:** Even an empty format carries four edge force lines and a central axis; sit content ON them — margins along the edges, key elements on the axis — never slightly off.
- **Why:** The mind halves the format and halves again, so corners and centre are anchors, and vertical and horizontal edges are detected most strongly.
- **Check:** Overlay the centre line and the margins; do key elements sit on them, or a few px off ("drifting toward the edge"; "the lines are stronger than the axis")?
- **Severity:** warning
- **Tells:** A "centred" hero a few px off; elements near but not on the margin; no usable axis at all.

### Alignment as route
- **Rule:** Aligned elements read as one line and one relationship: pick a small set of shared edges (a common left, centre or right axis) and put everything on them, with one spacing step per level of subordination repeated for deeper nesting; never scatter unique offsets. Use logical start / end properties so direction-dependent layout mirrors in RTL, reserve physical sides for physical geometry (notch, gesture direction), and mirror sequence indicators (steps, stars, progress) but never digits.
- **Why:** The brain sees a line where only edges align, and an edge a few px off is felt before it is seen; breaking the line tears attention [gestalt grouping].
- **Check:** Draw vertical guides through the leading edges of a column and count distinct edges; near-but-not-equal offsets (a few px) are the worst case. Check that each nesting level uses one consistent step (one step, e.g. 16 px, where no scale exists). Switch to RTL and look for un-mirrored layout — a static design proves the edges, a build proves RTL.
- **Severity:** warning (blocking when the offset breaks a label / value pairing)
- **Tells:** Icons, labels and values each on their own x; header, list and footer at three different insets; a centred block inside a left-aligned page; hand-positioned elements that stay put in RTL.
- **Catalog:** M-08, I-14

### Force-line continuity across scroll
- **Rule:** Keep organizing lines few and let each section's line carry over into the next: one block's axis leads and the next block's axis overlaps it so the eye steps onto it like a second rail. Do not relocate the axis abruptly from section to section.
- **Why:** A line that ends into empty space while the next section's axis sits somewhere unrelated reads as jumpy; this is the page-level twin of alignment [gestalt grouping].
- **Check:** Draw the main vertical (or horizontal) of each section down the page; do they overlap or hand off, or jump?
- **Severity:** warning
- **Tells:** Centred hero → left-aligned form → right-aligned pricing → centred footer; every section its own alignment.

### No axis conflict
- **Rule:** One organizing axis per screen. A dominant image or element with a strong internal axis (diagonal, horizon, directional subject) must not fight the layout's axis: align it, or let it set the axis and align the rest to it.
- **Why:** Competing axes make attention impossible to direct; the eye hops layer to layer and reads it as overload [cognitive load].
- **Check:** Draw the layout's axis and the hero's internal axis; do they agree? Do two adjacent columns have compositions that "don't get along"?
- **Severity:** warning
- **Tells:** A diagonal product shot inside a strictly vertical form; a horizon in the hero cutting through the title.

## Levels of hierarchy

### Contrast between, nuance within
- **Rule:** Strong contrast BETWEEN modules (the hierarchy, the dominant); NUANCE within a module — small, barely visible differences that refine without competing; IDENTITY across repeated modules (rhythm).
- **Why:** Internal contrast competes with the dominant; one pop-out per zone is all the eye can rank [pre-attentive pop-out].
- **Check:** Inside one card, count elements that differ strongly in lightness or size; more than one strong contrast inside a module is a violation.
- **Severity:** warning
- **Tells:** A coloured badge, a bold price and a dark icon all shouting inside one card; every card a mini-poster.

### Farther is lighter, thinner, cooler
- **Rule:** Build hierarchy with weight, lightness and temperature, not size alone: secondary elements are dimmer, thinner and cooler, not smaller; what is closer is more saturated, heavier, warmer.
- **Why:** Lightness, weight and warmth are read as distance and the brain decodes them honestly [depth cues].
- **Check:** For each secondary element, is it lighter or thinner than the primary? Is any recessive element warmer or darker than the dominant?
- **Severity:** warning
- **Tells:** Meta text in heavy black; captions at body weight; a warm accent used as a background layer.

### Depth by position, one depth relationship
- **Rule:** Elements pinned to the frame edges read as flat (anchored to the plane); an element floating off the grid near the centre reads as a separate depth layer. Use at most ONE spatial relationship per screen (plane + depth, or plane + height), never three stacked planes.
- **Why:** Depth is read relative to the plane; three simultaneous planes are hierarchy dissonance — hard to focus, a sense of disorder [depth cues].
- **Check:** List layers by apparent depth (shadow, scale, blur, position); more than two levels is a violation. Edge-anchored elements should not carry big shadows.
- **Severity:** warning
- **Tells:** A floating card, a floating action button and a floating toast at three elevations; shadowed elements glued to the edge.

### Space builds structure, size builds significance, form builds affordance
- **Rule:** The axes are not interchangeable: space and proximity build STRUCTURE (what relates to what) and cannot be replaced by size; size builds SIGNIFICANCE (the order of fixations), works in both directions (lowering meta as much as raising the dominant) and cannot group; form (background, border, control shape) builds AFFORDANCE, which neither size nor space can express.
- **Why:** Hierarchy without spacing collapses into a game with sizes, and text-only layouts lose their controls, which read as random lines until form is restored [gestalt grouping], [affordance and signifier].
- **Check:** For each defect, name the axis it belongs to: a grouping problem is fixed with space, not size; an importance problem with contrast or size, not gaps; an "is this clickable?" problem with form, never with size.
- **Severity:** note
- **Tells:** Trying to group with size; trying to signal interactivity with air; enlarging the dominant instead of isolating it.

### Controls read as controls; content reads as content
- **Rule:** Every interactive element carries a signal — background shape, border, underline, or placement in a consistent control zone — and the inverse holds: a static badge shaped like the buttons beside it collects dead clicks.
- **Why:** A control styled like the text next to it is invisible; a non-control styled like a button lies [affordance and signifier].
- **Check:** Squint at the screen and list what looks clickable; compare to what is. Do interactive and static siblings (chips, tags) share identical styling? A primary action with no signifier at all is blocking under lens 06 · Affordances are perceived, not physical.
- **Severity:** warning
- **Tells:** "Upgrade now" as plain grey text; pill tags that look like buttons.
- **Catalog:** A-11, A-19, A-20

### Counter-form is a designed object
- **Rule:** Emptiness has width, height, proportion, a centre and edges; its first job is separation, its second is direction (air on one side pushes the eye toward the content). Active air does a job; passive air is left over.
- **Why:** Form and counter-form are inseparable: without air the brain cannot isolate a shape and the dominant must be over-forced with contrast, while squeezed air becomes a figure of its own ("ringing air") [figure–ground].
- **Check:** For every empty zone larger than a gap, name what it does (separates X, directs to Y, pauses before Z); "it just happened to land there" is passive. For accents, run the counter-form test in the next entry.
- **Severity:** note
- **Tells:** Unequal leftover strips; crosses of air between tiles that read as a grid; a dominant crowded until it needs colour to be seen.

### A positional accent needs a counter-form
- **Rule:** Break out only into a place there is somewhere to break out into: a centred or broken-out element is positioned against a named empty shape — its edges, its centre, its proportion — and sits on the OPTICAL centre of that strip, not on the section or the grid. In a dense grid with no empty zones a positional accent is impossible; use size instead — a constraint, not a choice.
- **Why:** Counter-form is a plane, just white, and inherits the frame and plane tests; an element hanging in nowhere has no relationship to read and tears the route [figure–ground].
- **Check:** For every centred or off-grid element, name the empty shape it stands against (width, height, centre); cannot name it = violation. Is the element on the optical centre of that shape?
- **Severity:** warning
- **Tells:** A CTA centred on the page while the content column is left-aligned; a badge floating between two rows with no zone of its own; a centred element in a dense table.

## The spacing cascade

### Outer gap beats inner gap
- **Rule:** The gap BETWEEN modules is clearly larger than any gap INSIDE a module (letter → word → line → paragraph logic): inter-group ≥ 1.5× intra-group is the structural floor, the project's ladder supplies the values, and a card never has an internal gap larger than the gap to its siblings. However dense the screen, outer gaps keep their floor — density is made from the INSIDE (module contents, typography, component paddings), never by shrinking the gaps between modules.
- **Why:** Peripheral vision groups the layout by proximity before any fixation; when inner gaps compete with outer ones the boundaries disappear and modules merge into one [gestalt grouping], [focal vs peripheral vision].
- **Check:** Merge test — without reading, is it obvious where one card or section ends and the next begins? Measure the largest inner gap against the gap to the neighbour, and the smallest inter-module gap on the screen; on a dense screen expect the ratio to rise (≥ ~3) because the inside compresses while the outer floor holds.
- **Severity:** blocking when modules visually merge or the inner gap ≥ the outer gap; warning for a ratio between 1 and 1.5
- **Tells:** Cards that read as one continuous list or one grey mass; a section heading closer to the previous section than to its own content; a list whose items and groups share one gap.

### The outer-to-inner ratio is a mood dial
- **Rule:** Above the floor, choose the outer / inner gap ratio from the task's mood: ~2 is the clear default; ~2.5–4 is airy and premium (landings, editorial); dense tools sit near the floor and gain density inside their modules. Never at or below 1.
- **Why:** The ratio sets how strongly the periphery separates modules; the mood of a screen is largely this one number [gestalt grouping].
- **Check:** Compute the ratio for a representative module, state the zone, and compare with the declared mood, the task verb (lens 04) and the density the viewport can carry.
- **Severity:** warning
- **Tells:** A "premium" landing at ratio 1.3; a dense data table at ratio 4 that falls apart.

### The airy end breaks cohesion
- **Rule:** However airy the screen, inner gaps have a CEILING, both relative (a healthy ratio is not enough) and absolute (on a phone-width screen an inner gap past roughly a dozen px breaks the link between lines regardless of ratio); grouped lines also have a role-based leading ceiling. All added air goes to OUTER gaps and margins; module interiors stay under the ceiling.
- **Why:** At the loose end the lines of one module scatter and the block stops reading as a unit [gestalt grouping].
- **Check:** Cohesion test — does each module read as one whole, its lines closer to each other than to the neighbour? Is any inner gap above the absolute ceiling?
- **Severity:** blocking when a module falls apart; warning for inner gaps above the ceiling
- **Tells:** A title and its meta reading as two separate items; an "airy" card whose lines are as far from each other as from the next card.

### The gap gamut: adjacent steps differ by 1.5×
- **Rule:** A mature composition carries a SCALE of distinct space steps, one per level of the meaning hierarchy (merge / lines / controls / positions / macro-planes): inside one canvas, gap inside a molecule < gap between molecules < gap between groups, adjacent steps differ by at least ~1.5×, and the ladder never skips a level. The top step is a full-width dramaturgical pause — a counter-form with its own height, placed before the dominant — that divides the screen into planes of meaning before reading starts.
- **Why:** Space is read as levels only when adjacent steps are distinguishable; two nested levels sharing a value make the grouping invisible, and a pause is only a pause when it is far beyond the working gaps [gestalt grouping].
- **Check:** List every distinct gap value inside a card and on the page and sort them; each must map to a distinct level, no two nested levels may share a value, and any adjacent pair below ~1.5× (two values a few px apart) is a flag. Confirm the largest strip is ≥ ~1.5× the next gap and sits before the dominant, not after the footer.
- **Severity:** warning
- **Tells:** Label ↔ value gap equal to the gap between pairs; list rows spaced like the list's gap to its heading; six gap values, two of them indistinguishable; a "pause" that is just a bigger section gap ("no dramaturgy").

### Space first, shapes second, lines last
- **Rule:** Group by proximity first (related close, unrelated far); use a background shape only when a group must act as one unit (selectable row, draggable card); draw separator lines only where space is too expensive (tables, long settings lists), hairline and quiet, never combined with a gap that already did the job. A divider, border or box earns its place only by functional work.
- **Why:** Proximity is the cheapest grouping there is; the mind already sees the implied line, so a drawn one is clutter and a false figure, and uniform spacing plus lines to compensate reads as noise [gestalt grouping], [figure–ground].
- **Check:** For every divider, border and box, remove it mentally: does the grouping survive? If yes, it is redundant. Measure intra- and inter-group gaps; count separators that a gap would replace.
- **Severity:** warning
- **Tells:** A card in a card in a bordered section; a divider under every list row that is already spaced; every field with a bottom border and equal spacing; everything outlined; colour used to separate sections instead of spacing.

### The canvas law: a bordered surface is its own canvas
- **Rule:** A surface with a visible boundary (fill or border) opens a new canvas: its padding is its own page margin and is ≥ its largest inner gap, the spacing ladder restarts inside it from the smallest step, and a nested surface is never airier than its parent (a small plane has a small budget). A group WITHOUT a surface opens no canvas and follows the parent's ladder; because the border already separates, sibling cards sit close, a set of cards reads as one organism, and generous air lives only between screen sections.
- **Why:** The boundary does the separating — air added on top of a border double-encodes the same grouping and pushes cards apart until they stop reading as a set — and every surface is a new viewport with its own cascade [gestalt grouping].
- **Check:** Between sibling cards: a small gap? Between sections: the largest gap on the screen? Inside a card: padding ≥ the largest inner gap, and the ladder restarting from the smallest step? A card inside a card: is the inner one at least as dense? Surface-less groups: do they follow the page's ladder?
- **Severity:** warning
- **Tells:** Section-sized air between two cards of a set; a card whose internal air matches the page's section air; a tiny card with generous inner air; a "card" that is only a gap, treated as if it had a border.

### Frame test: the screen is a participant
- **Rule:** Page margins are the outermost inter-module gap (composition ↔ frame): they grow with the inner rhythm and stay ≥ ~0.5× the inter-module gap. The viewport budgets how airy a screen can be — a narrow screen has a lower airy ceiling than a wide one, and a nested plane's budget is smaller than its parent's.
- **Why:** If margins are smaller than the internal air, content is closer to the edge than to itself; the composition sticks to the frame and creates unintended tension [figure–ground].
- **Check:** Measure side margins against the inter-module gap. Is any content closer to the frame edge than to its own neighbours? Compare the declared density with what the viewport can carry.
- **Severity:** warning
- **Tells:** Generous air between blocks with content jammed to the edges; a mobile screen trying to be as airy as its desktop twin; airy inner blocks with thin side margins on a phone.

### Tension is the width of the gap spectrum
- **Rule:** Measure a screen's tension by its gap spectrum: identity is one gap everywhere (1×), maximum is a wide range from micro-merges to macro-pauses (tens of ×). Grow tension by SEPARATING the poles — tighter merges against larger pauses — not by shifting all values together.
- **Why:** Contrast in space is a difference of potential like any other contrast; a uniform rhythm is stasis, a wide spectrum is drama.
- **Check:** List the distinct gap values; compute largest ÷ smallest; compare with the declared tension (calm ≈ narrow spectrum, tense ≈ wide).
- **Severity:** note
- **Tells:** A "tense" hero laid out on one uniform gap; a calm settings page with a hero-size pause.

### Operations are introduced in a fixed order
- **Rule:** Build tension in this order and no other: (1) proximity — the inner / outer distinction; (2) rhythm differentiation — merge related blocks, grow the pauses around them; (3) asymmetry within a unit — merge title + meta, set the price apart; (4) position and rails — corners, guiding axes, a diagonal reading path — the most expensive move, used only at the extreme. On meaningful text the first move is outward only: readable lines group themselves by meaning and need less spatial help than a mute mass.
- **Why:** Each step relies on the previous one being readable; skipping to rails without proximity produces scatter, not tension.
- **Check:** If rails or corner spreads are present, are proximity and rhythm already clear underneath them?
- **Severity:** note
- **Tells:** Elements spread to the corners of a card whose inner grouping is still uniform.

### The extremes restructure, not just re-number
- **Rule:** At both ends of the density axis the composition changes structurally: controls cluster together with a small step and an enlarged gap before the content. Expect and allow structural moves at an extreme; do not expect a pure scaling of numbers.
- **Why:** Proximity is the primary axis; pushing it far forces regrouping [gestalt grouping].
- **Check:** At a declared extreme, are controls grouped and separated from content, or scattered at the old positions with bigger or smaller gaps?
- **Severity:** note
- **Tells:** A "dense" variant that is the base layout uniformly shrunk.

### The extreme scouts, the final domesticates
- **Rule:** The most extreme step of any axis reveals the technique in raw form (diagonal scatter, very strong tracking); the working form lives one step below the maximum, tamed into a system (calm rails, mild tracking by role). Ship the domesticated form.
- **Why:** Extremes are for discovering the move; production must keep the move legible and repeatable.
- **Check:** Does the screen read like the extreme (technique on display) or like the tamed version (technique in service)?
- **Severity:** note
- **Tells:** Diagonal layouts in a form; tracking that draws attention to itself.

### Density moves type by weight and tracking, not size
- **Rule:** Moving along the density axis changes display weight and tracking (dense: heavier, tighter; airy: lighter, looser) and role-based line heights (captions breathe more, multi-line headings stay tight); type SIZES stay stable.
- **Why:** Size changes the role ladder, while weight and tracking change tone without touching hierarchy (see lens 02 · Tracking is a tone knob, never a fit tool).
- **Check:** Compare a dense and an airy variant: are sizes identical while weight, tracking and leading differ?
- **Severity:** note
- **Tells:** An "airy" version made by enlarging type; a dense version made by shrinking headings below their role.

## Reading modes, rhythm and the grid

### Choose the reading mode first
- **Rule:** State the mode before composing — ANALYTICAL (text, forms, step flows): a bearing line, tension on one or two vertical axes, dominants appearing predictably along them, tempo alternating (after a dense block, a rest); EXPLORATORY (catalogs, dashboards, grids): dispersed attention, modules that rhyme, movable but expected accents, a simple grid with a clear scaling logic; COMBINED: the format split into a fast zone (theses, highlights, quotes — the most contrasting layer, scroll-driven) and a slow zone (a narrow body column plus a descriptor column), visibly separated. Never mix fast and slow content in one zone.
- **Why:** Analytical reading is focal and sequential and tires without rests; exploratory reading uses the periphery — the user does not know what they want, so the system must work without their participation [reading eye movements], [focal vs peripheral vision].
- **Check:** Name the mode. Analytical: can the bearing line be drawn and the rests pointed to? Exploratory: do modules share one skeleton with content-only differences, and are accents placed by a repeatable rule? Combined: are the zones separated? Then confirm the mode fits the task verb (lens 04).
- **Severity:** warning
- **Tells:** A form laid out as a mosaic; a catalog with a different composition per card; a longread with no image or pause for many screens.

### Layout order fits the reading mode
- **Rule:** Pick the layout order that carries the chosen mode: CENTRAL-AXIS (one vertical axis, symmetric, static, passive space — single-message pages); BLOCK (symmetric floors on a horizontal line, accented forms — editorial storytelling); MODULAR (asymmetric card grid on a horizontal line, active space, rhyming modules — catalogs, dashboards); BEARING (asymmetric, dynamic vertical bearing line — text-heavy longreads and step flows).
- **Why:** Each order is a profile on five axes (symmetry, movement, form, space, organizing line); symmetry reads slow and static, asymmetry fast and dynamic, and the order sets where dominants can appear.
- **Check:** Name the order; check that the organizing line (horizontal or vertical) is the one the content actually follows and that symmetric orders are not used for dynamic flows or vice versa.
- **Severity:** note
- **Tells:** A step flow centred and symmetric like a manifesto page; a catalog with a single central axis.

### Plane proportion signals the reading mode
- **Rule:** An elongated horizontal plane reads as a row (scanning, analytical); a square reads as an object (a static tile in an exploratory grid); a vertical reads as a poster or product (image over text). Changing a card's proportion switches a list into a catalog.
- **Why:** Proportion is the dynamics–statics axis projected onto shape and constrains what the inner composition can be (row: one line of meaning; square: a stack; vertical: image then text).
- **Check:** Do the module proportions match the declared reading mode? Does the inner layout fit the proportion?
- **Severity:** note
- **Tells:** Vertical poster cards in a settings list; a row card with a three-line stack inside.

### Rhyme: uniformity for recognition, variety for content
- **Rule:** Repeated modules share the compositional structure and differ only in nuance (photo size, heading length, tags); a special (featured) module merges at most TWO modules — three or more breaks the rhythm and the responsive grid — and is placed by a CONTENT rule ("first in section", "featured"), not by hand. Mixed content categories get a few RHYMING module variants.
- **Why:** Visual design balances uniformity (recognition) against variety (content): a confirmed skeleton lets the eye skip ahead, while a special of three or more survives grid shrinking badly and a manual placement fails under dynamic content [predictive brain].
- **Check:** Pick three modules and overlay them: same skeleton? Find the special: how many cells does it merge? Simulate the tablet and phone grid, and simulate two featured items landing adjacent (a "shining hole"). Check how the rhyming variants combine.
- **Severity:** warning
- **Tells:** Every card its own layout; a featured tile spanning three cells; a "featured" flag that produces two adjacent specials.
- **Catalog:** I-05

### No blinding monotony, and the inverted dominant
- **Rule:** A long uniform module feed blinds the eye: break long feeds with a rhythm shift, a composition pause (air) or a special (≤ 2 modules), placed by a repeatable rule, so dense zones give way to open ones; a short grid (one or two floors) needs no break. In a dense grid the entry point can be an EMPTY cell — a deliberate pause reads as the dominant.
- **Why:** After several identical floors the brain stops registering content, and emptiness is the contrast in a packed field [habituation].
- **Check:** Count identical floors in a row; more than ~3–4 with no shift is a violation. Does the screen breathe unevenly, or is it a monotone grid of identical boxes — the same card, gap and density everywhere? Is the pause placed by rule (every N items) rather than by taste?
- **Severity:** warning (note for short grids)
- **Tells:** Twelve identical rows; the same image-left / text-right block repeated for every section; cards undifferentiated by role.

### One grid describes every floor
- **Rule:** A single column grid governs every floor of the page; floors may use different module counts, but all module edges sit on the same grid, and module headings keep the SAME size across floors — differences are content only (rhyme, not restyling).
- **Why:** Rhyme by construction: the same skeleton with nuanced content makes a long page recognisable and lets the periphery skip ahead [predictive brain], [focal vs peripheral vision].
- **Check:** Overlay the column grid on every floor; any module edge off-grid? Compare module heading sizes across floors.
- **Severity:** warning
- **Tells:** Floor 3 on a different column count; a heading that grows in the "important" floor.

### The grid serves function
- **Rule:** Function decides the number of columns and where content binds; the grid helps, it does not dictate. Keep it simple — ~6 columns maximum, even splits that halve cleanly (4 → 2 → 1 across desktop / tablet / phone), detail expressed inside one column rather than by multiplying global columns; lines need not be equal-width.
- **Why:** A grid chosen first and then stuffed with content is the main mistake; simple grids with a clear scaling logic get built and survive production, elaborate ones mostly do not.
- **Check:** Can the column count be halved twice without holes? Is any module smaller than readable because the grid is too fine?
- **Severity:** warning
- **Tells:** A 24-column grid on a content page; an odd column count with no responsive story.

### Image fit in module
- **Rule:** Put images inside a fixed-ratio (or min / max) container and let them fit or cover — a horizontal image fills the width, a vertical one the height, centred by default, with gravity directed toward an edge when the subject demands. Make modules fluid; full-bleed is effective.
- **Why:** Images must adapt across breakpoints without breaking the module's proportion or the grid.
- **Check:** Any image at its intrinsic size inside a grid? Any subject cropped by dead-centre gravity?
- **Severity:** note
- **Tells:** Mixed-ratio images making rows uneven; a face cropped out of a centred cover.

## Whole-screen coherence

### Hint at hidden content
- **Rule:** Progressive disclosure needs a visible affordance: the next item peeks 16–32 px past a scroll edge; collapsed sections show a labelled disclosure ("Show 12 more results", not "More"); clamped text shows an ellipsis and a way to expand. Content hidden with zero cue may as well not exist.
- **Why:** A row of cards ending exactly at the edge looks complete, so nobody scrolls it [affordance and signifier], [gestalt grouping].
- **Check:** Find every scroller, collapse and clamp; confirm a cue is visible without interaction. A static design proves the peek and the labels; the clamp's reveal needs a build.
- **Severity:** blocking when content is reachable only past an uncued edge; warning for a weak cue
- **Tells:** Carousels with no peek; "More" links; chevron-less accordions.
- **Catalog:** C-28, G-15, I-06, H-14

### Layout adapts to the viewport
- **Rule:** Every screen adapts fluidly to size, resolution, orientation, safe areas and system chrome: no fixed-width layouts, no absolute positioning that breaks on resize or rotation, no clipped content or hidden actions. The primary action stays visible at every supported size.
- **Why:** A layout that breaks under resizing breaks the single dominant, visual calm and working defaults at once.
- **Check:** Resize, rotate and zoom: does the intent or the primary action change? Is anything truncated? A static design proves only the drawn breakpoints; mark the rest not-reviewed. Breakpoints, growth and clipping in detail: see lens 12 · Hold structure until it breaks and lens 12 · A critical action is never clipped.
- **Severity:** blocking
- **Tells:** Horizontal scroll on narrow widths; CTA below the fold on small screens; overlapping absolute elements.
- **Catalog:** L-04, L-05, L-11, L-12, L-13, B-18, D-35, I-15

### Stylistic cohesion
- **Rule:** Every element belongs to ONE visual language — the same shape idiom, texture or noise level, and colour world; an element styled unlike its context is brought into the system or removed.
- **Why:** An element that looks "not from here" breaks the composition regardless of how few styles there are; this is distinct from limiting the number of styles [gestalt grouping].
- **Check:** Scan for the odd one out: a sharp-cornered element in a rounded system, a glossy or noisy element among flat ones, a hue from a different world.
- **Severity:** warning
- **Tells:** A leftover promo block from an older design; a stock illustration in a different rendering style; one raw-saturated accent in a muted palette.

### Consistency beats perfection
- **Rule:** A coherent system with "imperfect" values beats a scattered interface with "correct" ones: where the project's decisions log or handbook defines values, drift from it is the finding, not the value's absolute quality, and the fix goes toward the local style, never toward the reviewer's own. Consistency never protects a blocker.
- **Why:** Decisions compound — a spacing value chosen once becomes a pattern, a depth strategy becomes an identity — and a confirmed expectation is what makes a long product feel effortless [predictive brain], [conventions].
- **Check:** Compare each value against the declared system: spacing off the declared grid, a second depth strategy, an accent outside the palette, a documented pattern reinvented. Inconsistency with what is already there is itself a tell of generated, undecided UI. Naming and platform conventions: see lens 06 · Consistency over creativity.
- **Severity:** warning
- **Tells:** Button heights 36 / 38 / 40 across screens; padding 14 / 17 / 22 in one flow; a second shadow strategy on one card.
- **Catalog:** B-17, G-02, M-02
