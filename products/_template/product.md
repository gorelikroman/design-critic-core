# Product layer — `<product name>`

> Loaded on top of the universal rules whenever work concerns this product
> (`products/README.md`). A row here without a source or a reference screen does not exist.
> Only the product owner edits this file; builds and reviews propose changes.
>
> **Names:** `<Official name>` · `<localized name>` · `<repo-slug>` — every name people use for
> this product in requests; the skill matches requests against this line.
> **Not this product:** `<a sibling product, site or app with a similar name>` — a request naming
> it loads its own layer, not this one. Delete the line if nothing is confusable.
>
> Product owner: `<name>` · Design system owner: `<name>` · Last updated: `<date>` ·
> Decisions log: `design-decisions.md` (this folder)
>
> Reading order — **build:** §5 → §4 → §2 → §9 → §6 · **review:** §6 → §5 → `design-decisions.md` →
> §10 · **spec:** §5 → §3 → `design-decisions.md` · **test:** §6 → §3 (formats) → §10.
> Without access to the sources in §0 / §2, start the answer with
> "Product: `<name>` (summary layer, `<date>`)".

## 0. Source of truth

<!-- Optional. Fill it when the product already keeps a handbook, a design-rules document or a
     decisions file somewhere else; delete it when this layer is the handbook. -->

- Canonical source: `<repository and path, or document link>`, captured at `<commit or date>`.
- When it is available, read it and trust it over this summary; a disagreement is drift, and
  this layer gets refreshed.
- When it is not, work from this file and `design-decisions.md`, and say "summary layer".
- Refreshing: re-read the source, update this file and the log, record the new commit or date
  above, bump the pack version.

## 1. The product

- What it is and for whom: `<one paragraph>`
- Platforms: `<desktop web | mobile web | iOS | Android | kiosk / POS / handheld>`
- Primary tasks (the verbs that matter most): `<buy …, find …, glance at …>`
- Users' typical state: `<hurrying | anxious | expert, daily use | …>`
- Locales and house formats: `<languages, RTL?, date / number / currency format>`

## 2. Design system sources

<!-- Where the truth lives. The skill reads these; it never invents values. -->

| Source | Link / path | Notes |
|---|---|---|
| Component library (design) | `<Figma library URL>` | |
| Design tokens | `<repo path or package, e.g. packages/tokens>` | |
| Component code | `<repo path or package>` | |
| Component docs / Storybook | `<URL>` | |
| Icon set | `<…>` | |

Token roles the skill should know by name (values stay in the source):

| Role | Token name | Use for |
|---|---|---|
| primary action | | |
| danger | | |
| surface / canvas | | |
| text primary / secondary | | |
| spacing ladder | | |
| type ladder | | |
| radius ladder | | |
| borders and elevation (shadows) | | |
| motion durations and easing | | |

## 3. Voice and terms

- Voice: `<e.g. calm, direct, "you" not "we">`
- Terms (one term per concept): `<Archive — not "move to storage">`, …
- Words never used: `<…>`

## 4. Components — when to use which

<!-- The inventory, filled from the library and a learn-mode review. -->

| Need | Use | Not | Reference |
|---|---|---|---|
| primary action | | | |
| status of an item | | | |
| confirmation of a destructive action | | | |
| empty state | | | |
| error on a field | | | |

## 5. Patterns

<!-- Recurring solutions with reference screens: checkout, onboarding, list + detail, tables,
     settings, search. Each links to where it is done right. -->

### `<Pattern name>`
- **Use when:** `<…>`
- **Structure:** `<zones, components, states>`
- **Reference:** `<Figma node / route / screenshot>`
- **Decisions log rows:** `<archetype · decision>`

### States every flow draws
- `<loading, empty, error, offline, success — which component each uses>`

## 6. Hard rules

<!-- The product's non-negotiables. Breaking one is debt with no context exception
     (review method §4.5). Keep this list short; everything else lives in design-decisions.md. -->

- `<e.g. never a native select; always the product's Select>`

## 7. Motion register

- Register: `<restrained | production polish | playful — lens 09 · Name the register before the first finding>`
- Durations and easing: `<token names>`

## 8. Tolerated exceptions (summary)

<!-- One line per exception the owner accepted; the full table with reasons lives in
     `design-decisions.md` · Tolerated exceptions. -->

- `<where — what it deviates from — see design-decisions.md>`

## 9. Working in the design file

<!-- The house mechanics a build must follow: where work happens and where it never does, which
     screen to start from, modes and variables to set, how layers are named, how a finished change
     reaches the handoff section, known tool pitfalls. Delete the section if there are none. -->

1. `<work only in section …; never in …>`
2. `<start from the nearest existing screen of the same shell>`
3. `<bind colours, spacing, radius, text styles, copy>`

## 10. Known drift and open questions

<!-- The critic reports these as known debt or `decision-needed`, not as new findings on every
     screen. Date the list; it goes stale. -->

**Decided, not yet built** (state on `<date>`): `<kit gaps, screens behind the rules, code not synced>`

**Conflicts with a universal `blocking` rule** — a product decision cannot override these; the
critic keeps reporting them until the owner changes the product rule:

- `<product decision>` — against `<lens NN · entry>`

**Open questions for the owner:** numbered in `design-decisions.md` · Open questions.
