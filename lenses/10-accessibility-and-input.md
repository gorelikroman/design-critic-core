# 10 — Accessibility and input

Checks the floors no project decision can lower: keyboard and focus, pointer targets and gestures, non-colour cues, names and semantics, structure and zoom, timing, screen-reader output. Order: what the input can prove → keyboard → targets → cues and names → structure, timing and announcements.
Pre-tests: walk the primary flow with the keyboard only; greyscale the screenshot; measure the smallest target; zoom to 200 %.
Every minimum here is `blocking`; numbers in this lens are floors, not tells. Contrast ratios are measured in lens 03 · Contrast floors, measured on the rendered pair; form design (label position, autocomplete, keyboards, paste, submit, checkboxes and switches) is lens 08; motion craft, reduced-motion variants, flashing and autoplay are lens 09; overlay anatomy is lens 11; mobile chrome and hover-on-touch are lens 12.

## Evidence, keyboard and focus

### Accessibility evidence by input type
- **Rule:** Judge each floor only from an input that can prove it. A design file or screenshot proves target size, contrast pairs, colour-only cues, label presence, text size and declared states. Code proves element types, attributes, handlers and declared names. Only a rendered, running build proves focus order, focus visibility, focus containment and return, live-region output, zoom reflow, forced-colours rendering and reduced-motion behaviour. Anything the input cannot prove is `not-reviewed`, never `fail` or `pass`.
- **Why:** A floor is a property of the rendered product; inferring it from a static artifact produces confident wrong verdicts in both directions [predictive brain].
- **Check:** For every entry below, state the input used. Static design → size, contrast, cues, labels. Code → semantics, attributes, handlers. Live → everything, including the screen-reader phrase actually heard.
- **Severity:** note
- **Tells:** "focus order OK" on a design-file review; "contrast passes" without a measured pair; the a11y section skipped because "the design system handles it".

### Every function has a keyboard path
- **Rule:** Everything a pointer can do, the keyboard can do, with no trap: Tab moves between widgets, arrows move within composite widgets (menus, tab lists, radio groups, grids), Enter and Space activate, Escape closes whatever opened last. Composite widgets follow their published keyboard pattern.
- **Why:** Anything reachable by mouse but not keyboard blocks a whole class of users, and keyboard reach is the substrate every assistive technology drives [conventions].
- **Check:** Complete the primary flow without a mouse. Press Escape in nested overlays; Tab out of every widget; arrow through every menu, tab list and combobox. Code proves handlers exist; only a live build proves the path. Static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** a click handler on a div with no key handler; a custom tab list where Tab walks every tab; a dropdown that opens only on click; Escape that closes nothing.
- **Catalog:** K-01, K-06, C-12, C-24, D-25, H-03, H-12

### Tab order follows meaning
- **Rule:** Focus order follows the meaningful visual order; the document order is fixed at the source, never patched with positive tab indices; composites use a single tab stop with roving focus inside.
- **Why:** A keyboard user builds a map of the screen from the order stops arrive [mental models]; CSS reordering that the focus order ignores breaks the map.
- **Check:** Tab through and number the stops on a screenshot; compare with the reading order. In code, search for `tabindex` greater than zero. Static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** focus jumping from header to footer to body; a visually first field reached last; `tabindex="5"`.
- **Catalog:** K-04, K-05

### Visible focus indicator
- **Rule:** Every keyboard stop has a visible indicator with at least 3:1 contrast against what it crosses, never clipped by overflow or overlays. Style the focus-visible state, not bare focus, so pointer clicks do not paint a ring; a custom ring is at least a 2 px solid perimeter verified on every surface it lands on; compound controls highlight the group when focus is within. Never remove the outline without a verified replacement; system focus colours survive forced-colours mode.
- **Why:** Sighted keyboard users have no other way to know where they are; a missing ring is a task blocker, not a style choice [focal vs peripheral vision].
- **Check:** Tab through the whole flow; every stop must be visibly indicated, on dark cards and over images included. Click with a mouse: no ring. In code, grep for `outline: none` / `outline-none` and confirm each has a replacement. Static design proves the ring's design only; the live build proves it appears. Ring contrast measurement: see lens 03 · Contrast floors, measured on the rendered pair.
- **Severity:** blocking
- **Tells:** global outline removal; a ring the same colour as the button fill; a ring that vanishes on the dark sidebar; a ring on every mouse click.
- **Catalog:** K-02, L-15

### Focus is never obscured
- **Rule:** Sticky headers, footers, overlays and frozen table columns never cover the focused element; the screen scrolls so the stop is fully visible. The same holds for the next required step and its error: nothing sits under the keyboard, a sticky CTA or a status message.
- **Why:** A focused control the user cannot see is a control the user cannot operate [focal vs peripheral vision].
- **Check:** Tab to rows under a sticky footer and to cells beside a frozen column at 200 % zoom. Open the keyboard over the last field of a form. Static design cannot prove this; mark not-reviewed. Clipping of the primary action itself: see lens 12 · A critical action is never clipped.
- **Severity:** blocking
- **Tells:** a focus ring half-hidden under a sticky bar; a frozen column painting over the ring; an error message under the keyboard.
- **Catalog:** K-03, I-15, D-35, F-11, B-18

### Focus moves in, stays in, and returns
- **Rule:** When a modal or sheet opens, focus moves inside it and the background becomes inert (visually and programmatically); Tab and Shift+Tab stay inside; Escape closes it where closing is safe; on close, focus returns to the trigger or the logical next point. Focus never moves to a toast.
- **Why:** Without containment a keyboard user tabs into a page they cannot see; without return they land at the top of the document and rebuild their place [working memory].
- **Check:** Open every overlay from the keyboard, Tab past its last control, press Escape, confirm where focus lands. Static design cannot prove this; mark not-reviewed. Overlay anatomy (title, close, initial focus by task): see lens 11 · Modals.
- **Severity:** blocking
- **Tells:** Tab escaping behind a modal; focus lost after a dialog closes; focus jumping to a toast.
- **Catalog:** H-03, H-04, K-11

### Route changes move focus and update the title
- **Rule:** After client-side navigation, focus moves to the new heading or main landmark and the document title changes to describe the new context, most-specific part first.
- **Why:** Without a full page load nothing tells a screen reader that anything happened; the user hears silence and keeps reading the old page [change blindness].
- **Check:** Navigate client-side with a screen reader running; note what is announced and where focus sits; read the tab title. Static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** a single tab title for the whole app; focus left on the link that was clicked; the new page announced as nothing.
- **Catalog:** K-10

### Skip link to the main landmark
- **Rule:** When repeated chrome precedes the content, the first Tab stop is a link that jumps to the main landmark; it may be visually hidden until focused.
- **Why:** A keyboard user otherwise tabs through the same navigation on every page [habituation].
- **Check:** Load the page and press Tab once; a skip link must appear and work. Code proves it exists; a live build proves it is first. Static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** forty stops before the first heading; a skip link that scrolls but does not move focus.
- **Catalog:** K-13

### Hidden content is neither focusable nor announced
- **Rule:** Collapsed sections, closed menus, off-screen panels and elements at zero opacity are removed from the focus order and the accessibility tree until shown. Nothing invisible remains a focusable trap.
- **Why:** A focus stop on nothing visible is a dead moment the user cannot explain [inattentional blindness]; announced hidden text lies about what is on screen.
- **Check:** Tab into collapsed sections and closed drawers; nothing inside should receive focus. In code, look for `opacity: 0` and off-screen positioning without `inert`, `hidden` or `aria-hidden`. Static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** Tab disappearing for three presses; a screen reader reading the closed menu; a transparent icon still tabbable.
- **Catalog:** K-16, A-18

### Shortcuts follow platform conventions
- **Rule:** Keyboard shortcuts follow the platform's conventions, show the platform's modifier symbols, work on non-QWERTY layouts, and any custom single-key shortcut can be disabled or remapped.
- **Why:** Speech-input and switch users can trigger single-key shortcuts by accident; a shortcut that conflicts with the platform's is learned wrong [conventions].
- **Check:** List the shortcuts; find the setting that disables or remaps single-key ones; switch to a non-QWERTY layout. Static design cannot prove this; mark not-reviewed.
- **Severity:** warning
- **Tells:** a bare "j" and "k" with no off switch; ⌘ shown to a Windows user.
- **Catalog:** K-12

## Targets, pointer and gestures

### Target size
- **Rule:** Floors: 24 × 24 CSS px for any pointer target (WCAG 2.2 AA, with its spacing, inline-text and essential exceptions). Recommended: 44 × 44 CSS px on touch, 40 × 40 px on desktop, 32 × 32 px for a mouse-only control, 24 px tall for a text link. Platforms: 44 pt on iOS, 48 dp on Android, even when the glyph is smaller; extend the hit box with an invisible layer on the wrapping control. Frequent actions get larger targets than rare ones.
- **Why:** Pointing time grows with log(distance / width) [Fitts's law]; below the floor a tap misses and the task fails, not the finger.
- **Check:** Measure the interactive box, not the glyph, of the smallest control: icon buttons, close buttons, checkboxes, chips, table row actions. Below 24 px without an exception → fail; below 44 px on touch or 40 px on desktop → warning. A design file or screenshot with a scale can prove size; only a live build proves the hit box matches the drawing.
- **Severity:** blocking below the 24 px floor; warning below the platform recommendation
- **Tells:** a 16 px icon button with no padding; a "×" in a corner that needs a precise tap; a 20 px icon button on a phone.
- **Catalog:** A-03, A-04, A-05

### Distance and edges
- **Rule:** Sequential related targets sit close (a just-filled field and its Next; Cancel and Confirm inside ~200 px); the primary action is the largest interactive element in its area; persistent critical actions go to screen edges and corners, which have infinite effective width; the most-used action is one click away and anything done more than once a day has a shortcut.
- **Why:** Pointing cost is distance over width [Fitts's law]; a large target far away can cost more than a small one near the last fixation.
- **Check:** Measure the distance from the last field to the primary action and the gap between paired actions; count clicks to the most frequent action. A static design proves distances. Thumb zones on phones: see lens 12 · Thumb reach.
- **Severity:** warning
- **Tells:** "Continue" far from the last field; Cancel and Confirm on opposite sides of a wide dialog; two clicks plus a confirm for the product's primary action.
- **Catalog:** A-02, B-17

### Label and control share one target
- **Rule:** The label of a checkbox, radio or switch is part of its hit area, with no dead zone between box and text; a whole row toggles the option only when the row reads as one option and carries no second primary action.
- **Why:** The label is the largest thing in the group and where the eye lands; a gap between box and text collects failed taps [Fitts's law].
- **Check:** Click the label text and the gap between box and text; the control must toggle. Count primary actions in a row that toggles on tap; more than one → fail. Code proves the association (`for` / wrapping); a live build proves the gap. Group labels and legends: see lens 08 · Options and groups are labelled; the whole label is the target.
- **Severity:** blocking
- **Tells:** a checkbox that toggles only on the box; a card that both opens and selects on one tap.
- **Catalog:** A-07, A-08, C-04

### Hit areas never overlap and decorative layers never eat clicks
- **Rule:** Two commands never share pointer territory; extended hit boxes stop before the neighbour's. Decorative overlays (glows, scrims, gradients) pass pointer events through and are hidden from assistive technology. Where no density system exists, adjacent bordered controls get ~12 px and borderless icon or text buttons ~24 px of clearance.
- **Why:** An overlap makes the fired command depend on a pixel [Fitts's law]; a layer on top makes a live-looking control dead.
- **Check:** Overlay the expanded hit boxes; any overlap between two commands → fail. Click every corner of a control and click through any glow. Code can prove `pointer-events`; only a live build proves the overlap. Visual affordance of controls: see lens 06 · Affordances are perceived, not physical.
- **Severity:** blocking when two commands overlap; warning for clearance and decorative layers
- **Tells:** three icon buttons packed at 4 px; a card whose hover glow blocks its own button; a "×" whose hit box covers the neighbouring tab.
- **Catalog:** A-02, A-06, A-19, A-20

### One click, one command
- **Rule:** A single click or tap fires one unambiguous command; open, select and toggle are separate targets. An irreversible action never fires on pointer-down; the user can drag off and release to cancel. No click fires once movement has clearly become a scroll or a drag.
- **Why:** A control that does two things on one press cannot be predicted [mapping]; firing on pointer-down removes the last chance to abort [slips lapses mistakes].
- **Check:** List the commands one click fires on cards, rows and chips; more than one → fail. Press, drag off, release on a destructive control: nothing fires. Touch-scroll starting on a button: no click. Code proves the event used; a live build proves behaviour. Card-level click model: see lens 11 · Card click model.
- **Severity:** blocking
- **Tells:** a row that opens details and selects on the same tap; delete on `pointerdown`; a list that opens an item when the finger scrolls.
- **Catalog:** A-01, A-09, A-17, J-16

### Gestures have a single-pointer alternative
- **Rule:** Multi-point or path-based gestures (pinch, rotate, swipe, drag, path drawing) and motion or tilt controls have a single-pointer, tap-or-click alternative and a keyboard path, unless the gesture is essential. Every drag has a non-drag route (move buttons, menu, position entry, tap-to-place); every hidden swipe action and long-press action is reachable another visible way; motion controls can be turned off. System edge gestures keep priority over the app's; pull-to-refresh supplements explicit refresh and does not fire inside nested scrolling.
- **Why:** A gesture is invisible and needs two hands, fine motor control or a screen that moves; the alternative is how everyone else, and the keyboard, gets there [affordance and signifier].
- **Check:** For each gesture, name and perform the tap and keyboard equivalent; reorder a list without dragging; find every swipe action without swiping; swipe from the screen edge. Static design can list gestures but cannot prove alternatives; mark not-reviewed unless the alternative is visible in the design. Drag hints and the eight drag states: see lens 09 · Gestures are invisible: hint, fallback and every drag state.
- **Severity:** blocking
- **Tells:** reorder by drag only; swipe-to-archive with no menu; pinch as the only zoom; a shake gesture with no setting.
- **Catalog:** J-01, J-02, J-03, J-04, J-11, J-12, J-13, J-14

### Swipe never deletes irreversibly
- **Rule:** One accidental swipe never destroys data: swipe-to-delete ends in undo or confirmation, never immediate permanent removal.
- **Why:** A swipe is a slip waiting to happen, and slips need a second defence [slips lapses mistakes] [layered defences].
- **Check:** Swipe-delete an item and look for undo or a confirmation. A live build or prototype proves it; static design cannot; mark not-reviewed. Safeguard design: see lens 05 · Destructive safeguard.
- **Severity:** blocking
- **Tells:** an item gone on release with no toast; a red swipe that skips the confirm the button path has.
- **Catalog:** J-05

### Cursor matches the operation
- **Rule:** On pointer platforms the cursor reflects the operation: text over editable text, grab and grabbing over draggables, resize on handles, not-allowed only when the control is genuinely unavailable. A pointer cursor is the web convention for links and for non-standard clickable containers; on native buttons it is a project convention, never a failure.
- **Why:** The cursor is the pointer's affordance [affordance and signifier]; a wrong one promises an operation the element does not have.
- **Check:** Hover each operation and note the cursor; flag inconsistency within the product, not a default cursor on a native button. Only a live build proves this; mark not-reviewed otherwise.
- **Severity:** note
- **Tells:** a grab cursor on a static card; text cursor over a button; not-allowed on a button that is merely loading.
- **Catalog:** A-12, A-13

## Cues, names and semantics

### Non-colour cues and reduced motion
- **Rule:** Error, success, warning, selected, checked, required, interactive, and every chart value carry a second cue alongside colour: icon, text, underline, shape, border, position, pattern. Icons beside status text may be decorative; icons that stand alone need a label. Chart palettes are safe for colour-vision deficiency and series differ by more than hue. Motion is a third channel that can also be lost: under a reduced-motion preference the interface still works and every state a motion communicated stays perceivable through a static cue.
- **Why:** About one in twelve men reads red and green as one channel [colour vision deficiency]; greyscale screenshots, sunlight and forced colours drop the hue channel, and lightness carries the form anyway [luminance carries form]; reduced-motion users lose the motion channel by choice or necessity [motion perception].
- **Check:** Greyscale the screenshot: status, selection, links, required marks and chart series must still read; simulate deuteranopia on charts. Enable reduced motion and confirm nothing depends on movement. A static design proves the colour side fully; only a live build proves the motion side. What the reduced variant keeps: see lens 09 · Reduced motion means gentler, not none and lens 09 · Motion is never the only channel; palette side: see lens 03 · Salience survives grayscale; states on a phone: see lens 05 · Selected and disabled survive greyscale.
- **Severity:** blocking
- **Tells:** a red border as the only error; green and red dots with no label; the active nav distinguishable only by hue; a five-series chart in five hues of one lightness; a "saved" state signalled only by a pulse.
- **Catalog:** L-03, A-11, C-16, C-20, I-14, E-03, N-02

### Forced colours and high contrast keep the states
- **Rule:** Under a forced-colours or increased-contrast mode, focus rings, checkboxes, switches, icons, borders and selected states stay visible; nothing that carries state is drawn only with a background colour that the mode removes.
- **Why:** These modes replace author colours with system colours; a state painted as a background fill disappears with it [luminance carries form].
- **Check:** Enable forced colours (Windows) or increased contrast (macOS, iOS) and walk the flow; look for vanished checkboxes, rings and icons. Only a live build proves this; mark not-reviewed otherwise.
- **Severity:** blocking
- **Tells:** a toggle whose knob disappears; a selected tab with no underline once the tint is gone; a custom checkbox that becomes an empty square.
- **Catalog:** L-15

### Native elements first, ARIA last
- **Rule:** A real button for actions, a real link for navigation, a real label, a real table; never a clickable div or span. A role is a promise of the full keyboard model and is added only for what the platform cannot supply; native semantics are never changed without need, hidden or presentational roles never sit on focusable elements. No ARIA beats bad ARIA.
- **Why:** Native elements ship focus, keyboard activation, name, role and form behaviour for free; a wrong role misleads a screen reader worse than none [conventions].
- **Check:** In code, search for click handlers on non-interactive elements and for custom roles; in the accessibility tree confirm each control has a native role. Static design cannot prove this; mark not-reviewed. Button-versus-link choice: see lens 11 · Button for actions, link for locations.
- **Severity:** blocking
- **Tells:** `div` menus; a "button" that navigates; `aria-label` on a plain span; redundant `role="button"` on a button.
- **Catalog:** K-06, A-14

### Every control exposes name, role and state
- **Rule:** Each interactive element has an accessible name that includes its visible text, a role, and a value or state that updates when it changes (pressed, expanded, checked, selected, "in favourites"). Names exist even where the visual omits a label. Verify in the accessibility tree, not the DOM.
- **Why:** Name, role and state are the entire interface for a screen reader and the vocabulary for voice control; a name that differs from the visible label makes "click Save" fail [recognition over recall].
- **Check:** Read the accessibility tree for every control; toggle each stateful control and re-read its name and state; compare `aria-label` with visible text. Code proves declared names; only a live tree proves the computed name. Icon-only buttons: see lens 11 · Icon-only controls carry a name.
- **Severity:** blocking
- **Tells:** a control announced as "button"; a toggle whose state never changes in the tree; a visible "Save changes" named "submit-btn".
- **Catalog:** K-07, B-03, K-09, A-18

### Every field has a programmatic label
- **Rule:** Each input has a persistent label associated in code, so clicking the label focuses the field and assistive technology announces it; a placeholder is never the label. Required and optional are marked programmatically as well as visually.
- **Why:** The label is what is announced and what enlarges the target; a placeholder vanishes on the first keystroke and usually fails contrast [recognition over recall].
- **Check:** Click each label; the field must focus. In the tree, each input has a name. Static design proves label presence, not association. Label position, hints, autocomplete and keyboard type: see lens 08 · Visible label: floating or above the field and lens 08 · Keyboard and autocomplete match the field.
- **Severity:** blocking
- **Tells:** placeholder-only forms; a label that does not focus its field; an asterisk with no programmatic required state.
- **Catalog:** D-02, D-05, C-03

### Images and icons: alt by purpose
- **Rule:** Every image has an alt attribute: empty for decorative, the meaning for informative, the action for functional, the exact text for images of text, a summary plus nearby data for charts. Decorative icons, including icons beside text labels, are hidden from assistive technology. Important text never lives in a bitmap.
- **Why:** A missing alt reads the filename; a decorative icon announced twice doubles every label; text in an image cannot be enlarged, translated or read aloud [recognition over recall].
- **Check:** Audit every image and icon in the tree; find images containing text. Code proves attributes; a design file can list which images are decorative.
- **Severity:** blocking
- **Tells:** `alt="image"`; "magnifying glass search"; a pricing table shipped as a PNG.
- **Catalog:** K-08, L-10

### Media has a text equivalent and keyboard controls
- **Rule:** Content video has captions; content audio has a transcript; meaningful media has a description; player controls are keyboard-operable; purely decorative loops are hidden from assistive technology; nothing autoplays with sound.
- **Why:** Media is the one content type that has no fallback unless one is authored [conventions].
- **Check:** For every video or audio, find the caption, transcript or description; Tab into the player. Static design can note the intent; a live build proves it. Pause controls for loops longer than 5 s: see lens 09 · No autoplay without a pause; no critical information in timed UI.
- **Severity:** blocking
- **Tells:** a product tour video with no captions; a background loop that is read out; audio that starts on load.

### Page language is declared
- **Rule:** The document declares its language and any fragment in another language declares its own.
- **Why:** Screen readers choose the voice and hyphenation from it; a wrong language is read as nonsense [conventions].
- **Check:** Inspect the root language attribute and fragments in other languages. Code proves it; static design cannot; mark not-reviewed.
- **Severity:** blocking
- **Tells:** a localised product with the template's default language; a quoted foreign phrase read in the wrong voice.
- **Catalog:** M-07

## Structure, zoom, timing and announcements

### Structure is navigation; zoom and reflow
- **Rule:** One main landmark; repeated landmarks (two navs) carry distinguishing labels; headings describe their sections in a coherent outline — one H1, no skipped levels, chosen by document structure, never by default size; the page title is most-specific-first; anchored headings offset under sticky chrome so a deep link is not hidden. The page works at 200 % zoom and reflows at 320 CSS px width with vertical scrolling only; two-dimensional content such as tables scrolls inside its own container. The viewport never disables or caps zoom.
- **Why:** Screen-reader users navigate by landmarks, headings and links; zoom users need reflow, not a horizontal scroll; the outline is the page's table of contents [chunking] [recognition over recall].
- **Check:** Open the headings and landmarks list in a screen reader; zoom to 200 % on a 1280 px window and resize to 320 px: no horizontal scroll, no lost content or function. Deep-link to a heading under a sticky header. In code, grep the viewport meta for `user-scalable=no` or `maximum-scale=1`. Static design proves the heading hierarchy visually only. A heading-level skip with no navigation impact is reported as a warning, not a blocker. Input-side zoom rule: see lens 08 · Never block paste, typing or zoom.
- **Severity:** blocking for clipped or unreachable content at 320 px / 200 % and for a capped zoom; warning for outline defects
- **Tells:** horizontal scroll at 320 px; a heading tag picked for its size; three unlabelled navs; a heading anchored under the sticky header; a viewport that caps zoom.
- **Catalog:** K-14, L-04

### Large text and spacing overrides do not clip
- **Rule:** Typography survives a larger base font, the platform's largest accessibility text size, and user overrides of line height, letter spacing and paragraph spacing: nothing clips, overlaps or hides a command. Text containers have no fixed height.
- **Why:** Fixed heights and pixel-locked layouts break the moment a reader enlarges text, and enlarged text is the most common accommodation there is [critical print size].
- **Check:** Raise the browser base font size; on mobile set the largest accessibility text size; apply a text-spacing override. Look for clipped or overlapping text and vanished buttons. In code, inspect fixed heights on text containers. A design file can show fixed heights; only a render proves the overflow. Typographic units and scale: see lens 02 · Respect the reader's settings.
- **Severity:** blocking
- **Tells:** fixed-height cards; a button label cut at the largest text size; a table cell that hides its second line.
- **Catalog:** L-05, L-06, L-07

### Timed paths and session expiry
- **Rule:** No action, information or undo lives only in something that disappears on a timer; a timed element that must exist has a 5 s floor and pauses on hover and focus. Sessions warn before expiry, allow extension, and preserve entered data through re-authentication. Content that moves or updates on its own for more than 5 s is pausable, and nothing flashes more than three times per second.
- **Why:** A vanished undo link is data loss on a schedule and a silent expiry throws away work [loss aversion]; flashing above the rate is a seizure risk, a safety floor nothing overrides.
- **Check:** Find every timer and auto-dismissing surface; test whether anything essential disappears; let a session expire mid-form and return. A live build proves it; static design shows only that the toast carries an action; mark the timer not-reviewed. Toast placement and copy: see lens 05 · Toast behaviour; autoplay controls and flash rate: see lens 09 · No autoplay without a pause; no critical information in timed UI and lens 09 · No flashing above three per second.
- **Severity:** blocking
- **Tells:** "Undo" only inside a 3 s toast; error toasts that self-dismiss; a form lost at session timeout; a "live" dot blinking five times a second.
- **Catalog:** N-12, F-09, N-04, N-03

### Status changes are announced without moving focus
- **Rule:** Dynamic statuses — saved, result count, loading, loaded, toasts, inline validation — are announced through a polite live region that exists from page load, without moving focus. Form-level failures not tied to a field use an assertive alert region. Loading never looks frozen: the busy region is marked and named, and updates are announced without excessive repetition.
- **Why:** A screen-reader user hears nothing that changes outside the current focus [change blindness]; a region added at the moment of the update is missed by the reader that watches for changes.
- **Check:** Trigger a save, a search and a load with a screen reader running; note what is announced and whether focus moved. In code, confirm the region is rendered before the update. Only a live build proves this; mark not-reviewed otherwise.
- **Severity:** blocking
- **Tells:** a toast that is silent to a screen reader; "Saved" as an assertive alert; a spinner with no name; focus jumping to the status.
- **Catalog:** K-11, F-04

### Errors are associated and announced
- **Rule:** A failing field is marked invalid in code, linked to its inline error so the error is read with the field, and focus moves to the first invalid field on submit; the error sits beside the field with text and an icon, never a red border alone.
- **Why:** An error that is only visual, or only announced somewhere else, is an error the user cannot find [gestalt grouping].
- **Check:** Submit invalid data with a screen reader running; note where focus lands and what is read with the field. Code proves `aria-invalid` and `aria-describedby`; a live build proves the announcement. Static design proves placement and colour-only cues. Copy, timing and the value surviving: see lens 05 · Validation keeps the value and speaks in text and lens 05 · Error visibility on submit.
- **Severity:** blocking
- **Tells:** a red border with no text; an error summary the field does not reference; focus staying on the submit button.
- **Catalog:** E-03, E-04

### Focus and announcement after adding or removing items
- **Rule:** When an item is added, removed or moved (a row, a tag, a list entry), focus lands at a logical point — the new item, the next sibling, or the control that acted — and the change is announced; the list does not scroll or lose focus unexpectedly.
- **Why:** Focus dropped to the document start after a delete resets the user's place [working memory]; an unannounced removal is a silent change [change blindness].
- **Check:** Add and remove items with a screen reader on; note where focus goes and what is said. Only a live build proves this; mark not-reviewed otherwise.
- **Severity:** blocking
- **Tells:** focus jumping to the top of the page after "Remove"; a deleted row that is never announced; a list that scrolls to the top on add.
- **Catalog:** K-17, I-18

### Announcements are not redundant
- **Rule:** The phrase a screen reader speaks for a control says the name, role and state once; the visible label, an aria-label and a title do not repeat each other, and an icon's text does not double the label.
- **Why:** "Search, search, button, search" costs a second per control and buries the state [cognitive load].
- **Check:** Listen to the full phrase for each control; count repeated words. Only a live build proves this; mark not-reviewed otherwise.
- **Severity:** warning
- **Tells:** a label and a title with the same text; an icon with alt text beside its own label; "button button".
- **Catalog:** K-15

### Verify in the accessibility tree and with real assistive technology
- **Rule:** Names, roles and states are confirmed in the accessibility tree, not inferred from the DOM; the flow is tested with at least one real screen reader and, where speech input is plausible, voice control; automated checkers are a pre-test, not evidence.
- **Why:** Automated tools catch a minority of failures and none of the phrasing problems; the tree is what assistive technology actually receives [conventions].
- **Check:** The review states which assistive technology was used on which screens; findings on announced phrases cite what was heard. Anything not tested is `not-reviewed`.
- **Severity:** warning
- **Tells:** "passes the automated checker" as the whole a11y evidence; names verified by reading `aria-label` in source; no screen reader named in the report.
- **Catalog:** K-18

## Reference tables

Floors (blocking) and recommendations (warning) cited across this lens. Contrast ratios are listed for completeness; they are measured under lens 03.

| Measure | Floor | Recommendation |
|---|---|---|
| Pointer target, any platform | 24 × 24 CSS px (spacing, inline, essential exceptions) | 44 × 44 CSS px touch · 40 × 40 px desktop · 32 × 32 px mouse-only · 24 px tall text link |
| Touch target, iOS | — | 44 × 44 pt |
| Touch target, Android | — | 48 × 48 dp |
| Clearance between controls (no density system) | — | ~12 px bordered · ~24 px borderless |
| Related sequential actions | — | ≤ ~200 px apart |
| Normal text contrast | 4.5:1 | — |
| Large text contrast (≈ 24 px regular / 19 px bold) | 3:1 | — |
| Non-text contrast (borders, icons, states, focus ring) | 3:1 | — |
| Focus ring perimeter (custom) | — | ≥ 2 px solid |
| Zoom | works at 200 % · zoom never capped | — |
| Reflow | 320 CSS px, vertical scroll only | — |
| Flashing | ≤ 3 per second | — |
| Auto-moving content | pausable when > 5 s | — |
| Timed element holding an action | never auto-dismissed; otherwise ≥ 5 s, paused on hover/focus | — |
