# Lens 06 — Choice, trust and ethics

Checks whether the user can choose knowingly, whether the product earns trust where money,
data and commitment change hands, and whether the choice architecture serves the user.
Order: walk the commitment path and its exit side by side → read every pre-selected control →
count what the user must hold in memory → apply the trust devices on money, data and success
screens → run the dark-pattern list last, as the floor. Pre-tests: squint (banner-shaped
content), grayscale without hover (signifiers).

## Choice and consequence

### Choice with consequence
- **Rule:** Every option in a choice carries its consequence next to it ("Resumes on 15 Oct", "Charged today", "Cannot be undone"). A choice without a consequence is a blind choice.
- **Why:** The user chooses what happens next, not the label; a consequence placed elsewhere must be carried in memory or discovered on a later screen where reversing costs more [working memory].
- **Check:** For each option, find the caption, figure or sentence that says what happens on picking it; it sits inside the option's block, not in a footnote or below the fold. A static design can prove this.
- **Severity:** warning
- **Tells:** bare-noun options ("1 month", "3 months") with the price or the restart date somewhere else; consequence only in a footnote below the fold.
- **Catalog:** M-03

### Defaults are labelled recommendations
- **Rule:** A pre-selected option is a recommendation plus status quo plus saved effort: label it as one ("Recommended", "Most popular") and justify it in the user's interest. Never a silent default that costs more, commits longer, or pre-answers a consent, donation, paid or sensitive question.
- **Why:** Defaults are accepted as given [defaults]; a default that serves the product and not the user is a dark pattern with a checkbox.
- **Check:** List every pre-selected control; note what it costs relative to the alternatives; write its justification in the user's terms; confirm the reason for the pre-selection is visible on screen.
- **Severity:** warning; blocking when the default adds a charge or pre-answers consent
- **Tells:** the most expensive plan pre-selected with no label; an add-on checkbox that starts checked; "renews automatically" only in the terms; a pre-ticked upsell.
- **Catalog:** C-07, M-13

### Dimmed, not hidden
- **Rule:** Options unavailable right now are shown dimmed with the reason, not removed.
- **Why:** The user sees the full shape of the choice and why part of it is closed [recognition over recall]; a missing option reads as a product without it and sends people to support.
- **Check:** Compare the option list across scenarios (region, plan, role, stock): does it shrink silently in some? Every dimmed option has a tooltip or caption saying why.
- **Severity:** note; blocking when the removal steers toward the pricier or profit-side choice (see No dark patterns)
- **Tells:** a plan that exists for some users and vanishes for others with no trace; greyed-out options with no tooltip or caption saying why.

### Control signals the question type
- **Rule:** The control tells the user how many answers are expected before they tap: a checkbox means multi-select and needs an explicit Continue; a radio or a bare tappable option means single-select and may advance on tap. Never the same control for both.
- **Why:** "One or several?" is answered by the shape of the control, not by instruction text [affordance and signifier] [conventions]; a wrong signal makes users miss answers or wait for a button that never comes.
- **Check:** Across the flow: every multi-select shows checkboxes and a Continue; every single-select does not; the same question archetype is not built two ways.
- **Severity:** warning
- **Tells:** checkboxes on a question that accepts one answer; a multi-select with no Continue; radios on one step and checkboxes on the next for the same kind of question.

### Symmetric friction
- **Rule:** Easy to enter means easy to leave. Subscribe and cancel, opt-in and opt-out, buy and return, sign up and delete account are reachable in the same number of steps and at the same visibility. Asymmetry is legitimate only in the user's defence (confirming an irreversible deletion), never for revenue.
- **Why:** Friction that points one way spends the user's effort against them; it is the definition of a dark pattern and the first thing regulators and reviewers look for.
- **Check:** Pair every opt-in with its opt-out; count steps on both paths; compare button prominence, visibility and styling; on a cancel path, confirm a "cancel anyway" exists past any retention offer. A static flow proves step count; prominence needs the two paths' screens side by side.
- **Severity:** blocking
- **Tells:** a primary "Subscribe" and a "contact support to cancel" link; a retention popup with no "cancel anyway"; an exit hidden behind a menu the entry never needed; a decline link styled to vanish; one-click buy, multi-step return.
- **Catalog:** M-13

### Optional is labelled and skippable
- **Rule:** An optional step says "(optional)" in its title and offers a visible skip. Mark the exception, not the rule: in a mostly-required form the optional fields say "(optional)"; in a mostly-optional form the required ones are marked, consistently and programmatically, with a legend if a mark is used.
- **Why:** Marking the exception keeps the form quiet [cognitive load]; a skip that exists but is hidden is sludge.
- **Check:** Every optional step or field says so; every skip is visible without scrolling or hovering; the marked side is consistent across the flow; a bare asterisk has a legend.
- **Severity:** note; blocking when an optional step looks mandatory or its skip is hidden (see No dark patterns)
- **Tells:** asterisks on nine fields out of ten; a survey step with no way past it; optional data presented as required.
- **Catalog:** D-05, D-06

## Memory and attention

### Groups and open threads stay within working memory
- **Rule:** An undivided homogeneous group holds at most 4–5 items; open threads between steps at most 3–4; anything the user must remember from a previous step is restated on screen where it is needed. Comparison columns: (see lens 04 · Side-by-side comparisons stay at most four columns).
- **Why:** Active memory holds about four chunks; what is visible lives in external memory for free [working memory].
- **Check:** Count items in every undivided group; count what the user must carry from a previous step (a price from step 1 to confirm in step 3); at each decision, the needed value is on screen.
- **Severity:** warning
- **Tells:** eight identical rows with no grouping; a confirmation that does not restate what is confirmed.
- **Catalog:** M-03

### Related things sit together
- **Rule:** Keep related things together in space and time: label, error and hint sit next to their element. Do not duplicate one piece of information across modalities on one screen. No purely decorative elements on complex-task screens (forms, checkouts, data screens).
- **Why:** Intrinsic and extraneous load share one budget; split attention is load in itself [cognitive load].
- **Check:** Measure the distance from every error and hint to its target; list decorative elements on forms, checkouts and data screens; list states signalled three ways where one would do. (error placement and surface: see lens 05 · Error surface matches severity)
- **Severity:** warning
- **Tells:** an error summary at the top with the field at the bottom; an illustration inside a payment form; icon + word + colour for a trivial state.

### Show options and state instead of asking for recall
- **Rule:** Visible menus over hidden ones, autocomplete over blank fields, entered data visible wherever it is needed again. Unlabelled icons only for hyper-conventional signs (magnifier, close, back).
- **Why:** Recognition is cheap and near error-free; recall is expensive and fragile [recognition over recall].
- **Check:** List every icon without a label and ask whether it is universal (see lens 11 · Icon-only controls carry a name); list every place the user must retype or recall something already given; list hidden filters.
- **Severity:** warning
- **Tells:** a mystery-meat icon bar; "enter the code from the previous screen"; hidden filters.
- **Catalog:** B-12, M-03

### Key messages first and last
- **Rule:** In a sequence (scroll, steps, carousel, feature list) the key messages come first and last, never in the middle; the final screen restates the takeaway.
- **Why:** Primacy and recency; the middle sags, most strongly when items arrive one at a time [serial position].
- **Check:** List the sequence and locate the most important item; read what the final screen says.
- **Severity:** note
- **Tells:** the key benefit is item 4 of 7; the last screen is only a "Done" button.

### Important content is not a banner
- **Rule:** Important content (a required step, a warning, a deadline, a CTA, a hint, empty-state help) lives in the content flow and looks like content, never like an advertisement: not a bright bordered rectangle, not a right-hand column block, not a wide banner strip, not a gradient tile with an illustration.
- **Why:** Users have learned to exclude ad-shaped regions from the scan path, most strongly during a goal-directed task [banner blindness].
- **Check:** Squint at the screen; for each important message ask whether it could be mistaken for a promo, and where it sits (right rail, top strip, promotional tile).
- **Severity:** warning
- **Tells:** "Verify your identity to continue" in a gradient tile with a rounded illustration; the only hint on the page in a coloured box in the right column; "your session will expire" styled like a sale banner.

### Novice guidance fades but stays available
- **Rule:** Hints, tours, onboarding, wizards and worked examples are dismissible, collapse after first success or offer a direct path, and do not return for a user who has seen them, while staying reachable. Do not strip the scaffolding to serve experts either.
- **Why:** Support that helps a novice becomes extraneous load for an expert [expertise reversal].
- **Check:** Every tooltip, hint and tour has a dismiss and a state in which it stops appearing; the dismissal is remembered in the scenario model (session: returning); a fast path exists for the returning user. A static design proves the dismiss control; persistence needs a build or the scenario model.
- **Severity:** warning
- **Tells:** the same welcome tooltip on every login; a permanent "how it works" block on a daily-use screen; a tour with no skip; the expert path hidden behind the wizard.

### Chunk long strings and long forms
- **Rule:** Split long numbers, codes and IDs into groups; break long forms into meaningful sections; group navigation, but only into structures the user already has.
- **Why:** Working memory counts meaningful blocks, not symbols; a grouping the user has no schema for does nothing [chunking].
- **Check:** Any run of more than five digits ungrouped? Any form of more than about six fields without sections? Do groups match a real schema (date, phone, card)? (digit separators: see lens 07 · One number format per product)
- **Severity:** warning
- **Tells:** a 16-digit card number in one run; a 20-field form with no headings; a 3-3-3 split of a code users know as 4-4.

## Convention, defaults and configuration

### Affordances are perceived, not physical
- **Rule:** Every interactive element carries a visible signifier: buttons get shape plus fill, shadow or border; links get an underline or a distinct colour plus another cue; inputs a visible boundary; draggables a handle; disabled states look inert. Never hover alone (absent on touch), never colour alone.
- **Why:** On a screen nothing is physically clickable; the appearance is the whole mechanism, and a raised control reads as nearer, therefore figure, therefore actionable [affordance and signifier] [depth cues].
- **Check:** Without hovering and in grayscale, tell what is interactive; list flat elements with no signifier, links distinguished by hue only, and cards that are links but look like content. A static design can prove this.
- **Severity:** blocking for a primary action with no signifier; warning otherwise
- **Tells:** text-only "buttons"; a field with no border; a card that is a link but looks like content.
- **Catalog:** A-19, B-05, B-14, J-07, L-14

### Conventional things in conventional places
- **Rule:** Place conventional elements in their conventional slots by default (logo top-left, primary navigation left or top, search top-right); models are genre-specific, and novelty must preserve category recognisability: a checkout looks like a checkout. Spend uniqueness on typography, rhythm, illustration, voice and detail, never on breaking the base task model.
- **Why:** Users arrive with strong expectations from thousands of other screens; matching them means the interface is understood without learning, and each broken convention is paid for in load [mental models] [conventions].
- **Check:** Is the page instantly recognisable as its category? List every relocated basic element and the value it buys.
- **Severity:** warning
- **Tells:** search in the footer; a checkout that looks like a landing page; a menu that opens in an unexpected direction.

### Consistency over creativity
- **Rule:** Reuse patterns and terminology; respect platform conventions; prefer predictable behaviour over clever design. Third-party surfaces inside the product follow the same patterns.
- **Why:** Consistency scales trust faster than originality; a stock pattern arrives already learned [schemas and scripts].
- **Check:** Same object, same name, same control everywhere? Any component invented where a stock one exists? Any novel gesture with no affordance? (terminology: see lens 07 · One voice, flexible tone)
- **Severity:** warning
- **Tells:** three names for one entity; a custom picker next to a native one; a novel gesture with no affordance.
- **Catalog:** M-02

### Defaults must work
- **Rule:** Out-of-the-box behaviour succeeds without domain knowledge. Configuration (optional settings, preferences, advanced options, fine-tuning) never blocks progress.
- **Why:** The system, not the user, owns correctness; a good default beats a perfect options list [defaults].
- **Check:** Walk the flow accepting every default; it completes with a sensible result.
- **Severity:** warning
- **Tells:** empty required selects; a "choose a plan" gate with no preselection; blank date ranges on reports.

### Simplicity over configuration
- **Rule:** Optimise for the common case; progressive disclosure for advanced options only; no setup before value.
- **Why:** Configuration is load spent before the task starts [cognitive load].
- **Check:** Which fields on the screen serve fewer than about 20 % of users, and are they collapsed?
- **Severity:** warning
- **Tells:** long forms where most fields are "optional"; a preferences page as the onboarding step.

## Trust and ethics

### Money is explicit
- **Rule:** Price is visible before the commitment and repeated consistently through the flow; the screen where money moves says what is charged today, what is charged later and when; recurring payments, trials and limitations are disclosed before commitment; discounts read as lines in the calculation and the arithmetic adds up.
- **Why:** The first price seen becomes the reference and a different figure later reads as a loss; a total that does not add up destroys trust in every other number [reference point] [loss aversion].
- **Check:** Follow one price through the flow; add up the summary by hand; read the pre-commit screen for price, recurrence, trial terms and limitations.
- **Severity:** blocking when the arithmetic is wrong or a charge, renewal or shipment is undisclosed; warning otherwise
- **Tells:** a total that differs from the lines above it; "from $X" on one screen and a different figure at checkout; the renewal price only in the terms.
- **Catalog:** M-12

### Cancel next to commit
- **Rule:** The way to cancel, pause or get a refund is stated next to the commitment, not on a separate policy page.
- **Why:** The exit shown at the entrance is what makes the entrance safe to walk through.
- **Check:** On the commitment screen, find the sentence about cancelling or refunds.
- **Severity:** warning
- **Tells:** a subscription CTA with no mention of how to stop it.
- **Catalog:** M-12, M-13

### Number links to source
- **Rule:** A statistic or a claim in numbers carries its source next to it (a footnote, a link).
- **Why:** Numbers are trusted more than words, but only when the reader can see where they come from; without a source a number reads as advertising.
- **Check:** Every hero number and percentage has a source within the same block.
- **Severity:** note
- **Tells:** "94 % succeed" with nothing under it.

### What happens next
- **Rule:** After a commitment (order, application, submission) the screen shows the sequence that follows, as steps with timeframes, and the one thing the user must do, if anything.
- **Why:** The anxiety after committing is "did it work and what now"; a timeline answers both [feedback loop].
- **Check:** The success screen has a next-steps sequence; a mandatory action is visually distinct from optional ones. (tone of the success screen: see lens 05 · Success is quiet)
- **Severity:** note
- **Tells:** "Thank you for your order" and a logo.

### A human and a name
- **Rule:** Where a person is involved (a reviewer, a specialist, a support agent), show a name and, where appropriate, a face. Address the user by name when it is known.
- **Why:** A name makes the process accountable, a face removes distrust, and personalisation in the most visible spot shows the system remembers.
- **Check:** Does the flow ever name who is on the other side?
- **Severity:** note
- **Tells:** "Your request will be reviewed" with no one reviewing it.

### Privacy sentence where data is asked
- **Rule:** Where personal or sensitive data is requested, one short sentence next to the field or button says what happens to it; data processing and consent consequences are disclosed before commitment.
- **Why:** The question "who sees this?" is asked at the field, so the answer belongs there, not in the footer [cognitive load].
- **Check:** Every sensitive field has its sentence; the pre-commit screen names the data processing.
- **Severity:** note
- **Tells:** a health or financial question with the privacy statement only in the footer.
- **Catalog:** M-12

### Permission requests are explained first
- **Rule:** Explain the benefit and context before a system permission request; trigger the OS prompt only when the feature needs it, not on launch.
- **Why:** The user decides on the permission from the context they have at that moment, and the system prompt carries none.
- **Check:** When does the OS prompt appear, and is there a pre-prompt naming the benefit? A static design shows the pre-prompt; timing needs a build.
- **Severity:** warning
- **Tells:** a location or notification prompt on first launch with no explanation.
- **Catalog:** M-14

### No dark patterns
- **Rule:** Flag as blocking, whatever the project's own rules say:
  - **asymmetric friction** — harder to leave than to enter: cancel via support, retention loops without "cancel anyway" (see Symmetric friction);
  - **surprise charges** — a renewal, a shipment or a fee the user was not shown before committing (see Money is explicit);
  - **costly silent defaults** — the pricier option or an add-on pre-selected without a label (see Defaults are labelled recommendations);
  - **sludge** — mandatory-looking optional steps, hidden skips, optional data presented as required (see Optional is labelled and skippable);
  - **hidden options** — a choice removed for some users without trace or reason (see Dimmed, not hidden);
  - **hidden refusal** — preselection, hierarchy or wording that hides refusal, cancellation or the less profitable choice; a decline link styled to vanish;
  - **a fake second primary** — two equally loud CTAs where one is the product's preference (see lens 01 · Single dominant);
  - **consent without a control** — "you agree" with checkmarks drawn already ticked and no way to decline;
  - **dead ends** — a terminal state with no way out (see lens 05 · No dead ends);
  - **push-to-complete pressure** — countdowns, scarcity or guilt copy used to force order completion.
- **Why:** Choice architecture always nudges [defaults] [framing]; the line is whether the nudge serves the user or exploits them, and these patterns convert once and cost the product its users, its reviews and, in regulated domains, its licence.
- **Check:** The choice-architecture test: would the user call the choice fair after seeing both reference points (the one the screen offers and the one it withholds), the full cost and every outcome [reference point] [anchoring]? Walk the commitment and the exit paths side by side; read every pre-selected control; read every terminal. Run the five manipulation flags on each finding: concealment, deception, asymmetry, conflict of interest, harm to autonomy. Influence is unavoidable; manipulation is any of the five.
- **Severity:** blocking
- **Tells:** see each item above.
- **Catalog:** C-07, M-12, M-13

### No UX folklore
- **Rule:** A finding, and a design decision, cites a real mechanism with its evidence level, never folklore: "7 ± 2 items", the "8-second attention span", "10 % of the brain", learning styles, left/right-brain user types, "more options is always worse", "beautiful = objectively faster", "users won't scroll", "users will notice it, it's right there". Fast is not final; an effect existing is not the effect being large; popular is not true.
- **Why:** Folklore produces confident wrong constraints (amputated menus, stripped content) that the real mechanisms do not support, and a finding justified by folklore is dismissed with one search.
- **Check:** Read the rationale of each finding and each decision; strike any folklore citation and name the mechanism that replaces it (foundations/perception-and-cognition.md).
- **Severity:** note
- **Tells:** "max seven items because Miller"; "users can only hold seven items"; a feature cut "to reduce choice overload".
