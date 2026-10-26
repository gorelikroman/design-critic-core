# 02 — Typography

Checks type as a system: roles and the ladder, typefaces and weights, size, measure and leading, case and tracking.
Order: inventory every distinct (face, size, weight, case) combination and map each to a role; walk the ladder top-down;
measure body size, characters per line and leading; then case and tracking. Pre-tests: the style inventory; a render with
the longest realistic string and one unbreakable string; 200 % zoom where the input allows. Static designs prove sizes, ladders,
measure and case; zoom, overrides, font loading and truncation reach are runtime (not-reviewed). Text contrast: lens 03 · Contrast floors, measured on the rendered pair; the accessibility procedure: lens 10.

## Roles and the ladder

### Style by role from a small scale
- **Rule:** Define a handful of sizes named by role (display, title, heading, body, caption, label, value, control text), each carrying size, line height and weight together, and style every text by its role — never by "how big it should look". One role, one style. Emphasis inside a role is one weight step up, not a size change. Choose a heading's element by document structure, then style it. Deviate from the scale as little as possible.
- **Why:** Roles make hierarchy predictable and repeatable across screens [predictive brain]; size-by-eye produces near-duplicates that fragment the ladder until it is noise; a role is one decision instead of three.
- **Check:** Inventory computed sizes on the screen and count distinct values; for each text node name its role and confirm the style matches the role's definition; a size that exists for no role is a defect. Compare heading sizes within each section. The number of size steps the task verb allows: (see lens 04 · Size steps equal the roles to distinguish).
- **Severity:** warning
- **Tells:** Eleven font sizes on one page; two nearly equal sizes for the same role; a "slightly larger body" invented for one card; a heading element picked for its default size.

### Every text layer is bound to a role
- **Rule:** No bare text with a manual size, weight or line height. A layer mixing two styles is allowed only for emphasis inside body text (body + body-emphasis).
- **Why:** Unbound text cannot be audited, migrated or kept consistent; it is where ladders drift.
- **Check:** Count unbound text layers (design file: a detached or missing text style; code: an inline size override with no type class). Any non-body layer with two styles inside? A design file or code proves this; a screenshot cannot — mark not-reviewed.
- **Severity:** warning; the project's log may make bound styles mandatory
- **Tells:** Detached styles on "special" screens; inline font-size overrides.

### Limit style variety
- **Rule:** Keep the number of distinct text styles on one screen small — a handful of roles (heading / subhead / body / caption / control). Five-plus distinct styles, or stacked competing effects on one text, read as overload.
- **Why:** Too many styles means everything shouts and the eye cannot settle [attentional capture]; variety must serve hierarchy, not decorate [cognitive load].
- **Check:** Count distinct (face, size, weight, case) combinations on the screen; more than ~5 is a tell. Count effects (shadow, outline, gradient) stacked on one heading.
- **Severity:** warning
- **Tells:** Seven sizes on a settings page; two effects (shadow + outline) on one heading.

### The ladder never skips a level
- **Rule:** Heading levels step down in size with no gaps: if a page has a title and cards, the card headings sit one step below the section level, not two. Adjacent levels differ BY SIZE, not only by weight or colour. A child never out-prominences its parent; a heading is never smaller than body unless it is deliberately an overline.
- **Why:** A skipped level makes two roles look like one, or one role look like two; hierarchy is read from contrast patches before words [gist first], and weight or colour alone cannot separate adjacent levels reliably (see Adjacent weights do not mix; Thin needs more contrast).
- **Check:** List the heading sizes present top to bottom; every step present? Any two adjacent roles at the same size? Any child heading larger than its parent?
- **Severity:** warning
- **Tells:** Title 30 → card heading 14 with nothing between; section and card headings at the same size in different weights; a third-level heading larger than its second-level parent.
- **Catalog:** K-14

### One title per screen; a section is never larger than the title
- **Rule:** Exactly one top-level title per screen. A section heading is never larger than the page title. An overlay (popup, modal, sheet, drawer) title sits one step below the screen title.
- **Why:** The title is the typographic dominant; anything at its size or above creates a second entry point [attentional capture] (see lens 01 · Single dominant).
- **Check:** Count top-level titles; compare the largest section heading with the title; check overlay titles against the ladder.
- **Severity:** blocking
- **Tells:** Two titles; a hero number card whose heading outsizes the page title; a modal title at title size.

### Adjacent weights do not mix
- **Rule:** Weights that carry hierarchy must differ obviously; never pair neighbouring weights (bold next to semibold, regular next to light) as if they were two levels. Emphasis inside one role is one weight step up (body → body-emphasis); a level needs an obvious weight difference or a size step.
- **Why:** A one-step weight difference is below the threshold the eye reads as a level; it produces a "which one is the heading?" moment.
- **Check:** List weights in use; any two adjacent weights doing different jobs on one screen?
- **Severity:** warning
- **Tells:** Semibold labels next to bold headings of the same size.

### Same string, same style on twin screens
- **Rule:** The same text in the same role carries the same style on every twin (mobile / desktop, variants of one flow, success / error variants), or its declared responsive counterpart.
- **Why:** Twins that disagree are the most frequent typographic defect in large reviews; the user notices the drift as "something changed" without knowing what [predictive brain].
- **Check:** Diff twin screens: for every shared string, is the style identical or the declared responsive counterpart?
- **Severity:** warning
- **Tells:** A subtitle that is a lead on mobile and a caption on desktop; a plan name bold in one flow and regular in another.

### Text inside controls keeps the control's style
- **Rule:** Text inside buttons, options, chips, tabs, breadcrumbs and inputs keeps the control's text style, even when the same words appear as values elsewhere in a different style.
- **Why:** The role differs (a control vs a value), so the style differs; restyling control text breaks affordance consistency across the product [affordance and signifier].
- **Check:** Any button or option whose text was restyled to match a nearby value or heading?
- **Severity:** warning
- **Tells:** A "Continue" set as a heading; answer options in body style on one screen and control style on another.
- **Catalog:** A-20

## Typefaces, weights and glyphs

### Meaning font vs utility font
- **Rule:** One sans-serif solves ~90 % of tasks; a second face must earn its place; rarely more than three families (range; pick per product), paired for contrast, not similarity, and never added to satisfy a checklist. If two typefaces are used, split them by job: one for what the user reads as meaning (headings, names, values, prices, options, button text), one for utility the user scans (labels above values, hints, legal, placeholders, running prose). The utility face is never a heading and never larger than body size (entered text in a field is the one exception).
- **Why:** Body text should be neutral so the form does not distract from content [cognitive load]; the heading may attract. Two faces with overlapping jobs produce near-identical styles competing for the same role; near-identical sans pairs read as a mistake.
- **Check:** Count the families. Heuristic per line: "could this line be moved out into interface noise?" → utility face; "is it a meaningful unit of the screen?" → meaning face. Find utility-face headings and utility text above body size.
- **Severity:** warning
- **Tells:** A heading in the label face; a caption in the display face; a third face for "brand moments"; two similar geometric sans faces.

### Thin needs more contrast
- **Rule:** The thinner or smaller an element, the more contrast it must carry; thin AND low-contrast is invisible. Below 18 px stay at weight 400 or heavier; weights under 300 are display-only at 28 px and above.
- **Why:** Contrast sensitivity peaks at mid spatial frequency and falls off at high frequency — thin strokes, hairlines, small type [contrast sensitivity]; thin strokes also vanish on low-DPI screens.
- **Check:** List every hairline, thin-weight text and small caption; hold each to a higher contrast bar than large elements, not a lower one. Find any light weight below 18 px. Icon strokes beside text: (see lens 11 · Stroke matches text weight; one set per surface).
- **Severity:** warning; blocking when the pair also fails a contrast floor (see lens 03 · Contrast floors, measured on the rendered pair)
- **Tells:** A light-weight grey caption; light 300 body text; a divider at 5 % opacity that nobody sees; thin icons on a tinted surface.
- **Catalog:** L-08, L-01

### Glyph distinctness
- **Rule:** Protect glyph distinctness in the chosen face (I / l / 1, O / 0), above all in codes, IDs and entered values; avoid decorative glyphs in UI text.
- **Why:** Words are recognised by parallel letter recognition, not silhouette [letter recognition]; an ambiguous glyph is a misread code.
- **Check:** Set a confirmation code, an ID and a revealed password in the chosen font; can 0 and O, 1 and l be told apart? List decorative or display glyphs used in body or control text.
- **Severity:** warning
- **Tells:** A confirmation code where 0 and O match; a decorative face on form labels.

### OpenType and variable fonts through their properties
- **Rule:** Use the dedicated property where one exists (weight, optical sizing, numeric variants, small caps, super- and subscripts); reserve raw feature or axis tags for custom axes and stylistic sets. Load the weights and styles the design uses so the browser does not synthesise bold or italic. Serve web-compressed font files.
- **Why:** Properties keep working when a non-variable fallback renders; raw tags silently do nothing; synthesised faces distort the design.
- **Check:** In code: search for raw weight tags; compare rendered bold against the loaded faces. A static design cannot prove this; mark not-reviewed.
- **Severity:** note
- **Tells:** Faux bold; a variable font with only one weight file loaded.

## Size, measure and leading

### Body size floors by viewing distance
- **Rule:** Reason in visual angle, not px. Body text stays on the reading-speed plateau for its viewing distance: roughly a 16 px equivalent for long-form on desktop; UI text ~14 px for inputs and menus, ~13 px captions, rarely below 12 px. A phone held closer may run 10–30 % smaller (see lens 12 · Phones have no periphery), but inputs stay at 16 px on mobile; a distant screen needs larger. Secondary text (captions, legal) is held to the floor too.
- **Why:** Reading speed is flat above ~0.2° angular x-height and drops sharply below it [critical print size]; below the floors legibility and zoom behaviour fail.
- **Check:** Judge body size against the device and distance; measure body size on the widest and narrowest supported viewport; check captions and legal text against the floor.
- **Severity:** warning; blocking when legal or safety-critical text is below the floor
- **Tells:** Tiny body on a desktop dashboard; 11 px metadata; legal text nobody can read.
- **Catalog:** L-08

### Line length and reading alignment
- **Rule:** Body paragraphs sit in columns of ~40–75 characters per line (range; pick per product: 40–50 in narrow columns, 60–75 for long-form). Body is aligned to the language's natural direction, ragged on the far edge; the leading edge is the anchor. Never stretch prose across the full screen width; never justify interface text; centre body only for short blocks of one or two lines.
- **Why:** Reading is fixations plus saccades with an asymmetric span; the return sweep undershoots on long lines, multiplies on short ones, and loses its anchor without a straight leading edge [reading eye movements].
- **Check:** Compute characters per line for every paragraph (column width ÷ average glyph width) on the widest supported viewport; outside the range is a violation. Flag centred paragraphs longer than two lines, justified text, and any full-width prose.
- **Severity:** warning
- **Tells:** Desktop prose at 110 characters; a paragraph in a narrow sidebar at 25; a centred four-line paragraph; justified paragraphs with rivers; paragraphs spanning a 1400 px container.
- **Catalog:** L-08, L-09

### Leading by role, line length and density
- **Rule:** Headings around 1.1; body 1.5–1.6; anything wrapping to three or more lines at least 1.4 even in a tight row; unitless values so leading scales with size. The longer the line, the more leading. A heading's leading is always tighter than the body's; multi-line content headings stay tight; captions and meta breathe more. Line height also echoes the composition's air: tight layout → tighter leading, airy layout → looser.
- **Why:** Long lines need help finding the next line [reading eye movements]; headings read as one unit; loose leading inside a tight block (or the reverse) makes inner and outer air disagree and reads as incoherent [gestalt grouping]. Leading is a size-dependent optical correction, not a style choice.
- **Check:** Compare heading leading with body leading (heading < body); read the leading of card descriptions and multi-line labels; compare the leading of a block with the gaps around it — airy leading in a dense card, or tight leading in an airy section, is a mismatch.
- **Severity:** warning
- **Tells:** A two-line heading with body leading (a "two-line gap"); heading leading on a three-line card description; a fixed 24 px line height on a 32 px title; loose paragraph leading inside a compact list.
- **Catalog:** L-08

### Tabular numbers on anything that changes
- **Rule:** Timers, counters, prices and table columns use tabular figures; numbers in tables align to the trailing edge, text to the leading edge; digits never reverse in RTL.
- **Why:** Proportional digits shift layout as values update and wobble in columns.
- **Check:** Watch a counter tick; scan a numeric column for a ragged edge. A static design proves alignment; jitter is runtime — mark not-reviewed.
- **Severity:** warning
- **Tells:** Prices jittering in a cart; left-aligned totals.
- **Catalog:** I-14, M-08

### Wrap deliberately; truncate without losing content
- **Rule:** Balance headings; prevent orphans on descriptions; allow long words, links and IDs to break; keep labels and badges on one line. Skip balancing on long-form text. Truncate single lines with an ellipsis and multi-line text with a line clamp, and whenever the hidden text matters keep the full value reachable (tooltip, expand, title).
- **Why:** Bad wrapping and widows only appear at real content lengths; truncation with no way to reach the value hides content.
- **Check:** Render with real long strings and one unbreakable string; look for orphans, overflow and unreachable truncations. A design file with placeholder names cannot prove this; mark not-reviewed unless long strings were rendered.
- **Severity:** blocking for truncated content with no way to reach it; warning for wrapping
- **Tells:** A one-word last line on every description; an ID that overflows the card; clipped names with no tooltip.
- **Catalog:** I-06, C-28, M-09

### Respect the reader's settings
- **Rule:** Typography survives 200 % zoom, a larger base font or system text size, and overridden line height, letter-spacing and paragraph spacing; sizes and text-related spacing use relative units where the codebase allows; text containers use a minimum height, never a fixed height; no important text lives in a bitmap.
- **Why:** Fixed heights, pixel-locked layouts and text baked into images clip or freeze the moment a reader enlarges text.
- **Check:** Zoom to 200 %; raise the browser's base font size or the system text size; apply a text-spacing override; look for clipped, overlapping or unreachable text; find images containing text. Zoom and overrides are runtime; a static design can still show fixed-height text boxes. The full zoom and reflow procedure: (see lens 10 · Structure is navigation; zoom and reflow).
- **Severity:** blocking when content is clipped or unreachable at 200 % or the largest text size; warning otherwise
- **Tells:** Fixed-height cards; a viewport that caps zoom; labels that vanish at the largest accessibility size; a headline baked into an image.
- **Catalog:** L-04, L-05, L-06, L-07, L-10

## Case, tracking and rendering

### Caps only for short labels
- **Rule:** Uppercase only for short labels and kickers (≤ ~20 characters, ≤ 2–3 words), always with loosened tracking. A sentence, a description, product meta or running text is never caps.
- **Why:** Words are read by parallel letter recognition; caps running text has no ascenders or descenders and reads ~10–18 % slower [letter recognition]; caps tolerates tight leading but needs tracking.
- **Check:** Find caps strings longer than ~20 characters or one line; check that every caps label has positive tracking.
- **Severity:** warning
- **Tells:** A caps subtitle; a caps paragraph in a hero; caps button text of six words; tight caps with no tracking.
- **Catalog:** M-10

### One utility voice: caps plus tracking
- **Rule:** Labels, kickers and descriptors share one voice across the product: short caps with positive tracking. The amount of tracking is proportional to how noisy the content is that the layer must cut through — mild in calm tables, strong in long-form, strongest in a catalog. Case is a tone knob on par with tracking, not a decoration.
- **Why:** With weight and colour frozen, caps + tracking alone reproduces the tonal contrast between meaning and utility; a consistent voice lets the eye group the utility layer and skip it at will [gestalt grouping].
- **Check:** Are all utility labels in the same voice? Does tracking grow with the noisiness of the surrounding content, or stay constant everywhere?
- **Severity:** note
- **Tells:** Some labels caps, some sentence case; caps labels with zero tracking in a catalog.

### Tracking is a tone knob, never a fit tool
- **Rule:** Never compress tracking to fit text into a space. Tracking follows size and role: large display text slightly negative (about −0.02 em), body near zero, small caps and utility text positive; a single letter-spacing for all sizes is wrong somewhere. Positive tracking lightens a line, negative tracking compacts and "darkens" it — with weight and colour frozen, tone is rebuilt from tracking and case, so tracking carries hierarchy when used deliberately and by role.
- **Why:** Compression collapses the crowding window [crowding]; the space between letters converts into the optical tone of a line — pseudo-weight without weight. Tracking is the lowest rung of the spacing cascade (tone); above it sits grouping, at the top the dramaturgy of pauses (lens 01).
- **Check:** Any negative tracking on small or body text? Any caps without positive tracking? Is tracking consistent per role and across screens? Is tonal contrast between meaning and utility made by tracking and case rather than by extra weights or colours, and does the single strongest tracking sit on the single action or kicker?
- **Severity:** warning
- **Tells:** A squeezed label that "just fits"; inconsistent tracking on the same role across screens; uppercase labels with no tracking; four weights doing what two trackings could; tracking scattered across many roles.

### Rendering hygiene
- **Rule:** Font smoothing set once at the root, never per component. Underlines take position and thickness from the font and skip descenders; a dotted underline signals extra information. Copy stored in natural case and transformed by style. Smart punctuation in rendered text (curly quotes, en dash for ranges, a single ellipsis character, a non-breaking space between a number and its unit). Text stays selectable except on genuine drag or gesture surfaces and controls. Language and direction are set so hyphenation, quotes and bidi behave.
- **Why:** These are the invisible details that separate typeset from typed.
- **Check:** Zoom on links, abbreviations and ranges; try selecting body text; check the document language and direction. Mostly runtime or code; a static design shows punctuation and underlines only.
- **Severity:** note
- **Tells:** Three periods; a hyphen in "2010-2020"; underlines cutting through descenders; unselectable error messages.
- **Catalog:** M-07

## Reference tables

| Measure | Value | Entry |
|---|---|---|
| Body size, long-form desktop | ~16 px equivalent; a phone may run 10–30 % smaller; inputs 16 px on mobile | Body size floors by viewing distance |
| UI text | ~14 px inputs and menus; ~13 px captions; rarely below 12 px | Body size floors by viewing distance |
| Weight | ≥ 400 below 18 px; under 300 only as display at ≥ 28 px | Thin needs more contrast |
| Characters per line | ~40–75 (40–50 narrow; 60–75 long-form) | Line length and reading alignment |
| Leading | headings ~1.1; body 1.5–1.6; ≥ 1.4 for three or more lines; heading < body | Leading by role, line length and density |
| Tracking | display ≈ −0.02 em; body ≈ 0; small caps and utility positive; never negative to fit | Tracking is a tone knob, never a fit tool |
| Caps | ≤ ~20 characters, ≤ 2–3 words, positive tracking | Caps only for short labels |
| Distinct styles per screen | ~5 or fewer | Limit style variety |
| Zoom and overrides | 200 % zoom; largest system text; text-spacing override; nothing clipped | Respect the reader's settings |
