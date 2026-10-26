# 03 — Colour and surfaces

Checks colour as a system and the surfaces it sits on: hierarchy and salience, meaning and contrast, the colour system, depth and dark mode.
Order: name the project's direction (table below); desaturate the screen; map hues and lightness; measure every rendered
text and UI pair with a tool; then inspect ramps, gradients, surfaces and the dark twin. Pre-tests: grayscale; a contrast tool
on the actual rendered pair. Values are measured, never estimated: the critic reports pair, value and threshold and does not repaint.
Colour-only meaning and contrast floors are floors (blocking); the accessibility procedure lives in lens 10.

## Naming the project's direction

Name the direction before the first finding; findings are then measured against it, not against a generic ideal. Record it in the project's decisions log with a foundation temperature (warm / cool / neutral / tinted) and a depth strategy (borders-only / subtle shadows / layered shadows). Intent must be systemic: a direction declared warm and built on cold greys is a finding, and every value is checked against the stated direction. The direction calibrates `warning` and `note`; it never lowers a floor.

| Direction | Feel | Typical products | Reviewer's calibration |
|---|---|---|---|
| Precision and density | Tight, technical, monochrome; borders-only depth; 4 px base; 11–14 px type; system or monospace faces | Developer tools, admin dashboards | Density is not a defect; shadows and generous radii are |
| Warmth and approachability | Generous spacing, soft shadows, warm neutrals, 8–16 px radii, 15–16 px body | Collaborative tools, consumer apps | Airiness is intended; harsh borders and cold greys are the drift |
| Sophistication and trust | Cool tones, layered depth, restrained accent | Finance, enterprise B2B | Playful easing and loud colour are off-direction |
| Boldness and clarity | High contrast, dramatic space, few large elements | Modern dashboards, data-heavy apps | Big scale jumps are a decision, not a flatness bug |
| Utility and function | Muted, functional density, an engineering-tool look | Engineering and ops tools | Decoration of any kind is the tell |
| Data and analysis | Chart-optimised, numbers-first, tabular figures | Analytics, BI tools | The number is the focal point; chrome must recede |

## Hierarchy and salience

### Harmony by task
- **Rule:** Choose the scheme by how much attention the screen needs, not by taste. Most screens: a low-contrast harmony (monochromatic or analogous), contrast only from lightness, nothing shouts. Action: spend one high-contrast (complementary) accent on the ONE most important element. Never make the whole screen high-contrast.
- **Why:** Distance on the colour wheel is contrast, contrast is arousal, arousal pulls attention [attentional capture]; contrast is a scarce budget, spent on the single action.
- **Check:** Map the hues in use on a wheel; how far apart are they? Is the one far-apart accent on the primary action, or spread across the screen?
- **Severity:** warning
- **Tells:** A screen where every colour is far from every other; no single place for attention to land.

### Colour balance is never equal
- **Rule:** One base colour dominates, one supports, one accents (~60-30-10). Weight is INTENSITY (saturation × brightness), not area: a muted colour can cover most of the screen and still yield to a small vivid accent; two large saturated fields fight.
- **Why:** One flavour must lead; two equally loud fields read as disorder — the colour twin of the single dominant (see lens 01 · Single dominant) [attentional capture].
- **Check:** Name the dominant, secondary and accent by intensity. Are there two large fields of comparable saturation?
- **Severity:** warning
- **Tells:** A saturated header over a saturated section; a "brand" colour and a "category" colour at equal loudness.

### One hue, many shades
- **Rule:** Build hierarchy and mood by moving saturation and brightness of a SINGLE hue (surface, hover, muted, accent) while keeping the hue stable. Reserve a second, contrasting hue for the single most important accent.
- **Why:** Emotion rides saturation and brightness, not hue (darker / desaturated reads calm and secondary; brighter / saturated reads active and primary). A one-hue scale is automatically harmonious and fits a role system [processing fluency].
- **Check:** Count hues on the screen; is meaning carried by hue swaps, or by shade steps of one hue?
- **Severity:** warning
- **Tells:** Four unrelated hues for four card types; a state expressed by switching hue instead of shade.

### Combine colours by lightness, not hue
- **Rule:** Build hierarchy, legibility and every colour pairing on lightness difference; hue is a secondary layer. To make two colours read as contrasting or an element pop, change their LIGHTNESS and keep the hue. Reason in a lightness / luminance model and settle the lightness relationships first. In the hierarchy toolbox hue comes last — after lightness contrast, space, size and weight; lines and boxes after that.
- **Why:** The luminance channel carries edges and fine detail; the chroma channel is blurry; two very different hues of equal lightness read as low contrast, and saturation barely moves luminance [luminance carries form].
- **Check:** For every pair meant to contrast (text / surface, accent / surround), compare lightness values; near-equal lightness is no contrast regardless of hue. Convert to grayscale: every relationship that mattered must survive.
- **Severity:** warning; blocking when text legibility depends on it
- **Tells:** A vivid label on a mid-tone surface of the same lightness; "contrast" achieved by cranking saturation; two hues used as "contrast" with matching lightness.

### Salience survives grayscale
- **Rule:** Reduced to luminance, the dominant / primary action must remain the highest-contrast element. If it dissolves, fix it by lightness (darker or lighter), not by saturation.
- **Why:** Peripheral vision reads brightness first [focal vs peripheral vision]; a bright hue matching its surround in lightness looks colourful yet is functionally invisible [luminance carries form].
- **Check:** Desaturate the screenshot; is the primary action still the most contrasting patch? Does each status colour still differ from its neighbours?
- **Severity:** blocking — for the dominant dissolving, and for a state or meaning that differs by hue alone (see Colour as a code)
- **Tells:** A lime or fuchsia button that disappears in grayscale; a selected state that only differs by hue.
- **Catalog:** A-11

## Meaning, status and contrast

### Colour as a code
- **Rule:** Colour is the strongest pop-out for scanning categories, status and priority, under limits: ≤ ~5–6 category colours (hard ceiling ~7), each maximally separated, then add a second channel (icon, shape, text, position); every colour → meaning mapping is STABLE across the product; status uses the conventional mapping (green go, red stop, amber warn) AND a redundant cue (icon + text), never hue alone. Ordered scales (heatmaps, density) never use a rainbow: a perceptually uniform scale with monotonically increasing lightness. Where a status colour's meaning is load-bearing (finance), verify it per locale — green-for-gain is not universal.
- **Why:** Beyond ~6 hues discrimination collapses into slow serial search [pre-attentive pop-out]; re-colouring a concept costs recognition [conventions]; a weak red–green channel (~8 % of men) hits exactly the success / error pair [colour vision deficiency]; rainbow lightness jumps invent false boundaries.
- **Check:** Count category colours; diff the mapping across screens; for each status find the non-colour cue; check ordered scales in grayscale for monotonic lightness. The redundant-cue procedure for interactive, error, selected and required states: (see lens 10 · Non-colour cues and reduced motion).
- **Severity:** blocking for status, state or meaning by hue alone; warning otherwise
- **Tells:** A dozen near-duplicate tag colours; "pending" blue here and amber there; a jet-palette chart; red / green status with no icon or text.
- **Catalog:** L-03, A-11, B-06, B-14, C-16, I-14

### One hue, one meaning
- **Rule:** A hue (anything within ~15°) means one thing across the interface. If the accent means interactive, it does not decorate static headings, and interactive elements are not rendered neutral. Semantic hues are never used against their meaning (danger on a non-destructive action). Selected states may use the accent as state, not emphasis. Where filled colour encodes primary emphasis, one action per view gets it, peers stay neutral, and the colour goes on the background, not the label — but a filled button is only one way to make the dominant; recolouring controls is never the fix when the project has another emphasis mechanism (see lens 01 · Single dominant).
- **Why:** Users read a near-miss hue as the same colour [conventions]; three filled buttons means no primary.
- **Check:** Find accent used on non-interactive text; find status hues used decoratively or against their meaning; count filled accent backgrounds per view.
- **Severity:** blocking for a semantic colour against its meaning; warning for accent on static text or several filled primaries
- **Tells:** Blue section titles next to blue links; red "Save"; a row of three filled buttons.
- **Catalog:** B-04, B-06

### Colour spent in proportion to severity
- **Rule:** Escalate the visual weight of a status with its severity and reversibility: a dot + word for background or binary states; a filled chip for three or more states or "action required"; a coloured container or border only for a genuine failure. Destructive colour is reserved for the irreversible; bad news that is not the user's fault can be a calm, neutral card without alarm colour or icon.
- **Why:** Colour is a budget (see Harmony by task); a warning spent everywhere becomes noise [warning habituation]; a solid semantic fill on every row reads as a "Christmas tree".
- **Check:** Rank every status treatment on the screen by loudness and by severity; the two orders must agree. Count red elements; more than one red on a screen with one failure is a violation.
- **Severity:** warning
- **Tells:** A red border on "shipped"; every list row with a filled colour chip; a reversible "pause" in destructive red.

### Contrast floors, measured on the rendered pair
- **Rule:** Body text ≥ 4.5:1; large text (≥ 24 px, or ≥ ~18.7 px bold) ≥ 3:1; non-text UI needed for recognition (icons, borders, focus and state indicators) ≥ 3:1 — computed on relative luminance between the foreground and the background it actually renders on (the card, not the page), in both appearances, including translucent surfaces, computed colours and the worst region of an image or gradient. Report the pair, the measured value and the threshold; leave the colours alone unless asked. Fix contrast by changing lightness, holding hue. Mid-lightness backgrounds cap what any text can reach.
- **Why:** A legal and physiological floor: failing pairs are invisible to a large share of users and in bad light [contrast sensitivity] [colour vision deficiency]; colour is one of the few interface concerns with an exact answer, and an estimate is a guess with a decimal point.
- **Check:** Measure every text / background and UI / background pair with a tool; never report a value that was not computed. Check muted greys, dividers that carry meaning, placeholder text, disabled states (exempt from the floor but held legible), and every pair on a dark surface, not just primary text on white. The full procedure and the other floors (target size, zoom, reflow): (see lens 10 · Structure is navigation; zoom and reflow).
- **Severity:** blocking for text, control text or a meaning-carrying UI element below its floor; warning for other pairs
- **Tells:** Placeholder-grey helper text; a light border that is the only field boundary; white text on a mid-tone brand colour; text over a gradient measured at its average; disabled text that passes on light but fails on dark.
- **Catalog:** L-01, L-02, L-16, K-02

## The colour system

### Defined roles only
- **Rule:** Every colour on the screen resolves to a defined role — surface, text, border, hierarchy, state, feedback, emphasis — and every role's value comes from the brand palette: the brand defines which of its own colours plays each semantic role, error, success, warning and info included, never a hue borrowed from outside it. No ad-hoc helper colours, no decorative colours, no borrowing a role's value because it looks right today (a separator as text colour, a text colour as a background); if a role has no value, add the role from the palette. Colour never stands alone as meaning (see Colour as a code).
- **Why:** Colour is a structural tool, not decoration; a colour that cannot be named by role does not belong, an off-palette colour breaks the system's coherence, and a borrowed value breaks the first time its own role is restyled.
- **Check:** List every colour on the screen and name its role; anything unnamed fails. For each semantic role (error, success, warning, info) confirm its value is a brand-palette colour, not an off-palette import. In code or a design file: for each role, list where it is applied and whether the property matches the role. Remove colour mentally: does meaning survive?
- **Severity:** warning for an undefined, decorative, borrowed or off-palette colour; blocking when the stray colour is the only carrier of meaning
- **Tells:** Values outside the defined set; a semantic colour (an error red, a success green) picked from outside the brand palette; a "nice" teal for one card; captions coloured with the border value.

### Primitives by hue, semantics by role
- **Rule:** Primitives name a value (a hue and a step) and are never applied in a component. Semantic names name a job (secondary text, subtle border, solid accent) and are the only tier components reference. One naming grammar, one word per concept: "accent" for the brand colour and "primary" reserved for "most prominent of its group". A component-level name is a documented exception, not a habit.
- **Why:** The semantic seam is what makes dark mode, white-label and increased-contrast themes possible without auditing every usage.
- **Check:** In code or a design file's variables: search components for raw ramp references; look for names by appearance or first use ("blue button", "sidebar grey", "text 2"). A screenshot cannot prove this; mark not-reviewed.
- **Severity:** warning
- **Tells:** "primary" meaning brand in one place and body text in another; a primitive applied directly in a component.

### A system is a few ramps, each step with a job
- **Rule:** One neutral ramp (carrying most of the UI, with the most steps), one accent ramp, and only the status ramps the product renders. Every step exists because a role consumes it (page background, subtle background, component background, hover, active, subtle border, border, strong border / focus, solid fill, solid hover, low-contrast text, high-contrast text). Generate no step no role uses.
- **Why:** Ramps without roles become a gradient to pick from by eye, and the palette outgrows its structure.
- **Check:** Inventory every colour literal; sort by lightness within hue; collapse near-duplicates; assign each survivor a role. Report the inventory before proposing changes.
- **Severity:** warning
- **Tells:** Forty greys; a warning ramp nothing uses; two accents next to each other.

### Well-formed ramps
- **Rule:** Steps are evenly spaced in perceived lightness (not the format's lightness number); vividness peaks mid-ramp and falls at both ends; steps sit denser at the light end; no two adjacent steps are indistinguishable; both ends stop short of pure black and white. Hue is not constant end to end: darker steps shift hue toward the nearest dark primary (red, green, blue are the darkest hues), lighter steps shift toward a warm or cool light as the project defines — the same natural darkening as a hand-picked hover or pressed step (see Natural darkening and cool shadows). Across hues, match lightness exactly and vividness proportionally to each hue's own maximum. Compute with a colour library in a perceptual space; never eyeball or hand-derive. Declare an sRGB value before any wide-gamut override: a wide-gamut colour with no fallback fails rather than degrades, and a clipped gamut flattens ramp steps.
- **Why:** Ramps built by varying the format's lightness number bunch and drift; copied saturation numbers leave yellows and cyans washed out; unequal lightness across hues gives status colours unequal weight; a ramp held to one constant hue reads flat next to the natural darkening and lightening the eye expects.
- **Check:** Plot perceived lightness per step; compare hue angle across steps — the darkest steps should drift toward the nearest dark primary and the lightest toward the project's chosen warm or cool light, never sit at the seed hue throughout; place the danger and brand mid-steps side by side and compare weight. In code: search for wide-gamut colours without a fallback.
- **Severity:** note; blocking for a wide-gamut colour with no fallback
- **Tells:** A pale end where two steps look identical; a warning colour visibly weaker than the danger colour; banding on a hero; a ramp whose darkest and lightest steps sit at the same hue angle, reading flat.

### Natural darkening and cool shadows
- **Rule:** To darken a colour realistically, lower brightness and RAISE saturation — never lightness alone; in a hue-saturation-lightness model also shift the hue toward the nearest dark primary (red, green, blue are the darkest hues; yellow, cyan, magenta the lightest). Hand-picked darker steps (hover, pressed) follow this; computed ramps shift hue toward the dark or light primaries across their steps, the same way (see Well-formed ramps). Cast shadows are cooler, hue-shifted and slightly desaturated, never plain black or a black layer at low opacity.
- **Why:** Lightness-only darkening reads flat and dead; a warm light produces a cool shadow [colour constancy].
- **Check:** Inspect the hover / pressed / darker steps of an accent: saturation up and hue drifted, or brightness only? Inspect shadow colour: neutral black or a cool tint?
- **Severity:** note
- **Tells:** A pressed state that looks like the button with a grey veil; pure-black drop shadows at 20 %.

### Muted and tinted, not raw and neutral
- **Rule:** Living palettes are half-tones, not maximum-saturation swatches; greys are tinted a few points warm or cool (ivory, graphite, blue-grey), never mathematically flat neutral — and the tint matches the declared foundation temperature.
- **Why:** Raw 100 % saturation reads cartoonish; muted tones read considered and premium (an "innovative" brand may deliberately go saturated); flat neutral greys read dead beside anything tinted.
- **Check:** Inspect the saturation of the main fills and the chroma of the greys; a pure zero-chroma grey next to a tinted palette is the tell; compare the tint with the direction named above.
- **Severity:** note
- **Tells:** Pure primary-red error banners; a zero-chroma mid-grey in an otherwise warm palette; a direction declared warm built on cold greys.

### Gradients avoid mud
- **Rule:** Keep gradients within adjacent or short-arc hues, or one hue varying lightness. If two distant hues are required, insert a mid-stop of the pure hue between them on the shorter arc and interpolate in a perceptual space; a polar space keeps two distant hues vivid but may introduce unasked-for hues, so add a third stop to avoid a grey dead zone. Keep text off gradients or measure the worst region.
- **Why:** A gradient is a spatial mix: distant hues pass through a dull midpoint and complementaries cancel to grey [colour opponency]; the default interpolation muddies midpoints.
- **Check:** Sample the gradient's midpoint; is it greyer or duller than both ends? Any text over a gradient measured at its average rather than its worst region?
- **Severity:** warning
- **Tells:** A purple-to-green blend with a brown middle; a two-stop complementary gradient; a blue-to-pink gradient going grey in the middle.

### Gradients serve a function
- **Rule:** In product UI a gradient earns its place by a job: depth or atmosphere, a legibility scrim (dark → transparent under text over imagery), a focus vignette lifting the dominant, or a section transition. Decorative angular, conic or mesh gradients belong to marketing surfaces, not product screens.
- **Why:** Decoration on a task screen is extraneous load [cognitive load]; a scrim or vignette is a functional depth cue [depth cues].
- **Check:** For each gradient name its job; "looks nice" is not one.
- **Severity:** note; warning on a task screen
- **Tells:** A mesh gradient behind a form; a conic background on a dashboard.

### No colour-psychology folklore
- **Rule:** Reject any colour choice justified by pop colour psychology ("this hue converts", "blue builds trust", "red boosts focus", gendered palettes, N colours = premium). Mood comes from saturation + lightness; salience from contrast and isolation; trust from overall visual quality. Justify colour only by contrast, legibility, semantic convention, consistency and restraint.
- **Why:** The classic colour–behaviour claims failed replication or are context-dependent at best; the one surviving lever is saturation / brightness → arousal.
- **Check:** Read the rationale for each colour decision; strike any hue–meaning-chart argument and ask for a mechanism. The UX twin: (see lens 06 · No UX folklore).
- **Severity:** note, as a review of rationale, not of pixels
- **Tells:** "We made it green because green means go"; a functional colour remapped per locale on a hue-meaning chart rather than a verified convention.

## Surfaces, depth and dark mode

### Shadows for elevation, borders for structure
- **Rule:** Cards, buttons and floating layers take depth from layered translucent shadows (a 1 px ring plus a small lift plus faint ambient); in dark mode a single faint light ring. Dividers, table cells, input outlines and hairline separators stay borders. One depth strategy per product (the direction's borders-only / subtle shadows / layered shadows), and a shadow or line only where spacing has not already done the separating (see lens 01 · Space first, shapes second, lines last; lens 01 · Depth by position, one depth relationship).
- **Why:** Translucent shadows adapt to any background; a fixed border colour was designed for one; dividers are structure, not depth [depth cues] [figure–ground].
- **Check:** Place the component over an image or a different surface; a solid border that no longer matches is a finding. Count depth strategies on the screen.
- **Severity:** note
- **Tells:** Grey 1 px borders on cards over a photo; layered shadows on list separators; a second depth strategy on one screen.

### Concentric border radius
- **Rule:** When rounded elements nest with an even inset, outer radius = inner radius + padding. Past ~24 px of padding, treat the layers as independent surfaces and pick each radius on its own.
- **Why:** Equal radii on a nested pair leave the corner gap thicker than the sides — the most common reason an interface feels subtly off [optical vs geometric].
- **Check:** Measure radius and padding on every nested card, input-in-card, button-in-pill and image-in-card pair.
- **Severity:** warning
- **Tells:** A 12 px card with 8 px padding around a 12 px inner card; a pill button with a square-cornered inner badge.

### Optical over geometric
- **Rule:** Align and size by eye, not by numbers, and compensate: round shapes overshoot squares; horizontals are drawn thinner than verticals; rounding starts before the geometric corner; an icon + text button gets less padding on the icon side (about the text side minus 2 px); a play triangle nudges a couple of pixels right; asymmetric glyphs are fixed in the asset, not with margins.
- **Why:** Perception measures optical size and position — the eye centres visual mass, not bounding boxes [optical vs geometric].
- **Check:** Zoom to 400 % on icon buttons, play controls, arrows and stars; compare visual mass against the box. If a layout "is aligned by the numbers" but looks off, the eye is right.
- **Severity:** note; warning for a visibly off-centre dominant
- **Tells:** A play glyph that sits left of centre in its circle; a trailing chevron that looks pushed out.

### Image outlines are pure black or white at low opacity
- **Rule:** Images get a 1 px inset outline at ~10 % opacity: pure black in light mode, pure white in dark. Never a tinted neutral, never the accent.
- **Why:** A tinted ring picks up the surface beneath and reads as dirt on the image edge; the outline is a separator, not a themed element [figure–ground].
- **Check:** Inspect image edges against light and dark surfaces.
- **Severity:** note
- **Tells:** Slate-coloured image borders; images with no edge sitting on white.

### Dark mode is tuned, not inverted
- **Rule:** Dark is a semantic remapping: swap the roles first, then re-tune by hand. Base surface is a near-black grey, not pure black; body text is off-white at reduced emphasis, not pure white; elevation is expressed by LIGHTER surfaces (closer = lighter), not by shadows; every accent is lightened and desaturated a step or two so it does not vibrate; the dark end of each ramp is widened; greys stay slightly tinted; light elements may need a lighter weight or a slightly smaller size. Contrast is sufficient (the floors), not maximal, and every pair is re-measured. One switching mechanism (system preference alone; a class when users can override; or a light-dark function with the colour scheme declared) used everywhere, with colour transitions suppressed during the flip. Dark is a user choice: ship both themes, honour the OS setting, never force dark by default.
- **Why:** Pure white on pure black maximises halation and fatigue; saturated hues glow on dark; shadows vanish on dark; light-on-dark reads larger and heavier [optical vs geometric]; contrast is not symmetric, so a pair passing in light can fail in dark [contrast sensitivity]; dark helps photophobia and cataracts but hurts astigmatism and is worse for normal vision.
- **Check:** Toggle dark mode. Base and text values not at the extremes? Elevated surfaces lighter than their parent? Accents desaturated against the light twin, no neon? Text weights not visibly heavier than in the light twin? Every pair re-measured? Every value switches, no half-themed components? A theme switch that follows the system? A static design proves values; the switching mechanism is code — mark not-reviewed.
- **Severity:** warning; blocking on a contrast-floor failure in dark or pure-white body text on pure black
- **Tells:** An auto-inverted palette; a vibrating saturated accent; a glowing accent button on near-black; shadowed cards on a dark ground; some components still light after the switch; forced dark mode.
- **Catalog:** L-16

## Reference tables

| Measure | Value | Entry |
|---|---|---|
| Body text contrast | ≥ 4.5:1 | Contrast floors, measured on the rendered pair |
| Large text (≥ 24 px, or ≥ ~18.7 px bold) | ≥ 3:1 | Contrast floors, measured on the rendered pair |
| Non-text UI needed for recognition | ≥ 3:1 | Contrast floors, measured on the rendered pair |
| Category colours | ≤ ~5–6, hard ceiling ~7, then a second channel | Colour as a code |
| Same-hue tolerance | ~15° reads as one colour | One hue, one meaning |
| Colour balance | ~60-30-10 by intensity, not area | Colour balance is never equal |
| Concentric radius | outer = inner + padding; independent past ~24 px padding | Concentric border radius |
| Image outline | 1 px inset, ~10 % opacity, pure black or white | Image outlines are pure black or white at low opacity |
| Dark accents | lightened and desaturated a step or two; base near-black, text off-white | Dark mode is tuned, not inverted |
