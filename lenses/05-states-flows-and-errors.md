# Lens 05 — States, flows and errors

Checks, in order: the scenario model that says which states must exist; the states themselves;
destructive paths; error copy and surface; flow structure; status and feedback; the five-case
stress set. Pre-tests: greyscale the screen, list every terminal screen, throttle the network
where a build runs. A static design proves a state is drawn, not that runtime reaches it: mark
runtime checks `not-reviewed`. Error wording lives here; product voice is lens 07; announcement
and focus mechanics are lens 10.

## 1. Scenario coverage

A list of states answers "what exists". It does not answer why a state occurs, how an earlier
choice changes a later screen, which combinations are impossible, or which branch is covered.
The scenario model does, and keeps the combinatorics from drowning the review.

### Scenario dimensions
- **Rule:** Before judging states, list the independent axes that change interface behaviour,
  each with a domain of values and a risk level: `critical` (can block the user or money) or
  `standard`.
- **Why:** A state is a consequence of a value on some axis; without the axis the critic cannot
  say whether a state is reachable or which of its neighbours are missing.
- **Check:** The review lists the dimensions and their values for the flow before it lists
  states. A state whose axis the critic cannot name is unexplained. Any input type.
- **Severity:** warning
- **Tells:** "loading / error / empty" pasted under every screen identically; no persona or
  session axis on a flow that clearly has guests and members.

| Dimension | Domain |
|---|---|
| `persona` | role, permissions |
| `session` | signed in or not, new or returning |
| `data` | 0 / 1 / many / corrupted |
| `environment` | viewport, offline, slow network |
| `flow` | choices made earlier on the path |
| `screen` | local outcomes: success / validation error / server error |

Risk is assigned per axis by the product: an axis that can block the user or money is `critical`.

### Scenario constraints
- **Rule:** Kill the impossible before enumerating: `exclude` rules (this combination cannot
  occur) and `require` rules (if X, then Y is mandatory) cut the raw matrix to the valid space.
  Do not enumerate spaces above roughly 50 000 raw combinations; cut dimensions and say so.
- **Why:** The full Cartesian product grows exponentially and is mostly nonsense; constraints are
  where the product logic lives, and a review that skips them reviews fiction.
- **Check:** Each constraint is written down with its reason; the valid count is stated next to
  the raw count.
- **Severity:** note
- **Tells:** a coverage table with rows like "guest + admin permissions"; "all combinations
  covered" with no number.

### Scenario cases
- **Rule:** Each scenario has a name, a priority (`critical` / `standard`), one concrete value on
  every dimension, a path through the screens with the expected state on each, and an outcome:
  `completed` / `blocked` / `recoverable_error`.
- **Why:** A scenario that leaves a dimension unassigned is a family of scenarios, and a family
  cannot be walked; the outcome is what reveals whether the end of the path is a dead end.
- **Check:** Walk the path on the artifact; every screen on it exists in the declared state.
- **Severity:** warning
- **Tells:** scenarios named after screens rather than after situations; a path with a gap
  ("…and then somehow the order page").

### Scenario coverage rules
- **Rule:** Run five deterministic checks, line by line:
  1. every required state of every screen is reached by at least one declared scenario through
     a valid transition (reached, not merely listed);
  2. every value of every critical dimension appears in at least one scenario;
  3. every pair of values from different dimensions appears at least once in the valid space
     (pairwise suffices; a full matrix is not needed);
  4. every scenario ending in `blocked` or `recoverable_error` ends on a screen with an explicit
     next step;
  5. flow invariants (true along the whole path: "the full price is always visible", "progress
     is never lost") are listed, each with the scenarios that confirm it.
- **Why:** These are the minimum that turns "we thought about edge cases" into a claim someone
  can falsify.
- **Check:** A coverage table: scenario → screens/states → covered? Gaps are logged as findings
  with a suggestion, never silently dropped; standard-priority pairwise gaps are logged too.
- **Severity:** warning (blocking when a critical dimension has an uncovered value)
- **Tells:** an error state no scenario reaches; a blocked scenario whose last screen has no
  action; an invariant nobody wrote down but everyone assumes.

### Coverage is declared, not executed
- **Rule:** Coverage proves that every corner case is designed and reachable through declared
  transitions; it does not prove that shipped code behaves this way. Say which one was verified.
- **Why:** A design review inspects what is drawn or written; runtime behaviour needs the running
  product.
- **Check:** The report says "declared coverage" or "observed on the live product", never a
  blend.
- **Severity:** note
- **Tells:** "all states verified" written after looking only at a design file.

## 2. States

### State vocabulary
- **Rule:** Use one shared vocabulary for states: `default · loading · empty · validation_error ·
  server_error · success · permission_denied · custom`; `custom` is always named ("out of
  stock", "pending approval"). On mobile the same words apply; the book's four mandatory mobile
  states (loading, empty, error, success) are the same states under the same names.
- **Why:** The same word on every screen is what lets the critic count; two teams calling one
  thing "empty" and "zero state" produce two half-counts.
- **Check:** Every screen card lists which of the eight the screen shows and which are required
  but absent.
- **Severity:** note
- **Tells:** states named after the visual ("grey screen") or after the ticket.

### Required states present
- **Rule:** A screen that loads data shows `loading`, `empty` and `server_error`; a screen that
  accepts input shows `validation_error` and `success`; a screen behind a permission shows
  `permission_denied`. Every screen defines at least loading, empty, error and
  success/confirmation, and on mobile all four are mandatory on every screen. A missing required
  state is a finding, never an assumption.
- **Why:** The unhappy states are where users decide whether to trust the product, and they are
  the states nobody draws unless made to; a state that is not designed does not exist.
- **Check:** Against the scenario model: which states are required here, which are present. In a
  design file, count the variants per screen; the empty state has a next step and the error
  state has a recovery. On a live product, reach each state.
- **Severity:** blocking
- **Tells:** only the populated variant exists; a list screen delivered with three tidy rows; a
  form with no error variant; a spinner with no skeleton; "No data" with nothing to do.
- **Catalog:** I-17, N-10

### Every component ships every state
- **Rule:** A new component or variant covers hover, focus, active, disabled, loading, selected,
  empty, error and narrow width, on every surface that carries its peers. A state applied to
  some instances and not others is an incomplete change.
- **Why:** The absent state is what breaks in production, and a surface review cannot see what
  is missing.
- **Check:** Enumerate the states the component accepts and render each; list the surfaces that
  carry its siblings and confirm the change reached them. States that differ in meaning never
  look identical side by side.
- **Severity:** warning
- **Tells:** a new size with no disabled style; a control added to one screen but not to the
  sibling screens that already have its peers.
- **Catalog:** A-15

### Five kinds of nothing
- **Rule:** Five distinct nothings, each with its own shape and action: `first use` (nothing
  exists yet; explain what goes here and offer the create action); `no results` (something
  exists; the filter or query found none — show the query, offer to broaden or clear it, no
  create action); `cleared by the user` (minimal, no illustration; offer undo if the clear was
  recent); `unavailable or locked` (say what it does and what unlocks it); `load failure` (the
  product could not find out; say what happened and offer retry). Offline and timeout are load
  failures, never empties. An empty state never offers an action the current user cannot
  perform.
- **Why:** Each cause calls for a different action (create something / broaden the query / undo
  / unlock / retry); one generic "Nothing here" forces the user to guess which situation they
  are in.
- **Check:** Find all five. First use offers the first action; no-results names the query or
  filter and offers to clear it; cleared offers undo when recent; unavailable or locked names
  the unlock path; load failure says what happened and offers retry. Go offline on a build and
  read the state; a static design can show the drawn variants only.
- **Severity:** warning
- **Tells:** one illustration and one sentence reused for all five; a search with zero hits
  showing the onboarding "add your first item" copy; a failed fetch rendered as an empty list;
  a "Create" button on an empty state shown to a role that cannot create; a cleared list with
  no undo though the clear just happened.
- **Catalog:** I-17, G-12, M-11, N-10

### Empty state shape
- **Rule:** An empty state is quiet: one illustration or none, one heading, one sentence, one
  primary action that creates the missing thing. The heading is section-level, not the page
  title (the page already has one). Persistent instructions never live only in the empty state
  (see lens 07 · Empty-state copy points forward).
- **Why:** The empty state is a prompt, not a celebration and not an error; one action keeps it
  a prompt.
- **Check:** Count the actions and headings on it. Static design suffices.
- **Severity:** note
- **Tells:** two buttons; an empty state with a title bigger than the page title; three
  paragraphs of explanation.
- **Catalog:** M-11

### Loading preserves layout and names the outcome
- **Rule:** A loading state either reserves the space the content will take (a skeleton matching
  the final geometry, not imitating interactivity, not stealing focus on load) or names what the
  user will get ("Finding the best match"); the updating region is marked busy and announced
  politely, and every spinner has an accessible name. On a background refresh stale data stays
  visible with an unobtrusive updating mark, never a spinner over content; on a slow network
  structure or cached content appears before an empty screen with an endless spinner.
- **Why:** A spinner is a promise with no object; content that jumps when it arrives is the
  visible cost of a lazy loading state; an unnamed spinner is silence to a screen reader
  [feedback loop].
- **Check:** Throttle the network and watch the layout as data lands; every loading state either
  preserves layout or names the result; read the busy region with a screen reader. A static
  design can show the skeleton and the copy; announcement and shift are runtime, mark
  `not-reviewed`.
- **Severity:** warning
- **Tells:** a bare spinner in the middle of a blank screen; "Loading…" as the only text;
  shimmer blocks the wrong size; a page that reflows twice while loading; a determinate bar
  whose percentage is invented.
- **Catalog:** F-02, F-03, F-04, F-05, F-06, N-08, N-09

Feedback scales with the wait (measured performance targets are in lens 13; press states in
lens 09):

| Wait | What the user must see | Catalog |
|---|---|---|
| within ~100 ms | input was received: pressed state, local change, or progress | F-01, A-16 |
| under ~1 s | local feedback is usually enough | F-02 |
| longer | an explicit loading state | F-02 |
| lengthy | progress or stages, a way to keep working, and where the result will land (kept in notifications or history) | F-02, F-13 |

Determinate progress only when a truthful percentage exists; otherwise indeterminate (F-03).

### Selected and disabled survive greyscale
- **Rule:** A selected option is marked by more than colour (border, fill, a control state, a
  check); a disabled option is dimmed, present and still readable.
- **Why:** Interactivity and state must survive a greyscale view [colour vision deficiency]; a
  control the user cannot see is a control the user cannot understand.
- **Check:** Greyscale the screenshot: can the critic still tell selected from unselected and
  disabled from enabled? Static design suffices.
- **Severity:** blocking
- **Tells:** selection shown only by a colour tint; disabled buttons at 20 % opacity with
  unreadable labels.
- **Catalog:** A-11, A-15, L-03, C-16, C-20

### Disabled means unavailable, and says why
- **Rule:** Native disabled only for controls that are genuinely unavailable; when the control
  must stay focusable (for a tooltip or discoverability) use an aria-disabled pattern with
  activation blocked in code, never both. The reason a control is off is visible nearby; a
  disabled state is never the only explanation of what is missing. Disabled controls are
  contrast-exempt but kept legible.
- **Why:** A natively disabled control cannot receive a tooltip for keyboard or touch users, so
  "why is this off?" goes unanswered.
- **Check:** Hover and tab to every disabled control: can the critic learn why? Fill a form
  wrong: is what is missing stated, or is a grey button the only signal? Runtime for focus;
  static design shows the reason text or its absence.
- **Severity:** warning
- **Tells:** a greyed button with a tooltip nobody on touch can open; a submit disabled until
  valid with no explanation (see lens 08 · Submit stays enabled; busy shows beside the label).
- **Catalog:** B-08, B-09

## 3. Destructive and irreversible actions

### Destructive safeguard
- **Rule:** A destructive or irreversible action is confirmed by a dialog that names the object,
  the scope and the consequence ("Delete the March report? This removes it for all 4 members
  and cannot be undone."). The confirm button repeats the specific verb ("Delete report"),
  never "Yes", "OK" or "Confirm"; the safe action is visible, separated, and holds the default
  and initial focus. Legal, financial, medical and other risky actions get review, confirm and
  correct, or a reliable undo. Typing the object's name is reserved for extremely dangerous,
  rare operations.
- **Why:** The confirmation exists to make the user read what will happen; a generic "Are you
  sure?" is clicked through [warning habituation].
- **Check:** Does the confirmation name the object and the scope? Cover the body: do the buttons
  alone say what happens? Which button is the default, and where does focus land (runtime)?
- **Severity:** blocking
- **Tells:** "Are you sure?" with OK/Cancel; the destructive button pre-focused or styled as the
  primary; delete-all confirmed with the same copy as delete-one; a typed-name ritual on a
  routine operation.
- **Catalog:** E-10, E-12, E-13, E-14, E-15, B-06, B-07, I-10

### Reversible is undo first
- **Rule:** A reversible action does not ask for confirmation; it happens and offers undo.
  Confirmations are reserved for rare, expensive or irreversible consequences; routine safe
  actions never prompt. Prefer a constraint or a safe default over one more warning.
- **Why:** Confirmations for reversible actions train users to click through, which disarms the
  one confirmation that matters [warning habituation].
- **Check:** List every action that prompts; for each, ask "could this be undone instead?".
  Count confirmations on non-destructive actions. Static design suffices.
- **Severity:** warning
- **Tells:** "Archive this?" dialogs; a confirmation before pausing something that can be
  resumed; "Are you sure?" on every save.
- **Catalog:** E-11, E-16

### Slips cannot commit, and work is never lost silently
- **Rule:** An irreversible action never fires on pointer-down; submit is idempotent (a double
  click creates one record, one payment); swipe-to-delete offers undo. Valid input survives
  validation errors, network errors, Back and re-authentication; leaving with unsaved work
  offers save, discard or continue editing; a session about to expire warns first and can be
  extended. "Cancel" (discards an unfinished action) and "Close" (dismisses a view) are labelled
  explicitly wherever their consequences differ.
- **Why:** Human failures are structural [slips lapses mistakes], not stupidity; a defence at
  each layer catches the slip the previous layer missed [layered defences].
- **Check:** Press, drag off, release: nothing fires. Double-click submit and count records.
  Fail a request, press Back, re-authenticate: the typed value is still there. Edit, then
  navigate away. Runtime only; a static design can show the unsaved-changes dialog and the undo
  affordance, and nothing more, so mark the rest `not-reviewed`.
- **Severity:** blocking
- **Tells:** a form that clears on a server error; delete on one accidental swipe; a "Cancel"
  that silently discards an hour of edits; two orders from one impatient double-tap.
- **Catalog:** A-17, B-10, J-05, D-13, D-31, E-09, E-17, E-18, N-12, N-14

### Red is reserved
- **Rule:** The danger colour is spent on two things only: irreversible or destructive actions,
  and field-level validation. A reversible action gets the normal primary; a system error gets a
  calm neutral surface. The colour never carries the risk alone: the label names the
  destructive verb.
- **Why:** Pop-out works only when it is rare [pre-attentive pop-out]; spent on every warning,
  red stops meaning "stop".
- **Check:** List every red element on the screen and classify it: destructive, validation, or
  neither; "neither" is the finding. Greyscale: is the destructive button still identifiable by
  its label? Static design suffices.
- **Severity:** warning
- **Tells:** a red "Pause subscription"; a red banner for "could not load"; red used for
  "required".
- **Catalog:** B-06

### Destructive item is last and quiet
- **Rule:** In a menu or a list of actions the destructive item sits last and is not coloured
  red in the menu itself; the colour appears on the confirmation. A dangerous command is not
  immediately adjacent to a safe one of the same size and style.
- **Why:** Navigation should not be scary; the warning belongs where the decision is taken.
- **Check:** Position and colour of the destructive item in menus; the gap and style difference
  between a destructive and a safe button that sit together.
- **Severity:** note
- **Tells:** a red "Delete account" row in the middle of the settings list; "Delete" and "Save"
  as twin buttons 8 px apart.
- **Catalog:** B-07

## 4. Errors: copy and behaviour

### Error copy answers four questions
- **Rule:** Every error, in text, answers what happened, where, what was saved, and what to do
  next; not every error needs four sentences, but none may leave a question unanswerable from
  the screen. No generic message ("Something went wrong", "Error 500", "Invalid input"), no
  error without a recovery path, and a server error is never presented as the user's mistake.
- **Why:** Errors are the moment users decide whether the product is trustworthy; a message that
  leaves one of the four open sends them to support or away; the failure was structural
  [slips lapses mistakes], so the message is part of recovery, not a verdict.
- **Check:** Read the message and answer the four questions from it alone; "what do I do now?"
  must be answerable. On a build, simulate a server failure: the message must not ask the user
  to fix valid data. Static design: read every error variant.
- **Severity:** blocking
- **Tells:** "Something went wrong"; "Oops"; "Error 500"; an error with no next step; a form
  error that does not say whether the typed data survived; "Invalid input" with no field named.
- **Catalog:** E-02, E-08, M-04

### One problem, one next step
- **Rule:** One error message names one problem and offers one next step. Use the same recovery
  verbs everywhere ("try again", "check", "go back") and the same retry label on every page.
- **Why:** Two problems in one message produce paralysis [cognitive load]; two words for the
  same action produce doubt about whether it is the same action.
- **Check:** Count problems and next steps per message; grep the flow for retry labels.
- **Severity:** note
- **Tells:** "Check your card details or contact your bank or try later"; "Retry" here, "Try
  again" there, "Reload" elsewhere.
- **Catalog:** M-02

### No jargon, no blame, no codes
- **Rule:** No status codes, stack traces, "server", "request", "invalid", "illegal", internal
  object or process names; no exclamation marks; no "oops"; no blame ("you entered", "you
  failed"). It is not the user's job to understand what broke.
- **Why:** Codes and jargon transfer the burden of diagnosis to the user [cognitive load]; blame
  turns a recoverable moment into a confrontation.
- **Check:** Scan messages for numbers, technical nouns and second-person accusations.
- **Severity:** warning
- **Tells:** "Error 500"; "Invalid input!"; "You have entered an incorrect value".
- **Catalog:** M-01

### Error surface matches severity
- **Rule:** Three levels, three surfaces. The user cannot continue: a full page with a fixed
  headline, "your progress is safe", one retry and one support link. A specific action failed
  but the screen is usable: a toast, or a persistent inline message when the error is critical
  or actionable. A field is wrong: an inline message under the field. Never a modal for a
  recoverable field error; never an auto-dismissing toast for a blocked flow. A message sits at
  the level it affects: field error by the field, card status in the card, page alert at the
  top.
- **Why:** The surface tells the user how bad it is before they read a word [gist first].
- **Check:** Classify each error by "can the user continue?" and see whether the surface and
  the placement match. Static design suffices.
- **Severity:** warning
- **Tells:** a blocking failure shown as a toast that auto-dismisses; a modal for a wrong
  postcode; a page-top banner for one field.
- **Catalog:** F-08, F-12

### System error is calm
- **Rule:** A system error (not the user's fault) is presented on a neutral surface with a soft
  accent, a plain headline and body text; no red, no alarm icon, no shouting, and no request to
  re-enter valid data.
- **Why:** The user did nothing wrong; alarm colour tells them they did [framing], and calm keeps
  them on the page.
- **Check:** Is the error page or toast red? Is the icon an alarm? Does the copy point at the
  input? Static design suffices.
- **Severity:** note
- **Tells:** a red banner with a triangle for "could not load your orders"; "check your details"
  after a timeout.
- **Catalog:** E-08

### Validation keeps the value and speaks in text
- **Rule:** A field error keeps what the user typed, marks the field, and says what to change,
  in text beside the field, never by border colour alone. Constraints and format hints appear
  before input. Inline validation fires only after the user had a fair chance to finish (after
  leaving the field or a meaningful pause, then on submit), never on an empty field at first
  focus, and never blocks typing. An error is removed only once fixed; no success mark before
  required validation completes, and not on every ordinary field.
- **Why:** Clearing the field on error punishes the user twice [slips lapses mistakes]; colour
  alone is invisible to many users [colour vision deficiency].
- **Check:** Look at the error variant of every field: value present, text present? Greyscale
  it. On a build: focus then leave an empty field (no error yet); partially fix (error
  remains); count green checkmarks. Programmatic association and announcement: lens 10 ·
  Errors are associated and announced.
- **Severity:** blocking (a cleared value or a colour-only error); the timing rules are warning
- **Tells:** a red border and nothing else; a cleared field; "invalid" without what is valid; an
  error on an untouched field; a checkmark on every field.
- **Catalog:** E-01, E-03, E-05, E-06, E-07, D-13

### Error visibility on submit
- **Rule:** On submit, the first error-marked field is inside the viewport: the view scrolls or
  repositions to it and focus lands on it. With several errors, a summary at the top links to
  each field and focus moves to the summary or to the first error. Submit stays enabled until
  the request starts (see lens 08 · Submit stays enabled; busy shows beside the label).
- **Why:** Users must not search for what went wrong; an error that appears out of view is not
  seen [change blindness].
- **Check:** Submit a long form with the first invalid field above the fold; submit with two or
  more errors; note where focus lands. Runtime; a static design can show the summary and inline
  variants only.
- **Severity:** blocking
- **Tells:** a toast "fix the errors" with no scroll; an error summary at the top with no links;
  focus left on the submit button.
- **Catalog:** E-03, E-04

### Toast behaviour
- **Rule:** A toast sits in a fixed place that covers no control, keyboard, primary action or
  next required step; one at a time (a new one replaces the old, or messages combine by
  priority); it auto-dismisses on a timer proportional to its length with a floor and a ceiling,
  pauses on hover and focus, and a toast carrying an action stays long enough to notice and use
  (on web, an important action is better without auto-dismiss). It is announced politely, can be
  closed with a button and with Escape, never holds the only copy of information the user will
  need later, and its copy states the outcome ("Link copied"), not "Success". Position, motion
  and stacking mechanics: lens 11 · Toasts.
- **Why:** A toast is a courtesy notification; anything the user must act on outlives a timer
  and belongs inline [working memory].
- **Check:** Where does it sit, how many can stack, what does it cover, does anything important
  live only there? Show it with the keyboard open. Timing and announcement are runtime.
- **Severity:** warning
- **Tells:** stacked toasts over the primary button; a 3-second toast holding an order number; a
  "success" toast with a required next step inside it; a toast over the keyboard.
- **Catalog:** F-08, F-09, F-10, F-11, F-16

### Success is confirmed, not assumed
- **Rule:** A success state appears only once the outcome is confirmed, not when the request was
  sent. An optimistic update is used only with a clear, safe rollback; on failure the true state
  is restored and explained (a switch reverts and says the change was not saved). A bulk action
  reports counts succeeded and failed, never a generic "Done".
- **Why:** Success shown early destroys trust in every later message [feedback loop].
- **Check:** Compare success message timing with the server response; fail the request after an
  optimistic update; run a bulk action with a partial failure. Runtime; a static design can only
  show whether a partial-failure variant exists.
- **Severity:** blocking
- **Tells:** "Payment successful" before the response; a toggle that stays on after the save
  failed; "Done" over a bulk action that half-failed.
- **Catalog:** F-07, F-14, F-15, C-18

### Success is quiet
- **Rule:** A success state confirms, says what happens now and what happens next, and points to
  where to go; celebration is understated and the next step is the loudest thing. The
  post-commitment timeline is lens 06 · What happens next.
- **Why:** After a commitment the user wants reassurance and orientation more than confetti.
- **Check:** Does the success screen answer "what now / what next / where to"? Static design
  suffices.
- **Severity:** note
- **Tells:** a full-screen animation with no next step; a success page whose only button is
  "Done".

## 5. Flow structure and anxiety

### Give, then ask
- **Rule:** Before asking the user for anything (data, money, a decision), give them something:
  the result so far, the reason the data is needed, or what will happen next.
- **Why:** Anxiety is relieved before input, not after; a form that opens with a demand converts
  worse than one that opens with a reason.
- **Check:** On every input screen: what precedes the first field?
- **Severity:** note
- **Tells:** a form that begins at the first field; a payment step with no reminder of what is
  bought.

### Form subtitle explains
- **Rule:** The subtitle of a form answers "why is this needed" or "what happens next"; a helper
  under a sensitive field says what it is for.
- **Why:** Explanation is the cheapest anxiety reducer, and it cuts support contacts.
- **Check:** Read the subtitle: does it explain, or merely repeat the title?
- **Severity:** note
- **Tells:** title "Your address", subtitle "Enter your address".

### Recovery primary, exit secondary
- **Rule:** When a flow is interrupted (soft block, error, off-protocol answer), the path back is
  the primary action and the exit is secondary (outline, ghost or text link). Never the
  reverse.
- **Why:** The button hierarchy is a recommendation [defaults]; recommending the exit abandons
  the user.
- **Check:** On every interruption: which action is primary? Static design suffices.
- **Severity:** warning
- **Tells:** a primary "Quit" next to a ghost "Go back"; equal-weight buttons on a recovery
  screen.

### No dead ends
- **Rule:** Every terminal screen of every path (blocked, declined, disqualified, error, empty)
  has at least one explicit next action, and every terminal declared in the product logic has a
  screen.
- **Why:** A dead end is where the session ends.
- **Check:** From the scenario model, list the terminals, open each, find the action. Static
  design suffices for drawn terminals; undeclared terminals need the spec.
- **Severity:** blocking
- **Tells:** a "not eligible" message with no button; a decline branch that exists in the spec
  and not in the design.
- **Catalog:** G-12, M-11

### CTA names the next step
- **Rule:** The primary button names the next step or the reward ("See your plan", "Continue to
  payment"), not a generic verb, and on a payment step it says what will be charged. Verb-first
  labelling in general: lens 07; money disclosure: lens 06 · Money is explicit.
- **Why:** Motivation lives in the verb; certainty about money lives in the label
  [predictive brain].
- **Check:** Read the buttons of the flow in sequence without the screens: can the critic tell
  where each leads?
- **Severity:** note
- **Tells:** "Next", "Next", "Submit"; "Pay" with no amount when money moves.
- **Catalog:** B-02

### Context before action
- **Rule:** An action that affects an object (pause, change, cancel) opens with a card that
  names exactly what will be affected, then one sentence on consequence and reversibility, then
  the options.
- **Why:** It removes the question "is this about the thing I think it is?" before the decision.
- **Check:** First block of the action screen or dialog: is it the object?
- **Severity:** note
- **Tells:** a "Pause" dialog with options and no mention of which subscription.
- **Catalog:** M-03

### Sub-task stays in context
- **Rule:** A sub-task inside a flow (add an address, apply a coupon, change a setting) is an
  overlay over the dimmed page, not a separate screen; it has one primary action and returns to
  where it started, at the same scroll position.
- **Why:** Leaving the page loses context and progress signals [working memory]; a transitional
  state does not deserve its own page.
- **Check:** Does the sub-task navigate away? Does it return to the same scroll position
  (runtime)?
- **Severity:** note
- **Tells:** "Add address" as a full page that lands the user back at the top of checkout.
- **Catalog:** H-01, G-06

### Progress is honest
- **Rule:** Progress indicators show the true structure of the flow: an exact count where the
  user is tracking a commitment ("Shipment 3 of 6"); rhythm without a count where the flow asks
  a series of questions and the number would discourage; no false precision under branching.
  Never a bar that jumps backwards or restarts silently.
- **Why:** Progress is a promise about the remaining effort [predictive brain]; a false one
  breaks trust at the end.
- **Check:** Compare the indicator's steps with the actual number of screens on the longest
  path; does the total change with branches?
- **Severity:** note
- **Tells:** a 4-step indicator over a 9-screen flow; "Step 2 of 3" followed by "Step 2 of 5".
- **Catalog:** D-30

## 6. Status and feedback

### Status escalates
- **Rule:** Status is signalled at the lowest intensity that suffices and escalates only with
  severity or the need for action: a dot and a word for background or binary states; a badge
  when there are three or more states or an action is required; a container border only for
  failure. The same status uses the same colour on every screen.
- **Why:** Colour is spent in proportion to severity; when every state is a filled pill, the one
  that needs action disappears [pre-attentive pop-out].
- **Check:** List statuses across the surface with their treatment and colour; look for
  inversions (a quiet failure, a loud "delivered") and drift (green here, blue there for the
  same state). Static design suffices.
- **Severity:** warning
- **Tells:** a list that reads as a row of coloured pills; the same "shipped" in two colours;
  "failed" as a small grey word.
- **Catalog:** L-03

### One status mark, three scales
- **Rule:** A status appears once per view in the dominant position and is echoed, not repeated,
  at smaller scales (list dot → detail hero → timeline marker). Do not stack a badge, a border
  and a coloured heading that all say the same thing.
- **Why:** A signal repeated at full volume twice is noise; a signal echoed at three scales is a
  system.
- **Check:** Count how many elements on the screen carry the status; keep one loud.
- **Severity:** note
- **Tells:** an alert strip above a heading that already says the same thing in the same colour.

### Calm bad news
- **Rule:** Bad news that is not the user's fault (out of stock, delayed, not available in this
  area) is a calm card at the top with no red and no alarm icon, with the alternative directly
  below it.
- **Why:** Do not frighten; offer a path [framing]. The alternative is the point; the bad news is
  the context.
- **Check:** Is there an alternative? Is it adjacent? Is the card red?
- **Severity:** note
- **Tells:** a red banner "Out of stock" with no alternative; the alternative two screens away.

### Critical instruction is not an error
- **Rule:** A critical instruction inside content ("do not freeze", "take with food") is a muted
  callout, not an alert component and not red.
- **Why:** An instruction is not an error; using the error surface for it devalues both
  [warning habituation].
- **Check:** Classify each alert-styled element: error, warning, or instruction?
- **Severity:** note
- **Tells:** storage instructions in a red alert box.

## 7. The stress test

### Scope one component and infer its axes
- **Rule:** One component per run, restated in one sentence (what it accepts, renders, and where
  it lives). Stress only what varies: keep an axis when the component accepts something that can
  take that shape in production, and say which axes were dropped and why.
- **Why:** A component built against one happy path looks finished until real content arrives;
  running every axis against every component buries the real breaks.
- **Check:** Write the scenario list before building the harness.
- **Severity:** note
- **Tells:** "the settings page" as a component; item-quantity scenarios on a text input.

### The scenario axes
- **Rule:** Content length (empty, one word, typical, several sentences, one unbreakable
  60-character string); content shape (emoji alone and mixed, RTL, mixed direction, diacritics
  and tall scripts, numbers where columns align); quantity (zero, one, realistic, ten times
  realistic); container (a 320 px box, squeezed by a flex or grid sibling, a very wide box);
  state (loading, error, disabled, only where the component has them); environment (dark mode,
  200 % zoom, reduced motion, offered as toggles rather than simulated on the page).
- **Why:** Each axis catches a distinct failure class: collapsed boxes, overflow, line-height
  jumps, blank regions, min-content blowout, unbounded measure, colour-only errors, contrast
  collapse.
- **Check:** Render the real component, untouched, in its real environment, once per scenario in
  a single column with a label above each; widths are fixed containers on the page, never a
  resized viewport. Verdicts come from the entries each break violates; the harness itself
  issues none.
- **Severity:** note
- **Tells:** a harness that restyles or re-themes the component (it observes a different
  component); a rebuilt lookalike instead of the real import.

### Look once, report what visibly broke, name the owning discipline
- **Rule:** One load, one pass; findings are observations ("text escapes the field's trailing
  edge"), never predictions or taste ("spacing feels tight"). Each break names the discipline
  that owns the fix: typography for wrapping and truncation, layout for containers, writing for
  empty-state copy, accessibility for state and zoom, colour for dark mode. "Everything
  survived" plus the scenario list is a complete report; the rendered page stays up as half of
  it.
- **Why:** A predicted failure is a code review in costume; an unowned break starts in the wrong
  place.
- **Check:** Every row in the findings table has an observed symptom and an owning discipline.
- **Severity:** note
- **Tells:** findings phrased as preferences; a clean run padded with suggestions.

### The reviewer's minimum stress set
- **Rule:** Even without a harness, a design review renders or imagines five cases for every
  text-bearing component: the longest realistic string, an unbreakable string, zero items,
  320 px width, and 200 % zoom. Add RTL where the product localises.
- **Why:** These five expose most blocking findings elsewhere in the skill: unreachable
  truncation, clipped content, a missing empty state, horizontal scroll, fixed heights.
- **Check:** Note in the review which of the five were actually observed and which are
  `not-reviewed`.
- **Severity:** note
- **Tells:** mockups showing only "John Doe" and three perfect cards.
