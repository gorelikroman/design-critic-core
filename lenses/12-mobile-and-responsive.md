# 12 — Mobile and responsive

Checks the screen as it lives on a phone and as it stretches to its desktop twin: structure and flow on a small screen, reach and touch, safe areas and platform chrome, then how the layout holds under resize, growth and the keyboard. Order: structure → reach → chrome → growth.
Pre-tests: resize continuously; rotate; open the keyboard over the primary action; verify on hardware.
Screen states on a phone (all four mandatory) are in lens 05 · Required states present; hit-area floors in lens 10 · Target size; the viewport rule in lens 01 · Layout adapts to the viewport.

## Phone structure

### Mobile screen structure
- **Rule:** One intent per screen, a strong vertical hierarchy, no dense multi-column layouts, and the primary action visible without hunting.
- **Why:** [cognitive load] — a phone shows one column at a time, so every competing block is paid for in scrolling and attention; a screen that feels busy is doing too much.
- **Check:** Is the primary action on the first viewport? Count columns carrying text or inputs; more than one is a tell. Intent and the dominant action: see lens 04 · One intent per screen and lens 04 · The primary action is the screen's verb.
- **Severity:** warning
- **Tells:** desktop table crammed into a phone; two-column forms; a settings panel inside a task flow.

### Phones have no periphery
- **Rule:** On a phone the whole content is in focus: elements may shrink 10–30 % versus desktop without losing optical size; horizontal movement is weak; perception is faster and consumption is quick. Tap targets keep the platform floor regardless (see lens 10 · Target size).
- **Why:** [focal vs peripheral vision] — the viewing distance is shorter and the format narrow, so peripheral vision barely participates.
- **Check:** Is the phone version a proportional shrink of desktop, or the same optical sizes crammed in? Are any desktop-only peripheral signals (side rails, hover cues) load-bearing on the phone?
- **Severity:** warning
- **Tells:** desktop type sizes on a phone forcing one word per line; a side rail carrying the only status.

### Lists over grids
- **Rule:** Lists by default for clarity and scanning; grids only when the items are visual and the grid is justified; long lists virtualised.
- **Why:** [reading eye movements] — a single column gives every item a full measure and one scan path; a grid halves the measure and doubles the paths.
- **Check:** Is a grid carrying text-heavy items? Do titles truncate? Does a long list stay smooth on hardware (static design cannot prove this; mark not-reviewed)?
- **Severity:** note
- **Tells:** two-column cards with truncated titles; a grid of text rows.

### Flow direction follows scroll
- **Rule:** Mobile flows progress top to bottom. A primary action never depends on content below the current scroll position, and the user never scrolls up to continue or complete.
- **Why:** [working memory] — a step that needs context above the fold forces a backward search and a reload of what was already read.
- **Check:** Trace the flow: does any step require scrolling up to understand context or find the CTA? Does a sticky CTA depend on fields not yet seen?
- **Severity:** blocking
- **Tells:** summary above, inputs below, "Confirm" at the top; a sticky header CTA that depends on unseen fields.

### Bottom tab bar or drawer
- **Rule:** With 2–5 peer sections switched often, primary navigation is a visible bottom tab bar. With 6 or more sections, or in a content-heavy product where browsing is the task, a drawer or a "more" tab is not a defect. Hiding five or fewer primary sections behind a menu is the failure; the count is the tell.
- **Why:** [recognition over recall] — visible tabs show the product's structure; a menu makes the user recall what is behind it.
- **Check:** Count top-level sections and how often the user switches between them. Five or fewer peers behind a ☰ → fail; six or more, or content-led → context, record the count. Component rules: see lens 11 · Tabs over hamburger for primary navigation.
- **Severity:** warning
- **Tells:** three sections behind a ☰; a bottom bar with one item; a bar holding more than five peers (then the IA is the problem).

## Reach, touch and native feel

### Thumb reach
- **Rule:** Primary actions sit in thumb-friendly zones; no critical action lives only in the top bar; touch targets forgive imprecision.
- **Why:** [Fitts's law] — distance from the thumb's rest position and target size set the cost; a control outside the arc adds a grip change on top.
- **Check:** Is the primary CTA in the bottom third? Is any critical control only in the top bar? Do targets meet the platform floor (see lens 10 · Target size)?
- **Severity:** warning
- **Tells:** "Done" only in the top-right; tiny inline icon buttons; a confirm chip against the top edge.

### Touch gets a hover equivalent
- **Rule:** Nothing that hover reveals — an action, a value, a tooltip — is reachable only by hover. Row actions get a visible or tappable route; column charts support a finger slide across columns with pop-up values; keyboard gets an equivalent too.
- **Why:** [affordance and signifier] — a hover-only affordance does not exist for a finger; the value or action is present but unsignified and unreachable.
- **Check:** On a touch device, or with hover disabled: tap and hold every hover-revealed control; drag a finger across each chart in the prototype and read every plotted value. A static design cannot prove the slide; check the prototype or mark not-reviewed. Desktop side of the same rule: lens 11 · Tables and charts expose values.
- **Severity:** blocking
- **Tells:** a static chart image; tap-only tooltips that vanish; row actions that appear only on mouse-over.
- **Catalog:** L-14

### Numeric keypad for numeric input
- **Rule:** Numeric-only fields present the numeric keypad, never the alphanumeric keyboard.
- **Why:** [slips lapses mistakes] — the wrong keyboard costs a switch on every entry and invites format slips.
- **Check:** Input mode or keyboard type on amount, code, quantity and card fields. Static design cannot prove it; check code or the build. Labels, autocomplete and other keyboard hints: see lens 08 · Keyboard and autocomplete match the field.
- **Severity:** blocking
- **Tells:** QWERTY keyboard on an amount field; a date field that opens the text keyboard.

### The eleven tells of a website in a browser
- **Rule:** On a phone each of the eleven below reads as "a website in a browser", and each has a one-line fix (table). Fix them at the platform layer before touching motion.
- **Why:** [conventions] — most "the app feels janky on mobile" reports are these platform-layer defects, not animation problems.
- **Check:** On a real device: tap a hover-styled control; long-press a button; scroll to the top of a sheet; rotate; open the keyboard. In code: search for `user-scalable=no`, a fixed `100vh` shell, `user-select: none` on body, a `touchmove` prevent-default hack. Static design cannot prove any of these; mark not-reviewed.
- **Severity:** warning
- **Tells:** hover stuck after a tap; the page zooming into an input; content under the notch.

| # | Tell on the phone | Fix |
|---|---|---|
| 1 | Hover state stuck after a tap | Gate hover styles behind a hover-capable pointer (see lens 09 · Hover is visible; scale only a standalone element) |
| 2 | Grey or blue flash on tap | Clear the tap highlight, then supply a press state (see lens 09 · Every pressable element has a press state) |
| 3 | Wrong layout height under the browser bar | Dynamic viewport height for app shells, small viewport height for heroes; never a fixed `100vh` shell |
| 4 | Page zooms into inputs | Input text at 16 px or larger. Disabling zoom instead is blocking (see lens 08 · Never block paste, typing or zoom) |
| 5 | Laggy taps | Press feedback on pointer-down plus `touch-action: manipulation` |
| 6 | Pull-to-refresh hijacks a custom scroller | `overscroll-behavior: none` on the root, `contain` on inner scrollers |
| 7 | Content stops at the notch | Cover the viewport plus safe-area insets, with fallbacks (see Safe areas and system bars) |
| 8 | Long-press selects button text | No-select on controls only, never on body |
| 9 | Carousel scrolls the page | Declare which axes the element owns |
| 10 | Status-bar colour mismatch | One theme colour per colour scheme |
| 11 | Works in emulation, wrong on the phone | Test on hardware (see Hardware is the bar) |

### Capability queries, not device sniffing
- **Rule:** Branch on what the platform reports (hover capability, pointer precision, safe-area insets, viewport units), never on the user agent or the screen width to guess "touch".
- **Why:** tablets with trackpads and laptops with touchscreens break every device guess.
- **Check:** In code: search for user-agent or width tests that decide hover or touch behaviour. Static design cannot prove this; mark not-reviewed.
- **Severity:** note
- **Tells:** an `isMobile` flag derived from width switching off hover.

### Hardware is the bar
- **Rule:** Sticky hover, tap delay, safe areas, keyboard resize and rubber-banding do not reproduce in desktop emulation. A fix is verified only when seen on a phone — ideally a few years old — with the keyboard open, and once in landscape.
- **Why:** a fix claimed from emulation ships every defect emulation hides.
- **Check:** The review states which findings were verified on hardware and which are "not verified".
- **Severity:** note
- **Tells:** "tested in device mode" as the only evidence.

## Safe areas, insets and platform chrome

### Breathing room, insets and bleeds
- **Rule:** Where no density system exists: about 12 px between adjacent bordered controls, about 24 px around borderless ones, 24 px or more between unrelated groups; compact tools may go tighter as long as hit areas stay distinct. Buttons in content layouts sit inside the layout margins (about 16 px inline on a phone) with a visible radius; edge-to-edge actions are valid only as deliberate platform chrome with safe-area padding. Backgrounds and media bleed to the edges; text and controls stay inside the margins; sticky chrome floats over content rather than consuming a strip.
- **Why:** [gestalt grouping] — a borderless control's boundary is the space around it; a button glued to three edges reads as system UI and clips on curved corners.
- **Check:** Measure control gaps; check that hero media bleeds while its text does not; look at bottom bars on a notched phone. The structural floor for gaps (inter-group ≥ 1.5× intra-group) is in lens 01.
- **Severity:** warning
- **Tells:** full-width square-cornered fixed CTA; icon buttons packed at 4 px; text touching the viewport edge.

### Safe areas and system bars
- **Rule:** Content and controls respect notches, cutouts, status and navigation bars, the home indicator and the keyboard; the viewport is covered plus safe-area insets, with fallbacks. Media may bleed under system chrome; text and actions never sit under it.
- **Why:** anything under system chrome is unreadable or untappable, and a bottom action under the home indicator is the primary action lost.
- **Check:** On a notched device with the keyboard open: is anything under the status bar, the home indicator or the keyboard? Rotate. Static design: check the frame's safe-area guides and the bottom bar's padding.
- **Severity:** blocking
- **Tells:** bottom CTA under the home indicator; content stopping at the notch; a sheet whose last row hides behind the keyboard.
- **Catalog:** L-13

### Platform patterns and predictable back
- **Rule:** Use platform patterns unless evidence says otherwise. Back behaviour is predictable: the system back gesture and the navigation back both work and go where the user expects; every modal has a native dismiss.
- **Why:** [conventions] — a control that behaves unlike the platform's version costs a learned expectation on every use; when it feels non-native, the product created the friction.
- **Check:** Custom back that breaks the system gesture? Modal with no native dismiss? Consistency and stock components in general: see lens 06 · Consistency over creativity.
- **Severity:** warning
- **Tells:** modal without a native dismiss; a custom swipe that fights the back gesture; a novel gesture with no affordance.

### Orientation is not locked
- **Rule:** Do not lock orientation unless it is essential to the task; the layout survives rotation without losing content or the primary action.
- **Why:** some users mount the device in a fixed orientation and cannot rotate it; a locked screen is unusable to them.
- **Check:** Rotate the device: does intent or the primary action change? Anything truncated? Static design: is a landscape variant designed, or is the lock justified by a stated reason?
- **Severity:** blocking
- **Tells:** landscape locked "because the layout breaks"; a rotated screen that drops the CTA.
- **Catalog:** L-11

## Responsive structure and growth

### Hold structure until it breaks
- **Rule:** Breakpoints come from the content — where the sidebar squeezes the measure below its minimum, where the grid drops below a usable column — not from device presets. Collapse late; prefer container queries for components; test the smallest and largest supported sizes first.
- **Why:** preset breakpoints throw away space the user paid for and break where nobody looked.
- **Check:** Resize continuously and watch for the moment structure breaks; desktop tested on resize and zoom, mobile on orientation and safe areas. Zoom to 200 % and reflow at 320 px are floors (see lens 10 · Structure is navigation; zoom and reflow). The viewport rule itself: lens 01 · Layout adapts to the viewport.
- **Severity:** warning
- **Tells:** 768 px and 1024 px because they are the defaults; a fixed-width layout; horizontal scroll at a supported width.
- **Catalog:** L-04, L-12

### Plan for growth
- **Rule:** No fixed width or height on text containers; buttons size from their label; translated strings grow, and short ones grow most, so a one-word button is the riskiest thing on the screen; larger system text must fit.
- **Why:** fixed sizes overflow the first time a long language or a large text setting arrives.
- **Check:** Render with pseudo-localised strings; set the largest accessibility text size; inspect fixed heights on text containers.
- **Severity:** warning
- **Tells:** a 96 px-wide button with hidden overflow; a label with a fixed height; a card that assumes a two-line title.
- **Catalog:** L-06

### A critical action is never clipped
- **Rule:** Never park a critical action where a resize, a scroll, the keyboard, large system text or a long translation clips or hides it. Keep it in flow, or in stable chrome: a sticky footer with safe-area padding; a modal's action row that does not scroll with its content. Resize and rotation never change the primary action.
- **Why:** a clipped primary action is a functional failure — the screen's verb cannot be done — whatever the layout looks like.
- **Check:** Open the keyboard over a form's submit; resize to the smallest supported width; set large text; rotate. Is the action still visible and tappable?
- **Severity:** blocking
- **Tells:** a primary action below the fold of a fixed-height modal; a submit hidden behind the keyboard; a CTA cut off at a supported width.
- **Catalog:** L-05

### Desktop widens the column, not the story
- **Rule:** The desktop twin keeps the mobile order in one widened column; it goes wider only where a side-by-side comparison needs it (two options, a timeline as a row), and it stays under the grid's readable maximum (even splits, about six columns at most).
- **Why:** [schemas and scripts] — reordering across breakpoints breaks twin-screen consistency and the user's script of the flow; width is only useful where things are compared.
- **Check:** Diff the order of blocks between breakpoints; every widening must correspond to a comparison (comparison and choice: lens 04).
- **Severity:** note
- **Tells:** a three-column desktop form whose mobile twin is a single stack in a different order.

### Longread dramaturgy
- **Rule:** A long page is a story on the scroll timeline: floors are events (setup → development → climax → resolution); each block is born from the previous, rhymes with it and adds something new. The vertical is the constant, the horizontal the variable that sets tempo. After a dense text block insert a rest (an image, air). State the motif on the first screen and develop it; end with a footer carrying the canonical closing set (name, copyright, subscribe, social, back to top).
- **Why:** [serial position] — the first and last floors are remembered best, and [vigilance] — a high perception tempo cannot be held long, so rests and a real closing are structural, not decorative.
- **Check:** Walk the page floor by floor: where are the rests? Does each floor pick up the previous axis (see lens 01 · Force-line continuity across scroll)? Is the last floor a real closing, not an afterthought?
- **Severity:** note
- **Tells:** six text floors with no pause; a page that ends mid-thought; a footer that is one grey line.
