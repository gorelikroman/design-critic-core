# UX/UI Rules Catalog — compressed digest (266 rules)

Design-system-agnostic. Rule IDs are the original Notion IDs; cite them in findings so they trace back to the catalog.
Levels: **REQ** = REQUIRED, **REC** = RECOMMENDED, **CTX** = CONTEXT-DEPENDENT. Platform as in the source.
"Check" = what to observe or measure in a Figma file, a running build, or code.

## A. Interaction and Hit Areas (20)

Evidence: WCAG 2.2 §§2.1, 2.4, 2.5; Apple HIG Accessibility; Android Accessibility; WAI-ARIA APG; Fluent 2.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| A-01 | REQ | All | Every interactive element has one unambiguous command; one click must not mean open + select + toggle at once. | List the commands a single click/tap fires; more than one = fail. |
| A-02 | REC | All | Visible area and actual hit area represent the same action; invisible clickable regions must not overlap neighbours. | Compare drawn bounds with hit bounds (Figma: frame vs. visual; code: hover/inspect). |
| A-03 | REQ | Web | WCAG 2.2 AA minimum target 24×24 CSS px (or sufficient spacing / equivalent); practical touch target ≥ 44×44 CSS px. | Measure target box and gap to neighbours; < 24 px without spacing = fail; < 44 px on touch = flag. |
| A-04 | REC | iOS | Touch target ≥ 44×44 pt even when the visible icon is smaller. | Measure the tappable frame, not the glyph. |
| A-05 | REC | Android | Touch target ≥ 48×48 dp. | Measure the tappable frame in dp. |
| A-06 | REQ | All | Expanded hit areas must not overlap so the triggered action becomes unpredictable. | Overlay expanded hit boxes; any overlap between two commands = fail. |
| A-07 | REC | All | The label of a checkbox/radio/switch is part of its clickable/tappable area. | Click/tap the label text; control must toggle. |
| A-08 | CTX | All | Whole row/card toggles a checkbox/radio only when there is no second primary action and the container reads as one option. | Count primary actions in the row; if > 1, whole-row toggle = fail. |
| A-09 | REQ | All | Card that opens details + checkbox for bulk select = two separate hit areas and two accessible commands. | Verify the checkbox does not open details and the card body does not select. |
| A-10 | REC | Desktop, Web | Hover feedback matches the action area; if the whole row highlights, clicking the row acts. | Hover the row, then click where it highlights; action must fire. |
| A-11 | REQ | All | Interactivity is not communicated by colour alone; add shape, underline, border, icon, text, state, or motion. | Desaturate the screen; interactive elements must still be identifiable. |
| A-12 | REC | Web, Desktop | Cursor matches the operation: text, grab/grabbing, resize; not-allowed only when genuinely unavailable. | Hover each operation and note the cursor. |
| A-13 | CTX | Web, Desktop | cursor: pointer for links (web convention) and non-standard clickable containers; for native buttons it is a DS convention, not a standard. | Check consistency within the product; do not fail a native button for default cursor. |
| A-14 | REQ | Web | A div with a click handler is not a button; use native button/link or supply role, name, state, focus, keyboard. | Inspect DOM: element type, role, tabindex, key handlers. |
| A-15 | REQ | All | Hover, focus, pressed, selected, disabled must not look identical when meanings differ. | Screenshot each state side by side; identical pairs = fail. |
| A-16 | REC | All | Press/tap gives immediate visual feedback even when the result waits on the network. | Throttle network; press; feedback must appear before the response. |
| A-17 | REQ | Web | Irreversible action must not fire on pointerdown; user can move away/cancel before release. | Press, drag off, release; nothing must fire. |
| A-18 | REQ | All | No invisible commands: opacity 0, transparent icon, or background-coloured text must not remain a focusable trap. | Tab through the page; focus landing on nothing visible = fail. |
| A-19 | REC | All | No hover/focus/pressed styling on static-looking elements; what looks like a button behaves like one. | Hover static text/chips; styling change without action = fail. |
| A-20 | REC | All | Interactive and static elements do not share identical styling (e.g. clickable vs. non-clickable chips). | Compare tokens/styles of clickable vs. static siblings. |

## B. Buttons, Links, and Commands (18)

Evidence: GOV.UK Button; Material 3 Buttons; Apple HIG Buttons; WAI-ARIA APG Button; WCAG Link Purpose.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| B-01 | REQ | All | Button = action; link = location/URL change. Do not disguise navigation as submission or vice versa. | For each control note whether it changes URL or performs an action; element must match. |
| B-02 | REC | All | Label starts with a specific verb and names the outcome ("Save changes", "Delete project"), not "Yes/OK/Submit". | Read labels out of context; must be understandable. |
| B-03 | REQ | All | Accessible name includes the visible label (voice control). | Compare aria-label / accessibilityLabel with visible text. |
| B-04 | REC | All | One visually dominant primary action per local context. | Count filled/primary-style buttons in the view; > 1 = flag. |
| B-05 | REC | All | Secondary actions less prominent but still identifiable; not near-invisible text. | Check secondary contrast and affordance. |
| B-06 | REQ | All | Destructive button names the destructive action; red colour alone must not carry the risk. | Label must contain the verb; check greyscale. |
| B-07 | REC | All | Dangerous command not immediately adjacent to a safe one with the same size/style. | Measure gap and compare styles of adjacent destructive/safe buttons. |
| B-08 | REC | All | Disabled only when objectively unavailable; otherwise keep discoverable and explain the requirement nearby. | Find each disabled control; is the reason visible? |
| B-09 | REQ | All | Disabled state is never the only explanation of an error. | Fill the form wrong; must see what is missing, not just a grey button. |
| B-10 | REC | All | Prevent duplicate submission or make it idempotent; double-click must not create two records. | Double-click submit; count network calls / records. |
| B-11 | REC | All | During a long operation keep button width stable and show progress/status; no layout jump. | Trigger loading state; measure width before/after. |
| B-12 | REQ | All | Every icon-only button has an accessible name; unfamiliar icons also need a visible label or tooltip. | Inspect a11y tree; hover for tooltip. |
| B-13 | REC | All | The same icon is not used for different commands unless text disambiguates. | Inventory icons across screens. |
| B-14 | REC | Web | Body-text links identifiable without hover; colour alone insufficient unless supported by another cue. | View at rest; underline/other cue present? Contrast link vs. text ≥ 3:1 if colour-only. |
| B-15 | REQ | Web | Link text makes sense in and out of context; repeated "Learn more" needs a specific accessible name. | List all link names on the page; duplicates with different targets = fail. |
| B-16 | REC | Web | Indicate external destination, new tab, download, or unusual file format in advance. | Check icon/text on such links. |
| B-17 | REC | All | Primary/secondary actions in consistent positions across screens unless platform convention dictates. | Compare button placement across screens/dialogs. |
| B-18 | CTX | Mobile | Sticky CTA must not cover content, keyboard, safe areas, or error messages. | Open keyboard, scroll to bottom, trigger errors; anything hidden = fail. |

## C. Checkboxes, Radios, Switches, Segmented Controls, Tabs (30)

Evidence: WAI-ARIA APG Checkbox/Radio/Switch/Tabs; Material 3; Apple HIG; NN/g.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| C-01 | REQ | All | Checkbox for independent binary or multi-select; radio for exactly one of a mutually exclusive group. | Map each control to its selection model. |
| C-02 | REC | All | Checkboxes square/rounded-square, radios circular. | Visual inspection of component shapes. |
| C-03 | REQ | All | Each checkbox/radio has its own visible label; each group has a shared label/legend. | Look for unlabeled controls and groups without a heading/legend. |
| C-04 | REC | All | Label sits next to the control and the whole label is clickable/tappable. | Click label text; must toggle. |
| C-05 | REC | All | Options vertical by default; horizontal only for short, comparable, non-wrapping options. | Check layout at narrow width; wrapping horizontal groups = flag. |
| C-06 | REQ | All | Radio group has at most one selected option; selecting a new one deselects the previous. | Select two; only one stays selected. |
| C-07 | CTX | All | Preselect a radio only for a safe, honest, likely default; never consent, donation, paid option, or sensitive choice. | Inspect default state of each group. |
| C-08 | REC | All | If returning to "unselected" is needed, provide an explicit None option, not radio re-click. | Look for a None/Not selected option where deselection matters. |
| C-09 | REQ | All | Mixed/indeterminate state looks different from both checked and unchecked. | Compare the three states visually and in the a11y tree. |
| C-10 | REC | All | Parent checkbox controls the group and stays in sync with children. | Toggle children; parent must update; toggle parent; all children follow. |
| C-11 | REC | All | Show "select no more than N" before interaction; at the limit explain a selection must be cleared. | Read the group's hint; hit the limit; message present? |
| C-12 | REQ | Web | Checkbox toggles with Space; radio group uses platform keyboard pattern incl. arrow keys. | Keyboard test: Space, arrows. |
| C-13 | REQ | All | Switch controls a persistent on/off state and shows current state; never a one-time command. | Does the switch trigger an action rather than a state? |
| C-14 | REC | All | Switch takes effect immediately; if a Save step is needed, use a checkbox. | Toggle switch; look for a Save button that gates it. |
| C-15 | REQ | All | Switch label stays stable across states ("Notifications — On/Off"), not "Enable" ↔ "Disable". | Toggle and read the label. |
| C-16 | REC | All | Switch state shown by position/shape (+ optional On/Off text), not colour alone. | Greyscale the two states; still distinguishable? |
| C-17 | CTX | Mobile | Finger drag on a switch is optional; tap on switch or label remains primary and fully functional. | Tap the label and the knob. |
| C-18 | REQ | All | If a switch update fails over the network, restore the truthful state and say the change was not saved. | Fail the request; state must revert with a message. |
| C-19 | REC | All | Segmented control for 2–5 short mutually exclusive options; longer lists need another control. | Count segments; > 5 = flag. |
| C-20 | REC | All | Every segment equally easy to activate; selected segment distinguishable beyond colour. | Measure segment sizes; greyscale check. |
| C-21 | REQ | All | Do not use a segmented control instead of tabs when the choice switches to a section with tablist semantics. | Does the choice switch whole content panels? Then it needs tab semantics. |
| C-22 | REC | All | Tabs switch peer views in one context; they are not wizard steps. | Are the tabs sequential/dependent? Then not tabs. |
| C-23 | REQ | All | Active tab visually clear, exposes programmatic selected state, associated with its panel. | Inspect aria-selected / aria-controls or platform equivalent. |
| C-24 | REQ | Web, Desktop | Tablist: Tab enters, arrows move between tabs, Enter/Space activates (manual mode); respect orientation. | Keyboard test. |
| C-25 | REC | Web, Desktop | Auto-activate on focus only when the panel appears without noticeable delay; otherwise require Enter/Space. | Throttle network; arrow through tabs; lag = switch to manual activation. |
| C-26 | CTX | Mobile | Swipe between tabs only for adjacent, homogeneous pages; supplements tapping, never replaces it. | Tap must work; swipe optional. |
| C-27 | REC | Mobile | During swipe the indicator and content move in sync; no conflict with system Back, carousels, maps, horizontal controls in the panel. | Swipe inside nested horizontal content; observe conflicts. |
| C-28 | REC | All | Overflowing tabs scroll with a visible continuation cue or overflow pattern; labels are not compressed to unreadable. | Narrow the viewport; check truncation and cue. |
| C-29 | REC | All | Switching tabs preserves local state (filters, scroll, text) unless the user resets it. | Enter text, switch away and back. |
| C-30 | REQ | All | Changing a radio option or tab must not trigger a critical action when the interaction looks navigational; separate selection from confirmation. | Change tabs/radios; any irreversible side effect = fail. |

## D. Forms and Data Entry (36)

Evidence: WCAG 2.2 §§1.3.5, 3.3; HTML Standard; web.dev Forms; GOV.UK; USWDS.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| D-01 | REC | All | Ask only for data needed for the current result. | For each field, name the result it feeds; none = remove. |
| D-02 | REQ | All | Every field has a persistent visible label; placeholder is not a label. | Type into the field; label must remain visible. |
| D-03 | REC | All | Labels short, specific, placed above fields. | Check label position and wrapping at narrow width. |
| D-04 | REC | All | Hint text explains format/constraints before input; not repeating the label, not hidden in a tooltip. | Read hint; is critical instruction only in a tooltip? |
| D-05 | REQ | All | Required/optional marked consistently and programmatically; a bare asterisk is not enough. | Look for legend explaining the mark; inspect required attribute. |
| D-06 | REC | All | Mostly-required form marks the optional fields; mostly-optional marks the required ones. | Count and check which side is marked. |
| D-07 | REQ | Web, Mobile | Correct type/inputmode/system keyboard for email, tel, URL, decimal, numeric. | Focus each field on mobile; observe keyboard. |
| D-08 | REQ | Web | Correct autocomplete purpose for name, address, email, phone, card, OTP, etc. | Inspect autocomplete attributes. |
| D-09 | REC | All | Do not block paste into email, password, card, or OTP fields. | Paste into each. |
| D-10 | REC | All | Do not split phone, card, OTP into many fields without proven need. | Count fields per value. |
| D-11 | REQ | All | When input is visually split, Backspace, paste, arrows, focus movement behave naturally and SR announces the value. | Keyboard + paste + SR test on split input. |
| D-12 | REC | All | Accept natural separators and format tolerantly (spaces, hyphens, case, local variants). | Enter "4111 1111 …", "+1 (555) …"; must be accepted. |
| D-13 | REQ | All | Valid input is not erased after validation error, network error, Back, or re-auth. | Trigger each event; input must survive. |
| D-14 | REC | All | Input mask does not break mid-edit, selection, paste, SR, or international values. | Edit in the middle, paste, enter a foreign format. |
| D-15 | REC | All | No numeric-stepper semantics for identifiers; preserve leading zeros and long values. | Enter "007"; check type=number is not used for IDs. |
| D-16 | REC | All | Field width may hint expected length but must still accept longer localized values. | Enter a long value; must not clip inaccessibly. |
| D-17 | REC | All | Long text uses a textarea with reasonable initial height and a way to expand. | Check control type and resize affordance. |
| D-18 | REQ | All | Show character limit before it is reached; announce approaching/exceeding accessibly, not by colour alone. | Read the counter; inspect live region. |
| D-19 | REC | All | Password Show/Hide control with stable label, clear state, preserved cursor position. | Toggle visibility mid-edit; cursor must stay. |
| D-20 | REC | All | Password requirements shown before an error and updated as met; no rules that break password managers. | Read the rules list; use a manager-generated password. |
| D-21 | REQ | All | Dates accepted in the user's locale format with an unambiguous example. | Enter locale date; hint shows e.g. "31 12 2025". |
| D-22 | CTX | All | Direct input for known dates (birth, document); calendar picker for nearby appointments; no browsing decades back. | Which pattern is used for which date type? |
| D-23 | REC | All | Select for compact familiar lists; radios for small important lists; searchable combobox for long lists. | Count options vs. control type. |
| D-24 | REC | All | No hundreds of countries/cities in a dropdown without search and typeahead. | Open the list; type a letter. |
| D-25 | REQ | Web | Combobox exposes expanded state, selected option, result count/status, and standard keyboard navigation. | Inspect aria-expanded, aria-activedescendant, live status; keyboard test. |
| D-26 | REC | All | Suggestions never take control: custom value, closing the list, and submitting remain possible. | Type a value not in the list and submit. |
| D-27 | REC | All | File upload supports a standard picker; drag and drop is additional. | Look for a Browse/Choose button. |
| D-28 | REQ | All | Before upload: accepted types, quantity, size limits. After: filename, size, progress, result, remove/replace. | Read pre-upload hint; upload a file; check post-state. |
| D-29 | REC | All | Do not require re-uploading the same file within one process without a security/privacy reason. | Walk the flow; count upload prompts for one file. |
| D-30 | REC | All | Multi-step form shows the step's purpose and overall progress without false precision under branching. | Read step indicator; does total change with branches? |
| D-31 | REQ | All | Back returns to the previous step with answers preserved; browser/system Back must not break the flow. | Use browser Back mid-form. |
| D-32 | REC | All | Group large forms by meaning; reveal short dependent questions progressively. | Look at section headings and conditional reveals. |
| D-33 | REC | All | No auto-advance between ordinary fields; predictable OTP/date entry may be an exception if keyboard users keep control. | Type to the field's max length; focus must not jump. |
| D-34 | REC | Mobile | Enter/Next moves to the next logical field; Done submits only when safe. | Check return-key type and behaviour per field. |
| D-35 | REQ | Mobile | On-screen keyboard must not cover the active field, hint, error, or primary action; screen scrolls correctly. | Focus the last field with keyboard open. |
| D-36 | REC | All | Autosave communicates Saving / Saved / Not saved and the time of last save where useful. | Edit, wait, look for status text. |

## E. Validation, Errors, and Recovery (18)

Evidence: WCAG 2.2 §§3.3.1–3.3.9; GOV.UK Validation; Fluent Message Bar; NN/g.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| E-01 | REC | All | Prevent errors with constraints and instructions before reporting them after submit. | Are constraints (format hints, limits) visible before input? |
| E-02 | REQ | All | Error says what happened, where, and how to fix; "Invalid value" is not enough. | Read each error message against the three parts. |
| E-03 | REQ | All | Error is programmatically associated with the field and shown nearby; colour/red border is not the only signal. | Inspect aria-describedby / aria-invalid; greyscale check. |
| E-04 | REC | Web | After submit with multiple errors, show a summary at top with links to fields; move focus to the summary or first error. | Submit with 2+ errors; observe focus and summary. |
| E-05 | REC | All | Inline validation only after the user had a fair chance to finish; no error on an empty field at first focus. | Focus then blur an empty field; tab into a field; observe timing. |
| E-06 | REQ | All | Remove an error only once fixed; no success before required validation completes. | Partially fix; error must remain. |
| E-07 | REC | All | No success mark on every ordinary field unless it adds reassurance. | Count green checkmarks. |
| E-08 | REQ | All | Distinguish server errors from validation errors; do not ask users to fix valid data after a 500/timeout. | Simulate 500; message must not blame the input. |
| E-09 | REC | All | Preserve input after a network error and offer Retry; retry must not duplicate. | Fail request, retry; count records. |
| E-10 | REQ | All | Legal, financial, medical, destructive, or risky actions get review/confirm/correct or reliable undo. | Identify risky actions; find the safeguard. |
| E-11 | REC | All | Prefer undo for frequent reversible deletions; confirmation for rare, expensive, irreversible ones. | Map each delete to undo vs. confirm. |
| E-12 | REQ | All | Confirmation names object, scope, and consequence ("Permanently delete 24 photos?"). | Read dialog title/body. |
| E-13 | REC | All | Confirm button repeats the specific command ("Delete"), not "Yes/OK/Confirm". | Read button label. |
| E-14 | REC | All | Safe action accessible and visually separated in a dangerous dialog; for irreversible actions initial focus often on Cancel. | Open dialog; where is focus; spacing/style of Cancel? |
| E-15 | CTX | All | Typing the object name or DELETE only for extremely dangerous, rare operations. | Frequency of the operation vs. the ritual. |
| E-16 | REC | All | No confirmation for routine safe actions. | List confirmations; any on safe actions = flag. |
| E-17 | REQ | All | Cancel ≠ Close: Cancel discards an unfinished action, Close dismisses a view; use explicit labels when consequences differ. | Check what each Cancel/Close actually does. |
| E-18 | REC | All | Leaving with unsaved work offers Save, Discard, Continue editing; never lose work silently. | Edit, navigate away. |

## F. System Status, Loading, and Feedback (16)

Evidence: WCAG Status Messages; Material Snackbar; Fluent Message Bar and Skeleton; web.dev INP/RAIL.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| F-01 | REQ | All | Immediately after an action the user can tell input was received (pressed state, local change, progress). | Act and watch the first ~100 ms. |
| F-02 | REC | All | < ~1 s: local feedback often enough; longer: explicit loading state; lengthy: progress/stages and a way to keep working. | Time the operation; match to the tier. |
| F-03 | REC | All | Determinate progress only when a truthful percentage exists; otherwise indeterminate. | Does the bar's % correspond to real progress? |
| F-04 | REQ | All | Loading must not look frozen; animation/text accessible; updates announced without excessive repetition. | SR test on loading; check aria-busy / live region. |
| F-05 | REC | All | Skeleton matches incoming geometry, does not imitate interactivity, does not disrupt focus on load. | Compare skeleton vs. loaded layout; focus position after load. |
| F-06 | REC | All | Do not cover useful content with a spinner on background refresh; keep stale data, indicate updating unobtrusively. | Trigger refresh; content must stay visible. |
| F-07 | REQ | All | Success confirms the completed outcome, not just that a request was sent. | Read success message timing vs. server response. |
| F-08 | REC | All | Snackbar/toast for brief non-critical feedback; critical and actionable errors persistent inline/banner/dialog. | Classify each message; critical in a toast = fail. |
| F-09 | REQ | All | Snackbar with an action stays long enough to notice and use; on web important actions better without auto-dismiss. | Time the toast; is the action reachable? |
| F-10 | REC | All | Do not stack multiple toasts; combine or replace by priority. | Trigger several; count visible. |
| F-11 | REQ | All | Status message must not cover keyboard, CTA, navigation, or the next required step. | Show message with keyboard open; check overlap. |
| F-12 | REC | All | Message placed at the level it affects: field error by the field, card status in the card, page alert at top. | Locate each message relative to its subject. |
| F-13 | REC | All | Background task: tell where the result will be and keep it in notifications/history. | Start task; navigate away; can you find the result? |
| F-14 | REQ | All | Optimistic UI only with clear safe rollback; on failure restore true state and explain. | Fail the request after optimistic update. |
| F-15 | REC | All | Bulk action reports counts succeeded/failed, not a generic Done. | Run bulk with a partial failure. |
| F-16 | REC | All | Temporary messages written as outcomes ("Link copied"), not "Success". | Read toast copy. |

## G. Navigation, History, and Search (18)

Evidence: WCAG 2.2 §§2.4, 3.2; GOV.UK; WAI-ARIA APG Breadcrumb; Nielsen heuristics.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| G-01 | REQ | All | Users know where they are: page title/heading, active nav, breadcrumb or step indicator when needed. | Land on the screen cold; identify location in < 3 s. |
| G-02 | REC | All | Global navigation in the same location and order across screens. | Compare nav across screens. |
| G-03 | REQ | Web | URL represents meaningful state users may open, refresh, bookmark, share. | Refresh/share the URL; same state restored? |
| G-04 | REQ | Web | Browser Back/Forward restore the actual previous state; no ejecting from the app or losing form data. | Navigate, press Back. |
| G-05 | REQ | Mobile | System Back follows platform history; no unexpected close, reset, or exit. | Press system Back on every screen. |
| G-06 | REC | All | Returning to a list preserves scroll, filters, sorting, selected context. | Open item, go back. |
| G-07 | REC | All | Navigation item names a destination; command item names an action ("Settings" vs. "Save settings"). | Read nav labels. |
| G-08 | REC | All | No new window/tab without reason; when used, warn and keep history comprehensible. | Check target=_blank usage and indicators. |
| G-09 | REC | All | Search provided where volume/frequency justifies; primary find path not hidden in overflow. | Where is search entry point? |
| G-10 | REC | All | Search works with Enter/Search key and an explicit button; suggestions do not replace submission. | Press Enter; click button. |
| G-11 | REC | All | Query stays visible and editable on results. | Look at results page header. |
| G-12 | REC | All | Zero results show the query, a likely reason, and a next step. | Search nonsense. |
| G-13 | REC | All | Active filters shown next to results, Clear all present, result count updates predictably. | Apply filters; observe chips/count. |
| G-14 | CTX | Mobile | Filters apply immediately or via Apply, but the model is clear; Apply previews count; live updates do not require Save. | Identify the model; check for preview count or missing Save. |
| G-15 | REQ | All | Pagination/infinite scroll works without precise gesture: explicit continuation, loading, error, retry, reachable footer. | Try to reach the footer; simulate a page-load error. |
| G-16 | REC | All | Pagination preserves query, filters, sorting; communicates page/range. | Go to page 2; check state and label. |
| G-17 | REC | All | Bottom navigation for 3–5 top-level destinations, not contextual actions. | Count items; any actions among them? |
| G-18 | REC | All | Breadcrumb = hierarchy, not history; last item is the current location, not a command. | Read breadcrumb; last item non-clickable/current. |

## H. Dialogs, Sheets, Popovers, Tooltips, Disclosure (14)

Evidence: WAI-ARIA APG Dialog; USWDS Modal; Material Dialogs; Apple HIG; WCAG 1.4.13.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| H-01 | REC | All | Modal only to interrupt for a decision or short task; complex multi-step goes on a page/full-screen. | Count steps/fields inside the modal. |
| H-02 | REQ | All | Modal has a clear title and a visible close/cancel command. | Look for title and close control. |
| H-03 | REQ | Web, Desktop | On open focus moves in; Tab/Shift+Tab stay inside; Escape closes when appropriate; on close focus returns to trigger or logical next. | Keyboard test the whole cycle. |
| H-04 | REQ | All | Content behind a modal is visually and programmatically unavailable. | Tab/SR behind the modal; inspect aria-modal / inert. |
| H-05 | REC | All | Initial focus by task: first field for input, start of content for reading, safe command for irreversible action. | Open dialog; note focus target. |
| H-06 | CTX | All | Click outside may dismiss a lightweight popover but must not destroy input or confirm a dangerous action. | Type then click outside. |
| H-07 | REC | Mobile | Bottom sheet has explicit close and height controls; drag handle has a non-drag alternative. | Find a close button; try without dragging. |
| H-08 | REQ | All | Tooltip is not the only route to critical info and holds no interactive content unless the pattern supports it. | List tooltip contents. |
| H-09 | REQ | Web | Hover/focus content is dismissible, hoverable, and persistent (WCAG 1.4.13). | Hover trigger, move onto content, press Escape. |
| H-10 | REC | All | Tooltips also appear on keyboard focus; touch devices get a clear alternative. | Tab to trigger; tap on touch device. |
| H-11 | REC | All | Popover does not cover its trigger or critical content; repositions at viewport edges. | Open near edge; check placement. |
| H-12 | REQ | Web | Accordion/disclosure button exposes expanded state, works with Enter and Space, is associated with its region. | Inspect aria-expanded / aria-controls; keyboard test. |
| H-13 | REC | All | When comparing sections, allow multiple open or show content directly. | Can two sections be open at once when comparison is the task? |
| H-14 | REC | All | Do not hide primary CTA, price, limitation, or mandatory condition in a tooltip or Learn more accordion. | Read all tooltips/accordions for such content. |

## I. Cards, Lists, Tables, Bulk Selection (18)

Evidence: Material 3 Cards; Fluent 2 Card; GOV.UK Table; WAI-ARIA Grid; WCAG.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| I-01 | REC | All | A card groups one object/topic and its related actions. | Count entities per card. |
| I-02 | CTX | All | Whole card clickable when it has one primary destination; nested actions have separate hit areas and do not trigger the card. | Click nested action; card must not open. |
| I-03 | REQ | Web | No button-in-button or link-in-link to make a card clickable; use valid structure or stretched-link. | Inspect DOM nesting. |
| I-04 | REC | All | Card shows the primary identifier and only what is needed to choose the next action. | Count fields; is the identifier first? |
| I-05 | REC | All | Fields and actions in the same order across repeated cards. | Compare several cards. |
| I-06 | REQ | All | Ellipsis must not hide the only distinguishing information; full value available via wrap, details, or accessible reveal. | Two items differing only in the truncated part? |
| I-07 | REC | All | Overflow menu for infrequent secondary commands; primary frequent command not hidden inside. | Open "…" menu; primary action there = fail. |
| I-08 | REQ | All | Multi-select clearly separates selection mode from opening; shows count selected. | Enter selection mode; count indicator present? |
| I-09 | REC | All | "Select all" states its scope (visible 20 / page / all 12,430). | Read label after select all. |
| I-10 | REQ | All | Destructive bulk action confirms scope; result reports partial failures and recovery. | Run bulk delete with a failure. |
| I-11 | REC | All | Table for comparing data across rows/columns, not page layout. | Is the table used for layout? |
| I-12 | REQ | Web | Data table has real header structure, caption/accessible name, header–cell associations. | Inspect th/scope/caption. |
| I-13 | REC | All | Sortable header shows sortability, active column, direction; repeated activation changes predictably. | Click header 3 times; observe. |
| I-14 | REC | All | Numbers aligned for comparison, consistent units/format; negative/anomalous values not colour-only. | Check alignment and greyscale. |
| I-15 | REQ | All | Horizontal scrolling must not cut off controls; frozen columns/headers must not cover focus rings or enlarged text. | Scroll and zoom 200%; tab through. |
| I-16 | CTX | Mobile | Table may become cards only if labels, comparison order, and all actions are preserved. | Compare desktop table vs. mobile cards. |
| I-17 | REC | All | Empty list, zero results, and load failure are distinct with different next steps. | Trigger each state. |
| I-18 | REC | All | Adding/removing a row must not unexpectedly move focus or scroll. | Add/remove; observe focus and scroll. |

## J. Touch, Gestures, Drag and Drop (16)

Evidence: WCAG 2.2 §§2.5.1–2.5.8; Apple HIG Gestures; Material; Android Accessibility.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| J-01 | REQ | All | Multi-point or path-based gestures have a single-pointer alternative unless essential. | For each gesture, name the tap/click equivalent. |
| J-02 | REQ | All | Every drag action has a non-drag alternative (move buttons, menu, position entry, tap-to-place). | Reorder without dragging. |
| J-03 | REC | Mobile | System edge gestures take priority; no primary horizontal gesture in a conflicting edge area without protection. | Swipe from the screen edge. |
| J-04 | REC | Mobile | Visible or easily discoverable alternative for every hidden swipe action. | Find the action without swiping. |
| J-05 | REQ | All | Swipe to delete never irreversibly deletes from one accidental gesture; undo or confirmation. | Swipe-delete; look for undo. |
| J-06 | REC | Mobile | Swipe direction matches language, platform, visible movement; test RTL separately. | Test in an RTL locale. |
| J-07 | REC | All | Draggable object has a signifier (handle, grab cursor, instruction, familiar pattern). | Look for handle/affordance. |
| J-08 | REQ | All | During drag show the lifted object, valid/invalid drop zones, and insertion position. | Start dragging; observe. |
| J-09 | REC | All | Drop zone large enough without pixel aiming; edge auto-scroll controllable. | Measure drop targets; drag to edge. |
| J-10 | REQ | All | Cancelling a drag restores object and state without data loss. | Press Escape / drop outside. |
| J-11 | REC | Mobile | Long press for secondary/contextual action with a visible alternative; never the only primary command. | Find each long-press action elsewhere. |
| J-12 | REC | Mobile | Pull to refresh supplements explicit/auto refresh, shows progress, does not trigger inside nested scrolling. | Pull inside a nested scroll view. |
| J-13 | REC | All | Button/keyboard alternatives for pinch, rotate, zoom when needed for the task. | Look for +/- and rotate buttons. |
| J-14 | REQ | All | Motion/tilt/shake controls have a conventional UI alternative and can be disabled. | Find the setting and the alternative. |
| J-15 | REC | Mobile | Touch feedback begins immediately; haptics may confirm but never replace visual/audio feedback. | Tap with haptics off. |
| J-16 | REC | All | No click fires after movement has clearly become a scroll or drag. | Touch-scroll starting on a button. |

## K. Keyboard, Focus, Screen Readers (18)

Evidence: WCAG 2.2 §§2.1, 2.4, 4.1; WAI-ARIA APG Keyboard Interface and Patterns.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| K-01 | REQ | Web, Desktop | All functionality available from the keyboard; no keyboard trap. | Complete the flow with keyboard only. |
| K-02 | REQ | Web, Desktop | Focus indicator always visible, sufficient contrast, not clipped by overflow/overlays. | Tab through; measure ring contrast (≥ 3:1). |
| K-03 | REQ | Web, Desktop | Sticky header/footer/modal must not obscure the focused element beyond WCAG limits. | Tab to items near sticky bars. |
| K-04 | REQ | Web | DOM/focus order follows meaningful visual order; CSS reordering must not confuse. | Tab order vs. visual order. |
| K-05 | REC | Web | No positive tabindex; fix DOM order, manage focus with standard patterns. | grep tabindex > 0. |
| K-06 | REQ | Web | Native semantics over custom ARIA imitations; no ARIA beats bad ARIA. | Inspect custom roles. |
| K-07 | REQ | All | Every control exposes accessible name, role, value/state, and state changes. | Read the a11y tree for each control. |
| K-08 | REQ | All | Decorative images/icons excluded from the a11y tree; meaningful images have concise alt text. | Inspect alt / aria-hidden / accessibilityElementsHidden. |
| K-09 | REQ | All | Icon button has an action label ("Add to favorites") and exposes the updated state ("In favorites"). | Toggle and re-read name/state. |
| K-10 | REC | Web | After SPA navigation, move focus to heading/main/logical point and update document title. | Navigate client-side; where is focus; title changed? |
| K-11 | REQ | Web | Dynamic statuses/errors announced via live region/status semantics without moving focus unexpectedly. | SR test on status changes. |
| K-12 | REC | Web, Desktop | Follow platform shortcut conventions; custom single-key shortcuts can be disabled/remapped. | List shortcuts; check settings. |
| K-13 | REQ | Web | Skip link to bypass repeated navigation blocks. | Tab once from page top. |
| K-14 | REQ | All | Headings form a meaningful hierarchy; visual size is no substitute for semantic markup. | Outline the heading tree. |
| K-15 | REC | All | SR announcements do not redundantly repeat label and state; test the full phrase heard. | Listen to each control announcement. |
| K-16 | REQ | All | Hidden/collapsed content is not focusable or announced. | Tab into collapsed sections. |
| K-17 | REC | All | After adding/removing an item, keep focus at a logical point and announce the change. | Add/remove with SR on. |
| K-18 | REC | All | Test with real AT (VoiceOver, TalkBack, NVDA, Voice Control), not only automated checkers. | Evidence of manual AT test. |

## L. Visual Accessibility and Responsive Design (16)

Evidence: WCAG 2.2 §§1.3–1.4; Apple and Android Accessibility; Fluent Accessibility.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| L-01 | REQ | All | Normal text contrast ≥ 4.5:1; large text ≥ 3:1 (WCAG AA). | Measure text/background contrast. |
| L-02 | REQ | All | Borders, icons, and component states needed for recognition ≥ 3:1 against adjacent colours. | Measure non-text contrast. |
| L-03 | REQ | All | Colour is not the only cue for error, success, selected, chart value, or required. | Greyscale the screen. |
| L-04 | REQ | Web | Usable at 200% zoom; reflows at 320 CSS px width (except justified 2-D content). | Zoom 200%; resize to 320 px; no horizontal scroll or loss. |
| L-05 | REQ | All | Larger system font / Dynamic Type must not clip text, buttons, fields, or hide commands. | Set largest accessibility text size. |
| L-06 | REC | All | Do not fix the height of text components that may wrap under translation/enlargement. | Inspect fixed heights on text containers. |
| L-07 | REQ | Web | User text-spacing overrides must not cause loss of content/functionality. | Apply WCAG 1.4.12 spacing bookmarklet. |
| L-08 | REC | All | Body text has readable size, line height, line length; sufficient contrast does not excuse thin/light fonts. | Measure size, line-height, measure, weight. |
| L-09 | REC | All | Text aligned to the language's natural direction; centered body only for short blocks. | Look for centered paragraphs. |
| L-10 | REQ | All | No important text in bitmaps without essential reason. | Find images containing text. |
| L-11 | REQ | All | Do not lock orientation unless essential. | Rotate device. |
| L-12 | REC | All | Layout adapts to available space and content, not device models. | Resize continuously; breakpoints by content? |
| L-13 | REQ | Mobile | Account for safe areas, cutouts, home indicator, system bars, keyboard. | Test on notched device with keyboard open. |
| L-14 | REC | All | Hover is not the only way to reveal an action; touch/keyboard get an equivalent. | Tab to and tap hover-revealed actions. |
| L-15 | REQ | All | High-contrast / forced-colors modes must not hide focus rings, checkboxes, icons, states. | Enable forced-colors / Increase Contrast. |
| L-16 | REC | All | Light and dark themes tested separately; semantic colours keep meaning and contrast in both. | Measure contrast in both themes. |

## M. Content, Localization, and Trust (14)

Evidence: WCAG Headings, Labels and Language; Nielsen heuristics; GOV.UK Content patterns.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| M-01 | REC | All | Use user/domain language, not internal DB, endpoint, or process names. | Scan copy for internal jargon. |
| M-02 | REC | All | Same term for the same concept throughout. | Build a term list across screens. |
| M-03 | REC | All | Show important info at the moment of decision; no recall from a previous screen. | At each decision, is the needed value on screen? |
| M-04 | REC | All | Label names the object, helper explains format/reason, button names the action, error explains problem and fix. | Classify each text element by role. |
| M-05 | REC | All | No ambiguous negatives or double negatives in checkboxes/questions. | Read checkbox labels for "not/disable". |
| M-06 | REC | All | Localize numbers, dates, times, currency, addresses, plurals; show time zone when it matters. | Switch locale; check formats. |
| M-07 | REQ | Web | Page language and fragment languages set in code. | Inspect html lang and lang on fragments. |
| M-08 | REQ | All | RTL adapts direction, nav order, directional icons, gestures; test numbers and brand separately. | Run in an RTL locale. |
| M-09 | REC | All | Layouts tolerate 30–50% text expansion without clipping. | Pseudo-localize with +50% length. |
| M-10 | REC | All | Avoid all caps for long labels/messages; sentence case preferred. | Find uppercase strings > a few words. |
| M-11 | REC | All | Empty state explains the situation and offers a relevant next step the user can perform. | Trigger empty state; is the CTA actionable for this user? |
| M-12 | REQ | All | Disclose price, recurring payments, trials, limitations, consent consequences, data processing before commitment. | Read the pre-commit screen for these items. |
| M-13 | REQ | All | No preselection, hierarchy, or wording that hides refusal, cancellation, or the less profitable choice. | Compare prominence of accept vs. decline; default states. |
| M-14 | REC | All | Explain benefit/context before a permission request; trigger the system prompt only when needed. | When does the OS prompt appear; is there a pre-prompt? |

## N. Motion, Performance, and Network Resilience (14)

Evidence: WCAG Motion, Flashing and Timeouts; web.dev INP/RAIL; Apple HIG; Nielsen heuristics.

| ID | Level | Platform | Rule | Check |
|---|---|---|---|---|
| N-01 | REC | All | Motion explains state relationships, gives feedback, or reinforces a spatial model; decoration must not delay the task. | For each animation, name its purpose; measure added delay. |
| N-02 | REQ | All | Respect prefers-reduced-motion / system setting: remove large movement, parallax, unnecessary zoom. | Enable reduce motion; observe. |
| N-03 | REQ | All | No hazardous flashing > 3 times per second above WCAG thresholds. | Inspect any flashing content. |
| N-04 | REQ | All | Auto-moving/auto-updating content > 5 s beside other content can be paused, stopped, or hidden. | Find pause control. |
| N-05 | REC | All | Carousel does not advance while reading/interacting; pause, prev/next, position indicator present. | Hover/focus carousel; check controls. |
| N-06 | REC | All | Animation does not block repeated actions or force waiting when the outcome is known. | Click rapidly; does it queue/block? |
| N-07 | REC | Web | Measure INP in the real product; polish does not compensate for delayed controls. | Check field INP data (target ≤ 200 ms). |
| N-08 | REC | All | Reserve space for images, errors, loaders, async content to avoid layout shift. | Measure CLS; watch load. |
| N-09 | REC | All | On slow network show structure or cached content before an empty screen with an endless spinner. | Throttle to slow 3G; first paint content? |
| N-10 | REQ | All | Offline and timeout states distinct from empty; provide Retry and explain unsaved-change status. | Go offline; read the state. |
| N-11 | REC | All | Available offline actions performed locally and synced later with clear status and conflict model. | Act offline; reconnect; observe sync status. |
| N-12 | REQ | All | Warn before session expiry, allow extension, preserve data through re-auth when safe. | Let session expire mid-form. |
| N-13 | REC | All | Background refresh does not reset scroll, selection, focus, or the field being edited. | Edit during refresh. |
| N-14 | REC | All | Retry uses a safe strategy; user never left guessing whether payment/submission succeeded. | Retry after ambiguous failure; check idempotency key / status. |

## Acceptance checklist

For every new component or change, all applicable items must be "yes":

- [ ] 1. Clear without hover what is interactive and what will happen.
- [ ] 2. Visible and actual action areas match.
- [ ] 3. Touch target large enough with sufficient spacing from neighbours.
- [ ] 4. Works with mouse, touch, keyboard, and screen reader.
- [ ] 5. Every control exposes correct accessible name, role, value/state, and label.
- [ ] 6. Default, hover, focus, pressed, selected, disabled states are distinguishable.
- [ ] 7. Double-click, repeated tap, and long press handled.
- [ ] 8. Slow network, timeout, offline, 4xx and 5xx handled.
- [ ] 9. Input preserved; Retry or Undo available.
- [ ] 10. Error shown near its cause with a clear fix.
- [ ] 11. Not obscured by keyboard, sticky UI, safe areas, or zoomed content.
- [ ] 12. Works at 200% zoom, large system text, narrow viewport, wrapped labels.
- [ ] 13. State distinguishable without colour; text and essential boundaries meet contrast.
- [ ] 14. Works in dark mode, high-contrast mode, reduced-motion mode.
- [ ] 15. Back/Forward, URLs, focus restoration, scroll restoration correct.
- [ ] 16. Tolerates localization, RTL, long names, leading zeros, very large values.
- [ ] 17. Loading, empty, zero-results, partial-success, permission-denied states differ.
- [ ] 18. Primary command available without relying only on gesture, overflow menu, tooltip, or long press.
- [ ] 19. Destructive-action protection matches real risk, not team habit.
- [ ] 20. Compliance checkable by observable criteria, not "it feels easy".

Turning a rule into a testable criterion (pattern from the catalog): replace "the card should be easy to use and clickable" with "clicking empty area, title, or preview opens one URL; the nested overflow menu does not open the card; the link is reachable with Tab, has a visible focus ring, activates with Enter; every action meets platform target size; SR announces object name and link role." Likewise "tabs should support swiping" becomes "tap opens the adjacent panel; if swipe exists it changes only to an adjacent panel, moves the indicator in sync, does not conflict with system Back or nested horizontal areas; web tabs follow APG keyboard pattern; swipe is never the only method."

## Evidence levels and debatable rules

Evidence tiers used by the catalog, strongest first:
1. Normative standards and official accessibility patterns: WCAG 2.2, WAI-ARIA APG, HTML Standard (forms).
2. Platform guidelines: Apple HIG (incl. Accessibility, Gestures), Android/Jetpack Compose accessibility, Material Design 3, Fluent 2.
3. Government design systems with accessibility testing: GOV.UK Design System (incl. validation pattern), USWDS.
4. Research and practical guidance: NN/g (heuristics, checkbox, toggle, error-message guidelines), web.dev (forms, INP), MDN (cursor).

Rules the catalog explicitly marks as contested, with the catalog's position:
- **"Card with a checkbox → whole card clickable."** Only when the whole card is one selectable option. If the card also opens details, activation and selection are separate commands (A-08, A-09, I-02).
- **"Every clickable element needs cursor: pointer."** A reasonable design-system convention, not a standard. Browser convention ties pointer to links; native buttons often keep the default cursor. The real requirements are discoverability, consistency, hover/focus states, correct semantics (A-13). Do not fail a native button for a default cursor; flag inconsistency instead.
- **"Every tab control should support swiping."** No. Swipe is an optional supplement for adjacent peer content on mobile and conflicts with system Back, carousels, maps, horizontal scroll. Tap and keyboard/AT behaviour are fundamental (C-26, C-27).
- **"Disabled button is the best error prevention."** Only when the reason is obvious; otherwise disabling hides the requirement (B-08, B-09).
- **"Every deletion needs confirmation."** Frequent reversible deletion is better with Undo; confirmation for rare/serious consequences; overused warnings stop being read (E-11, E-16).
- **"Inline validation while typing."** Only if no error is reported before input is complete; validate after blur or a meaningful pause, then on submit (E-05).
- **"Auto-activate tabs on focus is faster."** Only when the panel appears instantly; with latency it frustrates keyboard users (C-25).

## Version

Rules catalog v2.0 (2026-07-14). Each ID resolves to a full card in the project's rules knowledge base (rationale, good and bad examples, exceptions, design-stage check, implementation check, acceptance criterion, check type Auto / Hybrid / Manual). Origin and licence: SOURCES.md.
