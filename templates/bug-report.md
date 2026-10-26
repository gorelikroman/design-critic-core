# `<Short title: what breaks, where>`

<!-- Test mode (method/test-method.md §4). One defect per problem; list every case it fails.
     Severity comes from the rule, fix priority from the team. -->

- **Rule:** `<catalog ID>` · `<lens NN · entry>` · `<spec AC#, if any>`
- **Severity:** `<blocking | warning | note>` (from the rule)
- **Fix priority:** `<set by the team>`
- **Where:** `<screen / route + selector / component>` · state `<default | loading | empty | …>`
- **Environment:** build `<…>` · device / OS `<…>` · browser `<…>` · assistive technology `<…>` ·
  network `<normal | throttled | offline>`
- **Failed cases:** `<flow>-TC-NN`, …
- **Owning discipline:** `<typography | layout | writing | accessibility | colour | interaction | implementation>`
- **Against:** `<implementation (differs from the design) | design (the build matches the design, the design breaks the rule)>`

## Repro

1. Start: `<state>`
2. Action: `<step, with the input method>`
3. Observed: `<what happens>`

## Expected

`<the observable result the rule requires, quoted from its Check or the acceptance criterion>`

## Evidence

`<screenshot | recording | DOM / accessibility-tree excerpt | network log>`
