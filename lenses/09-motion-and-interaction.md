# 09 — Motion and interaction

Whether something should move, how it moves, and how the interface answers a hand. Order: name the product's motion register (one per product), run the frequency and purpose gates on every moving thing, then judge duration and easing,
choreography, physicality and overlay motion, gestures, interruptibility, properties, feedback and timing, reduced motion, and last the anti-slop signature.
Pre-tests: toggle reduced motion; open and close every overlay twice in a second; trigger the top three actions from the keyboard.
Hit areas → lens 10; overlay structure and focus → lens 11; mobile-native tells → lens 12; INP and load budgets → lens 13.
Static designs prove little here; prototypes prove origin and path; code and live builds prove the rest.

## Motion registers

### Name the register before the first finding
- **Rule:** Before any motion finding the critic names the product's register — restrained, production polish, or playful — and judges every duration, curve and overshoot against that register's band, never against a universal cap. One register per product (about 90 % of motions); a rare moment (success, onboarding, empty state) may borrow the next register up, eased into, never snapped. Default is restrained; production polish for shipped consumer and SaaS surfaces; playful only for rare moments or products whose register is play. The playful posture is for learning, portfolios and personal work; shipped task UI is judged through restraint or polish and reserves play for onboarding, empty states, showcases and celebrations.
- **Why:** Restraint applied to a kids app kills it; polish applied uniformly is the slop the anti-checklist flags; play leaked into utility actions fatigues on the tenth repeat [habituation].
- **Check:** State the register and its weighting in the review header. Derive it from product type and the moment (table below); where the project's log names one, use it. Then list every motion whose band, curve or overshoot belongs to another register.
- **Severity:** note (a weighting decision, not a defect; the mismatches it exposes carry their own severity)
- **Tells:** showcase-grade scroll choreography on a task screen; a portfolio-style hero inside an admin panel; a dashboard reviewed as if every delight moment were a defect.
- **Catalog:** N-01

| Register | Sub-registers | Products and moments | What it adds | What it cuts | Failure when over-applied |
|---|---|---|---|---|---|
| Restrained (default) | corporate — enterprise, dashboards, admin, healthcare, banking; the UI default: quick / standard / slow 200 / 300 / 450 ms, standard curve, 0–3 % overshoot, straight paths, slide-and-fade from one side | Productivity tools, SaaS dashboards, keyboard-driven apps, banking and serious UI; primary for productivity and dashboards, secondary for mobile, e-commerce and marketing (forms, nav) | The frequency gate; speed as perceived performance; interruptibility; origin-aware motion | Animation on high-frequency and keyboard-initiated actions; anything over ~300 ms (180 ms ideal); bounce on utility UI | A kids app or a marketing page judged as a shortcut-driven tool: every delight moment flagged, the product ends up dead and "correct" |
| Production polish | premium — fashion, finance, luxury, editorial, portfolios: 350 / 500 / 800 ms, gentle-float curve, 0 % overshoot, smooth curves and subtle parallax, fade + scale 98 → 100 % entrance; never squash-stretch | Shipped consumer apps, mobile apps, e-commerce, marketing pages, client work; primary for mobile, e-commerce, marketing, portfolios, kids apps | Enter recipe (opacity + small translate + small blur, never on body text); exits subtler than enters; zero-bounce springs; shadows over borders; optical alignment; animated icon swaps; 200–500 ms band | Instant state swaps; enter/exit symmetry; noticeable motion ("nice animation!" is a failure); too subtle is invisible, too slow is waiting | The recipe applied uniformly: blur on everything, identical fade-ups on every block |
| Playful | playful — social, kids, creative tools, celebrations: 150 / 250 / 400 ms, ease-out-back and bouncy springs, 10–20 % overshoot, arcs, bounce-up entrance, squash-stretch allowed · energetic — gaming, sports, events, fitness, marketing: 100 / 180 / 300 ms, expo / elastic curves, 15–30 % overshoot, dramatic diagonal arcs, snap-from-edge entrance | Creative portfolios, kids and educational apps, onboarding, empty states, product showcases, experiments; selective only elsewhere (onboarding, empty states, delighters, showcases) | Easing as personality; bounce and elastic curves in pure CSS; typed properties for curved paths; fill-mode discipline; scroll-triggered motion decoupled from scroll speed | Motion that fatigues on the tenth repeat; elastic easing on serious or error UI; effects with no "what could this become" answer; overshoot above 25 % (reads as broken); maximum everywhere (nothing stands out); no settle (chaos) | Delight leaks into utility actions: bouncy dropdowns, stagger on settings lists, mount animations on body copy |

Domain defaults: financial → restrained or premium, low density; healthcare → restrained and calm, 300–600 ms, very low density; enterprise SaaS → restrained; e-commerce → polish, medium; editorial → premium; social → playful; gaming → energetic.

### One register, applied everywhere; same trigger, same motion
- **Rule:** Every duration and easing value is explainable from the named register. A brand's motion identity is three constants: one signature easing for ~80 % of motions, a three-step duration palette (quick / standard / slow), one entrance pattern. Identical triggers produce identical motion product-wide; crisp and fast in a professional tool, allowed a touch slower or bouncier in a playful product, never both in one product.
- **Why:** Personality and learnability are both built by repetition [conventions]; a second motion voice reads as borrowed, and a surprise on the hundredth viewing is an irritation [habituation].
- **Check:** Pull the motion variables (or list every curve and duration in the code); do they fit one row of the table? Trigger the same interaction on three screens. Watch a whole session, not one instance. Static designs cannot prove this; mark not-reviewed unless the prototype carries motion.
- **Severity:** warning
- **Tells:** generic ease everywhere (no register); bouncy springs on one menu and linear fades on the next; a modal that scales on one screen and slides on another; three different curves for three dropdowns.

### Easing and overshoot follow the register and the moment
- **Rule:** The curve communicates: elastic and bouncy read as energetic and juvenile, ease-out and zero-bounce springs read as professional; brand personality, not habit, picks the family. Overshoot budget by register — restrained 0–3 %, polish 0 %, playful 10–25 %, energetic 15–30 % — and by moment: feedback 2–5 %, success 5–10 %, celebration 15–25 %, error always 0 %. Above 25 % reads as broken. Overshoot or bounce on a utility action (dropdown, toggle, menu, modal, settings) is always a finding, whatever the register; "add overshoot when it feels flat" applies to playful surfaces only.
- **Why:** Overshoot is the loudest personality signal and is felt before it is understood [gist first]; misplaced, it contradicts the brand in 200 ms and on an error or a destructive action it contradicts the meaning.
- **Check:** Name the brand in one adjective and the dominant easing family in the build; do they agree? List every bouncy or elastic use on error states, destructive confirms, disable transitions, financial or medical flows, and anything repeated often — each is a hit. Check overshoot is consistent across screens.
- **Severity:** warning; blocking on error, financial or medical flows
- **Tells:** overshoot on a dropdown or toggle; spring bounce on a settings panel; a bouncy error shake; a spring on a Delete confirmation; a bank app on ease-out-back; one bounce curve reused everywhere regardless of element.

### Delight survives the golden rule
- **Rule:** Even in the playful register the best motion goes unnoticed: it enhances without demanding attention, feels expected, serves a function, and does not fatigue on repeat. Celebration moments are the exception, not every button.
- **Why:** Delight is a first-time effect; on the tenth trigger the same motion is an attention tax [habituation] [attentional capture].
- **Check:** Trigger the interaction ten times in a row: still pleasant, or already annoying? Would the user notice if it were removed (good) or notice that it is there (bad)? Runtime only.
- **Severity:** warning
- **Tells:** a "wow" effect on a control used many times per session; users describe the motion rather than the task; onboarding animation replaying on every visit.

## Motion serves one of four usability jobs

### Four usability jobs: expectation, continuity, narrative, relationship
- **Rule:** Every motion that survives the frequency gate does at least one of four usability jobs, and the finding names which. **Expectation** — the object looks and behaves the way the user predicts; the gap between what is expected and what happens is closed. **Continuity** — the flow is unbroken within one scene and across the scenes of a journey. **Narrative** — separate moments read as one chain of cause and consequence in time and space. **Relationship** — motion shows how objects relate in space, time and hierarchy: which belongs to which, which is in front, which came from which. A motion that does none of the four is decoration and goes to the deletion test (lens 09 · Named purpose or nothing). Separate real-time motion (direct manipulation: the motion is the interaction) from post-action motion (a transition after the input that briefly locks the user out): post-action motion costs time on every repeat and carries the burden of proof. The jobs are a purpose test, not a licence: no job overrides the frequency gate, the keyboard rule, the register, the wait rule or reduced motion; when a technique would break one of those, the restraint rule wins and the job moves to a rarer moment or to a static cue.
- **Why:** Motion is read before it is understood — trajectories set predictions [predictive brain], continuous change keeps an object's identity [object constancy], and shared timing groups things [gestalt grouping]; each job is one of these mechanisms put to work, and a motion that engages none of them only charges attention [attentional capture].
- **Check:** For each moving element write "job: X, because Y" and "real-time / post-action". The purpose table maps onto the jobs: responding → expectation; revealing / concealing → relationship; transitioning and preventing a jarring change → continuity; explaining → narrative; emphasising → relationship; ambient and celebrating do none of the four and live only where the register allows them. A post-action transition on a frequent path fails the frequency gate whatever its job. Motion whose grouping or direction contradicts the static layout fails its own job.
- **Severity:** warning (no job can be named); note (a job named but weakly served)
- **Tells:** "it feels smoother" as the only rationale; motion that tells a different story from the layout; a transition justified as continuity that cuts the very object it claims to carry.
- **Use cases:** a review table with a "job" column beside every animation; a handoff spec that states the job next to each duration.
- **Implementation:** record the job as a field in the motion spec (trigger, job, real-time / post-action, register band) so the purpose survives into code; in code: a comment or token name that carries the job (`--motion-continuity-*`), not only the duration.
- **Catalog:** N-01

## Should it move at all

### Frequency gate
- **Rule:** The motion budget is set by how often a user meets the moment. 100+ times a day (shortcuts, command palette, core navigation): no animation. Tens of times a day (hover, list navigation, frequent toggles): nothing, or near-imperceptible. Occasional (modals, drawers, toasts): standard motion. Rare or first-time (onboarding, success, empty state): the only place delight lives. It must still be fine on the hundredth viewing.
- **Why:** Every replay charges an attention tax [attentional capture]; on a daily-use surface it compounds into "this app feels slow".
- **Check:** For each animated element estimate its daily frequency and place it in a tier; anything in the top two tiers with visible animation is a finding. Static designs cannot prove this; a prototype or code can.
- **Severity:** blocking (top tier); warning (second tier)
- **Tells:** animated command palette; page transitions on every route change in a work tool; hover animations on table rows.
- **Catalog:** N-01, N-06

### Keyboard-initiated actions never animate
- **Rule:** An action triggered from the keyboard (shortcut, Escape, Enter, focus jump) changes state instantly. Style focus with focus-visible, not bare focus, so keyboard users get a ring and mouse users are not shouted at; the ring itself never animates in (its floor: lens 10).
- **Why:** Keyboard users are the power users; motion decouples the result from the keystroke and reads as lag [feedback loop].
- **Check:** Trigger the action from the keyboard and look for any transition or delay; tab through and confirm the ring appears on the same frame. Code or live input only.
- **Severity:** blocking
- **Tells:** a palette that fades in on the shortcut; Escape that waits for a close animation before the next action is accepted; focus rings that fade in.
- **Catalog:** N-06, K-02

### Named purpose or nothing
- **Rule:** A motion sits in exactly one row of the purpose table; if it fits none, delete it. "It looks cool" is not a purpose. Content the user is reading or acting on stays still; decorative motion belongs on marketing surfaces. Attention budget: one hero motion per moment, at most 2–3 elements in active motion (ambient excluded). Animate for appear/disappear, navigation between views, expand/collapse, loading and progress, confirmation and error; do not animate hover position, tooltip appearance, text changes, or anything the user is waiting on.
- **Why:** Purpose decides duration, easing and property; purposeless motion is what the hundredth viewing punishes, and motion on a working screen pulls the eye away from the task [attentional capture].
- **Check:** For each animated element ask the author to name the purpose in one word from the table and "what does this tell the user that a cut would not?"; if neither has an answer, recommend deletion. The table's rows are tested against the four jobs (lens 09 · Four usability jobs: expectation, continuity, narrative, relationship): a row earns its place only by doing one of them. On information-dense views identify every moving element and name the task the movement serves.
- **Severity:** warning
- **Tells:** charts drawing themselves in on every filter change; numbers counting up on every render; floating hero elements in a functional app; parallax on a task screen; spinners that themselves bounce; everything on the screen fades-and-slides in.
- **Catalog:** N-01

| Purpose | What it communicates | Approach | Optimise for |
|---|---|---|---|
| Responding (feedback) | input was received | immediate state change, ≤ 100 ms | speed |
| Revealing / concealing (orientation) | where it came from, where it went | position + opacity, ease-out | clarity |
| Transitioning (continuity) | same thing, new state or place | shared element, directional move | legibility |
| Emphasising (attention) | look here | one scale or colour pulse | responsiveness |
| Preventing a jarring change | the layout did not teleport | short crossfade or height change | calm |
| Explaining | how this works — marketing and onboarding only | staged sequence | comprehension |
| Ambient (atmosphere) | the surface is alive — marketing only | slow, continuous, ≤ 20 % amplitude | subtlety |
| Celebrating (delight) | a rare earned moment | overshoot, particles | delight, rarely |

### Never animate what the user is waiting on
- **Rule:** No transition sits between the action and the thing the user waits for, and no animation blocks a repeated action whose outcome is already known. Operations under ~50 ms cut, they do not fade. Navigate first and fill in (shell, then data); prefetch on hover, on visible, or on intent; a blurred ~20 px placeholder resolves to the full image.
- **Why:** Fades and slides add perceived latency even when they look polished; a 600 ms modal entrance is 600 ms of waiting [feedback loop].
- **Check:** Time from click to interactive content; anything the user must "wait through" is a defect. Is the destination shell visible before its data? Click rapidly: does it queue or block?
- **Severity:** blocking
- **Tells:** a modal not clickable until its entrance ends; a transition on every navigation; results animating in one by one while the user tries to read them.
- **Catalog:** N-06, N-09

## Duration and easing

### Duration budgets by surface
- **Rule:** Durations follow the table for the product's register; a utility product never takes the expressive column. UI motion in the restrained register stays under ~300 ms (180 ms ideal) unless a reason is written down; the polish register runs 200–500 ms; playful "whatever serves the effect", still gated by frequency. Over 300 ms is context-dependent: a warning under restraint, acceptable under polish or play.
- **Why:** A 180 ms dropdown feels more responsive than a 400 ms one; perceived speed is speed [feedback loop]. A tooltip at 300 ms is sluggish; a full-screen page at 150 ms is a glitch.
- **Check:** Read every duration (variables or literals) against the register's column; anything above the column needs a written justification. Code, prototype or live input only.
- **Severity:** warning
- **Tells:** 500 ms fades on menus; 1 s page transitions; a "smooth" 800 ms accordion; hover at 250 ms.

| Element | Utility / task UI | Consumer / production polish | Marketing / expressive | Easing |
|---|---|---|---|---|
| Hover colour | < 100 ms | < 100 ms | < 100 ms | ease |
| Tooltip, micro-feedback | instant | 125–200 ms | 80–120 ms | ease-out |
| Press, button state, toggle | 100–150 ms | 100–160 ms | 120–180 ms | ease-out |
| Icon transition | instant | 150–250 ms | 150–250 ms | ease-out |
| Dropdown, small popover | 150–200 ms | 150–250 ms | ~200 ms | ease-out |
| Card enter / exit | — | 200–350 ms | 200–350 ms | ease-out |
| Modal, panel, drawer | 200–300 ms | 200–500 ms | 300–400 ms | ease-out (ease-in-out when moving on screen) |
| Page transition | 250–400 ms (sweet spot 200–300) | 250–400 ms | 400–600 ms | ease-in-out |
| Dramatic reveal, once | — | — | 600–1 200 ms | — |
| Ambient loop | — | — | 2 000–20 000 ms | sine |
| Spinner, progress | 1–2 s per loop | 1–2 s | 1 000–1 500 ms per revolution | linear |

Ranges; pick per product and record the choice in the project's log.

### Duration follows weight, distance and platform
- **Rule:** Smaller elements move faster; bigger and heavier elements take longer: light (tooltips, badges, icons) 80–200 ms; medium (cards, panels) 200–350 ms; heavy (modals, overlays, pages) 300–500 ms. Apply the distance and platform multipliers (reference tables); modals not under 200 ms (task) / 300 ms (expressive); pages not under 250 ms; micro-feedback not over 180 ms. One duration for everything is a tell.
- **Why:** Physical intuition — a badge and a sheet do not weigh the same [motion perception]; one global value gives nothing weight.
- **Check:** List the durations used. One value everywhere? Does the largest surface get the longest and the smallest the shortest?
- **Severity:** note
- **Tells:** a single 300 ms transition (or one shared spring config) on icons, cards and modals alike.

### Ease-out for entrances; never ease-in on an entrance
- **Rule:** Entering elements ease out (fast start). Moving or morphing on screen uses ease-in-out. Hover and colour changes use plain ease. Constant motion (progress, marquee) is linear. Exits use an accelerating (ease-in family) curve in every register — entrances stay ease-out, never the reverse. Ease-in on an entrance is a defect in every register.
- **Why:** Ease-in delays the first frames, which are the frames the user is watching; the same duration reads slower [motion perception]; on exit the reverse logic applies — attention has already moved on, so the motion should get out of the way quickly rather than ease into it.
- **Check:** Inspect the timing function of every enter and exit; any ease-in or symmetric ease-in-out on an entrance is a finding; an exit that eases out instead of accelerating away is a finding in every register.
- **Severity:** blocking (ease-in on an entrance); warning (wrong curve elsewhere, including an exit that fails to accelerate)
- **Tells:** built-in `ease-in`; symmetric ease-in-out on a popover; a spring with visible wind-up before movement; an exit that eases out and lingers instead of accelerating away.

### Curves come from a library, one set per product
- **Rule:** Deliberate UI motion uses a strong named curve, not the browser default keywords, and the product carries one easing set. Take curves from a published library; never invent one. Do not accept a second parallel set.
- **Why:** Default keywords are limp; a strong curve makes motion read as intentional at the same duration, and one set is what makes motion feel designed [processing fluency].
- **Check:** Look for the project's named easing set. Motion on raw keywords everywhere → recommend one set and reuse it. Count distinct curves across the product.
- **Severity:** warning (default keywords on deliberate motion); note (taste within a set)
- **Tells:** every transition on `ease`; a curve chosen because it looked familiar; three curves for three dropdowns.

| Curve | cubic-bezier | Use |
|---|---|---|
| Strong ease-out | (0.23, 1, 0.32, 1) | entrances, exits in restrained and polish registers |
| Strong ease-in-out | (0.77, 0, 0.175, 1) | moves and morphs on screen |
| Drawer | (0.32, 0.72, 0, 1) | sheets and drawers settling |
| Standard / crossfade | (0.2, 0, 0, 1) | default on-screen change, icon crossfades |
| Emphasised | (0.05, 0.7, 0.1, 1) | entrances that should draw attention |
| Accelerate | (0.3, 0, 1, 1) | exits, every register |
| Platform default (iOS) | (0.25, 0.1, 0.25, 1) | when matching native surfaces |
| Gentle float | (0.4, 0, 0.2, 1) | ambient, premium sub-register |
| Bounce settle | (0.175, 0.885, 0.32, 1.275) | playful register only |

### Exits are shorter, smaller and softer than entrances
- **Rule:** Exit = roughly 65–75 % of the entrance (e.g. 150 ms vs 300 ms), a fixed 8–12 px translate rather than the full distance, and less attention-grabbing; the entrance is never the shorter one. Exits ease with an accelerating curve in every register (see lens 09 · Ease-out for entrances; never ease-in on an entrance) — entrances stay ease-out, never the reverse. Consecutive exit and entrance overlap 100–150 ms so the eye has somewhere to go. Remove instantly when motion adds no information or the interaction is high-frequency; but an element that simply vanishes with no exit is a gap.
- **Why:** On exit the user's attention is already moving to the next thing; users care about what arrives, not what leaves [attentional capture].
- **Check:** Compare enter and exit durations and distances; symmetric or dramatic exits are findings; a primary element that disappears in one frame is a finding.
- **Severity:** warning; blocking when a primary element vanishes with no exit (disorienting — see Motion gaps)
- **Tells:** items shrinking to scale 0.5 and sliding 100 % on removal; exit as long as enter; exits on ease-out that "float away" in the expressive register; a dismissed item that grows first.

### Asymmetric timing where the user is deciding
- **Rule:** Slow on the deliberate phase (hold-to-confirm fill ~2 s, linear), snappy on the system response (release ~200 ms ease-out).
- **Why:** The slow phase is the user's, the fast phase is the system's; matching them confuses who is in charge [mapping].
- **Check:** Any press-and-hold or drag-to-confirm with identical press and release timing is a finding.
- **Severity:** warning
- **Tells:** a hold-to-delete that snaps back as slowly as it fills.

### Loops use linear or sine, never a UI curve
- **Rule:** Continuous rotation and progress are linear; breathing and floating are sine ease-in-out at 2 000–5 000 ms; a scale pulse stays within ±2 % (above ±5 % it demands attention); ambient amplitude ≤ 10–20 % of the primary motion; several floaters use different periods so they never sync. Ambient motion is a marketing-surface device, never a defect to add on task UI.
- **Why:** An eased loop has a visible beat that pulls the eye every cycle [attentional capture].
- **Check:** Watch three cycles; if the steps can be counted, it is too loud.
- **Severity:** note
- **Tells:** skeleton shimmer with ease-in-out; a CTA pulse at ±8 %.

## Choreography

### Stage one hero per beat
- **Rule:** The primary element gets the largest displacement and the most emphatic easing; everything else is subtler in every dimension. Non-hero elements may dim to 40–60 % (optional 2–4 px blur) while the hero acts. One primary action per timing beat.
- **Why:** Two elements competing for the eye is no hierarchy; the eye lands nowhere [attentional capture] [figure–ground].
- **Check:** Pause halfway through: is there exactly one thing to look at?
- **Severity:** warning
- **Tells:** backdrop, modal and content moving with equal amplitude; two "pops" on one success screen.

### One origin, one start, one pause
- **Rule:** Elements in a coordinated entry come from one direction or a shared origin (the trigger point): closer starts earlier, farther later; one easing family, only start times vary. Everything reacting to one trigger starts within 50 ms; landing may be staggered. After a sequence settles, 100–200 ms of stillness before the next motion.
- **Why:** Mixed directions read as chaos, a late starter reads as an unrelated event, and back-to-back motion has no punctuation [gestalt grouping].
- **Check:** Draw each element's travel arrow — parallel, or radiating from the trigger. Step frames from the click. In a chain (dismiss → shift → new item), is there a pause between beats?
- **Severity:** warning
- **Tells:** cards entering from three sides of one grid; backdrop dims, then 200 ms later the modal appears; a toast dismiss overlapping the next toast's entrance.

### Anticipation, follow-through and counter-motion
- **Rule:** A wind-up (small motion opposite the main direction, 100–200 ms, 10–20 % of the amplitude) only on large deliberate motions — never under 150 ms, never on hover, toggles or presses. Children trail the parent by 50–150 ms; trailing parts stop 100–200 ms after the leader; secondary motion (shadow, icon, ripple) runs at 30–50 % of the primary amplitude, offset 50–100 ms, with a different easing. Counter-motion answers the hero at 10–30 % of its speed in the opposite sense (hero slides right → background drifts left; hero lifts → shadow spreads and softens; hero expands → siblings compress). "Always three layers — primary, secondary, ambient" is a note for marketing and onboarding surfaces only; on task UI a single clean layer is correct.
- **Why:** A wind-up on a button reads as lag; simultaneous start and stop reads as mechanical; a hero over a frozen scene looks pasted on [motion perception].
- **Check:** Any recoil on a button or tooltip → remove. On a card entrance, does the shadow or content arrive 50–100 ms after the card, or in the same frame? What do non-hero elements do while the hero moves?
- **Severity:** note; warning on premium or expressive surfaces
- **Tells:** buttons that shrink before they grow; modal, title, body and buttons fading in at once; a sheet sliding up over a page that neither shifts nor dims.

### Stagger only for rare staged entrances, within a budget
- **Rule:** Stagger a group entrance only where sequence communicates hierarchy and the surface is rarely seen (first load of a hero, a success state); never on routine interactions or lists the user scrolls daily. Per-item delay 20–100 ms (range; pick per pattern — table below); total stagger under 500 ms regardless of count; with 3+ elements no more than a third are in motion at once (element 1 settles as element 3 starts); no single motion travels more than a third of its container without a keyframe change. On mobile cut stagger budgets by 30 %. Stagger is decorative and never blocks interaction.
- **Why:** A cascade on a list the user scrolls past all day is pure latency; a 12-item list at 80 ms is a second of waiting; dense simultaneous motion is where the eye loses the scene [attentional capture] [cognitive load].
- **Check:** Items × delay; if over 500 ms cap the delay, or stagger the first N and drop the rest in together. Check the surface's frequency tier. Longest travel against the viewport; count movers in the busiest frame; is content clickable before the cascade ends?
- **Severity:** blocking above 500 ms total or when content is unclickable until it ends; warning above the row budget, the 1/3 rules, or on a routine surface
- **Tells:** every list row fading in with a delay; lists that "type themselves in"; a dashboard whose last widget lands after 1 s; search results, settings and table rows staggered.

| Pattern | Per-item delay | Total budget | Use |
|---|---|---|---|
| Micro cascade | 20–40 ms | < 200 ms | list items, grid cells |
| Standard | 50–100 ms | < 400 ms | cards, panels, nav |
| Dramatic | 100–200 ms | < 600 ms | hero sections only |
| Wave | 30–60 ms | < 500 ms | data bars |

Overlap between consecutive items: 0 % methodical, 25 % brisk (default), 50 % fluid, 75 % rapid.

### Direction is vocabulary
- **Rule:** Up = growth or arrival, down = settling or completion, right = forward, left = back, scale-up = importance or emergence, scale-down = dismissal, centre-seeking = focus. Directional slides only for hierarchical (list → detail) or ordered (previous / next) navigation; lateral moves (tab to tab) crossfade. Intermediate frames telegraph where the thing is going (a control grows toward the finger, a card tilts in the drag direction).
- **Why:** Users read direction as a spatial model [mental models]; a wrong slide implies depth that is not there, and people predict the final state from the trajectory [predictive brain].
- **Check:** Forward from the right, back from the left, every time; tabs never slide; a dismissed item never grows first. Step through at reduced speed: does the midpoint read as "on the way to" the end state?
- **Severity:** warning; note for the trajectory hint
- **Tells:** a tab switch that slides; a delete that scales up; content that exits by fading and re-enters by sliding; a sheet that fades instead of rising.

### Enter and exit along the same path, and the path sets the expectation
- **Rule:** A surface leaves the way it arrived: a toast that slides in from the top dismisses upward, so swiping up dismisses it; a panel from the right returns to the right. An overlay that can be swiped away follows the finger during the swipe and leaves in that direction on release; Escape, backdrop click and the close button leave along the entrance path, shorter. Every transition explains an interaction — where a thing came from, where it goes, what acts on what — and sets an expectation the interface then honours. Motion that neither forms nor confirms an expectation is noise.
- **Why:** The trajectory is a predictive cue read by the automatic layer [predictive brain]; symmetric paths keep the mental map intact and make swipe-to-dismiss obvious [mapping].
- **Check:** Open and close every overlay and compare paths; swipe partway and release; for each animation name the expectation it sets or confirms ("wow" is not one); try dismissing in the direction the entrance implied.
- **Severity:** warning
- **Tells:** in from the right, out through the bottom; a toast that fades in place after sliding in; a swipe that releases into a fade; a modal that appears from a direction it cannot be dismissed toward; a bouncing hero illustration on a form.
- **Catalog:** H-06

## Physicality, origin and overlay motion

### Never appear from nothing
- **Rule:** Entrances start from scale 0.9–0.97 plus opacity 0, never from scale 0. Exception: a contextual icon swap crossfades from a small scale (~0.25) with opacity and a ~4 px blur, because the icon is small and the blur bridges it.
- **Why:** Nothing in the physical world grows from a point; a scale-from-zero entrance reads as a glitch [motion perception].
- **Check:** Inspect the initial transform of every entering element; step the first frames of a popover.
- **Severity:** warning
- **Tells:** scale-0 keyframes; a pure opacity fade with no transform on a panel that has a spatial origin.

### Popovers grow from their trigger; modals stay centred
- **Rule:** Menus, dropdowns, tooltips and popovers set their transform origin at the trigger and scale 0.95–0.97 → 1 with opacity, 150–250 ms ease-out. Tooltips additionally delay the first and not the next: once one is open, neighbours open instantly with no animation. Modals are not anchored to a trigger: centred origin, scale ~0.96 → 1 with opacity, 200–300 ms, backdrop opacity animated in the same beat. Keyboard model, focus and dismissal: lens 11 · Popovers, menus and dropdowns; lens 11 · Modals.
- **Why:** The panel should look like it came out of the thing you pressed; the spatial link is the explanation [mapping]. A modal says "on top of", not "out of". The first tooltip delay prevents accidental activation; the instant follow-up makes a toolbar feel fast [feedback loop].
- **Check:** Open each popover from triggers at different screen positions and watch where it grows from; in code a static centred origin on a trigger-anchored surface is a finding. Hover across a toolbar: a delay on every item is a finding. Open a modal and watch backdrop and panel arrive together.
- **Severity:** warning; note for the tooltip delay
- **Tells:** a dropdown growing from its own centre regardless of the button's position; a modal sliding up from a button; a backdrop appearing after the panel; a 500 ms wait on each icon in a row.
- **Catalog:** H-09, H-10, H-11

### Blur on enter belongs to the polish register
- **Rule:** In the production-polish register the enter recipe pairs opacity with a small translate and a small blur (about 2–8 px, never above ~20 px), never on body text, since blur on text delays readability at first paint. In the restrained register blur on enter is allowed only as a bridge — added when two states visibly overlap during a crossfade and no easing fixes it — never as a default recipe, and a missing blur there is never a finding. In any register, three or more components in one view sharing the same blur entrance is a slop tell.
- **Why:** Blur blends two objects into one perceived transformation, so the eye stops seeing a swap [motion perception]; copied onto everything, or run on text at first paint, it becomes the signature of a template rather than a considered recipe.
- **Check:** Name the register. In polish, does the enter recipe use opacity + small translate + small blur, and never on body text at first paint? In restraint, play the crossfade at 10 % speed: is the blur bridging two objects that would otherwise visibly overlap, or is it a default? Count blur entrances per view; three or more sharing the same treatment is a finding regardless of register.
- **Severity:** note; warning when a blur entrance sits on body text at first paint, or when three or more components share the same blur entrance in one view
- **Tells:** text morphs where both strings are readable mid-transition; icon swaps that double up; the same 4 px blur on every section, card and paragraph; a restrained-register screen defaulting to a blur-on-enter recipe with no overlap to bridge.

### Never opacity alone, rarely more than two properties
- **Rule:** Success, error, selection and the arrival of a primary element pair opacity with position or scale; opacity-only is right for backgrounding, crossfades and secondary content. One property is direct, two is polished, three or more is noise; rotation is never primary outside loading and playful icons. Property by intent: entrance position + opacity; exit position + opacity; press scale + colour; success scale + colour; error position-shake + colour; loading rotation + opacity; delete scale + opacity; selection scale + colour.
- **Why:** A fade carries no direction and no weight; every added property multiplies what the eye must parse [cognitive load].
- **Check:** List opacity-only state changes and keep only the secondary ones; count animated properties per element.
- **Severity:** warning (opacity-only on a primary state); note (too many)
- **Tells:** a validation error that fades in with no border, icon or shake; a card that translates, scales, rotates and blurs on entrance.

### Toasts enter and leave from one edge and retarget
- **Rule:** A toast enters and exits from the same edge, through interruptible transitions because toasts are added in bursts; a slightly slower, softer curve is acceptable because a toast has a personality of its own; a dismiss never overlaps the next toast's entrance without a pause. Timers pause when the tab is hidden and on hover or focus. Announcement, focus, placement and stacking policy: lens 05 · Toast behaviour and lens 11 · Toasts.
- **Why:** Toasts stack and fire in bursts; a keyframe stack tears [motion perception].
- **Check:** Fire five toasts quickly; swipe one away; switch tabs and come back.
- **Severity:** warning
- **Tells:** toasts sliding in from the right and fading out in place; a keyframe toast stack; a toast that keeps its timer running in a hidden tab.
- **Catalog:** F-09, F-10

### Sheets and drawers move with the hand
- **Rule:** A sheet is positioned by a translate of its own height (percentage, not pixels); draggable with 1:1 tracking, velocity dismissal, rubber-banding and a spring settle; content scrolls inside with overscroll contained. For a modal task the background dims and pushes back; a parallel non-blocking panel gets no scrim. Inert background, scroll lock, safe-area padding and the non-drag close: lens 11 · Sheets and drawers.
- **Why:** A sheet is the most gesture-heavy surface in an app and the one where "website" tells concentrate [mapping].
- **Check:** Drag slowly, flick, over-drag, scroll the content to its end. Hardware only for the gesture; a prototype can show the entrance.
- **Severity:** warning
- **Tells:** a sheet that closes only from a button; hard-coded pixel offsets; the page scrolling behind the sheet; a sheet that fades instead of rising.
- **Catalog:** H-07

### Modal, backdrop and content arrive as one beat
- **Rule:** Backdrop and panel animate in the same beat (backdrop never after the panel); the panel is interactive before its entrance ends; closing runs the entrance in reverse along the same path, shorter; content inside does not stagger in on a routine dialog. A stack (nested sheet, popover over a modal) collapses one level per dismissal, innermost first, and the underlying layer settles back with the same curve it left with. Focus, dismissal and misuse of modals: lens 11 · Modals.
- **Why:** A modal is a task interruption; one clean beat says "on top of" and lets the user act immediately [gestalt grouping]; collapsing two levels at once loses the user's place.
- **Check:** Open, click into it before the animation ends, close, and compare the two paths; press Escape with two layers open and watch whether the underlying layer returns to rest.
- **Severity:** warning
- **Tells:** a backdrop that dims 200 ms before the panel; a modal that cannot be clicked until settled; a title, body and buttons cascading in on a confirm dialog; Escape closing both a popover and its parent modal; a modal that stays pushed back after its child sheet closes.
- **Catalog:** H-03, N-06

## Twelve usability techniques

The usability-motion technique set: twelve named techniques, each serving one or more of the four jobs. They are vocabulary for findings — name the technique, its job and the failure — not a list of motions to add. Where an entry above already governs a technique, the entry here names it and defers. Each Why states the evidence: research, indirect research, or practice only. Overview: Reference tables · Usability-motion techniques.

### Easing as expectation
- **Rule:** Every motion that exists eases; linear motion is for loops only. "Always ease" never means "animate so there is something to ease": a snap on a frequent or keyboard action is correct. Curve, direction and overshoot: lens 09 · Ease-out for entrances; never ease-in on an entrance; lens 09 · Curves come from a library, one set per product; lens 09 · Easing and overshoot follow the register and the moment.
- **Why:** Job: expectation. Objects with mass accelerate and settle; eased motion reads as expected and disappears, linear motion reads unfinished [predictive brain] [motion perception]. Evidence: design argument and practice; recommended for predictability in the visualisation literature, but no controlled UI study isolating easing was found.
- **Check:** Step each animated change at 10 % speed; constant velocity with hard starts and stops on non-loop motion is a finding. Code, prototype or live only.
- **Severity:** warning
- **Tells:** a drawer sliding at constant speed; a curve that contradicts the brand (a bank on bounce).
- **Use cases:** a drawer decelerating into place; a sheet settling on a critically damped spring.
- **Implementation:** one named curve set held as variables; in code: `transition-timing-function: cubic-bezier(…)` or the Web Animations `easing` option from the curve table; springs for anything a hand can touch.

### Offset and delay encode grouping
- **Rule:** Timing tells the user what belongs together before anything is read: parts of one unit move as one, separate controls are offset from each other. The groups the motion forms match the groups the layout and the hit targets form — separate buttons never move as one row block, a label never lags its own control. Budget, per-item delay and frequency: lens 09 · Stagger only for rare staged entrances, within a budget; lens 09 · One origin, one start, one pause.
- **Why:** Job: relationship. Shared motion groups more strongly than static similarity or position, so timing that contradicts the layout overrides it [gestalt grouping]. Evidence: indirect research (grouping by common motion in animated displays); the UI use is practice.
- **Check:** Play the entrance at 10 % speed and write down the groups the motion forms; compare them with the static groups and the targets. Any mismatch is a finding.
- **Severity:** warning
- **Tells:** separate toolbar icons sliding in as one row block; an action button expanding into three actions that arrive as one lump; a caption that arrives before the image it belongs to.
- **Use cases:** a speed-dial expanding into separately offset actions; a result card whose image and text arrive together and whose action follows.
- **Implementation:** one delay step × index, capped by the stagger budget; in code: `transition-delay: calc(var(--i) * var(--step))` or the Web Animations `delay` option; a library's stagger-children option.

### Parenting links linked properties
- **Rule:** When one object's property drives another's — scroll offset drives a header's height and title size, a slider thumb drives its value bubble, a pager drives its indicator — derive the child from the parent continuously: direct (moves with), delayed (trails) or inverse (moves opposite). Real-time parenting, tied to the finger or the scroll, is where it pays; the child tracks 1:1 and never runs on its own clock, and it rests only in fully legible states. A scroll-linked child is correct here because its state is a function of position; a reveal or entrance is still triggered by scroll, not controlled by it (lens 09 · Scroll-driven motion is triggered by scroll, not controlled by it). Trailing offsets and counter-motion: lens 09 · Anticipation, follow-through and counter-motion.
- **Why:** Job: relationship. Linked motion states the hierarchy without a label [gestalt grouping] [mapping]. Evidence: indirect research (common-motion grouping); the technique is practice.
- **Check:** Drag or scroll the parent slowly and stop mid-way: does the child stop on the same frame, in a legible state? Does anything linked animate on a timer after the input stops?
- **Severity:** note; warning when the child lags a gesture or rests half-visible
- **Tells:** a collapsing header that finishes on a timer after the scroll stops; a value label that jumps while the thumb glides; a pager dot that moves only on release.
- **Use cases:** a large title collapsing into the navigation bar as the list scrolls; a slider's value bubble; a tab indicator following the swipe between tabs.
- **Implementation:** one progress value (0–1) from the parent, every child an interpolation of it — never two animations started together; in code: `animation-timeline: scroll()` or `view()` on the child for scroll-linked cases; one shared animated value mapped by interpolation on native.

### Transformation keeps one object through a change of role
- **Rule:** When an object changes what it is for (play → pause, search icon → search field, menu → close, submit → progress → done), morph the same object rather than swapping it. The object keeps its footprint, its accessible name and state update with every role, the label stays while the user needs it, and nothing morphs into an unrelated object. The full button → spinner → check morph is a rare-moment device for the polish or playful register; the default for a routine submit remains a spinner beside the kept label (lens 09 · Every micro-interaction has four parts). Icon swaps: lens 09 · Never appear from nothing.
- **Why:** Jobs: continuity, narrative. Continuous change lets the eye keep the identity; morphing unrelated things asserts a relation that is not there [object constancy]. Evidence: research for animated changes of position, size and shape in data graphics; UI control morphs themselves are practice only.
- **Check:** Step through the states: one object throughout? footprint stable, no layout jump? name and state exposed per role? any morph into something unrelated?
- **Severity:** warning
- **Tells:** a submit button shrinking into a circle and shifting the form; a spinner replacing the label on a routine form; a card morphing into an unrelated screen.
- **Use cases:** play/pause morph; search icon expanding into the field; menu icon morphing into close as the menu opens.
- **Implementation:** morph parts with transform and opacity, or interpolate shapes that share structure; in code: SVG path or CSS `clip-path` interpolation between shapes with the same point count; update the control's accessible name or pressed state on each role.

### Value change shows live data as live
- **Rule:** A value that changes while the user watches — because the user changed an input or live data arrived — may animate its change (roll, tween, bar growth) so the change and its direction are seen. A value that is merely loaded does not count up. The final value is readable at once, digits keep a fixed width, the change is instant under reduced motion, and assistive technology receives the final value, not the tween. Tabular digits: lens 02 · Tabular numbers on anything that changes; counting on every render stays slop: lens 09 · The generated-interface motion signature.
- **Why:** Jobs: narrative, relationship. A silent swap of a value is missed [change blindness]; a visible change connects the number to what it measures. Evidence: research on animated value changes in charts (change tracking improved for most chart types tested, not all); number count-ups and odometer rolls are practice only.
- **Check:** Change an input that drives a total: does the total visibly change? Reload: does anything count up from zero? Is the final value readable and announced once?
- **Severity:** note; warning when a user-driven value updates silently or when a count-up delays reading a money figure
- **Tells:** dashboard figures counting up on every visit; a price that changes silently after a toggle; digits shifting width while they roll.
- **Use cases:** a basket total rolling when the quantity changes; a live score counter; chart bars growing to their new values after a filter.
- **Implementation:** animate between old and new only on change; in code: a typed integer custom property (`@property --n { syntax: '<integer>' }`) with a transition, or a per-digit `translateY` roll; `font-variant-numeric: tabular-nums`; a polite live region set to the final value only.

### Masking changes what an object is by what it reveals
- **Rule:** When an object's role depends on which part of it is visible — a thumbnail that opens into the full image, a card that expands into its detail, a header image that crops into a cover — animate the mask (bounding shape and position) while the content stays in place, so the same content changes identity without a swap. The reveal grows from the trigger's own bounds, content is never stretched, the reverse runs the same path back to the same place, and the destination is interactive before the mask settles (lens 09 · Never animate what the user is waiting on). Occasional paths only; a path used dozens of times a session in a work tool cuts (lens 09 · Frequency gate). Under reduced motion it becomes a crossfade.
- **Why:** Job: continuity. The content never leaves the screen, so nothing has to be found again [object constancy]; a crossfade between two layouts is a cut the eye must reconcile [change blindness]. Evidence: practice only — no controlled study of mask transitions was found; the continuity argument rests on the general research on animated transitions.
- **Check:** Open and close one item three times from different positions: does the expansion start from that item and return to it? Pause mid-way: one object or two? Is content ever squashed? Try to act on the destination before the mask settles. Prototype, code or live only.
- **Severity:** warning (reveal from the wrong origin, distorted content, return to a different place); note (a plain crossfade where a mask would carry the continuity)
- **Tells:** an image that squashes while it expands; a detail view that grows from the screen centre whichever card was tapped; a close that fades out instead of shrinking back into its card; a width and height tween doing a mask's job.
- **Use cases:** card → detail container transform; photo thumbnail → full screen and back; circular reveal from the tapped control.
- **Implementation:** measure first and last bounds, animate the clip or the clipping container with transforms, keep the content's aspect ratio (FLIP) instead of animating layout; in code: `clip-path: inset(… round …)` or `circle()` transitions (basic shapes interpolate; polygons need equal point counts); the View Transitions API with one `view-transition-name` on source and destination; Compose `Modifier.sharedBounds` with `clipInOverlayDuringTransition`; iOS `matchedGeometryEffect`.
- **Catalog:** N-01, N-06

### Overlay motion shows what lies behind
- **Rule:** When one layer moves aside to reveal another — row actions under a swiped row, a page under a drawer, a search field above a list — the foreground moves and the background stays anchored (or recedes slightly), so the motion states which layer is in front and where the hidden one lives. Paths and symmetry: lens 09 · Enter and exit along the same path, and the path sets the expectation; gesture behaviour: lens 09 · Sheets and drawers move with the hand; layering: lens 11 · Materials and depth.
- **Why:** Jobs: relationship, narrative. A flat screen has no z-axis; which layer moves is the only depth statement [figure–ground] [depth cues]. Evidence: practice only.
- **Check:** During the move, does exactly one layer carry the motion? Does the revealed layer read as "behind", not as new content arriving?
- **Severity:** note; warning when the background moves as much as the foreground or the depth reads inverted
- **Tells:** a page and its drawer moving with equal amplitude; revealed actions fading in instead of being uncovered; a pull-down search that slides over the list instead of from above it.
- **Use cases:** swipe-to-reveal row actions; a navigation drawer; pull-down to reveal search above a list.
- **Implementation:** translate the foreground only, background fixed in z-order; in code: `transform: translateX()` on the foreground layer with the revealed layer beneath it, driven by the gesture with a spring settle.

### Cloning: new objects are born from their cause
- **Rule:** When an action creates new objects — add to basket, duplicate, a new item in a list, a message sent — let them originate from the cause the user is looking at and travel to where they will live, so action X visibly produces Y. One short eased path in one beat, transform and opacity only, never blocking the next action, landing where the confirmation lives (badge, list slot). The control's own pressed or added state still changes within 100 ms (lens 09 · Feedback within 100 ms, regardless of processing time); the clone is the story, not the feedback. Occasional actions only; bulk and keyboard-driven adds update in place (lens 09 · Frequency gate; lens 09 · Keyboard-initiated actions never animate). Under reduced motion there is no flight, only the landing state.
- **Why:** Jobs: narrative, relationship, continuity. An object that appears with no origin is a sudden materialisation the user must explain [change blindness]; one born from its cause keeps the chain visible [object constancy]. Evidence: design argument ("no sudden materialisations") and practice; no controlled study of clone-and-fly patterns was found.
- **Check:** Trigger the action: does the new object visibly come from its cause and land where it is confirmed? Trigger it five times fast: do clones queue or block? From the keyboard: instant? Under reduced motion: count and highlight only?
- **Severity:** warning (new object with no origin where the user must find it; a flight that blocks repeated taps); note (a fade-in where an origin would help)
- **Tells:** add-to-basket with nothing changing near the tapped button and a badge updating off-screen; a duplicate appearing at the end of the list with no link to its original; a fly-to-basket across the whole viewport that holds the button disabled.
- **Use cases:** a product thumbnail flying to the basket icon as the badge ticks; "duplicate" sliding the copy out of the original; a sent message rising from the composer; an action button spawning its speed-dial actions.
- **Implementation:** update the real state first; animate a lightweight snapshot from the source rect to the target rect on a fixed layer and remove it on landing — never move the real node across containers mid-flight; in code: measure with `getBoundingClientRect()` and run `element.animate()` on a fixed-position clone; or a temporary `view-transition-name` moved from source to target; `layoutId` in a React layout-animation library; iOS `matchedGeometryEffect`.

### Obscuration keeps the context behind in view
- **Rule:** When a primary surface sits over a context the user should stay aware of — a sheet over a map, a menu over a page, a lock screen over the wallpaper — obscure the context (dim, blur, frost) instead of hiding it, and let the obscuring arrive with the surface so the context is seen to recede, not vanish. The foreground stays legible over every background it can land on. Material behaviour and reduced transparency: lens 09 · Translucent surfaces arrive as material; stacking: lens 11 · Materials and depth; blur limits: lens 09 · Blur on enter belongs to the polish register.
- **Why:** Job: relationship (orientation: another world lies behind the primary one) [figure–ground] [depth cues]. Evidence: research exists for the see-through state, not the motion — semi-transparent layers keep the background in awareness but the background interferes with reading the foreground, and the acceptable level depends on task and content; the animated act is practice only.
- **Check:** Open the surface over the busiest background it can meet: does the foreground still pass its contrast floor (lens 03 · Contrast floors, measured on the rendered pair)? Is the obscuring an opacity change of a pre-blurred layer, or a blur radius tweened across the screen (lens 09 · Animate transform and opacity only)?
- **Severity:** note; warning when legibility depends on what is behind; blocking below the contrast floor
- **Tells:** a frosted panel unreadable over photos; a full-screen blur radius animating on every modal; a scrim that arrives after the panel.
- **Use cases:** a page dimmed and blurred behind a modal sheet; a frosted control panel over the home screen; a map dimming behind a place card.
- **Implementation:** set the blur once and animate the opacity of the surface and scrim, with a solid fallback; in code: static `backdrop-filter: blur()` on the surface plus `opacity` transitions; `@media (prefers-reduced-transparency: reduce)` → solid; native material views follow the platform's reduced-transparency setting.

### Parallax only where the surface is for looking
- **Rule:** Layers scrolling at different rates separate foreground from background. Parallax belongs on marketing, editorial and showcase surfaces, never on task screens (lens 09 · Named purpose or nothing); at most two layers; mapped directly to the user's scroll position, never scroll-jacked; off under reduced motion (lens 09 · Reduced motion means gentler, not none).
- **Why:** Job: relationship (depth priority). Motion parallax is a genuine depth cue [depth cues], but the usability claim is not supported: in the one controlled web study found, parallax was rated more fun with no difference in perceived usability, satisfaction or visual appeal, and some participants reported motion sickness. The accessibility standard names parallax as motion users must be able to switch off.
- **Check:** Surface type? Count layers moving at different rates; enable reduced motion — parallax stops; scroll fast and slow — layers stay tied to the thumb.
- **Severity:** warning on a task screen; blocking when it ignores reduced motion
- **Tells:** a parallax hero on a settings page; three or more parallax layers; a background drifting behind a checkout.
- **Use cases:** an editorial header image scrolling slower than the headline; a product showcase page; a wallpaper shift behind home-screen icons.
- **Implementation:** translate the background layer as a function of scroll; in code: `animation-timeline: scroll()` on a `translate` keyframe inside `@media (prefers-reduced-motion: no-preference)`; never scroll listeners writing layout properties.
- **Catalog:** N-02

### Dimensionality is spent on rare, spatial moments
- **Rule:** 3D devices — folding panels, flipping cards, objects built from layers in depth — give an object a spatial origin and say the hidden side still exists. Use them where the 3D metaphor is the content (a card with a back, a folded map) and the register allows it (onboarding, showcase, play), with rotation as a secondary property; on task UI, flat layering (overlay, a shared axis) gives the same origin without rotation. Rotation outside loading and playful icons: lens 09 · Never opacity alone, rarely more than two properties; register: lens 09 · Name the register before the first finding. Under reduced motion flips and folds become crossfades.
- **Why:** Job: narrative (a spatial framework) [depth cues] [mental models]. Evidence: research cuts against the general promise — adding a third dimension to spatial arrangements of interface items did not help spatial memory and was judged more cluttered, and rotation is harder to follow than translation or expansion; flips and folds as transitions are practice only.
- **Check:** Is the 3D metaphor load-bearing (does the back exist as content)? Which register? Is the rotation large, full-screen or on a frequent path? Reduced motion honoured?
- **Severity:** note; warning on a frequent task path; blocking when a full-screen rotation ignores reduced motion
- **Tells:** cube transitions between tabs; a settings card that flips to show a form; a 3D carousel on a dashboard.
- **Use cases:** a flashcard or payment card flipping to its back; a folding onboarding panel; a wallet's cards fanned in depth.
- **Implementation:** in code: `perspective` on the parent with `transform: rotateY()` and `backface-visibility: hidden` on the faces; `transform-style: preserve-3d` for layered objects; every 3D transition inside a reduced-motion branch.

### Dolly and zoom keep the user's place between levels
- **Rule:** Moving between levels of one space — map to place, photo grid to photo, month to day, icon to app, overview to detail — zooms (the object scales: the next level is inside it) or dollies (the view moves toward or away: the destination is ahead or behind), continuously, so the user keeps a map of where they are. Zoom in from the tapped element and back out to the same element; one axis of motion per transition; durations from the page and panel rows of lens 09 · Duration budgets by surface. Large full-screen zoom is a vestibular trigger: under reduced motion it becomes a crossfade (lens 09 · Reduced motion means gentler, not none). A zoom on a path used dozens of times a day in a work tool fails the frequency gate.
- **Why:** Jobs: continuity, narrative. A continuous change of viewpoint lets the user rebuild the space; a cut between levels forces re-orientation [object constancy] [mental models]. Evidence: research — animating viewpoint changes in a zoomable space improved users' reconstruction of the space with no time penalty, and animated scrolling improved reading time and errors over jumps; the gain is for real spaces the user navigates, not decorative zooms.
- **Check:** Open and close the same item from several positions: does the zoom begin at the tapped element and return to it? Is any level change a cut or a sideways slide? Enable reduced motion. Prototype, code or live only.
- **Severity:** warning (zoom from the screen centre regardless of source; return to the wrong place); blocking when a large zoom ignores reduced motion
- **Tells:** a calendar month → day change that slides sideways; a photo grid → photo that fades; an app-open zoom that always starts at the screen centre.
- **Use cases:** a home-screen app opening out of its icon and closing back into it; photo grid → photo with pinch back to the grid; a map flying to a searched place; calendar year → month → day.
- **Implementation:** one transform (translate + scale) anchored at the source rect, on a snapshot or the shared element, with text re-rendered at rest rather than scaled as a bitmap; in code: the View Transitions API with a `view-transition-name` on source and destination; FLIP with `transform: translate() scale()`; iOS `.navigationTransition(.zoom(sourceID:in:))` with `.matchedTransitionSource(id:in:)`; Compose `sharedElement` / `sharedBounds` inside `SharedTransitionLayout`; the map SDK's animated camera move with a capped duration.
- **Catalog:** N-02

## Springs, gestures and direct manipulation

### Springs for anything a hand can touch
- **Rule:** Drag, swipe, sheets, drag-to-dismiss and any motion the user can interrupt or reverse use springs, not fixed-duration curves. Default is critically damped (no overshoot); a little bounce (damping ~0.8, or bounce 0.1–0.3) only when a flick or throw preceded the motion. Never bounce a menu that merely faded in. Springs on non-gesture interactive elements are a polish choice, not a requirement.
- **Why:** A spring starts from the current value and carries velocity, so an interruption is continuous; a keyframe restarts and creates a wall [motion perception].
- **Check:** Grab a moving sheet mid-flight and reverse it; a jump, a snap or a wait is a finding. Live or code only.
- **Severity:** blocking (gesture motion that cannot be interrupted); note (bounce taste — the register entry decides)
- **Tells:** bounce on everything; CSS keyframes driving a draggable sheet; a sheet that finishes closing before it can be reopened.

| Spring | Stiffness / damping | Use |
|---|---|---|
| Very stiff | 400+ / 25–30 | snaps, toggles |
| Standard | 250–350 / 18–24 | most UI settle |
| Interactive (platform reference) | 300 / 20 | sheets, drag release |
| Gentle | 100–150 / 20–25 | premium surfaces |
| Bouncy | 150–250 / 10–15 | playful only, after a throw |
| Very bouncy | 100–200 / 5–10 | celebration only |

Damping ratio < 1 oscillates, = 1 is the fastest non-oscillating settle, > 1 settles slowly.

### Respond on pointer-down, track 1:1, keep the gesture honest
- **Rule:** Feedback starts the instant the pointer lands, not on release (drag start under ~50 ms). During a drag the element stays glued to the pointer, honouring where it was grabbed, and the UI updates continuously, not only at the end. Capture the pointer once a drag starts; ignore additional touch points mid-drag; require a small movement threshold (~10 px) before committing to a direction; no click fires once movement has become a scroll or drag; never lock out input while a transition runs.
- **Why:** The moment lag appears, the sense of direct manipulation collapses [feedback loop]; each missing hygiene detail produces a jump or a dead moment.
- **Check:** Press and hold a control: does anything change before release? Drag a sheet slowly: does it move with the finger or animate afterwards? Drag past the element's bounds; add a second finger mid-drag; tap during an open animation; touch-scroll starting on a button.
- **Severity:** blocking (no feedback on pointer-down); warning (drag that animates only on release; hygiene gaps)
- **Tells:** buttons that only react on click; a card that snaps its centre to the pointer on grab; a drag that stops when the pointer leaves the element; a sheet that jumps when a second finger touches.
- **Catalog:** A-16, A-17, F-01, J-15, J-16

### Velocity handoff and momentum projection
- **Rule:** When the gesture ends, the settle continues at the release velocity and the target is chosen from where the momentum would land (projected endpoint), not from the release point. Reverse-vs-commit is decided by velocity sign, not distance alone. Boundaries rubber-band with increasing resistance rather than a hard stop.
- **Why:** This is the seam between "fine" and "fluid": a flick should throw; an edge should feel like an edge, not a wall [motion perception].
- **Check:** Flick a sheet quickly across a short distance: it should dismiss. Drag past the limit: it should resist progressively. Hardware only; emulation cannot prove it.
- **Severity:** warning
- **Tells:** distance-only dismissal thresholds; hard stops at boundaries; a sheet that ignores a fast flick.

### Gestures are invisible: hint, fallback and every drag state
- **Rule:** Every drag, swipe or pinch has a visible alternative (button, long-press menu) and a first-encounter hint (edge peek, hint animation, tooltip). Drag handles are always visible on touch; on mouse, hover-reveal is acceptable only with a keyboard path (Enter to pick up, arrows to move, Enter / Escape to drop or cancel). Gesture meaning is consistent across lists and never collides (swipe-down on a sheet is dismiss or refresh, not both). Drag and drop has eight states: default; hoverable (handle, grab cursor); grabbing (grabbing cursor, lift ~1.03, 150 ms); dragging (ghost semi-transparent, placeholder at origin); over a valid target (highlight, placeholder moves); over an invalid target (no-drop cursor, warning tint); dropped (animates into place ~200 ms, gaps close); cancelled (animates back). The single-pointer floor itself: lens 10.
- **Why:** Users cannot see a gesture; platform convention is the only prior they have [conventions] [affordance and signifier]; missing drag states are where users lose the item.
- **Check:** Complete each gesture action without the gesture; compare swipe behaviour across lists; walk the eight states — invalid-target and cancel are the ones usually missing. A static design can show the states; a prototype or build proves them.
- **Severity:** blocking (no alternative); warning (no hint, inconsistent meaning, missing states)
- **Tells:** swipe-to-archive in the inbox and swipe-to-delete in sent; an item that snaps back without animation; no placeholder during drag.
- **Catalog:** J-02, J-04, J-07, J-08, J-10, A-12

## Interruptibility and first paint

### Transitions for interactive state, keyframes for one-shot sequences
- **Rule:** Anything the user can trigger twice in a second (toasts, toggles, open/close, hover) uses transitions or springs that retarget from the element's live on-screen value, never from its logical target. Keyframes are reserved for sequences that run once (a page hero, a loading state). Rapid clicks blend; they never queue.
- **Why:** Keyframes restart from zero on interruption and a start from the target causes a visible jump; both read as broken [motion perception].
- **Check:** Open and close a drawer rapidly; interrupt any animation midway and look for a snap, a restart or a jump. Code or live only.
- **Severity:** blocking (toasts, toggles); warning (elsewhere)
- **Tells:** keyframe slide-in on a toast stack; a toggle that replays its whole animation on every click; a closing modal that snaps fully open before re-closing; clicks that queue.
- **Catalog:** N-06

### Skip enter animations on first paint
- **Rule:** Elements already in their default state on page load do not animate in; they animate only on subsequent state changes. Static content (headings, paragraphs, navigation, prose) never animates on mount. Deliberate page-load entrances (a hero) are the exception and must still work on a hard refresh.
- **Why:** Everything animating on load is noise and delays the first usable frame [attentional capture]; an entrance whose only purpose is the entrance itself makes the page feel slow.
- **Check:** Hard-refresh and watch for icons, tabs, toggles, headings and body copy that fade or scale in.
- **Severity:** warning (static content on mount); note (controls popping in on load)
- **Tells:** segmented controls that pop in on load; every icon crossfading on mount; body copy fading up on scroll.

### Fill mode and the pre-animation flash
- **Rule:** Delayed sequences hold their start state before they begin (fill-mode backwards or both); without it elements paint in their final state, pop to invisible, then animate in.
- **Why:** The flash is the most visible bug in any staggered entrance and reads as unfinished [change blindness].
- **Check:** Any animation delay above zero without a backwards fill? Load with cache disabled and watch the first paint. Code or live only.
- **Severity:** warning
- **Tells:** content visible for a frame before fading in; a stagger whose first item flickers.

### Scroll-driven motion is triggered by scroll, not controlled by it
- **Rule:** Scroll is the trigger; the motion then runs over a fixed duration. Tying progress to scroll position makes slow scrolling play the animation slowly. Provide an intersection-based fallback where scroll timelines are unsupported.
- **Why:** Users scroll at random speeds; a reveal that stutters with the thumb feels broken [motion perception].
- **Check:** Scroll very slowly through a reveal: does the motion crawl with the scroll? Is there a fallback?
- **Severity:** warning
- **Tells:** half-faded sections parked mid-transition; parallax that only looks right at one scroll speed.

## Properties and performance

### Animate transform and opacity only
- **Rule:** Primary motion uses transform and opacity; colour, background and clip-path are acceptable on a few elements; width, height, margin, padding, top and left animate only on a single element, once, off the hot path (height tolerated for a short accordion; prefer clip-path for reveals); box-shadow, border-radius, filter and blur on large areas are avoided. Under 20 animated elements per viewport; 60 fps target, 30 fps tolerated for ambient only. A shadow "lift" is a pre-rendered shadow layer fading in, not a shadow tween. A compositing hint (will-change) only for transform, opacity or filter, only after a first-frame stutter is seen; never on every animated element, never "all".
- **Why:** Transform and opacity skip layout and paint; the rest re-run all three steps every frame and drop frames exactly when the user is interacting. Each promoted layer costs memory; browsers already promote on demand.
- **Check:** In code list the transitioned properties; anything in the expensive tiers on a frequently animated element is a finding. Count animated elements in the busiest frame; count will-change declarations against elements that actually stutter.
- **Severity:** blocking (layout or filter properties on the hot path); warning (one-off; global or unspecific will-change)
- **Tells:** animated height: auto on menus; margin-left slides; an accordion animating height on every row; a card hover tweening box-shadow; blur on backdrop enter; global will-change: transform on cards.

| Tier | Properties | Cost |
|---|---|---|
| Optimal | transform (translate, scale, rotate), opacity | compositor only; unlimited elements |
| Good | color, background-color, clip-path | paint; 10–15 elements |
| Acceptable | width, height, margin, padding | layout; 5–8 elements, never on the hot path |
| Avoid | box-shadow, border-radius, filter, blur | expensive paint; 1–3 elements |

### Transition only what changes
- **Rule:** Name the exact properties; never transition "all". When light/dark flips, colour, background, border and shadow transitions are disabled for the swap and restored on the next frame.
- **Why:** "All" animates properties nobody meant to animate and blocks browser optimisations; on a theme switch every colour transition fires at once and the switch smears instead of snapping.
- **Check:** In code search for `transition: all` and equivalents; toggle the theme and watch for a slow crossfade across the page.
- **Severity:** warning
- **Tells:** a theme toggle that smears; layout properties animating by accident; a 300 ms colour wash on theme change.

### Predetermined motion runs off the main thread
- **Rule:** Predetermined motion runs as CSS transitions or animations (or the Web Animations API); JavaScript-driven motion is reserved for dynamic, interruptible, gesture-driven cases. Do not drive a child's transform through a variable on the parent or update CSS variables per frame during a drag; set the value on the element.
- **Why:** Frame-based script animation drops frames while the page loads or scripts run; a parent-level variable recalculates styles for every descendant.
- **Check:** In code look for script-driven position animations that run during page load and for a runtime variable on a container driving a swipe.
- **Severity:** note
- **Tells:** tab indicators that stutter during navigation; a drawer that jitters while a list renders.

### Interpolate through typed properties, not strings
- **Rule:** Custom properties animate only when their type is declared; complex paths need decomposed transforms (separate x and y variables) rather than one monolithic transform.
- **Why:** Untyped variables swap instead of tweening, so the motion jumps.
- **Check:** Any animated custom property without a type declaration? Any curved path faked with straight segments?
- **Severity:** note
- **Tells:** a hue or progress value that steps instead of glides.

## Feedback: press, hover, timing

### Every pressable element has a press state
- **Rule:** A subtle scale-down on press (0.95–0.98; range, pick per product), 100–160 ms ease-out, through an interruptible transition so a release mid-press returns smoothly; combined with a background change where the design calls for it, with an opt-out for controls where motion would distract.
- **Why:** Press feedback is the interface saying "heard you"; without it the tap reads as lag even at zero latency [feedback loop].
- **Check:** Press and hold any button: nothing changing is a finding. Press then drag away: the release should be smooth. A static design can show the pressed variant; the timing is runtime.
- **Severity:** warning
- **Tells:** buttons that only change on hover; press feedback implemented with a keyframe that replays.
- **Catalog:** A-15, A-16

### Feedback within 100 ms, regardless of processing time
- **Rule:** The element that received input changes visually within 100 ms, synchronously; the spinner or loading state comes after, not instead. When motion is combined with sound or haptics, all fire on the causal event on the same frame, reserved for meaningful moments (commit, snap, success, error); haptics never replace visual feedback.
- **Why:** About 100 ms is the classic estimate for a response that feels "direct" [feedback loop]. It is an expert estimate from the early HCI literature, not a measured perceptual limit; the one direct measurement (web search) found delays under ~500 ms rarely noticed and delays over ~1 s usually noticed, with large differences between people. Keep 100 ms as the target for the pressed state, because that change costs nothing; above it the interface starts to feel laggy even when the operation is fast; latency between senses breaks the illusion and over-feedback trains users to ignore all of it [habituation].
- **Check:** Click and count frames to the first visible change; a state that waits for a network response is a defect. Trigger a haptic-backed action with haptics off, then on, and watch for an offset. Live only.
- **Severity:** blocking
- **Tells:** a button untouched until the API responds; a toggle that flips on server confirmation; haptic on every scroll tick; sound that lands after the animation.
- **Catalog:** F-01, A-16, J-15

### Hover is visible; scale only a standalone element
- **Rule:** Every hoverable element carries a noticeable hover state — nothing hoverable is left with no feedback at all. In a list, grid or group, hover changes colour, opacity or background, never scale or movement: with many elements the eye should not have to track several independently moving pieces. A single standalone element (a lone CTA, a hero card) may scale slightly on hover (about 1.02–1.05) as polish. Either way hover styling is gated behind a hover-capable pointer and reduced motion, and applies only where the primary input can hover with a fine pointer; touch gets press feedback instead (the touch-side rule: lens 12 · Touch gets a hover equivalent). Keystrokes, row hover, tab switches and selection in a work tool get instant feedback or a colour/opacity transition of ~100–150 ms (range; pick per product).
- **Why:** A hover state that is missing or too subtle to notice leaves pointer users without the feedback loop touch users get from press [feedback loop]; a custom animation on a high-frequency trigger charges its cost every time [attentional capture] — in a list this cost multiplies across peers, while a single standalone element has nothing to compete with; touch fakes hover on tap and leaves it stuck until the next tap.
- **Check:** Hover every interactive element on the screen: does each show a visible state? Measure the transition on hover and selection states of dense lists; for any scaling element, is it alone in its group or one of several peers (peers scaling is a finding)? Tap a hover-styled control on a phone and see whether the state sticks.
- **Severity:** warning
- **Tells:** an interactive element with no hover state at all; bounce-in icons on row hover; a 300 ms tab-switch fade; hover-scale on a grid of cards; an underline-on-hover that stays after a tap; icons that spin or wiggle on hover.
- **Catalog:** A-10, A-15, L-14

### Feedback is proportional, and loading never flickers
- **Rule:** Routine actions get subtle feedback (a state change); significant ones get prominent feedback (a toast, a confirmation page). Success for routine actions is transient; failure persists until dismissed or resolved. Spinners and skeletons get a show-delay of ~150–300 ms and a minimum visible time of ~300–500 ms. Loading-state shape, skeleton geometry and announcement: lens 05 · Loading preserves layout and names the outcome.
- **Why:** Uniform loudness trains the user to ignore all of it [habituation]; a 40 ms spinner is a flash, not information [change blindness].
- **Check:** Is "Saved" a toast and "Order placed" a page? Does an error toast vanish before it can be read? Throttle to "fast" and watch for flicker; load cached data and watch for a skeleton blink.
- **Severity:** warning
- **Tells:** confetti on a settings save; a failed save as a 2-second toast; a skeleton blinking on cached data; a spinner that collapses its container.
- **Catalog:** F-02, F-08

### Every micro-interaction has four parts
- **Rule:** Trigger → rules → feedback → loops and modes. The trigger is discoverable and a system trigger is announced; constraints are stated before the attempt (disabled with a reason, format hint), not after; feedback lands within 100 ms, proportional to significance and persistent enough to be noticed; a mode is visible (on/off) and a loop re-arms (pull-to-refresh available again). A spec or critique that skips a part has a hole.
- **Why:** Missing parts get filled in at implementation time by whoever is nearest [slips lapses mistakes]; an invisible mode is the classic source of mode errors.
- **Check:** For the most important control name all four parts. Worked shapes: submit → "Saving…" with spinner beside the kept label → "Saved" (re-enable after ~1.5 s) or error; like → fills and increments optimistically → mode liked / not, rollback plus toast on failure; toggle → thumb slides 100–150 ms, track colour changes, state exposed → mode on / off.
- **Severity:** warning
- **Tells:** a spinner replacing the button label; a toggle with no visible mode; pull-to-refresh that never re-arms.
- **Catalog:** F-01, K-07

## Response time, waiting and optimistic UI

### Response matches the wait window
- **Rule:** 0–100 ms: a visual state change on the element, no spinner, no copy. 100 ms–1 s: a spinner (commands, single values, full-page navigation) or a skeleton (content, first load, predictable layout). 1–10 s: progress — a deterministic bar with percentage and amounts ("3.2 MB of 6.8 MB"); if indeterminate and over 3 s, a pulsing bar rather than a spinner. Over 10 s: a background job — toast on start, persistent jobs indicator, notification on completion, never a silent failure. No generic "Loading…" past 3 s; no "Almost done…" past 3 s; no percentage that stops moving; a time estimate and a cancel for anything over ~5 s.
- **Why:** The windows (0.1 / 1 / 10 s) are long-standing expert estimates — direct, noticed, attention held, abandoned — not measured thresholds [feedback loop] [vigilance]; treat the boundaries as tells and judge by what the user can see during the wait. The often-quoted "400 ms Doherty threshold" does not appear in its source report and is not a rule. A stuck bar destroys trust faster than no bar.
- **Check:** Time the operation and match the tier; watch a slow operation end to end; force a long job and look for where its result lands. Live only.
- **Severity:** warning; blocking for a silent failure of a background job
- **Tells:** a 99 % bar for 20 s; an indeterminate spinner on a 40 s export; a report generation with no notification; "Almost done" that is not.
- **Catalog:** F-02, F-03, F-13

Feedback by action: fast API click (< 500 ms) → button state; form submit (0.5–2 s) → button spinner beside the label, then inline errors; small upload (1–5 s) → bar with percentage; large upload (5–30 s) → bar + estimate + cancel; report (10–60 s) → background + notification; bulk import (30 s–5 min) → background + email; toggle, like, follow (< 200 ms) → optimistic; delete with undo → optimistic + undo toast; permanent delete → confirm first, then spinner; navigation (< 1 s) → skeleton; auto-save → "Saving…" → "Saved" indicator.

### Optimistic only where failure is rare and reversible
- **Rule:** Optimistic updates for like, follow, upvote, add-to-list and similar (> 99 % success, reversible). Never for payment, file save, publish, send or permanent delete. Rollback restores the exact prior state, tells the user, and offers retry.
- **Why:** An optimistic "Paid" that rolls back is a lie the user already acted on [loss aversion].
- **Check:** List optimistic actions; any irreversible one is a defect; force a failure and watch the rollback and its message.
- **Severity:** blocking (irreversible action); warning (rollback without a message)
- **Tells:** a heart that un-fills with no toast; "Sent" that quietly disappears.
- **Catalog:** F-14, F-07

### Validation trigger is one system-wide decision
- **Rule:** Default validate on leaving the field; validate on change only for strength meters, character counts and async availability (with a ~300 ms debounce); always re-validate on submit and show every error inline; submit stays enabled until the request starts, then disables with a spinner beside the kept label. The same trigger on every form. Error shape, kept values and text: lens 05 · Validation keeps the value and speaks in text; paste and keystroke rules: lens 08.
- **Why:** Submit-only validation judges the user after five fields; inconsistent triggers break the learned rhythm [conventions] [slips lapses mistakes].
- **Check:** Same trigger on every form? Type in an async-checked field and watch the debounce; submit an empty form — the interface explains, not ignores.
- **Severity:** warning
- **Tells:** submit pre-disabled "until valid"; a username check firing on every keystroke; validation on blur in one section and on submit in another.
- **Catalog:** E-01, D-13

### No autoplay without a pause; no critical information in timed UI
- **Rule:** Anything moving or updating on its own for more than ~5 s has a visible pause, stop or hide control; a carousel does not advance while the user reads or interacts. Toasts carrying an action, an error, or information the user may need stay until dismissed; where auto-dismiss is acceptable, ~5 s is the floor and hover or focus pauses the timer. Placement, stacking and copy of toasts: lens 05 · Toast behaviour.
- **Why:** Motion the user did not ask for is a distraction at best [attentional capture]; a vanished undo link is data loss on a schedule.
- **Check:** Find every timer and every autoplaying element; can the user stop it, and does anything essential disappear? Hover a toast with an action and watch the timer.
- **Severity:** blocking (essential information in a timed element); warning (autoplay without controls)
- **Tells:** a looping hero video without a pause; error toasts that self-dismiss; "Undo" only inside a 3 s toast; a carousel advancing under the cursor.
- **Catalog:** N-04, N-05, F-09

### Resilience keeps the user's place
- **Rule:** Offline and timeout are their own states, distinct from empty, with Retry and a statement of what is unsaved; actions available offline run locally and sync later with a visible status and conflict model; the session warns before expiry, allows extension and preserves data through re-auth; a background refresh never resets scroll, selection, focus or the field being edited; a retry uses a safe strategy so the user is never left guessing whether a payment or submission succeeded. State shapes and copy: lens 05.
- **Why:** State the user set and the system forgot is work done twice [working memory]; an ambiguous retry on money is the costliest slip [slips lapses mistakes].
- **Check:** Go offline mid-form and read the state; let the session expire mid-form; edit during a refresh; retry after an ambiguous failure and look for an idempotency guard. Live only.
- **Severity:** blocking (data lost or payment ambiguous); warning (rest)
- **Tells:** an "empty" list that is actually offline; a refresh that drops the selection; a second charge on retry.
- **Catalog:** N-10, N-11, N-12, N-13, N-14, F-06

## Reduced motion and safety floors

### Reduced motion means gentler, not none
- **Rule:** Under a reduced-motion preference: slides, scales, springs, parallax and choreography become short opacity crossfades or instant changes; durations cut by half or more; autoplay and looping decoration removed entirely; feedback that aids comprehension (press, focus, spinners, progress) kept. Prefer motion opt-in (only under "no preference") so the static version is the default; a global kill-switch keeps durations tiny rather than zero so end events still fire. Vestibular triggers — large zoom, full-screen position transitions, spinning elements over ~100 px, parallax beyond two layers, rapid direction changes — always need the alternative.
- **Why:** The preference targets vestibular triggers, not feedback; stripping everything removes cues users need, and motion sickness is an accessibility failure, not a preference.
- **Check:** Enable the OS preference and walk the flow; every spatial motion must change and every state change must remain perceivable. Static designs cannot prove this; mark not-reviewed.
- **Severity:** blocking (movement ignores the preference; vestibular trigger without an alternative); warning (feedback removed)
- **Tells:** no reduced-motion handling at all; sheets still sliding; all transitions set to zero including focus rings; a reduced branch that only removes the hero animation.
- **Catalog:** N-02

### Motion is never the only channel
- **Rule:** Every state change an animation communicates also leaves a static cue: colour, icon, label, position.
- **Why:** Reduced-motion users, screenshots and anyone who blinked still need to see what happened [change blindness].
- **Check:** Freeze the end state: is it clear what changed? A static design proves this directly.
- **Severity:** blocking
- **Tells:** a "saved" state signalled only by a pulse; selection shown only by a sliding indicator.
- **Catalog:** N-02, A-11

### No flashing above three per second
- **Rule:** Nothing flashes more than three times per second above the general and red-flash thresholds.
- **Why:** Photosensitive seizure risk; a safety floor that nothing overrides.
- **Check:** Inspect any flashing, strobing or rapidly alternating content; measure the rate.
- **Severity:** blocking
- **Tells:** a strobing error indicator; a rapid-blink attention cue.
- **Catalog:** N-03

### Translucent surfaces arrive as material
- **Rule:** A glass surface animates blur and scale together on enter so it arrives as material, not as a fade; under a reduced-transparency preference it goes frosty or solid. Material hierarchy and stacking rules: lens 11 · Materials and depth.
- **Why:** Translucency conveys depth only when it behaves like a thing [depth cues].
- **Check:** Step the first frames of a glass panel; toggle reduced transparency.
- **Severity:** note
- **Tells:** a glass panel that fades in flat then sharpens; grey text on glass under reduced transparency.

## Gaps, slop and the fix ladder

### Motion gaps
- **Rule:** Any element that appears or disappears with no transition is a gap: an element that vanishes, a layout that jumps, a mode switch where the content snaps while the chrome animates, an expandable section that appears fully grown, loading → content or → error that snaps, an icon swap with no crossfade. Exception: keyboard-initiated actions and top-frequency-tier actions (100+ times a day) — there the snap is required, not a gap (see lens 09 · Keyboard-initiated actions never animate; lens 09 · Frequency gate).
- **Why:** The eye tracks continuity; an unexplained cut breaks the spatial model [change blindness] [motion perception] — but a cut the user asked for a hundred times a day, or one triggered from the keyboard, is the fastest correct answer, not an omission.
- **Check:** List conditional renders and ternary swaps with no enter/exit, dynamic inline styles with no transition, tab and mode switches, expandable sections, loading and error transitions, icon swaps; for each, check whether it falls under the keyboard or frequency exception before flagging it. Code or live only.
- **Severity:** blocking; not applicable for keyboard-initiated or top-frequency-tier actions
- **Tells:** a sidebar that disappears in one frame; an accordion that pops open; a tab strip that animates its indicator while the panel teleports; an icon that swaps with a hard cut and no crossfade.
- **Catalog:** N-08

### The generated-interface motion signature
- **Rule:** None of these is wrong once; what makes them slop is frequency and uniformity. Treat two or more on one screen as one systemic finding against the motion system, not per component: pulsing status dots and "live" indicators on things that are not live (any instance without a written brand rationale); hover-scale on every card, chip and row (three or more per view); stagger on every list including ones the user scrolls daily (two or more staggered lists per view); bounce or overshoot on menus, modals, toggles and settings that had no momentum (any instance); the same blur entrance on three or more components; an identical fade-and-rise on four or more elements (three is a polish baseline); motion-on-mount for headings, paragraphs and navigation; generic keyframe names and one shared spring config imported everywhere; the same duration for every animation; `transition: all`; gradients or glows drifting continuously behind content; numbers counting up on every render; skeleton shimmer that never resolves into a stable layout; page transitions on every route in a work tool; scale-from-zero entrances; parallax on functional screens; icons that spin or wiggle on hover; a permanent hover-lift shadow animation; typewriter text in product UI; confetti or particle bursts on routine actions; slow, large "elegant" spinners; entrance or scroll animation on the review's own report.
- **Why:** Each item fails the frequency or purpose gate or is a physical-correctness defect; together they read as one template stamped across the app rather than decisions [processing fluency] [habituation].
- **Check:** Count how many of the list appear on one screen and across three screens; name which gate each one fails. The strongest single tell is bounce on a surface nobody flicked.
- **Severity:** warning (systemic); each item carries its own severity when isolated
- **Tells:** as listed.

### Motion is not doing the job of hierarchy
- **Rule:** Motion must not be the reason something is noticed. If removing every animation makes the primary action or the key number stop standing out, the static hierarchy is broken and the motion is compensating (the static rule: lens 01).
- **Why:** Motion is a channel that reduced-motion users, screenshots and the second glance all lose [pre-attentive pop-out] [change blindness].
- **Check:** Disable animations (reduced-motion preference) and re-evaluate the screen's hierarchy with the blur pre-test.
- **Severity:** warning
- **Tells:** a pulsing CTA on a page with three equally weighted buttons; an animated gradient border on the "recommended" plan.

### Delete is the first fix
- **Rule:** A motion finding names the earliest rung that resolves it: delete → reduce (shorter, smaller, fewer properties) → fix easing → fix origin or physicality → make interruptible → move to compositor properties → asymmetric timing → polish → accessibility gating.
- **Why:** The cheapest correct fix is usually removal; polishing something that should not exist is its own defect.
- **Check:** Every motion recommendation states its rung.
- **Severity:** note
- **Tells:** review comments that tune easing on a hover effect that should simply go.

## Motion audit checklist

Run in this order; the philosophy questions can void every later item. Severity in brackets; register-dependent items say so. Visual polish rows (borders vs shadows, gradient colour space, icon-button optical centring) belong to lenses 03 and 11.

Philosophy
- [ ] How often is it triggered? Frequent = less or none — blocking at 100s/day; warning at tens/day
- [ ] Keyboard-initiated? Then it does not animate — blocking
- [ ] Serves orientation, feedback or continuity, not decoration; users would not consciously notice it in production UI — warning
- [ ] Tested under reduced motion — blocking if unhandled
- [ ] Still natural after the tenth interaction; easing fits brand and register; duration fits the register's band — warning

Motion gaps (before judging existing motion)
- [ ] Conditional renders and ternary swaps with no enter/exit — blocking, unless keyboard-initiated or top-frequency-tier
- [ ] Dynamic inline styles with no transition; tab or mode switch that animates the chrome but snaps the content — blocking, unless keyboard-initiated or top-frequency-tier
- [ ] Expandable sections that show/hide instead of animating (via transform or clip); loading → content and error states that snap — blocking, unless keyboard-initiated or top-frequency-tier

Enter, exit, easing and timing
- [ ] Exit as prominent as enter — warning; no exit at all, a primary element just disappears — blocking
- [ ] Polish register missing its opacity + small translate + small blur enter recipe — note; that recipe on body text at first paint, or shared by 3+ components in one view — warning; elements flash before a delayed animation (missing fill mode) — warning
- [ ] Default ease / ease-in-out instead of a named curve — warning; ease-in on an entrance — blocking; an exit that eases out instead of accelerating away — warning
- [ ] No springs on gesture-driven elements — blocking; on other interactive elements — note; inconsistent timing across related animations — note
- [ ] Transform origin not matching the trigger on dropdowns and popovers — warning
- [ ] Duration over 300 ms — warning under restraint; acceptable under polish or play

State transitions and interaction patterns
- [ ] Icon swaps not crossfaded (opacity + scale + blur) — note; tooltips not first-delayed / subsequent-instant — note
- [ ] Hover states without a ~100–150 ms colour transition — note; positional hover motion — warning; no press feedback — warning
- [ ] Animating from scale 0 instead of ≥ 0.9 — warning
- [ ] Animation not interruptible (keyframes where a transition is needed; queues instead of blends) — warning; blocking on toasts and toggles
- [ ] Width/height reveals where clip-path would avoid layout — warning

Performance
- [ ] Layout properties animated on the hot path — blocking; will-change global or unspecific — warning; continuous animations without purpose — warning
- [ ] CSS variables updated per frame during drag; distance-only swipe thresholds; abrupt boundary stops — note

Accessibility
- [ ] No reduced-motion handling; vestibular triggers (large zoom, spin, parallax) without an alternative; functional animation with no non-motion alternative; flashing above three per second — blocking
- [ ] Looping animation that cannot be paused — warning

## Reference tables

Duration modifiers (apply to the surface table above): travel 50 / 100 / 200 / 300 / 400 px / full screen → 0.8× / 1.0× / 1.3× / 1.5× / 1.6× / 1.8–2.0×; exit = 65–75 % of entrance; desktop / tablet / mobile / watch / TV-kiosk → 1.0× / 0.9× / 0.8× / 0.6× / 1.3×; container < 400 / 400–800 / 800–1 200 / > 1 200 px → 0.8× / 1.0× / 1.0× / 1.1× with max displacement 20 / 25 / 20 / 15 % of width; dark mode → intensity −10–20 % (bright on dark hits harder).

Latency ceilings: hover < 100 ms; press < 150 ms; drag start < 50 ms; release and settle 200–300 ms; long-press 500–800 ms; error shake 300–400 ms (2–3 oscillations, ±10–15 px, decreasing, no overshoot).

Quality diagnostic — symptom → likely cause → fix:

| Symptom | Likely cause | Fix |
|---|---|---|
| Robotic | linear easing, uniform timing, everything synced | ease-out in, ease-in-out on screen; offset starts 50–150 ms |
| Too slow | over budget; ease-in-out where ease-out works; long anticipation | the register's column; ease-out reads faster; anticipation ≤ 10 % |
| Jarring | under minimum; no easing; no resolution | modals ≥ 200 ms (task) / 300 ms (expressive), pages ≥ 250 / 400 ms; 50–100 ms settle |
| Flat, cheap | primary only; opacity-only; same easing everywhere | add a secondary reaction (expressive surfaces); vary primary vs secondary easing |
| Distracting | too many movers; amplitude; competing heroes; no pause | 1/3 rule; reduce amplitude; one hero; 100–200 ms between beats |
| Dropped frames | layout properties; > 20 elements; shadows and filters; all simultaneous | transform + opacity; stagger to spread load |

Interactivity vocabulary for findings: responsiveness (≤ 100 ms), direct manipulation (drag vs menu, inline edit vs dialog), precision, pliability (effort to change), continuous vs discrete (slider vs buttons), clear labels and feedback, expected behaviour (does what it looks like it does), consistency.

Usability-motion techniques — each technique, the job its own definition names, where it usually lives, how it usually fails, and how strong the evidence is. Entries: Twelve usability techniques.

| Technique | Job | Typical component | Common failure | Evidence |
|---|---|---|---|---|
| Easing | expectation | every transition | linear motion; a curve that contradicts the brand; easing used as a reason to animate | design argument, practice |
| Offset and delay | relationship | action menus, card groups | timing groups contradict layout groups | indirect research |
| Parenting | relationship | collapsing headers, sliders, pager indicators | child on its own clock; rests half-visible | indirect research |
| Transformation | continuity, narrative | play/pause, search field, submit → progress → done | layout jump; label lost; morph into an unrelated object | research (data graphics); UI morphs practice |
| Value change | narrative, relationship | totals, counters, charts | count-up on every load; silent swap | research (charts); counters practice |
| Masking | continuity | card → detail, thumbnail → full view | wrong origin; stretched content; different return place | practice only |
| Overlay | relationship, narrative | swipe actions, drawers, pull-down search | both layers move; depth reads inverted | practice only |
| Cloning | narrative, relationship, continuity | add to basket, duplicate, new item | no origin; flight blocks the next action | design argument, practice |
| Obscuration | relationship (orientation) | modals, sheets, frosted panels | unreadable foreground; animated full-screen blur | research on the see-through state only |
| Parallax | relationship | editorial and showcase headers | on task screens; ignores reduced motion | research: no usability gain, some motion sickness |
| Dimensionality | narrative | card flips, folds, layered objects | 3D as decoration on task UI; full-screen rotation | research against 3D for spatial memory |
| Dolly and zoom | continuity, narrative | maps, photo grids, calendars, app open | zoom from the centre; wrong return; ignores reduced motion | research |
