# Perception and cognition — the WHY behind every lens

Mechanisms of the eye, the brain and behaviour, grouped by system. Each entry states what is
known, how well it is known (established | qualified | contested | myth | not rated), and which
lens entries it drives. Lens entries cite these H3 names in square brackets; nothing else is
citable. The myths table at the end is the filter against pop-psychology rationales: any
finding that leans on "7±2", "the F-pattern", "blue means trust", "8-second attention span" or
"loss is 2× gain" is checked there and downgraded or rejected.

## Optics and the retina

### efficient coding
- **Claim:** The retina does not transmit pictures. It sends parallel, transformed streams about contrast, colour differences and change; uniform fields evoke weak responses, edges and onsets strong ones. Gain control adapts sensitivity at several levels from photoreceptor to cortex, so the system encodes differences, not absolute light.
- **Evidence:** established
- **Design consequence:** Reason about edges, contrasts and changes, never about "the image". A large flat area costs nothing; every unintended edge (a misaligned box, a banded gradient, a hairline that carries no meaning) is amplified and attracts. Drives (lens 01 · Space first, shapes second, lines last), (lens 03 · Gradients serve a function), (lens 03 · Well-formed ramps).
- **Myth it corrects:** "The eye sends ready-made camera frames to the brain."

### contrast sensitivity
- **Claim:** Luminance (physical light) ≠ brightness (the percept) ≠ lightness (inferred reflectance). Contrast is relative: a small target is judged by its difference from its background, a pattern by its swing between light and dark. Sensitivity is band-pass — best at intermediate spatial frequencies, weak for very fine structure (thin strokes, hairlines, small type) and for very gradual structure (slow gradients) — and it declines with age, low luminance, glare and distance from fixation even when acuity is fine. Effective contrast is compressed by ambient light, thin weights, anti-aliasing, overlays and background images.
- **Evidence:** established
- **Design consequence:** The thinner or smaller an element, the more contrast it must carry; thin AND low-contrast is invisible. Readability is luminance contrast, never hue difference. A ratio is measured on the rendered pair under the conditions users actually meet. Drives (lens 02 · Thin needs more contrast), (lens 03 · Contrast floors, measured on the rendered pair), (lens 10 · Forced colours and high contrast keep the states).
- **Myth it corrects:** "Brightness is the amount of light"; "one contrast formula fits every image"; "good acuity guarantees normal contrast vision"; "contrast sensitivity is fixed".

### simultaneous contrast
- **Claim:** From the retina onward neurons compare centre with surround (lateral inhibition, ON and OFF pathways as separate active signals). A grey looks lighter on dark and darker on light; a target beside a similar pattern is masked; a label on a busy texture disappears. "Lateral inhibition" is shorthand for a family of retinal and cortical interactions, not one explanation for every illusion.
- **Evidence:** established
- **Design consequence:** A tone cannot be judged in isolation; it is checked on every surface it appears on and next to every neighbour it will have. The same grey that is a divider on one surface is text on another. Drives (lens 03 · Contrast floors, measured on the rendered pair), (lens 03 · Muted and tinted, not raw and neutral), (lens 03 · Image outlines are pure black or white at low opacity).
- **Myth it corrects:** "Lateral inhibition explains every brightness illusion"; the retina as a literal edge detector.

### focal vs peripheral vision
- **Claim:** Only the fovea (a few degrees) samples densely. Acuity, colour discrimination and fine-detail contrast sensitivity fall with eccentricity while receptive fields and crowding zones grow. The periphery is a different code, not a blurred centre: it detects motion, onset and coarse structure, estimates layout and chooses the next saccade target. Enlarging a peripheral element restores acuity but not crowding or positional certainty. Saturated, large colour is visible in the periphery; small low-contrast colour is not. The faster the scroll, the narrower the zone that reads.
- **Evidence:** established
- **Design consequence:** Design for sequential inspection, not for an observer who reads the whole screen at once. Reading-critical text sits where the user fixates; the periphery may guide (size, contrast, isolation, motion) but never has to identify. Attention cannot be held, only intercepted and led. Drives (lens 01 · Single dominant), (lens 01 · Route in 0.3 s, no attention tearing), (lens 12 · Phones have no periphery), (lens 05 · Error visibility on submit).
- **Myth it corrects:** "The fovea is the only part that sees"; "the periphery is a blurred centre"; "no colour in the periphery"; "enlarging makes periphery equal to centre".

### cortical magnification
- **Claim:** Primary visual cortex over-represents the centre of gaze; the map is a preserved but heavily distorted coordinate system, not a picture in the brain, and the distortion is structural (receptor and ganglion-cell density), not a switchable zoom.
- **Evidence:** established
- **Design consequence:** Central content receives far more neural territory than the edges of a wide viewport; the most detailed content belongs near the likely fixation, and dense peripheral content cannot be "zoomed into" by attention. Drives (lens 12 · Desktop widens the column, not the story), (lens 12 · Phones have no periphery), (lens 01 · Order by importance; do not overload the entry point).
- **Myth it corrects:** "Cortical magnification is the brain's software zoom."

### crowding
- **Claim:** A peripheral target that is identifiable alone becomes unrecognisable when flanked; features are pooled, averaged or assigned to neighbours. Critical spacing grows roughly with eccentricity (about half the eccentricity as a heuristic, not a constant), is stronger radially than tangentially, and is almost independent of target size — enlarging does not cure it. Grouping cues (colour, depth, motion, an enclosing boundary, a dissimilar shape) release it; attention reduces it only partly. It harms identification, not detection.
- **Evidence:** established; qualified for the exact half-eccentricity ratio
- **Design consequence:** Spacing is a first-class variable separate from size. Every element needs a clear zone that grows with its distance from the likely fixation; peripheral UI (toolbars, corner meta) needs larger gaps than central UI, and tracking is never compressed to make text fit. Drives (lens 01 · Outer gap beats inner gap), (lens 02 · Tracking is a tone knob, never a fit tool), (lens 10 · Hit areas never overlap and decorative layers never eat clicks), (lens 11 · Stroke matches text weight; one set per surface).
- **Myth it corrects:** "Crowding is just blur or a lack of attention"; "the crowding distance is always exactly half the eccentricity".

### hemifields and retinotopy
- **Claim:** After the optic chiasm each tract carries the contralateral half of visual space from both eyes — not "left eye to right hemisphere". The relay nucleus between retina and cortex is modulated (attention and arousal set gain and mode); the fast-coarse and slow-fine channels stay partly distinct but are not "motion" versus "colour and form".
- **Evidence:** established
- **Design consequence:** No layout rule follows from hemispheres; the only usable fact is that central content gets far more neural territory than peripheral content. Rationales that assign "logical" content to one side of the screen are rejected. Drives (lens 06 · No UX folklore).
- **Myth it corrects:** "The left eye goes to the right hemisphere"; "the relay is passive"; "magno = motion, parvo = colour".

## Attention and eye movements

### attention networks
- **Claim:** Attention is a family of mechanisms, not one fuel tank or a spotlight of fixed size: spatial, feature-based and object-based selection; goal-driven (endogenous, slow, sustainable) and stimulus-driven (exogenous, fast, involuntary); partly separable dorsal and ventral networks. Stimuli compete for representation and attention biases the competition — raising gain, reducing noise, sharpening tuning and suppressing competitors — from the earliest stages upward. It raises contrast sensitivity and resolution at the focus but cannot create detail that was never sampled, cannot turn periphery into fovea, and cannot be spread everywhere at equal precision. Attention-demanding tasks are switched, not paralleled.
- **Evidence:** established for competition, cueing benefits and early modulation; qualified for a single mechanism and for the strict network division
- **Design consequence:** Reduce competition around important targets; limit simultaneous accents; never demand monitoring of two distant regions at once; salience must coincide with relevance. Diagnose which channel a signal relies on before judging whether it will be seen. Drives (lens 04 · One intent per screen), (lens 09 · Stage one hero per beat), (lens 05 · Sub-task stays in context), (lens 01 · Single dominant).
- **Myth it corrects:** "Attention is a single willpower"; "multitasking splits attention in half".

### covert attention
- **Claim:** Attention moves without the eyes and shifts to a saccade target before the eyes do; discrimination there improves. Gaze therefore is not attention: a fixation does not prove processing, and the absence of one does not prove neglect. Fixation duration reflects difficulty, not interest.
- **Evidence:** established
- **Design consequence:** Eye-tracking data is read as gaze allocation, never as comprehension or memory; heat maps count only alongside task-success data. Drives (lens 13 · Track only what answers a question), (lens 13 · Evidence, not taste), (lens 01 · Route in 0.3 s, no attention tearing).
- **Myth it corrects:** "Fixation = attention = understanding"; "eye tracking reads thoughts".

### load theory
- **Claim:** Under high perceptual load, distractors are filtered early because capacity is used up; under low load, spare capacity spills onto distractors. Cognitive load (working memory busy) weakens the goal that keeps attention on task, so distractors intrude more. The account is influential but not settled.
- **Evidence:** qualified
- **Design consequence:** A screen that keeps the user busy will not notice a side signal; a screen that is nearly empty lets every accent intrude. The critic checks that signals sit inside the task's focus and that nothing competes while the user is waiting or deciding. Drives (lens 04 · One intent per screen), (lens 09 · Never animate what the user is waiting on), (lens 05 · Sub-task stays in context).

### priority map
- **Claim:** Peripheral vision supplies a candidate map for the next fixation, prioritised by salience, task relevance, learned value, novelty, motion, meaning, expectation and search history. Gaze in natural tasks is allocated by task demands more than by bottom-up salience; there is no universal, task-independent scan path. The F-pattern is a description of text-heavy left-to-right pages, not a law.
- **Evidence:** established for presaccadic shifts and peripheral target selection; qualified for how the factors combine and for F-pattern generalisation
- **Design consequence:** Hierarchy suggests the next fixation rather than assuming one; the primary action must be findable before it is read; frequently compared values sit close enough to avoid needless saccades but not so dense that crowding rises. "Top-left because F-pattern" is never a rationale. Drives (lens 01 · Route in 0.3 s, no attention tearing), (lens 04 · A comparison rail appears exactly where numbers are compared), (lens 01 · Direction devices).
- **Myth it corrects:** "One natural scan path per interface"; "the F-pattern is a law".

### pre-attentive pop-out
- **Claim:** Visual search is guided competition over the priority map. A target defined by one unique strong feature (lightness, size, colour, orientation, isolation) is found at near-zero cost; a conjunction ("red AND round") or a target similar to its neighbours needs serial fixations. List length alone does not set difficulty — ten distinct items can beat five similar ones — and the tenth red button no longer pops out. The strict parallel/serial split is a simplification.
- **Evidence:** established for the guiding factors; qualified for the parallel/serial split
- **Design consequence:** Encode importance with ONE strong feature, never a combination; one pop-out per zone; remove look-alike competitors; keep locations and order stable; label when colour or shape is ambiguous. If the primary element needs two adjectives ("slightly bigger and slightly darker"), it does not pop. Drives (lens 04 · One accent per screen, made with the task's axis), (lens 01 · Hierarchy tools in order), (lens 11 · Destructive button names the action and keeps its distance), (lens 11 · Filters are visible, clearable and counted).
- **Myth it corrects:** "Salient = noticed"; "make it bigger and brighter".

### faces win
- **Claim:** Faces are processed holistically and configurally by a distributed network, and a face-like pattern captures attention before anything else. Inversion and distorted feature spacing disrupt recognition disproportionately; unfamiliar-face matching from photos is error-prone even for professionals; identity falls off quickly with eccentricity and crowding; about 2% of people cannot recognise faces at all; expressions are read probabilistically, not as fixed labels.
- **Evidence:** established
- **Design consequence:** A face is either the entry point or is kept away from the primary action it would out-compete. Tiny peripheral avatars never carry identity alone; avatars are paired with names; reaction icons never carry one assumed emotion. Drives (lens 01 · Distinctiveness sits outside the entry point's zone), (lens 01 · Image leads, text follows), (lens 11 · Icon-only controls carry a name).
- **Myth it corrects:** "One face zone"; "faces are recognised feature by feature"; "face blindness is rare and only after injury".

### Fitts's law
- **Claim:** Pointing time grows with the logarithm of distance divided by target width; coefficients vary by device. Screen edges and corners have effectively infinite width for a pointer, not for touch. The hand follows the eye: a target is found before it is pointed at.
- **Evidence:** established
- **Design consequence:** The hit area is never smaller than the visible control; small icons get larger invisible hit regions; touch targets are larger than mouse targets; sequential related targets sit close; persistent critical actions go to edges and corners; destructive actions are neither large nor convenient. Drives (lens 10 · Target size), (lens 10 · Distance and edges), (lens 12 · Thumb reach), (lens 11 · Destructive button names the action and keeps its distance).

### attentional capture
- **Claim:** Abrupt onsets, motion, flicker, strong colour and sounds capture attention involuntarily and quickly. Capture is probabilistic: goals, load, expectation and learned suppression of predictable distractors modulate it. Motion is the strongest peripheral attractor.
- **Evidence:** established; qualified for the exact boundary between the voluntary and involuntary systems
- **Design consequence:** Interruption (flash, motion, modal, sound) is reserved for genuine urgency; more than one motion source on screen at once is a competition the task loses; motion that does not communicate a real change is a cost. Drives (lens 09 · Frequency gate), (lens 09 · Stage one hero per beat), (lens 09 · No autoplay without a pause; no critical information in timed UI), (lens 10 · Timed paths and session expiry).
- **Myth it corrects:** "Motion is good because the periphery detects it."

### habituation
- **Claim:** Repeated identical signals stop evoking a response — eye-tracking, imaging and field data agree. A pulsing badge, a recurring banner or a warning on every routine save trains the user to ignore that class of signal, including the one instance that matters.
- **Evidence:** established
- **Design consequence:** A critical signal must be rare and visibly distinct from routine notifications; the same treatment never serves "cookie notice" and "payment failed"; looping decoration near the task is a warning. Drives (lens 05 · Red is reserved), (lens 05 · Toast behaviour), (lens 09 · Named purpose or nothing), (lens 05 · Error surface matches severity).
- **Myth it corrects:** "More warnings = safer."

### vigilance
- **Claim:** Detection of rare signals declines over prolonged monitoring with fluctuating arousal; there is no universal minute at which it drops. A second target within a few hundred milliseconds of the first is often missed (a laboratory window, not a UX threshold). Perception integrates over tens to hundreds of milliseconds in overlapping windows — there is no 60 fps "frame rate" of the brain.
- **Evidence:** established for the phenomena; contested for transferring the blink window to UX
- **Design consequence:** Two brief important messages never fire back to back in one stream; events get persistence and a log; a system that expects a human to catch a rare event needs redundancy and a status that escalates rather than a colour that flips. Drives (lens 05 · Status escalates), (lens 05 · One status mark, three scales), (lens 05 · Toast behaviour), (lens 14 · Interruption tolerance).
- **Myth it corrects:** "The brain runs at 60 fps"; "8-second attention span".

### inattentional blindness
- **Claim:** A fully visible but unexpected event is missed when attention is engaged elsewhere; misses rise with primary-task load, low similarity to the attended target, distance and low expectation. The event reached the retina and evoked neural responses — it lacked priority for awareness.
- **Evidence:** established
- **Design consequence:** "It is on the screen" is never evidence it was noticed. Feedback belongs next to the action, at the moment of action, and persists when missing it has consequences; a validation summary at the top of a form while the user is at Submit will not be seen. Drives (lens 05 · Error visibility on submit), (lens 05 · Success is confirmed, not assumed), (lens 10 · Status changes are announced without moving focus), (lens 10 · Errors are associated and announced).
- **Myth it corrects:** "Users see everything in front of their eyes."

### change blindness
- **Claim:** Large changes go unnoticed across a blank, a cut, a saccade, a blink, a reload or a shift of attention; about half of people miss a swapped conversation partner. Detection requires encoding before, preserving across, attending after and comparing. The world feels detailed because it is available for re-sampling, not because the brain keeps a photograph; memory across a saccade holds a few attended objects.
- **Evidence:** established
- **Design consequence:** Change is shown with continuity — expansion from the trigger, a brief highlight, before/after labels, focus moved to the new element — and the layout stays stable. A price that updates silently after a toggle, a list that reloads with no marker of what changed, a value that reverts on save: each is a failure of this mechanism, not of the user. Drives (lens 09 · Never appear from nothing), (lens 09 · Motion gaps), (lens 09 · Transition only what changes), (lens 05 · Success is confirmed, not assumed).
- **Myth it corrects:** "The user will surely notice an important change"; "the brain stores a sharp photograph of the whole field".

### saccadic suppression
- **Claim:** Around each saccade, sensitivity to low-frequency luminance and motion drops (suppression, not blindness) and whole-image displacements go unnoticed unless a landmark reveals them. Stability comes from an internal copy of the eye-movement command, predictive remapping, a few attended objects carried across the saccade and post-saccadic alignment to landmarks; which mechanism carries subjective stability is unresolved.
- **Evidence:** established for suppression and displacement suppression; qualified for the overall stability mechanism
- **Design consequence:** Changes that coincide with an eye movement, a blink, a page transition or a reload are invisible. Landmarks stay in place during change; important changes are introduced with motion or highlight while the user is looking, and confirmed persistently. Drives (lens 09 · Never appear from nothing), (lens 05 · Loading preserves layout and names the outcome), (lens 09 · Skip enter animations on first paint).
- **Myth it corrects:** "Vision is off during saccades"; "we see a smear".

### banner blindness
- **Claim:** Task-engaged users systematically skip regions that resemble advertising — by position (right rail, top strip), shape (bright bordered rectangle), animation, stock imagery and marketing language — especially during goal-directed tasks. The avoidance is learned and context-dependent.
- **Evidence:** established
- **Design consequence:** Operational content (notices, hints, empty-state help, the CTA) lives in the task flow and looks like content with specific language, never like a promo. Drives (lens 06 · Important content is not a banner), (lens 05 · Critical instruction is not an error).

### ensemble perception
- **Claim:** Without identifying individual items, people extract group statistics in one glance: mean size, orientation, numerosity, texture density, average expression, scene category. Peripheral vision may work as a compressed statistical description of the scene — useful, but incomplete as a model of everything the periphery does.
- **Evidence:** established for the phenomenon; qualified for the summary-statistic model of peripheral vision
- **Design consequence:** A list, chart or card grid is judged by its gist before anything is read. Repetition creates rhythm and lets a single exception pop; a uniform sea of similar items hides the one that differs, and one loud element among many loud elements is not distinct. Drives (lens 01 · Rhyme: uniformity for recognition, variety for content), (lens 01 · No blinding monotony, and the inverted dominant), (lens 11 · A card is one object, consistently laid out).

## Grouping, figure and hierarchy

### gestalt grouping
- **Claim:** Vision groups automatically before conscious reading: proximity, similarity, common fate, good continuation, closure, symmetry, common region and uniform connectedness (which can override distance and similarity). The principles are reliable tendencies whose winner depends on context, not laws. Texture segmentation runs on feature statistics, not drawn lines; the markup does not matter. Whatever spacing and similarity group together IS the structure the user perceives.
- **Evidence:** established for the principles; qualified for the order in which organisation processes run
- **Design consequence:** Spacing within a group is smaller than spacing between groups; similarity means shared role (a destructive and a safe action are never styled alike); containers and connectors only mark real semantic boundaries; whitespace and alignment come before dividers and nested boxes; every label, hint and error is closest to the element it belongs to; the structure survives a blur test. Drives (lens 01 · Outer gap beats inner gap), (lens 01 · Space first, shapes second, lines last), (lens 01 · Alignment as route), (lens 08 · Visible label: floating or above the field), (lens 06 · Related things sit together).
- **Myth it corrects:** "Gestalt principles are laws"; "every cluster needs a box"; "cards and shadows add clarity".

### figure–ground
- **Claim:** Which side of a boundary is the figure is decided by contrast, enclosure, convexity, size, symmetry, depth and familiarity, with boundary ownership coded early in cortex; T-junctions signal occlusion. Squeezed air becomes a figure of its own; a patterned background becomes a competing figure; a bordered surface becomes its own canvas.
- **Evidence:** established
- **Design consequence:** Emptiness is designed as an object with width, proportion, a centre and edges — its first job is separation, its second direction. A frame or shadow that crosses unrelated sections binds them; a scrim that does not occlude does not read as a layer. Drives (lens 01 · Counter-form is a designed object), (lens 01 · The canvas law: a bordered surface is its own canvas), (lens 03 · Shadows for elevation, borders for structure), (lens 11 · Background is inert and scroll is contained).

### gist first
- **Claim:** Perception goes whole → detail. Feature detectors fire before awareness; the gist of a layout is grasped in roughly 13–120 ms from low spatial frequencies, and hierarchy is read from contrast patches before any object is recognised. The entry point is decided in about 0.3 s, before reading.
- **Evidence:** established
- **Design consequence:** The composition must be readable blurred: the blobs must still show the hierarchy, and exactly one blob must lead. A small high-contrast element beats a large low-contrast one. Drives (lens 01 · Single dominant), (lens 01 · Contrast and air before size), (lens 03 · Salience survives grayscale), (lens 01 · Route in 0.3 s, no attention tearing).

### scene gist
- **Claim:** A scene's category is grasped in about 100 ms from global structure (openness, expansion, naturalness, roughness, navigability) before objects are identified; scene grammar (lamps above tables) speeds recognition and flags violations; navigation mixes body-centred and map-centred frames, and the internal map is schematic and fragmentary.
- **Evidence:** established for rapid gist; qualified for the division of labour among the scene regions
- **Design consequence:** A screen is read as a scene: users learn stable spatial roles (navigation, primary action, status) and orient before reading labels. Landmarks stay in place across screens; routes and exits are perceptually clear; global structure is established before dense detail; a destructive action in the navigation region is a grammar violation. Drives (lens 12 · Mobile screen structure), (lens 11 · Location is visible), (lens 01 · One grid describes every floor), (lens 11 · Button states are distinct and consistently placed).
- **Myth it corrects:** "A place is recognised by counting its objects"; "a literal map-picture in the head".

### object recognition
- **Claim:** Recognition builds increasingly complex, partly position-, scale- and viewpoint-tolerant representations along the ventral stream with distributed population codes. Easy images are categorised by a feedforward sweep within 100–200 ms; occluded, cluttered or unusual views need recurrent processing; coarse categorisation is faster than fine identification. There is no template match and no single recognition area; image classifiers are the best current models of the responses but not the mechanism.
- **Evidence:** established for the stream, invariance and recurrence; qualified for the biological invariance algorithm and the classifier correspondence
- **Design consequence:** Familiar shapes and stable conventions; when simplifying an icon keep its diagnostic contour and part relations (an envelope keeps its flap); separate segmentation from recognition with contrast and spacing; category recognition is easy, instance identification in clutter is not; icons are tested with and without labels, and never validated with an image classifier as a proxy for people. Drives (lens 11 · One glyph, recoloured per state; outline default, fill active), (lens 11 · Design at render size, on the grid, as vector), (lens 11 · Icon-only controls carry a name).
- **Myth it corrects:** "Recognition is template comparison"; "a grandmother cell for every object"; "recognition is purely feedforward"; "the brain is a convolutional net".

### optical vs geometric
- **Claim:** Perception measures optical size and position, not geometry. Round shapes need to overshoot squares to look equal; horizontals look thinner than verticals; rounding appears to start before the geometric corner; light on dark reads larger and heavier (irradiation), and a glowing screen amplifies it.
- **Evidence:** not rated
- **Design consequence:** Alignment and sizing are judged by eye; when a layout "is aligned by the numbers" but looks off, the eye is right. A dark theme is tuned, not inverted: light elements may need a lighter weight or a slightly smaller size. Drives (lens 03 · Optical over geometric), (lens 03 · Concentric border radius), (lens 03 · Dark mode is tuned, not inverted).

## Reading

### reading eye movements
- **Claim:** Reading is fixations plus saccades. The perceptual span is asymmetric (about 3–4 letters left of fixation, 14–15 right); the return sweep undershoots on long lines and multiplies on short ones; regressions rise with poor typography. Fixations remain necessary — "speed reading" that skips them trades comprehension. The eyes are never still even within a fixation (microsaccades, drift, tremor keep the image from fading), and one cannot smoothly trace a static line by will.
- **Evidence:** established; qualified for speed-reading claims
- **Design consequence:** Body text is left-aligned, ragged-right, 40–70 characters per line, with leading proportional to line length; the left edge is the anchor; long leader lines and centred multi-line paragraphs are flagged. Drives (lens 02 · Line length and reading alignment), (lens 02 · Leading by role, line length and density), (lens 02 · Wrap deliberately; truncate without losing content).
- **Myth it corrects:** "Speed reading removes fixations"; "the eye is still during fixation"; "eyes can smoothly scan any static object".

### letter recognition
- **Claim:** Words are recognised by parallel letter recognition, not by silhouette. Running text in capitals is roughly 10–18% slower: an unfamiliar pattern with no ascenders or descenders. Ambiguous glyphs (I/l/1, O/0) fail in codes and identifiers.
- **Evidence:** not rated
- **Design consequence:** Glyph distinctness is protected; decorative glyphs stay out of UI text; capitals are reserved for short elements (≤ 2–3 words), never running text. Drives (lens 02 · Glyph distinctness), (lens 02 · Caps only for short labels), (lens 08 · Identifiers are text, not numbers).
- **Myth it corrects:** "Words are read by their shape."

### critical print size
- **Claim:** Fluent reading needs an acuity reserve — characters several times the just-resolvable detail. Reading speed is flat above roughly 0.2° angular x-height and drops sharply below it; ~16 CSS px body text is a convention, the real variable is visual angle at the actual viewing distance. Ageing lenses transmit less short-wavelength light; acuity and crowding degrade text away from fixation.
- **Evidence:** established for the acuity reserve and contrast dependence
- **Design consequence:** Body size is judged in visual angle: roughly a 16px equivalent on a desktop, 10–30% smaller on a phone held closer, larger on a distant screen or a kiosk; captions and legal text are held to the floor too; the reader's own size settings are respected. Drives (lens 02 · Body size floors by viewing distance), (lens 02 · Respect the reader's settings), (lens 14 · Ultra-high legibility and touch targets).
- **Myth it corrects:** "16 px is a biological constant"; "bigger text fixes bad contrast".

### text–background polarity
- **Claim:** Dark-on-light gives a modest, replicated advantage in acuity and proofreading (a bright background contracts the pupil, reducing aberrations and increasing depth of field), for young and old alike; light-on-dark is legitimate in dark rooms, for glare and photophobia, and for OLED power. Pure black on pure white causes halation for long paragraphs; a WCAG ratio is a floor, not a perceptual model.
- **Evidence:** qualified for the polarity advantage and its pupil mechanism
- **Design consequence:** Both themes ship but are validated separately as real reading tasks — muted, disabled, placeholder and over-image text included; a barely-passing ratio at a small size in a thin weight is a failure in practice. Drives (lens 03 · Dark mode is tuned, not inverted), (lens 02 · Thin needs more contrast), (lens 03 · Contrast floors, measured on the rendered pair).
- **Myth it corrects:** "Dark mode reduces eye strain" and "dark themes are bad"; "WCAG pass = optimal".

## Colour

### colour opponency
- **Claim:** A single cone cannot separate wavelength from intensity; colour arises from comparing three broadly overlapping cone classes through opponent channels (roughly red–green, blue–yellow) plus an achromatic channel that carries fine detail. The chromatic channels have far lower spatial resolution than the luminance channel; saturation barely moves luminance. Two very different hues of equal lightness read as low contrast.
- **Evidence:** established
- **Design consequence:** Hierarchy, legibility and colour pairings are built on lightness difference; hue is a secondary layer; an edge defined by colour alone is blurry. Drives (lens 03 · Combine colours by lightness, not hue), (lens 03 · Gradients avoid mud), (lens 03 · One hue, many shades).
- **Myth it corrects:** "Colour is simply the wavelength of light"; "the cone classes are red, green and blue".

### luminance carries form
- **Claim:** The luminance channel carries edges, shape and fine detail; chroma is blurry. What survives grayscale is what the visual system uses to read structure. A vivid button that vanishes in grayscale has no hierarchy; two hues used as "contrast" with matching lightness have none.
- **Evidence:** established
- **Design consequence:** Meaning or state is never encoded by hue alone (a blocking failure); hierarchy is checked in grayscale and every relationship that mattered must survive. Drives (lens 03 · Salience survives grayscale), (lens 03 · Colour as a code), (lens 10 · Non-colour cues and reduced motion), (lens 05 · Selected and disabled survive greyscale).
- **Myth it corrects:** "Different colours give contrast"; "far apart on the colour wheel = distinguishable".

### colour constancy
- **Claim:** Perceived hue depends on surround, adaptation, illuminant and memory (a grey banana looks yellowish); constancy is partial. The same value reads differently on different surfaces, next to different neighbours and under different ambient light.
- **Evidence:** established
- **Design consequence:** Colours are checked on the surfaces and beside the neighbours they will actually have; a "success" green that matches the brand blue in luminance is not distinct; semantic roles get separate light and dark values, never an inverted palette. Drives (lens 03 · Contrast floors, measured on the rendered pair), (lens 03 · Muted and tinted, not raw and neutral), (lens 03 · Dark mode is tuned, not inverted).
- **Myth it corrects:** "Constancy makes colour independent of illumination"; "dark mode = invert the palette".

### colour vision deficiency
- **Claim:** Deficiency reduces discrimination along specific directions — mostly red–green, rarely blue–yellow — and almost never produces grayscale vision; about 8% of men and 0.5% of women of Northern-European ancestry are affected. A simulation reveals failures but never proves success.
- **Evidence:** established
- **Design consequence:** Every distinction carried by colour gets a redundant cue (text, icon, shape, position, pattern); red/green as the sole status distinction is blocking; every state (hover, focus, disabled, error, visited) is reviewed for colour-independence. Drives (lens 10 · Non-colour cues and reduced motion), (lens 03 · Colour as a code), (lens 11 · Tables and charts expose values).
- **Myth it corrects:** "Colourblind people see in black and white"; "a simulation pass proves accessibility".

### metamerism
- **Claim:** Two colours that match on one display or for one observer can differ on another; a match is a property of the whole chain (spectra, display, observer, surround), not of the values.
- **Evidence:** established
- **Design consequence:** A palette is never "perfectly accessible" in the abstract: contrast and distinctness are measured on the rendered pair on representative hardware, and semantic roles are defined by role, not by a value that happened to match. Drives (lens 03 · Contrast floors, measured on the rendered pair), (lens 03 · Primitives by hue, semantics by role), (lens 12 · Hardware is the bar).
- **Myth it corrects:** "A palette can be perfectly accessible."

## Depth and motion

### depth cues
- **Claim:** Depth is inferred from many cues weighted by reliability: occlusion (order, no distance), perspective, texture gradient, relative and familiar size, height in the field, atmospheric contrast (farther = lighter, lower contrast, cooler), shading under a light-from-above prior, cast shadows, blur, motion parallax; disparity only in real 3D. Full depth perception exists without stereopsis. Conflicting cues cause instability and discomfort.
- **Evidence:** established
- **Design consequence:** On a screen, layering is carried entirely by pictorial cues, so elevation, shadow, blur and occlusion must map to real state (active, interactive, modal) and stay consistent — one light direction, one depth relationship per screen, edge-anchored elements flat. Secondary elements recede by being lighter, thinner and cooler, not smaller. Drives (lens 01 · Depth by position, one depth relationship), (lens 01 · Farther is lighter, thinner, cooler), (lens 03 · Natural darkening and cool shadows), (lens 11 · Materials and depth).
- **Myth it corrects:** "The brain simply averages cues."

### motion perception
- **Claim:** Motion is computed from spatiotemporal change by direction-selective filters, not by comparing stored frames. Local measurements are ambiguous and are resolved by integrating edges, corners and context. Perceived speed depends on contrast (low-contrast motion looks slower), spatial frequency and eccentricity; a moving frame induces motion in a static object; prolonged motion produces after-effects; apparent motion links discrete events into a trajectory.
- **Evidence:** established
- **Design consequence:** Animation communicates a real change, is brief, interruptible and honoured under reduced motion; tiny or low-contrast motion is misjudged; a moving surround makes static content drift; a progress indicator's speed must not misrepresent progress. Drives (lens 09 · Named purpose or nothing), (lens 09 · Motion is not doing the job of hierarchy), (lens 09 · Reduced motion means gentler, not none), (lens 09 · Never animate what the user is waiting on).
- **Myth it corrects:** "Peripheral vision is always better at motion" (it detects large slow events; direction, speed and identity accuracy depend on size and contrast).

### object constancy
- **Claim:** When an object changes position, size, shape or colour continuously, it is seen as the same object and tracked without being re-identified; a cut between two states removes that link and leaves the viewer to compare the states from memory. Things that change together are grouped: in a crowdsourced perception study common motion grouped more strongly than changing luminance and than static size or luminance, and changing size more strongly than changing luminance or static position. Controlled experiments support animated transitions where the task is tracking change or keeping a map of a space: animated transitions between statistical charts improved judgements of change over static cuts (staged transitions were usually most accurate and most preferred, but not for every chart type); animating viewpoint changes in a zoomable space improved reconstruction of the space with no time penalty; animated scrolling at 300–500 ms cut task time by up to 5.3 % for reading and up to 24 % for symbol counting, and reading errors by up to 54 %, against jumps. The limits are as well documented: reviews of animation for explaining complex systems found little benefit over equivalent static graphics, because animations are often too fast or complex to perceive and are understood as discrete steps; transitions work when simple and predictable, and complex ones when staged; rotation is harder to follow than translation or expansion; morphing an object into an unrelated one asserts a false relation. The data-graphic and zoom transitions studied ran about 1 s or longer, beyond interface budgets, so their durations do not transfer.
- **Evidence:** qualified — established for tracking change in visualisations and for viewpoint navigation; indirect for interface transitions in general; no controlled evidence was found for most named motion techniques (masking, cloning, overlay, easing) beyond this continuity argument.
- **Design consequence:** Carry one object through a change instead of swapping it, start and end it at the element the user acted on, keep motion simple, stage complex changes, and never let timing group what the layout separates. Motion earns this benefit only where the user must track what changed or where they are; elsewhere it is cost. Drives (lens 09 · Four usability jobs: expectation, continuity, narrative, relationship), (lens 09 · Transformation keeps one object through a change of role), (lens 09 · Value change shows live data as live), (lens 09 · Masking changes what an object is by what it reveals), (lens 09 · Cloning: new objects are born from their cause), (lens 09 · Dolly and zoom keep the user's place between levels), (lens 09 · Offset and delay encode grouping).
- **Myth it corrects:** "Animation always aids understanding" — it aids tracking and orientation; for explaining a process it rarely beats an equivalent static sequence.

### optic flow
- **Claim:** Wide-field expansion and rotation patterns support heading, balance and time-to-contact. The same retinal shift can come from an object, the eye, the head or the whole scene; the cause is inferred from the eye-movement copy, vestibular and contextual signals.
- **Evidence:** established
- **Design consequence:** Full-screen scroll, zoom and parallax animations engage self-motion systems and cause vestibular discomfort; scroll-jacking that decouples scene motion from the user's gesture breaks the expected relation between action and sensation. Drives (lens 09 · Scroll-driven motion is triggered by scroll, not controlled by it), (lens 09 · Sheets and drawers move with the hand), (lens 09 · Respond on pointer-down, track 1:1, keep the gesture honest), (lens 14 · Scroll follows the touch).

## Memory and load

### working memory
- **Claim:** Working memory holds about four independent chunks (three to five), not seven plus or minus two — the classic seven was never derived as a limit and never as a menu rule. Only what must be held actively counts; what is visible lives in external memory for free. It is an active resource spent by every extra decision, tab switch and interruption; its limit contributes to change blindness.
- **Evidence:** established for the limit and its effects; qualified for the exact "four"
- **Design consequence:** An undivided homogeneous group holds ≤ 4–5 items; open threads between steps ≤ 3–4; side-by-side comparisons ≤ 4 columns; nothing is carried between screens that the interface could show; a confirmation restates what is being confirmed. Drives (lens 06 · Groups and open threads stay within working memory), (lens 04 · Side-by-side comparisons stay at most four columns), (lens 08 · Multi-step forms show purpose and preserve answers), (lens 08 · Never block paste, typing or zoom).
- **Myth it corrects:** "7±2: no more than seven items in a menu"; "users will remember codes and instructions".

### chunking
- **Claim:** Capacity is counted in meaningful units, not symbols; grouping only helps when the user already has a structure for it (date, phone, card number). A grouping with no schema behind it does nothing.
- **Evidence:** qualified
- **Design consequence:** Long numbers, codes and IDs are split into the groups users know; long forms into meaningful sections; navigation into structures the user already has, not arbitrary sevens. Drives (lens 06 · Chunk long strings and long forms), (lens 07 · One number format per product), (lens 08 · One value, one field).

### cognitive load
- **Claim:** Intrinsic and extraneous load share one resource; extraneous load hurts task and learning. Split attention — related things apart in space or time — is load in itself. Density is not load; hidden dependencies, remembered rules and duplicated information are.
- **Evidence:** established
- **Design consequence:** Label, error and hint sit next to their element; the same information is not repeated across modalities on one screen; complex-task screens carry no decoration; a dense but structured screen is not a defect. Drives (lens 06 · Related things sit together), (lens 05 · Validation keeps the value and speaks in text), (lens 08 · Hints before input, not in tooltips), (lens 01 · Prototypical layout, moderate colour, low incidental complexity).
- **Myth it corrects:** "Dense = high cognitive load."

### recognition over recall
- **Claim:** Recognising a shown option is cheap and near error-free; retrieving it from memory is expensive and fragile. Designers overestimate newcomers' memory.
- **Evidence:** established
- **Design consequence:** Options and state are shown: visible menus, autocomplete over blank fields, recents, format examples, entered data visible where it is needed; unlabelled icons only for hyper-conventional signs. Drives (lens 06 · Show options and state instead of asking for recall), (lens 11 · Icon-only controls carry a name), (lens 08 · Keyboard and autocomplete match the field), (lens 08 · Multi-step forms show purpose and preserve answers).
- **Myth it corrects:** "Users can be counted on to remember instructions and codes."

### serial position
- **Claim:** First and last items are recalled best; the middle sags; the effect is strongest when items are presented sequentially.
- **Evidence:** established
- **Design consequence:** In a sequence (scroll, steps, carousel, feature list) key messages go first and last; the final screen restates the takeaway rather than showing only a Done button. Drives (lens 06 · Key messages first and last), (lens 12 · Longread dramaturgy), (lens 05 · Success is confirmed, not assumed).

### forgetting curve
- **Claim:** Forgetting is fast then flattens; the shape is reliable, "X% after an hour" is false precision. Exposure is not learning — encoding depends on what the person does. Old knowledge blocks new (proactive interference) and new blocks old; cues work when they match the encoding context.
- **Evidence:** established for the shape and interference; qualified for consolidation timing and encoding specificity
- **Design consequence:** A one-time tour is not a strategy; a redesign leaves a transitional cue at the old location; "learned" behaviour is measured after an interval, not on day one; the system never forces recall of what it can show. Drives (lens 06 · Novice guidance fades but stays available), (lens 13 · Define the metric before the work), (lens 11 · Location is visible).
- **Myth it corrects:** "Seeing it once = remembering it"; "a logical redesign is easy for old users".

### spacing and retrieval
- **Claim:** Retrieval practice beats restudy after a delay; spaced exposure beats massed exposure (meta-analytic evidence across hundreds of experiments). Desirable difficulties apply to learning, not to basic operation.
- **Evidence:** established
- **Design consequence:** Teaching happens at the moment of use, by doing rather than watching; hints reappear when the situation recurs, not ten in a row on first launch; friction is never added to routine operation in the name of learning. Drives (lens 06 · Novice guidance fades but stays available), (lens 05 · Give, then ask), (lens 08 · Hints before input, not in tooltips).
- **Myth it corrects:** "A one-time tour explains everything"; "more repetitions in a row is better".

## Mental models and expectation

### predictive brain
- **Claim:** The retinal image is ambiguous; what is seen is an inference combining sensory evidence with learned regularities (light from above, objects continue behind occluders, the world is stable). Priors dominate when the signal is weak, brief, peripheral, low-contrast or ambiguous; strong evidence overrides expectation. The brain does not scan, it predicts and verifies: a confirmed prediction is pleasant, a broken one costs energy. Conscious processing is narrow (on the order of tens of bits per second) while the automatic layer is orders of magnitude wider, so design works with automatic processing first. Illusions are side-effects of normally useful assumptions, not failures; no expectation-free "objective look" exists.
- **Evidence:** established for perception as inference, priors and context effects; qualified for predictive coding as the literal neural algorithm
- **Design consequence:** The first pass confirms expectations (about nine-tenths of what the eye meets is what it predicted) and novelty is a thin second layer that never lives in the function of a control. Meaning never rests on a weak signal the user must fill in (icon-only controls with unusual glyphs, a state signalled by a faint hue shift); shaded elements read as raised or sunken through the light-from-above prior. Drives (lens 01 · Prototypical layout, moderate colour, low incidental complexity), (lens 06 · Conventional things in conventional places), (lens 03 · Shadows for elevation, borders for structure), (lens 11 · Modals).
- **Myth it corrects:** "We only see what we expect"; "illusions are failures of the visual system"; "one can just look objectively".

### schemas and scripts
- **Claim:** An organised knowledge structure for a typical situation guides attention, fills gaps and distorts recall; a script supplies the expected step order and violations are noticed. Context given beforehand aids comprehension; given afterwards it may not. Recent stimulation biases current perception (priming, adaptation); expected stimuli are detected faster; language labels steer categorisation.
- **Evidence:** qualified
- **Design consequence:** A stage is named before its fields; a flow follows the order the user's script expects (context, then action, then confirmation); familiar placement and meaningful context speed recognition; previews and labels prepare the user. Drives (lens 05 · Context before action), (lens 04 · Task profiles at a glance), (lens 08 · Multi-step forms show purpose and preserve answers), (lens 07 · Every screen answers four questions).

### mental models
- **Claim:** Users act through a selective working model built from the system image — what is actually observable — not from the designer's conceptual model. Experts organise by principles, novices by surface. Metaphors transfer relational structure only with a relevance cue. "Matching models improves usability" is an under-operationalised claim; the construct itself is a working hypothesis.
- **Evidence:** qualified; contested for the construct as a measurable entity
- **Design consequence:** Five layers are audited — objects (one thing with three names), relationships (visual nesting that contradicts the data), states (hidden or ambiguous), causality (a command that looks local but acts globally), constraints (a rule that appears only after an error). What a setting applies to is shown before it is changed. Drives (lens 07 · Every string has one role), (lens 08 · Switches change state now and say which state), (lens 06 · Choice with consequence), (lens 08 · Multi-step forms show purpose and preserve answers).
- **Myth it corrects:** "Users see the interface as the designer intended"; "a logical structure is enough"; "a good metaphor explains itself".

### expertise reversal
- **Claim:** Guidance that helps a novice (hints, onboarding, wizards, worked examples) becomes extraneous load for an expert; the expert's model is not ideal for everyone either.
- **Evidence:** qualified
- **Design consequence:** Novice support fades — dismissible, collapsed after first success, with a direct path — while staying available; the scaffolding is not stripped to serve experts. Drives (lens 06 · Novice guidance fades but stays available), (lens 04 · Layered UX), (lens 11 · Disclosure exposes its state and does not hide the essentials).
- **Myth it corrects:** "More guidance is better for everyone"; "the expert model is ideal for all".

### affordance and signifier
- **Claim:** An affordance is a possibility of action; a signifier is the visible cue that tells the user the action exists. On a screen every "affordance" is perceived, so what matters is the signifier: interactive elements must look interactive before use. Many "user errors" come from an interface that suggested the wrong model.
- **Evidence:** established
- **Design consequence:** Links are identifiable, inputs have a boundary, controls read as controls and content as content; hover-only clickability and gesture-only navigation are failures; minimalism is not the removal of cues. Drives (lens 06 · Affordances are perceived, not physical), (lens 11 · Links are identifiable and say where they go), (lens 08 · Fields have a visible boundary), (lens 01 · Controls read as controls; content reads as content).
- **Myth it corrects:** "This element has an affordance" (meaning: it looks clickable — that is a signifier); "clean = fewest cues".

### conventions
- **Claim:** Users hold shared mental models of where elements live (logo → home, magnifier, cart, gear, tabs, corner close); matching them makes an interface feel effortless. Consistency is about meaning and behaviour, not looks. Conventions are learned and not universal across platforms and cultures; an original interface is not automatically better — breaking a convention forces relearning.
- **Evidence:** established for shared placement models; qualified for "expectation match makes interfaces invisible"
- **Design consequence:** A convention is broken only for a measurable benefit, with a visible purpose, a clear signifier, an immediate reversible result and a familiar fallback; novelty in base patterns (search, links, close, back) is flagged. Drives (lens 06 · Conventional things in conventional places), (lens 06 · Consistency over creativity), (lens 12 · Platform patterns and predictable back), (lens 10 · Shortcuts follow platform conventions).
- **Myth it corrects:** "An original, unlike-any-other interface is always better"; "familiar conventions are universal"; "consistency = visual repetition".

### mapping
- **Claim:** The relation between a control and its effect is read from spatial and semantic correspondence: controls near what they affect, direction that matches the change, a label that names the resulting state. A poor mapping is a mistake waiting to happen.
- **Evidence:** not rated
- **Design consequence:** Scope and consequence are visible before commitment; a toggle describes the ON state; motion direction is vocabulary (forward goes forward); Cancel sits beside Commit and looks like the lighter option. Drives (lens 07 · Links say where they go; toggles describe ON), (lens 09 · Direction is vocabulary), (lens 08 · Switches change state now and say which state), (lens 06 · Cancel next to commit).

### feedback loop
- **Claim:** The model stays accurate only when every action returns a visible result: mapping tells the user what will happen, feedback tells them what did. Without it the user repeats, doubts or abandons; feedback that arrives late or far from the action is not connected to it.
- **Evidence:** not rated
- **Design consequence:** Every pressable element has a press state; a response arrives within about 100 ms regardless of processing time; success is confirmed, not assumed; autosave says its state. Drives (lens 09 · Feedback within 100 ms, regardless of processing time), (lens 09 · Every pressable element has a press state), (lens 05 · Success is confirmed, not assumed), (lens 08 · Autosave says its state).

## Choice, risk and bias

### Hick–Hyman law
- **Claim:** Choice time grows roughly logarithmically with the number of comparable, uncertain alternatives. "Fewer options always better" does not follow: thirty items in five clear groups beat a flat list, and hiding common actions behind layers costs more than showing them.
- **Evidence:** established for the law; qualified for its generalisation to menus and catalogues
- **Design consequence:** Large sets are structured, not amputated; a menu "limited to seven" that hides frequent actions under "More" is a defect; the navigation count is a tell, not a verdict. Drives (lens 04 · Comparison cost, not count of options), (lens 11 · Tabs over hamburger for primary navigation), (lens 06 · Simplicity over configuration).

### reference point
- **Claim:** Choices are coded relative to a reference point — what the user has, expects, was promised or saw during a trial — with diminishing sensitivity (0→100 feels larger than 1,000→1,100). Any effect claimed from prospect theory needs the reference point, outcomes and probabilities fixed in advance.
- **Evidence:** qualified overall; established for the fourfold pattern and its cross-cultural replication
- **Design consequence:** The real reference point is identified before any pricing or comparison UI; struck-out prices only if real and relevant; a comparison rail sits exactly where numbers are compared; when a product gets worse, the loss is named directly. Drives (lens 06 · Money is explicit), (lens 06 · Number links to source), (lens 04 · A comparison rail appears exactly where numbers are compared).
- **Myth it corrects:** "Prospect theory explains any decision and any price manipulation."

### loss aversion
- **Claim:** Losses weigh more than equal gains on average, but the classic coefficient of about 2.25 was a 1992 model parameter; meta-analyses give about 1.96 (with enormous heterogeneity) and about 1.31 for individual risky choices. Loss aversion is not negativity bias and not emotional intensity; the endowment effect shrinks with better procedures; risk attitude flips with domain and probability.
- **Evidence:** qualified
- **Design consequence:** "2×" is never cited as a design law and alarmist copy is never justified by loss aversion; what a trial removes and when is stated; risk is shown as percent plus natural frequency with a shared denominator; streaks get a freeze or recovery path; regret, cancellations and support load are measured, not only conversion. Drives (lens 06 · Money is explicit), (lens 06 · No dark patterns), (lens 05 · Calm bad news), (lens 13 · Define the metric before the work).
- **Myth it corrects:** "A loss is exactly twice a gain"; "people always avoid risk"; "the endowment effect proves loss aversion".

### framing
- **Claim:** Equivalent descriptions change preferences (gains vs losses, "90% survive" vs "10% die"); the average effect replicates but is moderate and depends on frame type, domain, probabilities, option set and audience — it shifts a distribution, it does not steer a person. Frames are set by unit and period, order and preselection, action names ("skip" vs "keep current plan"), colour and highlight.
- **Evidence:** established that framing can change choice; qualified for its size
- **Design consequence:** For serious decisions both frames are shown (benefit and risk, kept and lost, cost now and over the full period) with the same unit and base; a plan "per day" against a competitor's "per year" compares frames, not offers; a button names the consequence, not a feeling. Drives (lens 06 · Money is explicit), (lens 07 · Verb-first buttons that repeat the consequence), (lens 06 · What happens next).
- **Myth it corrects:** "The right framing guarantees a change of choice."

### anchoring
- **Claim:** A quantitative estimate shifts toward a number presented or considered beforehand. It is a robust group effect, but standard tasks cannot measure a stable individual trait, so "suggestible users" do not exist as a segment. Heuristics in general substitute an accessible cue for a hard computation and are adaptive when the environment supplies good cues.
- **Evidence:** established for the group effect and for its unreliability as an individual measure
- **Design consequence:** Every hidden reference point the UI supplies is listed — defaults, placeholders that look like values, the first plan, struck prices, preselected tips, estimates — and revision after the anchor is allowed; salience is aligned with importance. Drives (lens 06 · Defaults are labelled recommendations), (lens 07 · Placeholder copy is flagged), (lens 06 · Number links to source), (lens 08 · Hints before input, not in tooltips).
- **Myth it corrects:** "Anchoring is a personality trait"; "heuristics are the errors of a lazy brain".

### availability
- **Claim:** Frequency and probability are judged by how easily examples come to mind; a single vivid case outweighs a statistic. Representativeness crowds out base rates, though base-rate neglect is heterogeneous across people and strategies.
- **Evidence:** qualified
- **Design consequence:** Denominator and period accompany every rate ("18 of 42,000 orders in 30 days"); a testimonial is paired with aggregate statistics; a short time series is never styled as a trend; charts expose the values behind them. Drives (lens 06 · Number links to source), (lens 13 · Evidence, not taste), (lens 11 · Tables and charts expose values).
- **Myth it corrects:** "People always completely ignore base rates."

### defaults
- **Claim:** No neutral choice interface exists (set, order, naming, preselection, inaction outcome, steps). Defaults are the most robust tool — meta-analytic evidence across dozens of studies gives a medium-to-large average effect with wide heterogeneity, including null and reversed cases — working through implied recommendation, status quo and effort saving. "Nudging in general" has no reliable universal effect and shrinks sharply at scale; the possibility of opting out does not by itself make a default ethical. Friction is useful when symmetric and protective, harmful when asymmetric.
- **Evidence:** established for the average default effect; qualified for its mechanisms
- **Design consequence:** Every default is justified by the user's interest and labelled as a recommendation; opt-in for privacy, payment, risk and data transfer; active choice when preferences differ; effort symmetry for opposite actions (subscribe vs cancel, accept vs refuse); a preselected add-on or a "recommended" badge with no basis is a dark pattern. Drives (lens 06 · Defaults are labelled recommendations), (lens 06 · Defaults must work), (lens 06 · Symmetric friction), (lens 06 · Optional is labelled and skippable), (lens 06 · No dark patterns).
- **Myth it corrects:** "A default is a neutral technical setting"; "an opt-out makes the nudge ethical"; "nudges always work"; "any influence is manipulation".

### choice overload
- **Claim:** Choice overload is not a law: a meta-analysis found a near-zero mean effect; what matters is task complexity, set complexity, preference uncertainty and decision goal. Comparison cost, not option count, is the variable.
- **Evidence:** established for the null on average; qualified for the moderators
- **Design consequence:** Comparison cost is fixed first — grouping, comparable attributes, filters, trade-off explanations — before any option is cut; three plans with incomparable attributes are worse than ten comparable ones; a catalogue cut "to avoid overload" is a tell. Drives (lens 04 · Comparison cost, not count of options), (lens 04 · Choose among similar items: catalog, plan comparison, list of options), (lens 11 · Filters are visible, clearable and counted).
- **Myth it corrects:** "More options → worse choice."

## Error and recovery

### slips lapses mistakes
- **Claim:** Error is a description of a mismatch, not a cause. Slips (right goal, wrong action — competing habits, look-alike controls), lapses (a step dropped from memory), mistakes (wrong plan or model) and violations (a conscious bypass under pressure) need different fixes; behaviour moves between skill, rule and knowledge levels within one task. Recurrence is set by task and system conditions; blame without analysis prevents nothing; text instructions cure knowledge gaps, not slips.
- **Evidence:** established for the distinction and the system approach; qualified for the skill/rule/knowledge model
- **Design consequence:** Prevent (safe defaults, distinguishable objects and modes, preview before apply), detect (immediate local feedback, message next to the source), recover (undo, drafts, retry without duplicates, input preserved), learn (near misses, workarounds). Undo for frequent reversible local actions; review plus specific confirmation for rare irreversible ones; errors identified in text with a suggested fix; no redundant entry. Drives (lens 05 · Slips cannot commit, and work is never lost silently), (lens 05 · Reversible is undo first), (lens 05 · Error copy answers four questions), (lens 11 · Destructive button names the action and keeps its distance), (lens 08 · Forgiving inputs).
- **Myth it corrects:** "User error proves inattention"; "write an instruction and the error disappears"; "any error can be fully prevented"; "confirmation always prevents error"; "undo is always better than confirmation".

### layered defences
- **Claim:** Serious harm is an active failure plus latent conditions — identical environment names, a dangerous default, no versioning — passing through aligned holes in several imperfect layers. A forcing function can exclude a specific danger, but over-blocking creates workarounds; a checklist works only as part of a designed system; automation redistributes error, trust and monitoring load rather than removing the human.
- **Evidence:** established for the system approach and automation effects; qualified for forcing functions and checklists
- **Design consequence:** Irreversible actions are quarantined behind proportionate constraints, with data check, review and reversibility for legal, financial and data-changing actions; confirmations name action, object, scale and consequence; production and staging never share a header colour; system confidence and intervention paths are visible. Drives (lens 04 · Quarantine for the irreversible), (lens 05 · Destructive safeguard), (lens 05 · Validation keeps the value and speaks in text), (lens 05 · Progress is honest).
- **Myth it corrects:** "Automation removes the human factor"; "a checklist guarantees no errors"; "the systems approach means nobody is responsible".

### warning habituation
- **Claim:** Repeated identical warnings are auto-confirmed; the routine dialog trains the reflex that later dismisses the critical one. Compliance with security and safety warnings falls with every repeat.
- **Evidence:** established
- **Design consequence:** Confirmation is reserved for rare, serious, irreversible actions and is specific to them; red is reserved; error surfaces scale with severity so that the critical one looks unlike the routine one. Drives (lens 05 · Red is reserved), (lens 05 · Error surface matches severity), (lens 05 · Destructive safeguard), (lens 05 · Critical instruction is not an error).
- **Myth it corrects:** "More warnings = safer"; "confirm operation?" dialogs as protection.

## Aesthetics and first impression

### processing fluency
- **Claim:** The brain monitors the ease of its own processing and feels it as familiarity, beauty, trust and usability. Prototypical layout, symmetry and repetition raise fluency; solvable complexity gives interest through a second route. Fluency is one route to pleasure, not the whole of it.
- **Evidence:** qualified
- **Design consequence:** Function is fluent (a stranger says within a second what the screen is for and what to do); character is interesting (typography, rhythm, illustration, voice). Novelty in the task model — an unusual close gesture, controls that are "art" — is a defect. Drives (lens 01 · Prototypical layout, moderate colour, low incidental complexity), (lens 01 · Stylistic cohesion), (lens 06 · Consistency over creativity), (lens 06 · Conventional things in conventional places).
- **Myth it corrects:** "Beautiful = whatever the brain processes easily."

### aesthetic–usability
- **Claim:** Attractive systems are judged more usable and tolerated longer — the effect is real for perceived usability — but a multi-session study found no effect of aesthetics on task performance. Attractiveness, perceived usability and task success are three measurements.
- **Evidence:** qualified for the effect; established for the null on objective performance
- **Design consequence:** A polished screen whose task metrics were never measured is not evidence; an unreadable hierarchy (no dominant, no nameable route, dominant lost in grayscale) is blocking because it blocks the task, a nuance-level hierarchy or dominance issue is a warning, and a functional failure is blocking; aesthetics and usability are measured separately, and a purely stylistic taste call with no effect on the task is not a finding. Drives (lens 13 · Evidence, not taste), (lens 13 · Define the metric before the work), (lens 01 · Stylistic cohesion).
- **Myth it corrects:** "A beautiful interface is automatically more usable."

### first impression
- **Claim:** Attractiveness judgements form in about 50 ms and correlate with judgements at 500 ms; the strongest predictors are low visual complexity and high prototypicality, with moderate colourfulness. Visual complexity is heterogeneity and weak grouping, not element count: ten aligned rows are simpler than three unrelated blocks. The judgement is of attractiveness, not usability, and it is a different phenomenon from any "attention span".
- **Evidence:** qualified
- **Design consequence:** The layout looks like its genre; colourfulness is moderate; what is minimised is incidental complexity — distinct alignment systems, competing accents, irregular grouping, no repeating structure — never the content. A sparse but chaotic screen fails; a dense but coherent one passes. Drives (lens 01 · Prototypical layout, moderate colour, low incidental complexity), (lens 03 · Colour balance is never equal), (lens 01 · Consistency beats perfection).
- **Myth it corrects:** "8-second attention span"; "users decide in 8 seconds".

### symmetry and curvature
- **Claim:** Preference for symmetry and for curved over angular contours exists on average (curvature: meta-analytic), modulated by context and domain; meaningful asymmetry creates dynamics and hierarchy, perfect symmetry can look dull, and angles suit precision, speed, strength or warning. Shared taste is strongest for faces and landscapes, weakest for artefacts. No beauty centre and no formula of beauty exist; colour has no universal emotional dictionary.
- **Evidence:** established for the average curvature preference and distributed aesthetic processing; qualified for the rest
- **Design consequence:** Symmetry is used for stability and broken for hierarchy; radius is an intentional expression, not a blanket rule for every corner; "blue means trust" is treated as a learned convention to reinforce, never as self-explanatory. Drives (lens 03 · Concentric border radius), (lens 01 · Force lines and the central axis), (lens 01 · Contrast and air before size), (lens 03 · No colour-psychology folklore).
- **Myth it corrects:** "Symmetry is always more beautiful"; "round is always better"; "a beauty centre"; "beauty is fully subjective" and "beauty has a scientific formula"; "blue evokes trust and red urgency in everyone".

### credibility filter
- **Claim:** General knowledge about the brain does not protect against neuromyths: learning styles (matching format to a "style" does not improve outcomes), left/right-brained people (lateralisation is local; no globally dominant hemisphere in a sample of over a thousand), "10% of the brain", and the fabricated "8-second attention span". Some fast effects are real (50 ms attractiveness); the fabricated ones can only be refuted indirectly.
- **Evidence:** established for the chapter; contested for the goldfish statistic (unrefutable because fabricated)
- **Design consequence:** Before building on "science says": primary source? independently replicated? meta-analysis or one striking paper? sample size? who is selling it? Any single-number law used as a hard constraint is a note against the rationale, not the screen; a "visual learner mode" or a persona segmented by hemisphere is folklore. Drives (lens 06 · No UX folklore), (lens 13 · Evidence, not taste), (lens 03 · No colour-psychology folklore).
- **Myth it corrects:** "Learning styles"; "left-brained / right-brained"; "10% of the brain"; "8-second attention span".

## Consciousness and awareness

### conscious access
- **Claim:** Stimuli influence behaviour without awareness (masked priming, blindsight, unseen cues); awareness needs sufficient signal, attention and recurrent, sustained processing. Attention, confidence and consciousness are dissociable; no accepted theory exists (workspace, recurrent-processing and integrated-information accounts compete; the front-versus-back debate is open); there is no fixed frame rate and no single centre. Intelligent behaviour does not prove awareness.
- **Evidence:** established for the dissociations; qualified for the neural markers; contested for the theories
- **Design consequence:** Presence on screen does not guarantee conscious detection and behaviour does not prove notice; "users said they saw it" is a weak measure. State changes never rely on a single subtle cue or a brief transient — persistent, redundant feedback beats a 300 ms fade. Assistants are not described as "aware" in copy. Drives (lens 09 · Motion is never the only channel), (lens 09 · Never opacity alone, rarely more than two properties), (lens 05 · Success is confirmed, not assumed), (lens 10 · Status changes are announced without moving focus).
- **Myth it corrects:** "Vision = conscious seeing"; "if the brain processes it, the person sees it"; "consciousness sits in one centre"; "the brain assembles reality 60 times a second"; "intelligent behaviour proves consciousness".

## Myths and oversimplifications

All 79 rows of the source's myths database, plus the chapter-level corrections below them. Verdict as the source gives it: **M** = myth, **S** = strong simplification; the letter after it is the evidence grade of the correction (A established, B qualified, C contested).

| Myth | What is actually known | What the critic should do instead |
|---|---|---|
| Users see everything in the field of view, right in front of their eyes (M, A) | Without attention even a large visible object is not consciously registered (inattentional blindness, the gorilla study); we are aware mainly of what attention selected. | Treat "it is on the screen" as no evidence of notice; place signals in the task's focus. |
| The user will surely notice an important change — it is right there (M, A) | Changes that coincide with a transition, reload or a shift of attention are missed (change and inattentional blindness); salient motion does attract gaze. | Introduce important changes with motion, in focus, with persistent confirmation. |
| The brain stores a sharp photograph of the whole visual field (M, A) | Change blindness shows no complete internal copy; stability comes from active vision, attention and a world available for re-fixation. | Never rely on users comparing two states from memory. |
| The brain literally paints in the missing peripheral pixels (S, B) | Filling-in exists (blind spot), but the brain mostly does not represent unneeded detail and moves the eyes instead; the mechanism of subjective completeness is contested. | Assume the periphery holds gist, not detail. |
| The eye sends ready-made camera frames to the brain (M, A) | The retina transmits parallel transformed streams about contrast, colour differences and change, not pictures. | Reason about edges, contrasts and changes, not "the image". |
| Illusions are failures or breakdowns of the visual system (M, A) | They are side-effects of normally useful priors and predictions that misfire in unusual conditions. | Use illusions as evidence of which assumptions the layout triggers (e.g. light-from-above). |
| One can "just look objectively", switching off expectations (M, B) | Top-down influence is built into perception down to early cortex; no expectation-free view exists, though awareness of expectations helps. | Test with real users; do not trust the designer's own "fresh eyes". |
| The brain assembles reality exactly 60 times a second (M, A) | No single frequency; sensory, attentional and conscious processes run on different, overlapping timescales. | Reject frame-rate analogies for perception; keep animation rules empirical. |
| Consciousness is a series of identical discrete frames with continuity painted between them (S, B) | Competing discrete, continuous and hybrid models; temporal integration and postdiction exist, but fixed identical frames are unproven. | Do not derive timing thresholds from a "frame" model. |
| Vision = conscious seeing; we are aware of everything the visual system processes (M, A) | Blindsight and unconscious processing show vision guides behaviour without awareness. | Provide feedback that reaches awareness; do not infer awareness from behaviour alone. |
| Consciousness sits in one specific brain centre (S, B) | Distributed recurrent network activity; the front-vs-back debate is open. | Ignore "centre" rhetoric in design rationales. |
| Intelligent behaviour = consciousness; an AI that behaves intelligently is aware (M, B) | Function (discrimination, report, sensible answers) does not guarantee subjective experience — the hard problem. | Do not describe assistants as "aware" in copy. |
| The fovea is the only part of the retina that sees (M, A) | The whole retina sees; the periphery supplies coverage, event detection, twilight vision and saccade targets. | Design the periphery to guide, the centre to read. |
| The periphery is just a blurred centre (S, A) | Different coding format; the key limit is crowding, which blur does not reproduce; an isolated letter can be sharp yet lost among neighbours. | Judge spacing, not only size, for anything read off-centre. |
| We do not see colour in the periphery (M, A) | Colour is perceived with enough size and contrast; detecting a saturated colour and naming a hue are different tasks. | Peripheral colour cues must be large and saturated; naming still needs a label. |
| Peripheral vision is always better at motion (S, B) | Good at detecting large, low-frequency dynamic events; direction, speed and identity accuracy depend on size, contrast and eccentricity. | Use motion for alerting only; never for identification. |
| Enlarging an object makes peripheral vision identical to central (M, A) | M-scaling equalises acuity and contrast sensitivity but not crowding, positional uncertainty or all colour differences; critical spacing barely depends on size. | Increase spacing alongside size. |
| Cortical magnification is the brain's software zoom (M, A) | A fixed structural property of receptor and ganglion-cell distribution, not a switchable zoom. | Do not assume users can "zoom in" attentionally on dense peripheral content. |
| The crowding distance is always exactly half the eccentricity (S, A) | Critical spacing scales with eccentricity, but the coefficient varies with direction, similarity, grouping, task and field location. | Use 0.5·E as a heuristic; verify crowded clusters empirically. |
| Crowding is just blur or a lack of attention (M, A) | A separate phenomenon: occurs with large sharp letters, depends on spacing, harms identification not detection, not removed by attention or size. | Flag dense icon rows and adjacent badges as crowding, not "small text". |
| Speed reading removes fixations and grabs paragraphs peripherally (S, B) | Acuity and crowding cap the perceptual span; radical speed-ups trade comprehension (skimming); fixations remain necessary. | Design text for fixation-by-fixation reading (line length, leading). |
| The eye is completely still during fixation (M, A) | Microsaccades, drift and tremor are always present; without them a static image fades. | Nothing to do on screen; reject "static gaze" models in eye-tracking claims. |
| The eyes can be moved smoothly by will across any static object (M, A) | Without a real moving target the eyes make small saccades; pursuit is driven by a cortical motion signal. | Do not expect users to "trace" static lines smoothly (e.g. long leader lines). |
| We are aware of and control all our eye movements (S, A) | Most saccades and all micro-movements are automatic and unconscious; perception is suppressed during saccades. | Treat gaze as largely involuntary; guide it with hierarchy. |
| Eye movements are mechanical reflexes unrelated to thinking (M, A) | Some are reflexive (VOR, optokinetic), but in natural behaviour gaze is distributed by task and precedes action. | Read gaze data as task strategy, not reflex. |
| During a saccade we see a smeared picture (M, A) | Saccadic suppression lowers sensitivity before and during the saccade; neither smear nor displacement is perceived. | Changes timed with gaze shifts are invisible — announce them otherwise. |
| Attention is a single "willpower" one just tenses (S, B) | A set of mechanisms: spatial, feature, object; endogenous/exogenous; dorsal/ventral networks; partly captured by stimuli, limited by competition. | Diagnose which attention channel a signal relies on. |
| Several things can be done at once — attention just splits in half (M, B) | Automatised actions combine, but attention-demanding tasks are switched, not paralleled; accuracy and speed drop; inattentional blindness rises. | Do not design flows that require monitoring two regions at once. |
| Human attention span is shorter than a goldfish's — 8 seconds (M, C) | The number is fabricated; "attention span" is not one number; first impressions are fast (~50 ms) but that is a different phenomenon. | Strike the claim from briefs; invest in the first screen for aesthetic impression, not "span". |
| We use only 10% of our brains (M, A) | Nearly all regions are used daily; damage almost anywhere yields deficits. | Reject "unlock hidden potential" product claims. |
| Logical people are left-brained, creatives right-brained (M, B) | Lateralisation is local to networks; no globally dominant hemisphere (n = 1,011). | Never segment users or layouts by hemisphere. |
| People are visual, auditory or kinesthetic learners — teach in their style (M, B) | Matching format to "style" does not improve outcomes; choose format by content. | One strong multimodal interface, no "visual learner mode". |
| The 7±2 rule: no more than seven items in a menu (S, B) | The classic paper did not derive a menu rule; the limit is closer to ~4; grouping and recognisability matter more than a magic number. | Judge menus by grouping and labels, not count. |
| Users can be counted on to remember instructions and codes (S, B) | Working memory is tiny and recall unreliable; designers overestimate newcomers' memory. | Recognition over recall: show options, autofill, no cross-screen memory. |
| Recognition is comparison with a template in memory (M, A) | Pixel templates fail under image variability; the brain builds invariant representations ("untangling"). | Keep diagnostic structure when simplifying icons. |
| There is a "grandmother cell" for every object (M, B) | Highly invariant cells exist but many respond to several related concepts and live in memory structures; coding is populational. | Nothing to do; reject single-cell rhetoric. |
| All recognition "happens" in one area (IT) (S, A) | Distributed along the ventral stream, linked to memory, attention and action; no homunculus. | — |
| Recognition is purely feedforward (S, A) | Fast for easy images; hard images (occlusion, noise, odd views) need recurrent feedback. | Give difficult visuals more contrast, separation and time. |
| The brain works like a convolutional neural net (S, B) | CNNs are the best quantitative models of higher visual neurons but diverge from humans (adversarial examples, texture bias, no recurrence). | Do not validate icons with an image classifier as a proxy for people. |
| There is one "face zone" (FFA) where all face recognition happens (S, A) | A distributed network (OFA, FFA, STS) plus memory and social systems with different roles. | — |
| We recognise faces by a list of features (S, A) | Mostly holistic and configural: relations and the whole matter; inversion and composites disrupt it. | Do not distort facial proportions in illustrations or tiny avatars where identity matters. |
| Prosopagnosia is a rare consequence of severe brain injury (M, A) | Developmental prosopagnosia without lesions affects ≈2% of people. | Pair avatars with names; never rely on face alone. |
| We know what place we are in by recognising enough objects (S, A) | Scene gist is grasped in ~100 ms from global structure, often before objects. | Establish global layout before detail. |
| A literal map-picture of the terrain is stored in the head (M, B) | A distributed code in place and grid cells; schematic, distorted, fragmentary. | Provide explicit wayfinding cues; do not assume users hold a map. |
| Place and grid cells are about vision and sit in visual cortex (S, A) | They are in hippocampus and entorhinal cortex; work in darkness from self-motion; visual landmarks anchor them. | — |
| Colour is simply the wavelength of light entering the eye (S, A) | Depends on context, illumination (constancy) and memory of typical colour; colour is a brain inference. | Check colours on the surfaces and next to the neighbours they will have. |
| Colourblind people see the world in black and white (M, A) | Most distinguish many colours but confuse specific pairs (mostly red–green); full achromatopsia is very rare. | Redundant coding; avoid red–green as the sole distinction. |
| Blue evokes trust and red urgency in everyone (M, B) | No universal colour dictionary; meaning depends on context, culture, hue, saturation, neighbours and task. | Treat semantic colours as learned conventions to reinforce, never as self-explanatory. |
| Beauty is fully subjective — no shared regularities (M, B) | Statistical tendencies (fluency, symmetry, prototypicality, curvature) exist; weight varies by domain and person. | Use tendencies as probabilities; segment by audience. |
| Beauty is universal — apply the scientific formula (M, B) | Science gives probabilities, not a formula; culture, function, meaning can outweigh form. | Same. |
| There is a separate beauty centre in the brain (M, A) | Distributed sensory, evaluative, semantic and self-referential systems. | — |
| Beautiful = whatever the brain processes easily (S, B) | Complexity and novelty can please through interest and successful understanding; fluency is one route. | Keep function fluent, allow character to be interesting. |
| Symmetry is always more beautiful than asymmetry (M, B) | Symmetry contributes on average; meaningful asymmetry creates dynamics and hierarchy; perfect symmetry can look dull. | Break symmetry where hierarchy needs it. |
| Round shapes are always better than sharp ones (M, A) | Average preference for curvature, but angles suit precision, speed, strength or warning. | Radius as intentional expression, not a blanket rule. |
| A beautiful interface is automatically more usable (M, B) | Aesthetics lifts perceived usability and tolerance; success, time and errors may not improve. | Measure aesthetics and usability separately. |
| An original, unlike-any-other interface is always better — it stands out (S, B) | Users rely on learned conventions; breaking them forces relearning; innovate where it adds value, keep base patterns. | Flag novelty in base patterns (search, links, close). |
| Any influence on choice is manipulation (S, B) | No neutral environment; the line is drawn by goal, transparency, autonomy, ease of exit, symmetry of friction, verifiable consequences. | Audit intent and symmetry, not mere presence of influence. |
| A default is a neutral technical setting (M, A) | Defaults change choice via recommendation, status quo and effort; they are behavioural interventions. | Require a user-interest justification for every default. |
| If opting out is possible, the nudge is automatically ethical (M, B) | Ethics also needs clarity, honest goal, proportionality, fair distribution, protection of vulnerable groups, reversibility, accountability. | Apply the seven-question ethics check. |
| Nudges always work (M, A) | Heterogeneous mechanisms; overall effect contested and small at scale; needs an RCT of the specific design and long-term check. | Demand a test of the specific intervention. |
| More options → worse choice (S, A) | Mean overload effect ≈ 0 in the 2010 meta-analysis; comparison complexity, preference uncertainty and error cost matter. | Fix comparability and grouping before cutting options. |
| The right framing guarantees a change of choice (S, A) | Average effect moderate and context-dependent; it shifts distributions, not individuals. | Show both frames for serious decisions. |
| A loss is always felt exactly twice as strongly as an equal gain (M, A) | λ is a model parameter (2.25 in 1992; ≈1.96 and ≈1.31 in meta-analyses), not a universal emotional coefficient. | Never cite "2×" as a design law. |
| People by nature always avoid risk (M, A) | Attitude flips with domain and probability (fourfold pattern). | Present probabilities and outcomes honestly in both domains. |
| Loss aversion means any negative emotion is stronger than positive (S, A) | A preference parameter relative to a reference point, not negativity bias or emotional intensity. | Do not justify alarmist copy with loss aversion. |
| The endowment effect directly proves loss aversion (S, B) | The WTA–WTP gap also reflects procedure, understanding, preference uncertainty and seller role. | — |
| Prospect theory explains any decision and any price manipulation (S, A) | Testable prediction needs outcomes, reference point, probabilities and parameters fixed in advance. | State the reference point before claiming an effect. |
| Heuristics are the errors of a lazy brain (S, A) | Heuristics save time and data; quality depends on environment fit. | Give heuristics good cues instead of fighting them. |
| Anchoring is a stable personality trait (S, A) | Robust group effect; standard tasks cannot measure individual susceptibility. | Never build "suggestible user" segments. |
| People always completely ignore base rates (S, B) | Neglect is common but heterogeneous; some use base rates near-normatively. | Show denominators and base rates. |
| "User error" proves inattention or incompetence (M, A) | Recurrence is set by task and system conditions; blame without analysis prevents nothing. | Ask what made the error likely. |
| Write an instruction and the error disappears (M, A) | Helps knowledge gaps and rare procedures; slips, overload, poor distinguishability and conflicting stimuli are not cured by text. | Prefer constraints, distinguishability and feedback to text. |
| Any error can be fully prevented (S, A) | Specific classes can be made impossible; complex systems keep unknown scenarios — detection, recovery and learning are needed. | Design undo and recovery, not only prevention. |
| More warnings = safer (M, A) | Repeated identical warnings habituate and dull the critical one. | Make critical warnings rare and distinct. |
| Confirmation always prevents error (M, A) | Routine dialogs are auto-confirmed; for frequent reversible actions undo matters more. | Confirmation only for rare, serious, irreversible actions. |
| Undo is always better than confirmation (S, A) | Immediate, external, legal or irreversible consequences need prior review. | Choose by reversibility and consequence. |
| A checklist guarantees no errors (M, B) | Long, badly embedded or ritual checklists are skipped or ticked mechanically. | Short, sequenced, state-linked checklists. |
| Automation removes the human factor (M, A) | It creates monitoring, trust and intervention tasks and moves errors into configuration, data and interaction. | Make system confidence and intervention paths visible. |
| The systems approach means nobody is responsible (M, B) | A just system separates unintended error, risky compromise and conscious disregard while fixing conditions. | Keep accountability language without blame framing. |

#### Chapter-level corrections that are not rows in the database
These appear in chapter texts (mostly the applied "Vision in Design" chapters) and are useful filters, though not yet carded in the source:
- "The F-pattern is a law / put everything top-left" → an observation on text-heavy LTR pages; dashboards, checkout, galleries, mobile and RTL differ.
- "Fixation = attention / understanding" and "no fixation = not processed" → both false; covert attention exists, gaze ≠ comprehension.
- "Salient = noticed", "make it bigger and brighter" → salience raises probability only when relevant and uncrowded.
- "Gestalt principles are laws", "every cluster needs a box", "cards and shadows add clarity" → tendencies; over-grouping fragments the page.
- "16 px is a biological constant", "WCAG pass = optimal", "dark mode reduces eye strain" / "dark themes are bad", "bigger text fixes bad contrast" → conventions and floors, not perceptual truths.
- "Different colours give contrast", "far apart on the colour wheel = distinguishable", "a palette can be perfectly accessible", "simulation pass proves accessibility", "dark mode = invert the palette" → hue ≠ luminance; simulation reveals failures, never proves success.
- "This element has an affordance" (meaning: looks clickable) → that is a signifier; "clean = fewest cues", "consistency = visual repetition", "familiar feels good so it is good", "progressive disclosure = hide it", "intuitive for me = intuitive".
- "One main action per screen" → one stable priority structure; "dense = high cognitive load" → load cannot be read from density.
- "Motion is good because the periphery detects it" → costs unless it communicates change; "vision is off during saccades", "one natural scan path per interface", "eye tracking reads thoughts".
- "Seeing it once = remembering it", "a one-time tour explains everything", "a logical redesign is easy for old users" (proactive interference), "more repetitions in a row is better" (spacing wins).
- "Users see the interface as the designer intended", "a good metaphor explains itself", "the expert model is ideal for everyone".
- Notably absent from the source: "users don't scroll" and the "3-click rule" — there is no card on either; the critic does not cite the foundations for them. Both remain plain heuristics with no evidence rating.

## Chapters added in review (2026-09-26)
Eight chapters that existed only as a title were written on 2026-09-26 from verified sources and sit in the source with status "in review". They are not yet merged into this file as mechanisms; until the owner signs them off, the critic may cite them as `qualified` at most. Findings the lenses already use:
- **Time, waiting and responsiveness** — the 0.1 / 1 / 10 s windows are expert estimates, not measurements; the "400 ms Doherty threshold" is not in its source; "100 ms = 1 % of revenue" has no peer-reviewed source; the only peer-reviewed skeleton-vs-spinner comparison found no difference; liking a progress indicator is not the same as a shorter wait.
- **Interruptions, switching and multitasking** — interruptions of ~3–4 s multiply sequence errors in step tasks; resumption cost is seconds, not the mythical "23 minutes"; ignored notifications still distract; batching three times a day beats both a constant stream and switching everything off.
- **Emotion, affect and impression** — peak and end dominate remembered experience, but a plain average predicts nearly as well; emotion cannot be read reliably from faces; the "sunny-day mood" effect did not replicate.
- **Trust, authority and social influence** — social comparison moves behaviour by a few percent; the hotel-towel norm effect is contested; "two thirds obey" is one Milgram variant (43.6 % across 21 conditions); aggressive dark patterns nearly quadruple acceptance while fake urgency alone did nothing in one experiment.
- **Motivation** — expected tangible rewards lower later free-choice interest; informative positive feedback raises it; gamification helps learning results slightly but not motivation in rigorous studies.
- **Habits, reinforcement and dark patterns** — habit automaticity takes a median ~66 days with huge spread, not 21; dopamine codes prediction error, not pleasure; dark patterns are common and effective.
- **Why vision does not work like a camera** and **Examining popular myths about vision** — synthesis chapters; no fixed frame rate (flicker artifacts visible up to ~500 Hz at sharp edges), the brain does not flip the image, blue-filter glasses probably do not reduce eye strain, time outdoors is the one trial-backed factor against myopia.
Also in progress and flagged by the source: human error and forgiving design, central and peripheral vision, eye movements, visual stability and object recognition ("in review"); all light, retina, transmission and feature chapters are research first passes. Until those close, entries drawn from them keep their stated evidence level and the critic treats a `qualified` rating there as `contested` when a finding would be blocking on that basis alone.

## Glossary
One line per term, as the source's terms database defines them; duplicates merged.
- **Acuity reserve** — the excess of character size over the acuity threshold needed for comfortable, fluent reading.
- **Active vision** — vision as a process in which eye movements and attention themselves choose what information to acquire.
- **Affordance / signifier** — a perceived possibility of action / a visible cue that tells the user how to act.
- **Anchoring** — a shift of a quantitative estimate toward a previously presented or considered number.
- **Aperture problem** — the ambiguity of an extended edge's motion direction when viewed through a small window (receptive field).
- **Attentional capture** — sudden, moving or vivid stimuli automatically pulling attention.
- **Availability heuristic** — judging frequency or probability by how easily examples come to mind.
- **Banner blindness** — systematic ignoring of regions that resemble advertising.
- **Base rate** — the prior prevalence of an event or category before case-specific evidence.
- **Biased competition** — stimuli in a receptive field compete for representation; attention biases the competition toward the selected one.
- **Binocular disparity / stereopsis** — positional difference of a feature in the two eyes' images / depth perceived from it.
- **Blindsight** — responding to visual stimuli without awareness after V1 damage.
- **Border ownership** — coding of which side of a boundary belongs to the figure.
- **Critical spacing** — crowding's critical distance, roughly half the eccentricity; the minimum target–flanker distance at which crowding still impairs recognition.
- **Center–surround antagonism** — receptive-field organisation with opposite responses in centre and surround.
- **Change blindness** — failing to notice large scene changes that coincide with an interruption (blink, cut, screen change) or lack attention.
- **Choice architecture / nudge / default / sludge** — the organisation of the decision environment / an environment change that predictably shifts behaviour without banning options / the state that holds if nothing is changed / harmful or asymmetric friction.
- **Chunking / working memory / cognitive load** — grouping items into meaningful units / the active seconds-long system holding a few items / the amount working memory must process at once.
- **Cognitive bias / heuristic** — a systematic deviation from a normative criterion / a simplified strategy using part of the available information.
- **Colour constancy / colour opponency / trichromacy / univariance** — stability of surface colour across illumination / comparison of cone classes with opposite signs / coding by S, M, L cones / one receptor cannot tell wavelength from intensity.
- **Colour-vision deficiency (CVD)** — altered colour perception, mostly red–green; ≈8% of men.
- **Configural / holistic processing** — processing spatial relations among facial features / perceiving a face as one whole.
- **Contrast (Weber, Michelson) / contrast sensitivity / contrast ratio (WCAG)** — ΔL/L for a small object on a background; (Lmax−Lmin)/(Lmax+Lmin) for patterns / the inverse of the minimum detectable contrast / text-to-background luminance ratio, ≥ 4.5:1 for ordinary text.
- **Contrast gain control / divisive normalization** — adaptive sensitivity to the contrast range / a neuron's response scaled by the surrounding population's activity.
- **Corollary discharge / efference copy / reafference principle** — an internal copy of the motor command sent to sensory areas / used to predict the sensory consequences of movement / the principle by which self-caused sensory change is told apart from external change.
- **Cortical magnification / M-scaling** — disproportionate cortical representation of central vision / enlarging a peripheral stimulus to equalise cortical representation.
- **Covert attention / presaccadic attention** — shifting attention without moving the eyes / the attention shift to a saccade target before the eyes move.
- **Decision weight / value function / reference point / diminishing sensitivity / loss aversion** — the transformed influence of a probability / mapping of gains and losses to subjective value / the state relative to which outcomes read as gain or loss / equal changes matter less farther from the reference / losses weighted more than equal gains.
- **Endowment effect** — valuing an owned object differently from the identical object before ownership.
- **Endogenous vs exogenous attention** — voluntary, goal-driven vs stimulus-captured attention.
- **Ensemble perception** — rapid extraction of summary statistics of a group (mean size, direction, mood).
- **Error terms: slip / lapse / mistake / violation** — right intention, wrong execution / a dropped step / a wrong plan / a conscious rule deviation.
- **Expectation effect / prediction error** — a sensory response changed by expectation (expected suppressed, representation sharpened) / the discrepancy between predicted and actual signal.
- **Face-inversion effect / composite face effect** — disproportionate loss for inverted faces / aligned halves of two faces fusing into a new whole.
- **F-pattern** — denser fixations upper-left on text-heavy pages in Western languages (observation, not law).
- **Feature-based / object-based / spatial attention** — prioritising a feature everywhere / a whole object / a region of the field.
- **Figure–ground** — dividing a scene into a foreground object and a continuing background.
- **Fitts's law / Hick's law** — pointing time grows with distance and shrinks with target size / choice time grows logarithmically with the number of options.
- **Fixation / saccade / main sequence / fixational eye movements** — the stable interval between saccades / a rapid gaze jump / the fixed relation of saccade amplitude, peak velocity and duration / microsaccades, drift and tremor.
- **Fluent print size range** — letter sizes at which reading runs at maximum speed.
- **Forcing function / constraint / confirmation / undo** — a hard block until a condition is met / a system property narrowing possible actions / a pause to re-check intent before acting / reversal of a completed action.
- **Framing** — different judgements from formally equivalent presentations.
- **Gestalt grouping: proximity, similarity, good continuation, common region / uniform connectedness** — near or similar elements group / aligned elements read as one contour / elements in one bounded or connected area read as one object.
- **Global neuronal workspace / recurrent processing theory / posterior hot zone** — awareness as broadcast to a frontoparietal network / awareness from local feedback loops in sensory cortex / posterior sensory areas closely tied to the contents of experience.
- **Inattentional blindness** — not noticing a clearly visible object while attention is occupied.
- **Lateral inhibition** — neighbouring channels suppressing each other through antagonistic connections.
- **Luminance / brightness / text–background polarity** — photometric light measure / subjective lightness / dark-on-light (positive) vs light-on-dark (negative).
- **Manifold untangling / recognition invariance / core object recognition** — transforming representations until categories become linearly separable / robustness of recognition to position, size, view and lighting / fast (~100–200 ms) recognition at a glance.
- **Mental model / schema / script / conceptual model / system image** — the user's working model of the system / an organised knowledge structure for a typical situation / knowledge of a routine's step order / the designer's intended model / everything the product actually shows.
- **Motion energy / direction selectivity / global motion / optic flow** — directed motion measured by spatiotemporal filters / different responses to different directions / integrated object or field motion / the field of image velocities during relative motion.
- **Perceptual grouping / perceptual span / visual span** — automatic Gestalt grouping / the region around fixation yielding useful information per fixation in reading / the number of letters identifiable in one fixation.
- **Perceptual uniformity / luminance ordering / redundant coding** — equal data steps give equal perceived colour steps / monotonic lightness along a scale / duplicating a colour distinction with another cue.
- **Predictive coding / predictive remapping / prior / Bayesian inference** — the brain predicts input and passes up only the error / receptive fields shift to their post-saccadic position before the saccade / a built-in or learned expectation about the world / estimating the most probable cause by combining evidence with priors.
- **Priority map / selection history** — an internal map of where attention and the next saccade should go / prior goals, rewards and distractors changing later priority.
- **Processing fluency / prototypicality / aesthetic–usability effect** — subjective ease of processing / similarity to a category's typical member / attractive systems seeming more usable.
- **Prosopagnosia** — selective impairment of face recognition with intact object recognition.
- **Receptive field / retinotopy / visual hemifield / visual eccentricity** — the region whose stimulation changes a neuron's response / preserved neighbourhood of retinal points in central structures / left or right half of visual space relative to fixation / angular distance from the fixation point.
- **Recognition over recall** — recognising a shown option is easier than retrieving it from memory.
- **Representativeness heuristic** — judging probability by similarity to a prototype.
- **Saccadic suppression / saccadic suppression of displacement / transsaccadic integration** — reduced sensitivity just before and during a saccade / failing to notice a whole-image shift made during a saccade / combining information across a saccade.
- **Scene gist / spatial envelope / rapid scene categorization** — the general meaning of a scene grasped in ~100 ms / global scene properties (openness, expansion, naturalness, roughness) defining its shape without objects / classifying a scene within tens to hundreds of ms.
- **Serial position effect** — first and last list items recalled better than the middle.
- **Swiss cheese model / active failure / latent condition / warning habituation** — layered defences whose aligned holes let harm through / an error at the sharp end / a weakness laid earlier in process or technology / declining response to repeated similar warnings.
- **Top-down / bottom-up processing** — knowledge and expectation shaping perception / processing from signal to interpretation.
- **Vestibulo-ocular reflex / smooth pursuit / vergence** — eyes counter-rotating to head movement / slow tracking of a moving target / opposite eye movements changing the angle between visual axes.
- **Visual hierarchy / visual complexity / visual search** — the order in which elements attract attention / the number and heterogeneity of elements and relations to process / finding a target among distractors.
- **Visual stability problem** — why the world looks still though each saccade shifts the retinal image.
