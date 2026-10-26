# 11 — Components

Checks each component family against the structural rules that make it behave the way its name promises: buttons, links and icons; segmented controls and tabs; navigation, search and dropdowns; overlays (dialogs, sheets, popovers, tooltips, toasts, materials); disclosure, cards, lists and drag and drop; tables, charts and bulk selection. Order: the control's contract → its states → its keyboard model → its edge cases.
Pre-tests: name each component's family; count its states; open it from the keyboard.
Keyboard, focus and target floors are lens 10; checkboxes, radios and switches are lens 08 (from lens 08 · Checkbox for many, radio for one); how overlays move is lens 09; error, empty and loading states are lens 05; button and link copy is lens 07; primary navigation on a phone is lens 12.

## Buttons, links and icons

### Button for actions, link for locations
- **Rule:** A button performs an action; a link changes location. Navigation is never disguised as submission or the reverse. A link is a real link, so middle-click, Cmd/Ctrl-click, right-click and "open in new tab" work; an action is a real button.
- **Why:** Users predict the outcome from the element type [conventions] [mental models]; a "button" that navigates loses history and a "link" that submits fires twice.
- **Check:** For every control, note whether it changes the URL or performs an action; the element must match. Middle-click every navigation element. Code proves the element; a live build proves the behaviour. Semantics floor: see lens 10 · Native elements first, ARIA last.
- **Severity:** blocking
- **Tells:** a card that navigates on `onClick` with no anchor; "Submit" styled as a link; a menu of links rendered as buttons.
- **Catalog:** B-01, A-14, G-08

### Button states are distinct and consistently placed
- **Rule:** Rest, hover, focus, pressed, selected, loading and disabled never look identical when they mean different things; each interactive state is more prominent than rest, not less. Every button and link has a hover state on pointer platforms. During a long operation the button keeps its width and its label and shows progress beside it, with no layout jump. Primary and secondary actions sit in the same positions across screens and dialogs unless a platform convention dictates otherwise; on mobile a sticky primary action never covers content, the keyboard, safe areas or an error.
- **Why:** State is what tells the user whether the press was heard and whether pressing again is safe [feedback loop]; consistent placement lets the hand act before the eye reads [Fitts's law].
- **Check:** Screenshot each state side by side; identical pairs → fail. Trigger loading and measure width before and after. Compare button placement across dialogs. A design file proves the states exist; a live build proves they appear. One dominant per view: see lens 01 · Single dominant. Press feedback timing: see lens 09 · Every pressable element has a press state. Disabled with a reason: see lens 05 · Disabled means unavailable, and says why.
- **Severity:** blocking when states that differ in meaning look identical; warning otherwise
- **Tells:** hover identical to rest; a label that vanishes into a spinner; a button that shrinks while loading; Cancel on the left in one dialog and the right in the next.
- **Catalog:** A-15, B-05, B-08, B-09, B-11, B-17, B-18

### Destructive button names the action and keeps its distance
- **Rule:** A destructive button carries the destructive verb and the object ("Delete project"); red alone never carries the risk. A dangerous command is not immediately adjacent to a safe one of the same size and style.
- **Why:** Users act on position and label before they read the body [slips lapses mistakes]; colour is lost in greyscale and by a colour-blind user [colour vision deficiency].
- **Check:** Read the label for the verb; greyscale the dialog; measure the gap and the style difference between the destructive and the safe button. A static design proves this. Safeguards and menu placement: see lens 05 · Destructive safeguard and lens 05 · Destructive item is last and quiet.
- **Severity:** blocking
- **Tells:** a red "OK"; "Yes" as the destructive answer; Delete and Save side by side in the same filled style.
- **Catalog:** B-06, B-07, E-13

### Links are identifiable and say where they go
- **Rule:** A body-text link is identifiable at rest without hover: underline, or a distinct colour plus a second cue. Link text makes sense out of context, and repeated "Learn more" links get distinct accessible names. An external destination, a new tab, a download or an unusual file format is signalled before the click; new windows are opened only with a reason.
- **Why:** Screen-reader users navigate from a list of link names [recognition over recall]; an unsignalled new tab breaks the Back button and the user's map [mental models].
- **Check:** Extract all link texts and read them as a list; find duplicates with different targets. View body copy at rest and mark the links. Check icons on external and download links. A static design proves this. Link copy: see lens 07 · Links say where they go; toggles describe ON.
- **Severity:** blocking when link text is meaningless out of context or colour is the only cue below 3:1; warning otherwise
- **Tells:** three "Learn more" on one page; a link the same colour and weight as body text; a PDF that opens with no hint.
- **Catalog:** B-14, B-15, B-16, G-08

### Stroke matches text weight; one set per surface
- **Rule:** Icon stroke follows the adjacent text's weight: ~1.5 px beside regular text, ~2 px beside medium or semibold, ~2.5 px beside bold. One stroke convention and one icon library per surface. Inline icons are sized relative to the text, about 1–1.25 em.
- **Why:** A hairline icon beside bold text looks broken and a heavy icon beside regular text shouts [gestalt grouping]; two libraries on one toolbar look like two products.
- **Check:** Compare stroke weights across a toolbar and against their labels; list the icon libraries in use on the screen. A static design proves this.
- **Severity:** warning
- **Tells:** mixed outline and filled icons in one nav; icons visibly thinner than their labels; two chevron shapes on one page.

### One glyph, recoloured per state; outline default, fill active
- **Rule:** Icons take colour from the current text colour and get hover, selected and disabled states from styling, never from separate assets. Where a set has outline and filled variants, outline is the resting state and fill marks selected or active.
- **Why:** Separate assets drift and hard-coded fills ignore the theme; filled-everywhere leaves the active tab with no signal [pre-attentive pop-out].
- **Check:** Toggle the active tab; only one icon fills. In code, look for hard-coded fill colours inside SVGs and for icons that stay dark in dark mode. Design file proves the variant logic; code proves the colouring.
- **Severity:** warning
- **Tells:** filled icons on every tab; icons that stay dark in dark mode; a hover state shipped as a second PNG.

### Design at render size, on the grid, as vector
- **Rule:** Test every icon at the smallest size it renders (often 16 px); prefer simplified glyphs for small contexts; use the set's native grid sizes rather than fractional scaling; always vector.
- **Why:** Detail that reads at 48 px turns to mush at 16 [contrast sensitivity]; off-grid scaling renders soft.
- **Check:** View the icon set at its smallest use; look for blurred or unrecognisable glyphs. A design file at 100 % proves it.
- **Severity:** note
- **Tells:** 24-grid icons rendered at 18 px; raster icons; a detailed illustration used as a 16 px glyph.

### Mirror only direction-bound icons in RTL
- **Rule:** Under a right-to-left locale, flip navigation arrows, chevrons, text-alignment glyphs, "send" arrows and sound waves; leave logos, checkmarks, physical objects and media-playback glyphs alone; analyse composite icons part by part. Digits never mirror.
- **Why:** Meaning tied to reading direction must follow it; meaning tied to the physical world must not [conventions].
- **Check:** Switch to RTL and inspect each directional icon. A live build or an RTL frame in the design file proves it; otherwise mark not-reviewed.
- **Severity:** note
- **Tells:** mirrored clocks and logos; un-mirrored back arrows.
- **Catalog:** M-08

### Icon-only controls carry a name
- **Rule:** Every icon-only button has an accessible name describing the action ("Close", "Search", "Add to favourites") that updates with its state ("In favourites"); the glyph itself is hidden from assistive technology. An unfamiliar icon also gets a visible label or a tooltip. The same icon is never used for different commands unless text disambiguates.
- **Why:** A screen reader sees an unnamed button and a voice-control user cannot say what to press [recognition over recall]; one glyph meaning two things is an error trap [mapping].
- **Check:** Read the accessibility tree for every icon button; toggle stateful ones and re-read. Inventory icons across screens for one glyph with two commands. Hover unfamiliar icons for a tooltip. Code proves the name; a live tree proves it is computed. Name and state floor: see lens 10 · Every control exposes name, role and state.
- **Severity:** blocking
- **Tells:** buttons announced as "button"; names that describe the glyph ("magnifying glass"); the same pencil meaning "edit" here and "sign" there.
- **Catalog:** B-12, B-13, K-09

## Segmented controls and tabs

### Segmented control for two to five options
- **Rule:** A segmented control holds 2–5 short, mutually exclusive options; longer lists need another control. Every segment is equally easy to activate and the selected segment is distinguishable beyond colour. When the choice switches whole content panels, it is a tab list with tab semantics, not a segmented control.
- **Why:** The control's whole promise is that all options are visible and one is chosen [Hick–Hyman law]; past five, labels shrink below reading size [crowding].
- **Check:** Count segments; more than five → flag. Measure segment sizes; greyscale the selected state. Ask whether the choice switches a panel; if yes, it needs tab semantics. A static design proves count, size and greyscale; code proves semantics.
- **Severity:** blocking for tab behaviour without tab semantics or a colour-only selection; warning for count and size
- **Tells:** seven segments with truncated labels; a segmented control driving three different pages; a selected segment marked by a tint only.
- **Catalog:** C-19, C-20, C-21

### Tabs switch peer views, not steps
- **Rule:** Tabs switch between peer views in one context; they are never wizard steps or sequential, dependent screens. The active tab is visually clear, exposes its selected state, and is associated with its panel. Keyboard: Tab enters the tab list, arrows move between tabs, Enter or Space activates; auto-activation on focus only when the panel appears without noticeable delay. Overflowing tabs scroll with a visible continuation cue; labels are never compressed to unreadable. Switching tabs preserves local state (filters, scroll, typed text) unless the user resets it. Changing a tab never triggers a critical action when the interaction looks navigational.
- **Why:** Tabs promise that any order is fine and nothing is lost [mental models]; a tab that commits or resets breaks the promise silently [change blindness].
- **Check:** Are the tabs sequential or dependent? Then not tabs. Inspect the selected state and panel association in the tree. Arrow through the tabs with the network throttled. Narrow the viewport and look for truncation and a cue. Type in a panel, switch away and back. Change a tab and look for side effects. A static design proves the tab structure and overflow cue; code and a live build prove the rest.
- **Severity:** blocking for a tab that commits a critical action, a selected state absent from the tree, or no keyboard path; warning otherwise
- **Tells:** "Step 1 / Step 2 / Step 3" as tabs; six tabs squeezed to 9 px labels with no scroll cue; a filter panel reset by switching tabs; auto-activated tabs that lag a second each.
- **Catalog:** C-22, C-23, C-24, C-25, C-28, C-29, C-30

### Swipe between tabs is a supplement
- **Rule:** On mobile, swiping between tabs is optional and only for adjacent, homogeneous pages; tapping always works. During a swipe the indicator and content move in sync, and the gesture never conflicts with system Back, carousels, maps or horizontal controls inside the panel.
- **Why:** A gesture is invisible and collides with everything else horizontal on the screen [affordance and signifier]; tap is the promise the tab makes.
- **Check:** Tap must work; swipe inside nested horizontal content and watch for conflicts. A prototype or live build proves it; static design cannot; mark not-reviewed. Gesture alternatives floor: see lens 10 · Gestures have a single-pointer alternative.
- **Severity:** warning
- **Tells:** a tab bar where only swipe changes panels; a map inside a swipeable tab; an indicator that jumps after the content settles.
- **Catalog:** C-26, C-27

### Tabs over hamburger for primary navigation
- **Rule:** Primary sections are visible navigation: tabs when there are 2–5 peer-level, frequently switched sections; a bottom bar holds 3–5 top-level destinations and never contextual actions. A drawer or "more" is not a defect for 6 or more sections or for a content-heavy product where browsing is the task; the count is the tell, and hiding 5 or fewer primary sections behind a menu is the failure. Global navigation keeps the same place and order on every screen.
- **Why:** Visible tabs show the product's structure; a menu makes the user recall what is behind it [recognition over recall]; more than five tabs stops being a set the eye holds [working memory].
- **Check:** Count top-level sections and how often the user switches. Five or fewer behind a ☰ → fail; six or more or content-led → context, record the count. Any action among the bottom-bar items → flag. Compare the nav across screens. A static design proves this. Phone layout of the same rule: see lens 12 · Bottom tab bar or drawer.
- **Severity:** warning
- **Tells:** three sections behind a ☰; a bottom bar with one item, or with "Share" in it; tabs holding more than five peers (then the IA is the problem).
- **Catalog:** G-02, G-17

## Navigation, search and dropdowns

### Location is visible
- **Rule:** On every screen the user can tell where they are within three seconds: a page title or heading, the active navigation item, a breadcrumb or step indicator when depth or sequence needs it. A breadcrumb shows hierarchy, not history, and its last item is the current location, not a command. A navigation item names a destination ("Settings"); a command item names an action ("Save settings"). Every screen, error pages included, has a way out.
- **Why:** Wayfinding is the first question a screen answers [mental models]; an active item marked by hue alone disappears for a colour-blind user [colour vision deficiency].
- **Check:** Land on the screen cold and name the location; find the active item in greyscale; read the breadcrumb's last item; read nav labels as a list. A static design proves this. Dead ends: see lens 05 · No dead ends.
- **Severity:** blocking when the location cannot be identified or the screen has no exit; warning otherwise
- **Tells:** a detail page with no title and no back route; the active nav distinguishable only by hue; a breadcrumb ending in "Edit".
- **Catalog:** G-01, G-07, G-18

### URL carries state; Back restores it
- **Rule:** On the web the URL represents any state a user may open, refresh, bookmark or share: route, filters, tab, pagination, expanded panel, search query. Browser Back and Forward restore the actual previous state, including scroll position and form data; system Back on mobile follows platform history and never closes, resets or exits unexpectedly. With a sheet, drawer or modal open, Back closes it and does not navigate; a modal close goes one level, not two. Returning to a list preserves scroll, filters, sorting and selection.
- **Why:** Back is the most-used control on mobile and the most-violated convention [conventions]; state the user set and the system forgot is work done twice [working memory].
- **Check:** Refresh and share the URL; press Back after every navigation, with a sheet open, and after a deep scroll; open an item and return to the list. A live build proves this; code proves URL sync exists; static design cannot; mark not-reviewed.
- **Severity:** blocking
- **Tells:** a filter set lost on refresh; Back from a detail losing the list's filters; Back closing the app from a sheet; a modal that closes two levels.
- **Catalog:** G-03, G-04, G-05, G-06

### Continuation without precise gestures
- **Rule:** Pagination or infinite scroll works without a precise gesture: an explicit continuation, a loading state, an error with retry, and a reachable footer. Pagination preserves query, filters and sorting and shows the page or range. Pagination when users need a specific page or a shareable position; infinite scroll only for homogeneous browsing; "Load more" as the compromise that keeps position and Back working.
- **Why:** A footer that the list keeps pushing away is unreachable [Fitts's law]; a page-load failure with no retry is a dead end [layered defences].
- **Check:** Try to reach the footer; simulate a page-load error; go to page 2 and read the state and label. A live build proves this; a design file proves the continuation control and error state exist.
- **Severity:** blocking for an unreachable footer or a load failure with no retry; warning otherwise
- **Tells:** infinite scroll on a page with a footer; page 2 dropping the filters; a spinner that spins forever after a failed page.
- **Catalog:** G-15, G-16

### Search is full-text
- **Rule:** Search matches across all relevant visible content, partial words and phrases, ranked by relevance; never "starts with" only. Field-specific search is optional and explicitly labelled. Search is provided where volume or frequency justifies it, and the primary find path is not hidden in an overflow menu.
- **Why:** Content that is visible but not discoverable is content the user cannot use [recognition over recall].
- **Check:** Search for a word from the middle of a visible title; search a phrase. Find the search entry point without opening a menu. A live build or a stated search spec proves this; static design cannot; mark not-reviewed. Search timing targets: see lens 13.
- **Severity:** blocking
- **Tells:** prefix-only matching; search that hits one column silently; search two menus deep.
- **Catalog:** G-09

### Search submits, keeps the query, and says when nothing matched
- **Rule:** Search works with Enter or the keyboard's Search key and with an explicit button; suggestions never replace submission. On the results screen the query stays visible and editable. Zero results show the query, a likely reason, and a next step — broaden, check spelling, clear filters — and never a "create" call to action, because the user was looking, not making.
- **Why:** The query is the user's own words and the only anchor for a second try [working memory]; an empty results page that hides the query forces a retype.
- **Check:** Press Enter; click the button; read the results header; search nonsense. A design file proves the results and zero-results frames exist; a live build proves submission. Empty-state kinds: see lens 05 · Five kinds of nothing.
- **Severity:** warning
- **Tells:** a search field that only reacts to a dropdown pick; a results page with an empty box; "Create your first project" under a filtered search with zero hits.
- **Catalog:** G-10, G-11, G-12

### Filters are visible, clearable and counted
- **Rule:** Active filters are shown next to the results, with a Clear all, and the result count updates predictably. On mobile the model is explicit: either filters apply immediately, or an Apply button previews the count; live updates never also demand a Save.
- **Why:** A filter the user cannot see is a filter the user forgets [working memory]; two application models on one screen is a slip generator [slips lapses mistakes].
- **Check:** Apply filters and look for chips, a count and Clear all; on mobile identify the model and the preview count. A static design proves the chips and count exist.
- **Severity:** warning
- **Tells:** a result list silently filtered by yesterday's choice; an Apply button and live filtering on the same sheet; no count on Apply.
- **Catalog:** G-13, G-14

### Dropdowns and selection
- **Rule:** Arrow keys plus Enter choose. The user can type an existing option and confirm without opening the list; non-trivial option sets filter as the user types; a list of hundreds (countries, cities) never ships without search and typeahead. A combobox exposes its expanded state, the selected option and a result count, and suggestions never take control: a custom value, closing the list, and submitting stay possible. Control by size: a select for a compact familiar list, radios for a small important list, a searchable combobox for a long one. The default selection is safe.
- **Why:** Scrolling a long list repeatedly is recall work the control should do [recognition over recall] [Hick–Hyman law]; a suggestion list that captures Enter steals the submit.
- **Check:** Select with the keyboard only; type and watch the filter; count options against the control type; type a value not in the list and submit; inspect expanded state and live status in the tree. A design file proves control choice; a live build proves the keyboard and typeahead. Field-level rules: see lens 08.
- **Severity:** blocking for no keyboard path, no typeahead on a long list, or a combobox that ignores typed text; warning for control choice
- **Tells:** a native select with 200 countries; a combobox that ignores typed text; Enter picking the first suggestion instead of submitting.
- **Catalog:** D-23, D-24, D-25, D-26

## Overlays: dialogs, sheets, popovers, tooltips, toasts and materials

### Modal only for a decision or a short task
- **Rule:** A modal interrupts for a required decision or a short focused task. Not for information only, not for reference content (a panel), not for onboarding, not for a form of more than about 5 fields or a multi-step flow — those are a page or a full-screen view. A success state closes the modal rather than lingering in it.
- **Why:** Every modal is an interruption that blocks the page behind it [attentional capture]; a twelve-field modal is a page with worse navigation.
- **Check:** Count the fields and steps inside the modal; read what it contains and whether the page could hold it. A static design proves this.
- **Severity:** warning
- **Tells:** a modal with a scrollbar and its own tabs; a "Welcome" modal over the empty dashboard; success copy that leaves the modal open.
- **Catalog:** H-01

### Modals
- **Rule:** A modal has a clear title and a visible close or cancel command, and closes by the close control, Escape and — for a lightweight, non-destructive one — backdrop click; errors stay inside it. Initial focus follows the task: the first field for input, the start of the content for reading, the safe command for an irreversible action, so a destructive confirm opens on Cancel. Cancel and Close mean different things: Cancel discards an unfinished action, Close dismisses a view; when the consequences differ the labels say so.
- **Why:** Focus placement decides what Enter does [slips lapses mistakes]; a modal with no visible exit is a trap for anyone who does not know Escape [conventions].
- **Check:** Find the title and the close control; open the dialog from the keyboard and note where focus lands; press Escape; read what Cancel and Close each do. A static design proves title and close; a live build proves focus and Escape. Focus containment and return: see lens 10 · Focus moves in, stays in, and returns. Motion: see lens 09 · Modal, backdrop and content arrive as one beat. Confirmation copy: see lens 05 · Error copy answers four questions and lens 07 · Verb-first buttons that repeat the consequence.
- **Severity:** blocking for a modal with no title or no visible close, or a destructive confirm that opens on the destructive button; warning otherwise
- **Tells:** a modal that cannot be dismissed without completing; "Delete" focused on open; a "Cancel" that saves a draft.
- **Catalog:** H-02, H-05, E-14, E-17

### Background is inert and scroll is contained
- **Rule:** While a modal, drawer or sheet is open, the content behind it is unavailable visually and programmatically; the page does not scroll behind it; content inside scrolls within the surface with overscroll contained, and the action row of a scrolling modal stays put rather than scrolling away with the body.
- **Why:** A page that scrolls behind a sheet breaks the "on top of" model [figure–ground]; a reachable background is a keyboard trap in reverse.
- **Check:** Scroll to the end of the sheet's content and keep scrolling; Tab and screen-read behind the modal; open a long modal and find its buttons. A live build proves this; a design file proves the fixed action row.
- **Severity:** blocking
- **Tells:** page scrolling behind the sheet; a screen reader reading the page under the dialog; a primary action below the fold of a fixed-height modal.
- **Catalog:** H-04

### Sheets and drawers
- **Rule:** A bottom sheet has an explicit close and, where its height varies, visible height controls; a drag handle always has a non-drag alternative. The sheet is padded for the safe area at the bottom. A modal task dims and pushes back the background; a parallel, non-blocking panel has no scrim. A sheet is positioned by its own height (a percentage), not hard-coded pixels.
- **Why:** A sheet that closes only by dragging is a gesture-only control [affordance and signifier]; a scrim says "answer me first" and must not appear on a panel the user can ignore.
- **Check:** Find a close button; close without dragging; check the bottom padding on a notched phone; ask whether the scrim matches the sheet's blocking role. A design file proves close, padding and scrim; a live build proves the drag alternative. Drag physics: see lens 09 · Sheets and drawers move with the hand; safe areas: see lens 12 · Safe areas and system bars.
- **Severity:** blocking for a sheet that closes only by dragging; warning otherwise
- **Tells:** a handle with no close button; a sheet's primary action under the home indicator; a scrim over an inspector panel the user keeps open.
- **Catalog:** H-07

### Click outside dismisses only the lightweight
- **Rule:** A click or tap outside may dismiss a lightweight popover or a non-destructive modal, but never destroys typed input and never confirms a dangerous action.
- **Why:** Outside clicks are the most common slip on a page [slips lapses mistakes]; losing a paragraph to one is data loss.
- **Check:** Type into the dialog, then click outside; the input must survive or the dialog must stay. A live build proves this; static design cannot; mark not-reviewed. Unsaved-work guards: see lens 05 · Slips cannot commit, and work is never lost silently.
- **Severity:** blocking when input is lost or a dangerous action confirms; note otherwise
- **Tells:** a comment draft gone on a backdrop click; a payment sheet that "confirms" when tapped outside.
- **Catalog:** H-06

### Popovers, menus and dropdowns
- **Rule:** A popover, menu or dropdown belongs to its trigger: Escape closes it and returns focus to the trigger, arrows move within it, Tab leaves it. It never covers its own trigger or critical content and repositions at viewport edges. A hover-opened menu tolerates a diagonal path toward its items (a prediction cone) rather than closing when the pointer leaves the trigger's box.
- **Why:** The keyboard model is the promise the role makes [conventions]; a menu that closes on the way to its items punishes the fastest path [Fitts's law].
- **Check:** Open with the keyboard, navigate with arrows, close with Escape, confirm focus returns; open near a viewport edge; move the pointer diagonally into a hover menu. A live build proves this; static design proves placement only; mark the rest not-reviewed. Origin and motion: see lens 09 · Popovers grow from their trigger; modals stay centred.
- **Severity:** blocking for no keyboard path or lost focus on close; warning for placement and hover tolerance
- **Tells:** Escape that closes nothing; focus lost after close; a dropdown clipped by the viewport edge; a hover menu that vanishes on a diagonal.
- **Catalog:** H-11, H-03

### Tooltips carry nothing critical and nothing interactive
- **Rule:** A tooltip is never the only route to critical information — a price, a limitation, a mandatory condition, the primary call to action, a required format — and holds no interactive content unless the pattern is a rich popover built for it. Inline help comes first; a tooltip is the last resort.
- **Why:** A tooltip is absent on touch, invisible to a screenshot and easy to miss [inattentional blindness]; information the decision depends on must be on the page.
- **Check:** List every tooltip's content; anything essential → fail. Tap the trigger on a touch device. A static design proves the content; a live build proves reachability.
- **Severity:** blocking
- **Tells:** the plan's limits only in an "i" tooltip; a link inside a tooltip; a required date format shown only on hover.
- **Catalog:** H-08, H-14

### Hover and focus content is dismissible, hoverable and persistent
- **Rule:** Content that appears on hover or focus can be dismissed without moving the pointer (Escape), can be hovered without disappearing, and stays until dismissed or the trigger loses hover and focus. Tooltips also appear on keyboard focus; touch devices get a clear alternative.
- **Why:** A tooltip that vanishes when the pointer moves toward it cannot be read at magnification [focal vs peripheral vision]; a focus-blind tooltip hides the hint from keyboard users.
- **Check:** Hover the trigger, move onto the content, press Escape; Tab to the trigger; tap on a touch device. A live build proves this; static design cannot; mark not-reviewed. First-tooltip delay: see lens 09 · Popovers grow from their trigger; modals stay centred.
- **Severity:** blocking
- **Tells:** a tooltip that closes as the pointer crosses the gap; help text that only mouse users ever see.
- **Catalog:** H-09, H-10

### Toasts
- **Rule:** A toast carries brief, non-critical feedback and reads as an outcome ("Link copied"); critical or actionable errors go to a persistent inline message, banner or dialog. A toast is announced through a polite live region and never takes focus; its timer pauses when the tab is hidden and on hover or focus. Only one is visible at a time: a new one replaces the old or messages combine by priority.
- **Why:** A toast is peripheral by design [focal vs peripheral vision]; an error the user must act on cannot live somewhere the eye is not.
- **Check:** Classify every message: critical in a toast → fail. Fire five toasts quickly and count what is visible; switch tabs and come back. A design file proves the surface choice; a live build proves the region, focus and timers. Placement, timing floor and copy: see lens 05 · Toast behaviour; timed content floor: see lens 10 · Timed paths and session expiry; enter and exit motion: see lens 09 · Toasts enter and leave from one edge and retarget.
- **Severity:** blocking for a critical or actionable error in an auto-dismissing toast, or a toast that takes focus; warning otherwise
- **Tells:** "Payment failed" as a 3 s toast; five toasts stacked; a toast that keeps counting down while the tab is hidden.
- **Catalog:** F-08, F-10

### Materials and depth
- **Rule:** Where translucent chrome is used, content scrolls underneath it; a heavier material separates structure and a lighter one draws attention to controls; two light translucent surfaces never stack; larger surfaces read thicker (more blur, deeper shadow). Under a reduced-transparency preference the material goes frosty or solid. Text over glass is measured over the busiest region beneath it.
- **Why:** Translucency conveys hierarchy only when it is consistent [depth cues] [figure–ground]; stacked light glass collapses legibility.
- **Check:** Scroll busy content under the toolbar; check text legibility over the busiest region; count stacked translucent layers; enable reduced transparency. A live build proves this; a design file proves the stacking. How glass enters: see lens 09 · Translucent surfaces arrive as material; contrast floor: see lens 03 · Contrast floors, measured on the rendered pair.
- **Severity:** note
- **Tells:** grey text on glass; glass on glass; a translucent bar over a fixed strip of empty space.

## Disclosure, cards, lists and drag and drop

### Disclosure exposes its state and does not hide the essentials
- **Rule:** An accordion or disclosure control is a button that exposes its expanded state, works with Enter and Space, and is associated with the region it reveals. When comparing sections is the task, several can be open at once or the content is shown directly. The primary call to action, the price, a limitation or a mandatory condition never sit inside a collapsed "Learn more".
- **Why:** Collapsed content is out of sight and, for most users, out of existence [inattentional blindness]; a decision made without the hidden condition is a trap.
- **Check:** Inspect the expanded state and region association in the tree; press Enter and Space; try opening two sections when comparison is the task; read every collapsed section for decision-critical content. Code proves semantics; a static design proves what is hidden. Visible cues for hidden content: see lens 01 · Hint at hidden content.
- **Severity:** blocking for essentials inside a collapsed section or a disclosure with no keyboard path; warning otherwise
- **Tells:** a chevron-less accordion; a fee disclosed only under "More details"; a comparison page that closes section A when B opens.
- **Catalog:** H-12, H-13, H-14

### A card is one object, consistently laid out
- **Rule:** A card groups one object or topic and its related actions; it shows the primary identifier first and only what is needed to choose the next action. Fields and actions sit in the same order across repeated cards.
- **Why:** Repeated cards are read by rhyme: the eye learns the skeleton once and then reads only the differences [gestalt grouping] [schemas and scripts].
- **Check:** Count entities per card; find the identifier; overlay three cards and compare the order of fields and actions. A static design proves this. Rhythm of modules: see lens 01 · Rhyme: uniformity for recognition, variety for content.
- **Severity:** warning
- **Tells:** two products in one card; the price above the product name; the "…" menu on the left in one card and the right in the next.
- **Catalog:** I-01, I-04, I-05

### Card click model
- **Rule:** A whole card is clickable only when it has one primary destination; nested actions (a menu, a favourite, a checkbox) have their own hit areas and never trigger the card. No button inside a button or link inside a link to make a card clickable; use a valid structure or a stretched link. When the whole row highlights on hover, clicking anywhere in the highlight acts.
- **Why:** One click must map to one command [mapping]; a nested interactive inside an interactive is undefined for the keyboard and the screen reader [conventions].
- **Check:** Click the nested action; the card must not open. Inspect the nesting in code. Hover the row, then click where it highlights. A live build proves the behaviour; code proves the structure. One-command floor: see lens 10 · One click, one command.
- **Severity:** blocking
- **Tells:** the favourite star opening the detail page; an anchor wrapping a button; a row that highlights fully but acts only on its title.
- **Catalog:** I-02, I-03, A-08, A-09, A-10

### Truncation and overflow in cards and rows
- **Rule:** An ellipsis never hides the only distinguishing information between two items; the full value is reachable by wrapping, the detail view or an accessible reveal. An overflow menu holds infrequent secondary commands; the primary, frequent command is never inside it.
- **Why:** Two items that differ only in the clipped part are the same item to the user [recognition over recall]; a primary command behind "…" is a hidden primary.
- **Check:** Find two items that differ only in the truncated part; open every "…" menu and look for the primary action. A static design with realistic long strings proves this. Truncation rules for text: see lens 02 · Wrap deliberately; truncate without losing content.
- **Severity:** blocking for indistinguishable items or a hidden primary; warning otherwise
- **Tells:** "Invoice 2026-09-… " three times in a row; "Open" as the first item of an overflow menu.
- **Catalog:** I-06, I-07

### Empty by cause, action to match
- **Rule:** A list's empty states follow the five kinds of nothing (see lens 05 · Five kinds of nothing, lens 05 · Empty state shape) — first use, no results, cleared by the user, unavailable or locked, load failure — each with its own shape and action. One generic illustration for all of them is wrong for most of them.
- **Why:** Each cause calls for a different next step [mental models]; a "create" prompt under a failed search sends the searcher the wrong way.
- **Check:** Trigger each state and name its cause; check that the action matches lens 05 · Five kinds of nothing. A design file proves which variants exist.
- **Severity:** warning
- **Tells:** the same rocket illustration for "no results" and "no projects"; a "cleared" list that celebrates; a locked feature with no unlock path.
- **Catalog:** I-17

### Drop zones are forgiving and the drag ghost is inert
- **Rule:** A drop zone is large enough to hit without pixel aiming; auto-scroll at the container edge is controllable, not a runaway; during a drag, text selection is disabled and the dragged ghost is inert so it neither receives hover nor intercepts the drop. Cancelling a drag restores the object and its state without data loss.
- **Why:** The drop is the moment the item can be lost [slips lapses mistakes]; a ghost that catches its own drop and a runaway scroll are the two ways it happens.
- **Check:** Measure drop targets; drag to the container edge and watch the scroll speed; drag over text and look for selection; press Escape mid-drag. A live build or prototype proves this; static design proves target size only. Signifier, hint and the eight states: see lens 09 · Gestures are invisible: hint, fallback and every drag state; non-drag alternative: see lens 10 · Gestures have a single-pointer alternative.
- **Severity:** blocking for a cancel that loses data; warning otherwise
- **Tells:** a 4 px gap as the only drop target between rows; a list that scrolls to the bottom the instant the ghost touches the edge; text selecting during a drag.
- **Catalog:** J-09, J-10

## Tables, charts and bulk selection

### Table for comparing data, with real structure
- **Rule:** A table compares data across rows and columns; it is never page layout. A data table has a real header structure, a caption or accessible name, and header-to-cell associations. Sortable headers show that they sort, which column is active and in which direction, and repeated activation changes predictably.
- **Why:** Screen readers navigate a table by its headers [conventions]; a layout table announces nonsense and a sort with no indicator is a hidden state [change blindness].
- **Check:** Ask whether the table holds data or layout; inspect header cells, scope and caption in code; click a header three times and watch the indicator. Code proves structure; a static design proves the sort indicator.
- **Severity:** blocking for a data table without header structure or an accessible name; warning for sort indication
- **Tells:** a settings page built as a table; a sortable column with no arrow; a third click that does nothing.
- **Catalog:** I-11, I-12, I-13

### Numbers align and formats agree
- **Rule:** Numeric columns align to the trailing edge for comparison, share one unit and one format, and mark negative or anomalous values with more than colour.
- **Why:** Aligned digits let magnitude be compared by column width alone [ensemble perception]; a red-only negative is invisible to a colour-blind reader [colour vision deficiency].
- **Check:** Scan a numeric column for a ragged edge, mixed units or mixed decimals; greyscale the negatives. A static design proves this. Tabular figures: see lens 02 · Tabular numbers on anything that changes; formats: see lens 07.
- **Severity:** warning
- **Tells:** left-aligned totals; "12 000" above "12,000.00"; a loss shown red with no sign.
- **Catalog:** I-14

### Horizontal scroll and responsive tables keep every control
- **Rule:** Horizontal scrolling never cuts off controls; frozen columns and headers never cover focus rings or enlarged text. On mobile a table becomes cards only if labels, comparison order and every action survive the change.
- **Why:** A control past the scroll edge with no cue does not exist for the user [affordance and signifier]; cards that drop a column silently drop a comparison.
- **Check:** Scroll horizontally and zoom to 200 %; Tab through the frozen region. Compare the desktop table and the mobile cards column by column. A design file proves the mobile mapping; a live build proves the scroll and focus. Focus obscured: see lens 10 · Focus is never obscured.
- **Severity:** blocking for cut-off controls or a covered focus ring; note for the card mapping
- **Tells:** the row's "Edit" only reachable by scrolling right with no cue; a frozen column painting over the ring; mobile cards missing the status column.
- **Catalog:** I-15, I-16

### Tables and charts expose values
- **Rule:** Tables support scanning: alignment, consistent formats, predictable column types. Charts expose exact values, not only shapes: a column chart lets the user hover, drag or arrow across columns with pop-up values on desktop and slide a finger across them on mobile; every plotted value can be read.
- **Why:** If the exact value cannot be retrieved the chart is decoration [recognition over recall]; a shape shows a trend, a number supports a decision.
- **Check:** Read every plotted value from the chart; check that numeric columns share one format. A live build or prototype proves the hover and slide; a static design proves labels only; mark the interaction not-reviewed. Touch side of the same rule: see lens 12 · Touch gets a hover equivalent.
- **Severity:** blocking for chart values that cannot be read; warning for table scanning
- **Tells:** bars with no tooltip or labels; a chart shipped as an image; mixed units in one column.

### Selection mode is distinct and its scope is stated
- **Rule:** Multi-select clearly separates entering selection mode from opening an item and shows the count selected. "Select all" states its scope: the visible 20, this page, or all 12 430. A destructive bulk action confirms its scope, and its result reports partial failures with a recovery path rather than a generic Done.
- **Why:** A select-all that silently means "everything" is a data-loss slip at scale [slips lapses mistakes]; a "Done" over three failures hides work the user must redo [feedback loop].
- **Check:** Enter selection mode and look for the count; read the label after select all; run a bulk delete with one failure and read the result. A design file proves count, scope label and the result state; a live build proves the failure report. Result reporting: see lens 05 · Progress is honest.
- **Severity:** blocking
- **Tells:** "Select all" with no number; a bulk delete confirming "these items"; "Deleted" after two of twelve failed.
- **Catalog:** I-08, I-09, I-10
