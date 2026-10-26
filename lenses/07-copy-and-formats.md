# Lens 07 — Copy and formats

Checks the words and the numbers: one voice with a tone that follows the stakes, strings that
name what they act on, titles that promise, and one format per product for numbers, money,
dates and times, locale-aware by default. Order: read every string in the flow as a list
(buttons, links, toggles, titles) → then the numbers and dates → then localisation tolerance.
Error wording and recovery live in lens 05; twin-screen string drift in lens 02.

## Voice and wording

### One voice, flexible tone
- **Rule:** Read the surrounding copy before writing or reviewing: the product has one voice, existing copy defines it, and a local edit does not invent a new one. One term per concept ("Archive" in the menu is not "Move to storage" in the toast), in the user's domain language, never internal database, endpoint or process names. Tone flexes with stakes: warm and light for success, onboarding and empty states; neutral and minimal for routine actions; calm, plain and never playful for errors and destructive confirmations, with no "oops", no exclamation marks and no blame; serious and explicit for data loss and security. A deliberate brand voice is not a defect unless it creates ambiguity, inconsistency, translation risk, or a tone the stakes do not support. Rewording has a limit: an error that keeps firing is an interaction defect, not a copy defect.
- **Why:** Alternating synonyms make users wonder whether two things are different [mental models]; a joke in an error message is a joke at the user's expense.
- **Check:** List every label for the same action and every name for the same object across the flow; scan copy for internal jargon; read errors aloud. (error wording, placement and recovery: see lens 05 · Error copy answers four questions; the same string styled two ways on twin screens: see lens 02 · Same string, same style on twin screens)
- **Severity:** warning
- **Tells:** "Oops!" errors; "Continue" here, "Next" there, "Proceed" elsewhere; an endpoint name in a heading.
- **Catalog:** M-01, M-02

### Plain words, direct address, no assembled sentences
- **Rule:** Words a tired reader gets on the first pass; delete every word that does no work; no idioms, colloquialisms or untranslatable humour. Write "you", not "the user"; avoid "we" in errors ("Unable to load content", not "We're having trouble"); possessives sparingly ("Favorites", not "Your Favorites"); one perspective per flow. Match the input device ("tap", "click", or "select" when both apply). Skip unnecessary gender. Never build a sentence from fragments around a variable; use a full templated string with pluralisation.
- **Why:** Jargon costs a second read [processing fluency]; "we" reads as deflection; word order changes per language, so fragments do not translate.
- **Check:** Read each string for a word to cut; in code, search for string concatenation around counts and names. A static design shows the words; concatenation needs the code.
- **Severity:** warning; blocking for concatenated strings in a localised product
- **Tells:** "Please kindly note that"; `"You have " + n + " items"`.
- **Catalog:** M-01, M-06

### Every string has one role
- **Rule:** The label names the object; the helper explains the format or the reason, phrased positively and shown before the mistake; the button names the action; the error explains the problem and the fix. No string does two of these jobs.
- **Why:** Each role is read at a different moment (before typing, while typing, after failing); a string that serves two moments serves neither [cognitive load].
- **Check:** Classify each text element by role; find helpers phrased as prohibitions or shown only after the error; find buttons labelled with the object instead of the action.
- **Severity:** warning
- **Tells:** a hint that appears only after the error; a button labelled "Password" instead of "Save password"; a label that explains the format and leaves the object unnamed.
- **Catalog:** M-04

### Verb-first buttons that repeat the consequence
- **Rule:** A button label starts with the verb naming its action ("Send", "Save draft", "Delete project"); never "OK!", "Let's go!", "Yes"/"No" on anything consequential. A confirmation dialog is answerable without reading its body: "Delete this project?" offers "Delete project" and "Cancel". A multi-step flow uses one vocabulary throughout ("Get started" to enter; "Continue" or "Next", pick one, to advance; "Done" to finish).
- **Why:** Users act on the button, not the paragraph; a generic label forces them to read everything.
- **Check:** Cover the dialog body and ask whether the buttons alone say what happens; read the flow's buttons in sequence without the screens. (the next step and the amount on the primary button: see lens 05 · CTA names the next step; confirmation mechanics: see lens 05 · Destructive safeguard)
- **Severity:** warning; blocking for a destructive action with a generic label and no distinct treatment
- **Tells:** "Are you sure?" with Yes/No; "Submit" for everything.
- **Catalog:** E-13, M-04

### Links say where they go; toggles describe ON
- **Rule:** Link text makes sense out of context ("Read the billing docs"); "Click here" and bare "Learn more" fail, and each "Learn more" on a page gets a suffix. Link straight to a referenced setting instead of describing the path to it. Label a toggle or checkbox for what happens when it is on ("Send read receipts"), never with a negative or a double negative. Name navigation items for their contents ("Library", "Progress"), not vague umbrellas ("Home").
- **Why:** Screen-reader users navigate by a list of links; a negative toggle is a double negative; a specific label lets the reader predict what follows [predictive brain].
- **Check:** Extract all link texts and read them as a list; read each toggle and checkbox label with "on" appended; read checkbox labels for "not" and "disable".
- **Severity:** warning
- **Tells:** three "Learn more" on one page; "Don't show notifications" as a switch; "Go to Settings > Notifications > Email".
- **Catalog:** M-05

### One capitalisation policy
- **Rule:** Title case or sentence case per element type, applied to every instance; sentence case is the safer default (calmer, no per-word rules, localises cleanly). No all caps for labels or messages longer than a few words. Store copy in natural case and transform with CSS.
- **Why:** "Save Changes" beside "Discard changes" reads as sloppiness; a long run of capitals is read letter by letter [letter recognition].
- **Check:** List all buttons and headings and look for mixed policies; find uppercase strings longer than a few words. (caps and tracking as a tone device: see lens 02 · Tracking is a tone knob, never a fit tool)
- **Severity:** warning
- **Tells:** mixed case within a single toolbar; a paragraph in capitals.
- **Catalog:** M-10

### Every screen answers four questions
- **Rule:** From what is visible, every screen answers: Where am I? Where can I go? What is here? How do I get out? The interface feeds back in four kinds: it confirms completed actions, exposes ongoing status, warns before problems, and validates inline rather than on submit.
- **Why:** A screen without wayfinding is a maze; the reader builds a map of the product from what each screen names [mental models].
- **Check:** Answer the four questions from the screen alone: a title, a route onward, the content named, a way back or out. (action feedback and status: see lens 05 · Status escalates; trapped terminals: see lens 05 · No dead ends; confirmation only for destructive actions: see lens 05 · Destructive safeguard)
- **Severity:** warning
- **Tells:** a detail page with no title and no back route; "Are you sure?" on every save.

## Titles, emphasis and empty states

### Title is action or promise
- **Rule:** A screen title is what the user does or gets here, not the name of the section. The subtitle continues the title; it does not repeat the breadcrumb or the title.
- **Why:** A section name orients, a promise motivates; the user already knows the section from the navigation.
- **Check:** Title and subtitle read together as one thought; the subtitle contains new information.
- **Severity:** note
- **Tells:** title "Settings", subtitle "Manage your settings".

### Hero answers the core question
- **Rule:** On a status or detail screen the largest text answers the question the user came with ("On its way", "Action needed"); the identifier (order number, id) is demoted to meta.
- **Why:** The largest text is read first [gist first]; the id is for support, the answer is for the user.
- **Check:** Find the largest text on the screen: is it the answer or the identifier?
- **Severity:** note
- **Tells:** "Order #A-10482" as the headline with the status in a pill below.

### Emphasis by weight, not colour
- **Rule:** Emphasis inside a paragraph is carried by weight (the first phrase bolder, the rest secondary), not by colour, and never by making a phrase a heading.
- **Why:** Colour inside running text pops out and competes with links and status [pre-attentive pop-out]; weight keeps the paragraph one object.
- **Check:** Any coloured spans inside body text that are not links? Any paragraph broken into headings?
- **Severity:** note
- **Tells:** a brand-coloured sentence inside a paragraph; a paragraph broken into three headings.

### Empty-state copy points forward
- **Rule:** An empty state says what this place is, how to fill it, and offers one next action the user can actually perform; a search or filter empty state names the query and offers an exit ("No results for 'quarterly'. Clear filters"). Never park persistent information in an empty state, because it disappears once content exists. A placeholder shows the expected format and is never the only label.
- **Why:** "No results." is a shrug; a placeholder vanishes on the first keystroke.
- **Check:** Render every list at zero items and read the copy; confirm the offered action is available to this user; find onboarding instructions that live only in the empty state; find fields whose only label is a placeholder. (the five kinds of nothing and the empty state's shape: see lens 05 · Five kinds of nothing, lens 05 · Empty state shape)
- **Severity:** warning; blocking when the empty state hides the only way to proceed
- **Tells:** "No data"; onboarding instructions living only in an empty state; "Email" as placeholder with no label.
- **Catalog:** M-11, D-02

### Placeholder copy is flagged
- **Rule:** Placeholder or draft copy ("Lorem", "Answer option", "TBD", a foreign-language line, a test name) is marked as such on the artifact and listed in the review; it never reaches handoff unmarked.
- **Why:** Unflagged placeholders ship.
- **Check:** Grep the text layers or the DOM for known placeholder strings and for copy that contradicts the screen.
- **Severity:** warning
- **Tells:** "Answer option 2" on a production mockup; a step title from another product.

## Formats and localisation

### One number format per product
- **Rule:** Currency, numbers, percentages and units are formatted one way across the product: decimal and thousands separators, currency symbol position and spacing, decimals on prices, "%" placement, "/month" placement, the minus sign before a discount. Formats are locale-aware by default; a fixed house format is a project decision recorded in the project's decisions log. Either way, one format per product, and never two formats on one screen.
- **Why:** A format that changes reads as two different numbers; if users must count digits or question precision, numeric UX has failed.
- **Check:** Collect every money, number and percentage string in the flow and diff the formats; check each against the locale's rules or the logged house format; in a build, switch locale and re-check. A static design proves consistency; locale behaviour needs a build. (digit grouping: see lens 06 · Chunk long strings and long forms)
- **Severity:** blocking when two formats meet on one screen, a price shows the wrong number of decimals, or a number is ambiguous; warning for drift across screens of one flow
- **Tells:** "$37" here and "37$" there; "30 000 000" next to "1,000"; `$ 12`; `12,5 %`; four decimals on a price.
- **Catalog:** M-06

One house format, as an example of a fixed decision (a locale-aware product substitutes the locale's separators and keeps the principle):

| Element | Rule | Correct | Incorrect |
|---|---|---|---|
| Decimal separator | `.` | `1,234,567.89` | `1.234.567,89` |
| Thousands separator | `,` every 3 digits | `12,000` | `12000` / `12 000` |
| Currency | symbol before value, no space, 2 decimals by default | `$1,234.56` | `1234.56 $`, `$ 1,234.56`, `$1,234.5` |
| Percent | `%` after number, no space, 0–1 decimals unless justified | `12.5%` | `12,5 %`, `12.500%` |

### One date and time format per product
- **Rule:** Dates carry the month as a word (`DD MMM YYYY`), time is `HH:mm` 24-hour, combined `DD MMM YYYY · HH:mm`, or the locale's equivalent when formats are locale-aware; numeric-only dates are forbidden on user-facing surfaces. Relative time ("5 min ago") is optional and never replaces an audit timestamp; the time zone is shown when it matters. One format per product, recorded in the decisions log if fixed.
- **Why:** `07/01/2026` is ambiguous across locales; a misread date is a wrong decision.
- **Check:** Search the screen for `\d{1,2}[./-]\d{1,2}[./-]\d{2,4}`; find AM/PM mixed with 24-hour; find relative times on records with no absolute time; find times that cross zones with no zone shown.
- **Severity:** blocking
- **Tells:** `01/07/26`; AM/PM mixed with 24h; "yesterday" on a transaction record with no absolute time.
- **Catalog:** M-06, D-21

| Element | Format | Example |
|---|---|---|
| Date | `DD MMM YYYY` | `07 Jan 2026` |
| Time | `HH:mm` (24h) | `14:30` |
| Date + time | `DD MMM YYYY · HH:mm` | `07 Jan 2026 · 14:30` |

### Sensitive data during input
- **Rule:** Highly sensitive data is masked by default with an explicit user-controlled reveal; sensitive values never appear in errors, confirmations or logs; values do not persist on screen after submit or failure longer than necessary; autofill, copy, paste and screen capture are handled deliberately.
- **Why:** Security is a UX responsibility, not only a backend concern.
- **Check:** Card, ID and password fields masked with a reveal control? Any error or confirmation echoing the value? A static design shows masking and the reveal; echo in errors and persistence need a build.
- **Severity:** blocking
- **Tells:** the full card number in the confirmation; "Email x@y.z not found".

### Addresses, plurals and time zones localise too
- **Rule:** Beyond numbers and dates, addresses and plural forms follow the user's locale, and the time zone is shown when it matters.
- **Why:** A value in the wrong locale reads as a different value, or as a foreign product.
- **Check:** Switch locale in a build; check address forms, counts at 0, 1, 2 and 5, and timestamps that cross zones. A static design cannot prove this; mark not-reviewed.
- **Severity:** warning
- **Tells:** one plural form for every count; a postcode field in the wrong slot for the locale; a meeting time with no zone shown to a user in another one.
- **Catalog:** M-06

### Layouts tolerate text expansion
- **Rule:** Layouts tolerate 30–50 % text expansion without clipping or overflow.
- **Why:** Translated strings run longer than the source; a layout sized to one language breaks in the next.
- **Check:** Pseudo-localise with +50 % length; on a static design, lengthen the longest label by half and see what wraps or clips.
- **Severity:** warning
- **Tells:** a button whose label is cut in the first translation; a tab bar sized to four-letter words.
- **Catalog:** M-09

### RTL adapts direction
- **Rule:** In a right-to-left locale, layout direction, navigation order, directional icons and gestures mirror; numbers and brand marks are tested separately, since they do not mirror.
- **Why:** Reading direction sets where "next" and "back" are [reading eye movements] [conventions].
- **Check:** Run in an RTL locale; a static design cannot prove this; mark not-reviewed. (which icons mirror: see lens 11 · Mirror only direction-bound icons in RTL)
- **Severity:** warning
- **Tells:** a back arrow pointing the wrong way in RTL; a mirrored logo; a progress bar filling from the wrong side.
- **Catalog:** M-08

### Page language is declared in code
- **Rule:** The page language and the language of any fragment in another language are set in code.
- **Why:** Assistive technology picks pronunciation and hyphenation from the declared language; the wrong one reads text as noise.
- **Check:** Inspect the html lang attribute and lang on fragments; a static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** a page with no lang; a quoted foreign phrase read in the page's language.
- **Catalog:** M-07
