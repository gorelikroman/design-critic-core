# 14 — Devices: kiosk, POS, handheld (optional module)

**Optional module — load only when reviewing kiosk / POS / handheld / vending UI.** Screens of roughly 4–5", transactional, interruption-prone, used under glare, noise, motion and partial attention.
Every other lens still applies; where a device rule conflicts with a phone-app convention (lens 12), the device rule wins.
A verdict must name the device category — generic / unattended / handheld — or it is incomplete. Order: the all-devices rules, then the category rules, then the gate additions.
Rule of thumb: if a user hesitates during payment, device UX failed.

## All devices

### One transactional intent per screen
- **Rule:** One action, one instruction, no competing actions per screen. No settings access and no optional exploration during a payment.
- **Why:** [Hick–Hyman law] — every extra option on a payment screen adds decision time at the moment the user is least able to spend it; "what now?" is the device failing.
- **Check:** Each screen states exactly one thing to do. Any secondary link or menu during the transaction is a fault.
- **Severity:** blocking
- **Tells:** "Tap card — or choose another method — or enter loyalty number" on one screen; a gear icon on the payment screen.

### Ultra-high legibility and touch targets
- **Rule:** Touch targets ≥ 9–10 mm physical. Large, high-contrast typography. One dominant message per screen. No dense instructions.
- **Why:** [critical print size] — at arm's length, under glare and with split attention, type below the size read at full speed is not read at all.
- **Check:** Convert target sizes to millimetres at the device's pixel density. Read the screen from arm's length in one glance. Phone floors in points do not transfer (see lens 10 · Target size).
- **Severity:** blocking
- **Tells:** phone-sized 44 pt buttons on a low-density panel; paragraphs of instruction; thin light-weight type.

### Physical context awareness
- **Rule:** Assume glare, noise, partial attention and interruptions. Never rely on colour alone or sound alone to communicate state.
- **Why:** glare removes colour, noise removes sound and split attention removes reading time; a state must survive losing any one channel.
- **Check:** Mute it, desaturate it: is the state still unambiguous?
- **Severity:** blocking
- **Tells:** green flash as the only success signal; beep as the only error signal.
- **Catalog:** L-03

### Linear, controlled navigation
- **Rule:** Step-by-step linear flow. No hamburger menus, no tab navigation, no deep information architecture.
- **Why:** [schemas and scripts] — the user brings a transaction script (present, confirm, take the receipt), not an app model; anything explorable breaks the script. Devices are not apps.
- **Check:** Draw the flow: is it a straight line with at most a cancel or back?
- **Severity:** blocking
- **Tells:** home screen with a grid of destinations; a breadcrumb or tab bar on a terminal.

### Recoverable device errors
- **Rule:** Every error states a clear outcome ("Payment failed"), a clear next step ("Try again" / "Use another card") and returns to a clear reset state. No technical error codes, no vague messages, no blame language.
- **Why:** [feedback loop] — an error that names no next step leaves the loop open and the user guessing at a payment terminal.
- **Check:** Each error screen has outcome + next step + reset. Read for jargon and blame. General error copy: see lens 05 · Error copy answers four questions.
- **Severity:** blocking
- **Tells:** "Error 51"; "Transaction declined by host"; "You entered the wrong PIN".

### Mandatory device states
- **Rule:** Every device flow designs six states: idle · action requested (tap / insert / swipe / scan) · processing · success · failure · timeout or cancellation.
- **Why:** if a state is not designed it does not exist, and on a device the undesigned state is the one the user is left staring at.
- **Check:** Six states per flow in the file, including timeout. The four-state minimum for screens in general: see lens 05 · Required states present.
- **Severity:** blocking
- **Tells:** no timeout screen; "processing" reused for failure; a success screen with no exit.

### Visual feedback as the primary language
- **Rule:** The device is understandable without sound. Icon, text and state colour reinforce each other. Progress is explicit. Minimal text, simple language, forgiving touch zones, clear icons; it works for first-time users and tourists.
- **Why:** [feedback loop] — a silent, ambiguous device makes users repeat actions, and repeated actions on a payment device mean double charges or abandonment.
- **Check:** For each state: is there an icon, a short text and a colour, all agreeing?
- **Severity:** blocking
- **Tells:** text-only states; culture-specific icons; idioms.

### Device performance targets
- **Rule:** Immediate visual acknowledgement for every input; an explicit processing indicator, never silence; no blank or ambiguous screen; a clear success or failure outcome. No unexplained waiting, no decorative delays, no success animation that slows the exit.
- **Why:** [feedback loop] — a perceived freeze on a payment device is fatal, and forced waiting causes abandonment.
- **Check:** Targets in the table, measured on the device. Any deliberate delay or celebratory animation on the exit path is a fault. Static design cannot prove timing; mark not-reviewed. Web and phone targets: lens 13 · Performance targets.
- **Severity:** blocking
- **Tells:** 1.5 s of confetti before the receipt screen; a spinner appearing 800 ms after the card tap.

| Moment | Metric | Target |
|---|---|---|
| Input feedback | Touch → visual feedback | ≤ 100 ms |
| Card interaction | Card present → UI feedback | ≤ 150 ms |
| Processing start | Action → processing indicator | ≤ 300 ms |
| Idle transition | Idle → ready / active | ≤ 500 ms |
| Freezes | Any unresponsive UI | 0 |
| Artificial delays | Forced waiting | not allowed |

### Scroll follows the touch
- **Rule:** A scroll gesture affects only the container where it started; reaching a scroll limit never propagates to another container; horizontal and vertical scroll never conflict; accidental background scrolling is forbidden. Avoid nested scroll areas on small screens. Primary actions never depend on hidden or overflow content.
- **Why:** [mapping] — the finger maps to one surface; when the page moves instead, the user fights the screen, and success that depends on undiscoverable scrolling is a no-go.
- **Check:** Scroll a list to its end: does the page move? Is the CTA reachable without scrolling?
- **Severity:** blocking
- **Tells:** scroll chaining; a carousel inside a scrolling page; "Confirm" below a scrollable terms box.

### Copy word limits
- **Rule:** Hard limits: primary instruction 3–5 words · secondary hint ≤ 7 · error message ≤ 6 · success message ≤ 4. No polite fillers, no marketing tone, no technical jargon.
- **Why:** [gist first] — the user takes the screen in one glance; if reading takes longer than acting, the copy is too long. Devices are not marketing surfaces.
- **Check:** Count words on every string.
- **Severity:** blocking
- **Tells:** "Please tap or insert your card to continue with your payment"; "Thank you for shopping with us today!".

| Context | Max words |
|---|---|
| Primary instruction | 3–5 |
| Secondary hint | ≤ 7 |
| Error message | ≤ 6 |
| Success message | ≤ 4 |

## Unattended devices and handheld terminals

"Zero assistance" and "Attract loop and idle" apply to unattended devices (vending, kiosk, parking, EV charging, self-service). "Role clarity", "Operational speed", "Interruption tolerance" and "Grip and reach" apply to handheld terminals (operator-carried, passed to the customer).

### Zero assistance
- **Rule:** Unattended devices: assume nobody will help. The device teaches the interaction; one instruction per screen; no multi-step instructions on one screen.
- **Why:** [mental models] — a first-time user has no model of the device; its own screen is the only teacher, and a first-time failure is the UX failing.
- **Check:** Hand the flow to someone who has never seen it; count hesitations.
- **Severity:** blocking
- **Tells:** "1. Select 2. Pay 3. Collect" on one screen; an instruction that assumes prior use.

### Attract loop and idle
- **Rule:** Unattended devices: idle is functional UX — a clear ready-to-pay signal, supported payment methods shown, legible at distance, subtle motion to indicate life. Forbidden: brand-only animation with no instruction, distracting motion, text-heavy idle.
- **Why:** [motion perception] — subtle motion is the cheapest signal that the device is alive; without it, or under a logo loop, the user cannot tell it is ready or how to pay.
- **Check:** From two metres: can the critic tell it is on, ready, and how to pay?
- **Severity:** blocking
- **Tells:** full-screen logo loop; screensaver photography; a static idle that looks switched off.

### Role clarity
- **Rule:** Handheld terminals: control ownership is always visually and contextually clear. Operator-facing and customer-facing states are visually distinct; it is always clear who should act; customer input states never resemble operator configuration states; the transaction outcome is visible before the device is handed back.
- **Why:** two people share one screen in turns; when either hesitates over whose turn it is, the device has failed both.
- **Check:** From a screenshot alone, is it clear whose turn it is? Is there a distinct visual language per side?
- **Severity:** blocking
- **Tells:** the same layout for "enter amount" (operator) and "enter PIN" (customer); the outcome shown only after handback.

### Operational speed
- **Rule:** Handheld terminals: direct, predictable, minimal interactions. No unnecessary confirmations, no redundant intermediate screens, immediate feedback after every action, no artificial delays between steps.
- **Why:** [warning habituation] — a confirmation on every step stops being read within a shift, and every extra screen slows an operator who runs the flow hundreds of times a day.
- **Check:** Count screens between "amount entered" and "card requested"; each extra one needs a reason.
- **Severity:** blocking
- **Tells:** "Are you sure?" on every step; a splash between steps; animated transitions that block input.

### Interruption tolerance
- **Rule:** Handheld terminals: transaction state survives temporary network drops; no silent resets; interrupted flows resume clearly or fail explicitly; the user never has to ask whether a transaction completed.
- **Why:** [feedback loop] — "did it go through?" means the system failed to communicate state, and the retry that follows is a duplicate charge.
- **Check:** Kill the network mid-transaction: what does the screen say, and does it recover to a known state? Static design cannot prove this; mark not-reviewed.
- **Severity:** blocking
- **Tells:** return to idle with no message; ambiguous "Please wait" with no timeout; duplicate charges after retry.

### Grip and reach
- **Rule:** Handheld terminals: one-hand, limited-precision use. Primary actions reachable without a grip change; no top-edge-only critical actions; no precision drag gestures; touch targets tolerate imprecision.
- **Why:** [Fitts's law] — a small or distant target costs time and errors, and on a device held in one hand it also costs a grip change. Phone equivalent: lens 12 · Thumb reach.
- **Check:** Primary CTA in the lower reach zone? Any slider or drag required?
- **Severity:** blocking
- **Tells:** swipe-to-confirm; "Cancel" only in the top corner; small tip-percentage chips near the edge.

## Device approval gate additions (one failure → no-go)

- [ ] Linear flow only; no menus, tabs or deep IA (Linear, controlled navigation)
- [ ] Touch targets ≥ 9–10 mm; legible at a glance (Ultra-high legibility and touch targets)
- [ ] Six states designed per flow, including timeout / cancellation (Mandatory device states)
- [ ] Word limits met on every string (Copy word limits)
- [ ] State never carried by colour alone or sound alone (Physical context awareness)
- [ ] Performance targets met on the device (Device performance targets)
- [ ] Scroll never chains; primary action never depends on overflow content (Scroll follows the touch)
- [ ] Unattended: attract loop shows readiness and payment methods (Attract loop and idle)
- [ ] Handheld: role, speed, interruption and grip rules met (Role clarity · Operational speed · Interruption tolerance · Grip and reach)
- [ ] Tested on the smallest supported screen; certified per device model
