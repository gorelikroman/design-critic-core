# Product layer — `<product name>`

> Loaded on top of the universal rules whenever work concerns this product
> (`products/README.md`). A row here without a source or a reference screen does not exist.
> Only the product owner edits this file; builds and reviews propose changes.
>
> **Names:** `<Official name>` · `<localized name>` · `<repo-slug>` — every name people use for
> this product in requests; the skill matches requests against this line.
>
> Product owner: `<name>` · Design system owner: `<name>` · Last updated: `<date>` ·
> Decisions log: `design-decisions.md` (this folder)

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

## 6. Hard rules

<!-- The product's non-negotiables. Breaking one is debt with no context exception
     (review method §4.5). Keep this list short; everything else lives in design-decisions.md. -->

- `<e.g. never a native select; always the product's Select>`

## 7. Motion register

- Register: `<restrained | production polish | playful — lens 09 · Name the register before the first finding>`
- Durations and easing: `<token names>`
