# Lens 08 — Forms and inputs

Checks every field, control and submit path: what is asked and how it is labelled; what the
input tolerates; what happens on submit and between steps; which control carries which choice.
Pre-tests: type into every field (label still visible?), paste into every field, open each field
on a phone (which keyboard?), tab through. Errors and validation timing: lens 05; accessibility
floors: lens 10; dropdowns, comboboxes, tabs and segmented controls: lens 11; thumb reach and
safe areas: lens 12.

## 1. Asking and labelling

### Ask only for data the result needs
- **Rule:** Every field feeds a named result of the current step; a field that feeds nothing is
  removed, not made optional.
- **Why:** Every field is a decision and a chance to fail [cognitive load].
- **Check:** For each field, name the result it feeds; none means remove. Static design
  suffices. Progressive disclosure of advanced options: lens 06.
- **Severity:** warning
- **Tells:** "How did you hear about us" between address and payment; ten optional fields on a
  sign-up.
- **Catalog:** D-01

### Visible label: floating or above the field
- **Rule:** Every field has a visible label at all times: either static, placed above the
  field, or floating — sitting inside the empty field and moving above it (or outside it) on
  focus or fill. Both are fine; the choice is a project decision, not a universal preference.
  The label is short and specific, and bound to the field programmatically, so it is announced
  and clicking it focuses the field. A placeholder is never the label: it vanishes on the first
  keystroke and usually fails contrast; when used, it shows a format example. The failure that
  matters is a label that disappears with nothing to replace it (placeholder-only, or a floating
  label that never moves), or a floating label that becomes unreadable once it moves — below the
  body-size floor or the contrast floor.
- **Why:** The label is what assistive tech announces and what the user re-reads to check what
  they typed; a label that vanishes forces recall [working memory] [recognition over recall].
- **Check:** Fill every field: is a label visible — static or floated — and readable? Click each
  label: the field focuses (runtime or code). For a floating label, check the empty, focused and
  filled variants: legible at rest (contrast as text, not as placeholder), legible once moved
  (body-size floor, contrast floor), not animated on every focus. Check label wrapping at narrow
  width. Static design: read the filled and, where floating, the moved variant.
- **Severity:** blocking
- **Tells:** placeholder-only forms; a label that disappears on focus with nothing replacing it;
  a floating label at placeholder contrast or below the body-size floor once moved; a label to
  the left that wraps on a phone; "Email" as placeholder with no label.
- **Catalog:** D-02, D-03, M-04

### Fields have a visible boundary
- **Rule:** Every editable field sits in a visible container (border or fill) that marks its
  extent; an underline alone or no boundary is not enough. Field width may hint at the expected
  length but the field still accepts longer localised values without clipping.
- **Why:** The boundary is the field's signifier [affordance and signifier]; on a screen nothing
  is editable except by appearance.
- **Check:** Without hovering and in greyscale: can the critic tell where each field starts and
  ends? Enter a long value: does it clip inaccessibly? Static design for the first; runtime for
  the second.
- **Severity:** warning
- **Tells:** borderless underline-only inputs; a field with no border on a card of the same
  colour; a postcode field that clips a long postcode.
- **Catalog:** D-16, A-11

### Hints before input, not in tooltips
- **Rule:** Hint text explains format and constraints before input, beside the field, without
  repeating the label and never only in a tooltip; a date field shows an unambiguous example in
  the user's locale; a placeholder, when used, is a format example. Hints are phrased positively.
- **Why:** Prevent first, report second [slips lapses mistakes]; a constraint learned after
  submit is an error that could have been avoided.
- **Check:** Read each hint: does it add format or constraint information? Is any critical
  instruction only in a tooltip? Static design suffices.
- **Severity:** warning
- **Tells:** hint "Enter your phone number" under "Phone number"; a required format revealed
  only by the error; a date field with no example.
- **Catalog:** D-04, D-21, E-01, H-08

### Required and optional are marked once, consistently
- **Rule:** Mark the minority: in a mostly-required form mark the optional fields "(optional)"
  in the label; in a mostly-optional form mark the required ones. The mark is consistent and
  programmatic (the platform's required attribute), and a bare asterisk is not enough: one
  visible explanation per form. Optional steps: lens 06 · Optional is labelled and skippable.
- **Why:** Marking the exception keeps the form quiet; a screen reader needs the programmatic
  mark, not the glyph.
- **Check:** Count which side is marked; look for the legend; inspect the required attribute in
  code.
- **Severity:** warning
- **Tells:** asterisks on nine fields out of ten; an asterisk with no legend; "(optional)" here
  and "*" there.
- **Catalog:** D-05, D-06

## 2. What the input tolerates

### Forgiving inputs
- **Rule:** Input tolerates common, non-semantic variation: case-insensitive; trims leading and
  trailing whitespace; collapses repeated spaces; accepts natural separators (spaces, hyphens,
  parentheses in phone and card numbers); normalises paste artefacts (non-breaking spaces,
  smart quotes); accepts localised variants with identical meaning (`12,5` = `12.5`, `é` = `e`
  where applicable). An input mask never breaks mid-edit, selection, paste, screen readers or
  international values.
- **Why:** The interface assumes intent, not precision; if intent is clear but input fails, the
  form failed.
- **Check:** Paste ` John ` with a trailing space; type an email in caps; paste `+1 (555) …`
  and `4111 1111 …`; edit in the middle of a masked field. Runtime or code; a static design can
  only show whether the hint copy demands an over-strict format.
- **Severity:** blocking
- **Tells:** "Invalid format" on a valid value; a strict regex on a free-text field; a mask that
  jumps the cursor.
- **Catalog:** D-12, D-14

### Never block paste, typing or zoom
- **Rule:** Inputs accept paste (passwords, one-time codes, card numbers, email), accept free text
  and validate afterwards rather than filtering characters as typed, and the viewport never caps
  zoom. Fix input zoom on iOS by keeping input text at 16 px, not by disabling zoom.
- **Why:** Password managers, one-time-code autofill and screen magnifiers are the user's tools;
  fighting them is a failure.
- **Check:** Paste into every password and code field; type invalid characters; pinch-zoom the
  page. In code: paste handlers, viewport scaling, input font size. Runtime or code only.
- **Severity:** blocking
- **Tells:** paste prevented; characters filtered as typed; user scaling disabled; a 14 px input
  that zooms the page on focus.
- **Catalog:** D-09

### Keyboard and autocomplete match the field
- **Rule:** Input type and input mode summon the right keyboard (email, telephone, URL, decimal,
  numeric); an autocomplete purpose is set on every field about the user (name, email, phone,
  address, card, login, one-time code) so browsers and password managers fill it in one tap;
  spellcheck and auto-capitalisation are off on usernames, emails and codes. The numeric keypad
  on mobile as a mechanic: lens 12 · Numeric keypad for numeric input.
- **Why:** The wrong keyboard costs extra taps and format errors on every entry; autocomplete is
  an accessibility requirement and a one-tap form fill.
- **Check:** Focus each field on a phone and observe the keyboard; inspect the autocomplete
  purpose on identity fields; does the password manager offer to fill? Runtime or code; a static
  design can only annotate the intended keyboard. Reference table at the end.
- **Severity:** warning
- **Tells:** a QWERTY keyboard on an amount field; a full keyboard for a 6-digit code; an
  auto-capitalised email; password managers not offering to fill.
- **Catalog:** D-07, D-08

### Identifiers are text, not numbers
- **Rule:** Codes, account numbers, postcodes and other identifiers use a text field (with a
  numeric input mode where useful), never numeric-stepper semantics; leading zeros and long
  values are preserved.
- **Why:** A number field drops `007`, rejects long values and adds stepper arrows nobody asked
  for.
- **Check:** Enter `007`; check the field type in code.
- **Severity:** warning
- **Tells:** a number type on an ID; stepper arrows on a postcode.
- **Catalog:** D-15

### One value, one field
- **Rule:** Phone, card and one-time code are not split into several fields without proven need.
  When a value is visually split, Backspace, paste, arrows and focus movement behave as in one
  field, and a screen reader announces the whole value.
- **Why:** Splitting breaks paste, autofill and editing; the user thinks in one value.
- **Check:** Count fields per value. On a split input: paste the whole value, press Backspace
  across a boundary, read it with a screen reader. Runtime.
- **Severity:** warning
- **Tells:** six one-character boxes that refuse a pasted code; a card number in four fields
  that ignore paste.
- **Catalog:** D-10, D-11

### Autofocus on desktop, never on phones
- **Rule:** On desktop and other pointer-first layouts, focus lands in the first field on load.
  At phone widths — touch input, an on-screen keyboard — autofocus on load is never used; the
  user places the cursor. A "×" to clear every value field is a convention a project may adopt
  and record; recommended for search and filters and for a field whose value is long, but its
  absence is not a defect.
- **Why:** On desktop an empty first field costs nothing and saves a click; on a phone an
  unrequested keyboard covers the screen, and an unexpected focus jump strands a screen-reader
  user with no context.
- **Check:** Load the screen on desktop: does focus land in the first field? Load it at phone
  width: is a keyboard summoned unasked, or does focus jump away from the start of the page?
  Runtime; mark `not-reviewed` on a static design.
- **Severity:** warning
- **Tells:** a phone keyboard covering the page on load; a desktop sign-in or search screen where
  the user must click the field before typing; focus in field three of a ten-field form on
  desktop with no reason.
- **Catalog:** H-05

### Password fields show rules live and accept managers
- **Rule:** Password creation shows the requirements before the first error and marks each as
  met while typing; rules never break password managers (no rejected paste, no arbitrary
  character bans, no maximum below manager defaults); a Show/Hide control has a stable label,
  a clear state and preserves the cursor; the platform password component is used so managers
  recognise the field.
- **Why:** A rule revealed after failure is an error that could have been prevented
  [slips lapses mistakes]; a manager-generated password rejected by an arbitrary rule sends
  the user to a weaker one.
- **Check:** Read the rules list before typing; paste a manager-generated password; toggle
  visibility mid-edit and confirm the cursor stays. Runtime; a static design shows the rules
  list and its met/unmet variant.
- **Severity:** warning
- **Tells:** rules revealed only after a failed submit; "no special characters"; a Show button
  that resets the cursor.
- **Catalog:** D-19, D-20, D-09

### Long text grows; limits are announced
- **Rule:** Long text uses a multi-line field with a reasonable initial height and a way to
  expand; a character limit is shown before it is reached, and approaching or exceeding it is
  announced accessibly, not by colour alone.
- **Why:** A single-line box for a paragraph hides what was written; a limit discovered at submit
  throws work away.
- **Check:** Check the control type and resize affordance; read the counter; inspect the live
  region in code.
- **Severity:** warning
- **Tells:** a one-line input for "Tell us more"; a counter turning red with no text; the limit
  revealed by the error.
- **Catalog:** D-17, D-18

### Dates accept the locale format
- **Rule:** Dates are accepted in the user's locale format with an unambiguous example; direct
  typed input for known dates (birth, document expiry), a calendar picker for nearby
  appointments; never browsing decades back in a picker. Display formats: lens 07.
- **Why:** A date typed in the user's own convention is the one they get right [conventions]; a
  picker for a birth date is forty taps.
- **Check:** Which pattern is used for which date type? Enter a locale date; the hint shows the
  expected order.
- **Severity:** warning
- **Tells:** date of birth via a month-by-month calendar; a month-first order imposed on a
  locale that writes day first.
- **Catalog:** D-21, D-22, M-06

### File upload states before and after
- **Rule:** Before upload: accepted types, quantity and size limits, and a standard picker
  button, with drag and drop as an addition. After: filename, size, progress, result, and
  remove or replace. The same file is never re-uploaded within one process without a security
  or privacy reason.
- **Why:** The user cannot see the file's state unless the interface tells them
  [feedback loop].
- **Check:** Read the pre-upload hint; upload a file; check the post-state; walk the flow
  counting upload prompts for one file.
- **Severity:** warning
- **Tells:** a drop zone with no Browse button; "Upload" with no accepted types; a file that
  vanishes after upload with no name shown.
- **Catalog:** D-27, D-28, D-29

## 3. Submitting and moving through the form

### Submit stays enabled; busy shows beside the label
- **Rule:** Submit is enabled until the request starts, then shows a spinner beside the original
  label at a stable width; validation runs on submit and focuses the first failing field (see
  lens 05 · Error visibility on submit). A disabled state is never the only explanation of what
  is missing; a control disabled because a requirement is unmet says so nearby (see lens 05 ·
  Disabled means unavailable, and says why). Duplicate submission is prevented or idempotent.
- **Why:** A disabled-until-valid submit hides why nothing happens; a bare spinner loses the
  button's name [feedback loop].
- **Check:** Submit an empty form: the interface explains, not ignores. Trigger the busy state
  and measure width before and after. Double-click and count records. Runtime.
- **Severity:** warning
- **Tells:** a greyed-out submit with no explanation; a spinner replacing the label; a button
  that shrinks while busy.
- **Catalog:** B-08, B-09, B-10, B-11

### Autosave says its state
- **Rule:** Where a form autosaves, it shows Saving / Saved / Not saved, with the time of the
  last save where it matters; a failed save is stated, never silent.
- **Why:** Unsure whether work is saved, the user redoes it or loses it [feedback loop].
- **Check:** Edit, wait, look for the status text; fail the save. Runtime.
- **Severity:** warning
- **Tells:** no indication at all; "Saved" that stays after a failed request.
- **Catalog:** D-36

### Multi-step forms show purpose and preserve answers
- **Rule:** Each step names its purpose; overall progress is shown without false precision under
  branching; Back (in-app, browser or system) returns to the previous step with answers
  preserved and never breaks the flow; large forms are grouped by meaning, and short dependent
  questions are revealed progressively. Lost answers on Back are covered by lens 05 · Slips
  cannot commit, and work is never lost silently; indicator honesty by lens 05 · Progress is
  honest.
- **Why:** The user models what remains [predictive brain]; a Back that loses answers punishes
  checking.
- **Check:** Read the step indicator; does the total change with branches? Use browser or system
  Back mid-form. Look at section headings and conditional reveals.
- **Severity:** warning
- **Tells:** "Step 2 of 3" then "Step 2 of 5"; browser Back ejecting to the home page; every
  conditional question visible at once.
- **Catalog:** D-30, D-31, D-32, G-04, G-05

### No auto-advance; Next moves forward
- **Rule:** Focus never jumps between ordinary fields on reaching a length; predictable
  one-time-code or date entry may advance only if keyboard users keep control. On mobile the
  return key reads Next and moves to the next logical field; Done submits only when submitting
  is safe.
- **Why:** An unrequested focus jump breaks editing and disorients; a Done key that submits half
  a form loses work.
- **Check:** Type to a field's maximum length: focus must not jump. Check the return-key type
  per field. Runtime.
- **Severity:** warning
- **Tells:** focus jumping out of a date field mid-correction; "Go" on a field in the middle of
  a form.
- **Catalog:** D-33, D-34

### The keyboard covers nothing the user needs
- **Rule:** With the on-screen keyboard open, the active field, its hint, its error and the
  primary action stay visible and the screen scrolls to keep them so; a sticky action bar or a
  status message never covers content, the keyboard or an error.
- **Why:** A field the user cannot see cannot be corrected.
- **Check:** Focus the last field with the keyboard open; trigger an error with the keyboard
  open. Runtime on a device; mark `not-reviewed` on a static design.
- **Severity:** blocking
- **Tells:** submit hidden behind the keyboard; an error under a sticky footer; a toast over the
  keyboard.
- **Catalog:** D-35, B-18, F-11

## 4. Choice controls

### Checkbox for many, radio for one
- **Rule:** Checkbox for an independent binary or a multi-select; radio for exactly one of a
  mutually exclusive group (at most one selected; selecting a new one deselects the previous).
  Shapes follow convention: square checkbox, round radio. Options are vertical by default,
  horizontal only for short, comparable, non-wrapping options; where returning to "none" must
  be possible, an explicit None option, never a radio re-click. Space toggles a checkbox;
  arrows move within a radio group. A radio is preselected only for a safe, honest, likely
  default, never for consent, a donation, a paid option or a sensitive choice. Changing a radio
  or a tab never triggers a critical action: selection stays separate from confirmation.
- **Why:** The control's shape tells the user how many answers are expected before they tap
  [conventions] [affordance and signifier].
- **Check:** Map each control to its selection model; try to select two radios; check the layout
  at narrow width; inspect the default state of each group; change an option and look for side
  effects. Design file for shape and defaults; runtime for keyboard and side effects.
- **Severity:** blocking (a second selectable radio, a selection that commits, a paid or consent
  option preselected); warning for shape and layout
- **Tells:** checkboxes on a single-answer question; two radios selected; a horizontal radio
  group wrapping on a phone; a pre-ticked add-on.
- **Catalog:** C-01, C-02, C-05, C-06, C-07, C-08, C-12, C-30

### Options and groups are labelled; the whole label is the target
- **Rule:** Each checkbox, radio or switch has its own visible label next to it, and each group
  has a shared label or legend. The label is part of the tappable area; a whole row or card
  toggles the control only when the container reads as one option and holds no second primary
  action.
- **Why:** A dead zone between control and label collects failed taps [Fitts's law]; a group
  without a legend is a list of unrelated questions to a screen reader.
- **Check:** Click the label text: the control toggles. Count primary actions in a toggling
  row: more than one fails. Look for groups without a heading. Target sizes: lens 10.
- **Severity:** blocking (an unlabelled control or group); warning (a label that is not part
  of the target)
- **Tells:** a bare checkbox beside "I agree" that toggles only on the box; a card that both
  opens details and selects on any tap.
- **Catalog:** C-03, C-04, A-07, A-08, A-09

### Mixed state and selection limits are visible
- **Rule:** An indeterminate (mixed) checkbox looks different from both checked and unchecked,
  visually and in the accessibility tree; a parent checkbox controls its group and stays in
  sync with the children; a "select no more than N" limit is shown before interaction and, at
  the limit, the interface says a selection must be cleared.
- **Why:** A mixed state drawn as checked misreports the group; a limit discovered by a dead
  click is an unexplained failure.
- **Check:** Compare the three states side by side; toggle children and parent; hit the limit
  and read the message.
- **Severity:** warning
- **Tells:** a mixed state drawn as checked; a parent that stays unchecked after all children
  are ticked; a fifth option that silently refuses.
- **Catalog:** C-09, C-10, C-11

### Switches change state now and say which state
- **Rule:** A switch controls a persistent on/off state and shows the current state; it is never
  a one-time command. It takes effect immediately; if a Save step is needed, use a checkbox.
  The label stays stable across states ("Notifications", with On/Off shown by position), never
  "Enable" ↔ "Disable"; the state is shown by knob position and shape, not colour alone;
  tapping the switch or its label is the primary method and finger drag is optional. If the
  update fails over the network, the switch returns to the true state and says the change was
  not saved (see lens 05 · Success is confirmed, not assumed).
- **Why:** A switch is a promise that the world changed when it moved [feedback loop]; a
  flipping label makes the state a double negative.
- **Check:** Does the switch trigger an action rather than a state? Is a Save button gating it?
  Toggle and read the label; greyscale the two states; tap the label; fail the request.
- **Severity:** warning
- **Tells:** a "Send report" switch; a switch that needs Save; "Disable notifications" as a
  switch label; on/off told only by green versus grey.
- **Catalog:** C-13, C-14, C-15, C-16, C-17, C-18

Segmented controls and tabs (C-19 to C-30) are components: lens 11.

## Reference tables

### Keyboard and autocomplete by field (D-07, D-08)

| Field | Input type or mode | Autocomplete purpose | Also |
|---|---|---|---|
| Email | email | email | spellcheck and auto-capitalise off |
| Phone | telephone | telephone | accepts `+`, spaces, hyphens, parentheses |
| URL | url | url | auto-capitalise off |
| Amount, quantity | text with decimal or numeric input mode | — | numeric keypad; never a stepper for identifiers |
| One-time code | text with numeric input mode | one-time code | paste allowed; spellcheck off |
| Name, address, card | text | the platform's name, street address, postal code and card purposes | one-tap fill |
| Username | text | username | spellcheck and auto-capitalise off |
| Password | password | new password / current password | paste allowed; Show/Hide |

### Target sizes for form controls (floors and exceptions: lens 10)

| Context | Minimum | Recommended | Catalog |
|---|---|---|---|
| Web (WCAG 2.2 AA) | 24 × 24 CSS px, or equivalent spacing | 44 × 44 on touch; 40 × 40 on desktop | A-03 |
| iOS | — | 44 × 44 pt, even when the glyph is smaller | A-04 |
| Android | — | 48 × 48 dp | A-05 |
| Adjacent controls | ~12 px clearance between bordered controls; ~24 px around borderless ones | — | — |

### Sizes and expansion

| Item | Value | Catalog |
|---|---|---|
| Input text size on mobile | 16 px, so the page does not zoom on focus | — |
| Text expansion under translation | layouts tolerate 30–50 % longer strings without clipping | M-09 |
| Character limit | shown before it is reached; announced, not colour-only | D-18 |
| Segmented control | 2–5 short options; longer lists need another control (lens 11) | C-19 |
