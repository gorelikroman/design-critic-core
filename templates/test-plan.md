# UX test plan — `<flow / feature>` · `<build>` · `<date>`

> Test mode (`method/test-method.md`). Cases cite the rule that defines "correct"; results
> are `passed` · `failed` · `blocked` · `not-run`. Catalog rows can be exported as a CSV with
> `scripts/catalog_to_tests.py` and pasted into §3.
>
> Tester: `<name>` · Sources: `<UX spec, build note, design file>` · Build: `<version / URL>`

## 1. Scope

- Screens / components: `<…>`
- Platforms and devices: `<browser + OS | device + OS>`
- Input methods: mouse · keyboard · touch · screen reader `<which>` · throttled network · offline
- Lenses: `<01, 04, 05, 07, 10, …>` · Catalog sections: `<A, B, D, E, K, L, …>` · Levels: `<REQ | REQ + REC>`
- Out of scope: `<…>`

## 2. Scenario coverage

| Scenario | Priority | Path (screen → state) | Case IDs |
|---|---|---|---|
| S1 | critical | | |

States to reach on the build (from the state matrix):

| Screen | Required states | Reached | Case IDs |
|---|---|---|---|
| | | | |

## 3. Cases

| ID | Title | Rule | Scenario | Preconditions | Steps (input method) | Expected | Severity if failed | Result | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| `<flow>-TC-01` | | `<catalog ID / lens NN · entry / AC#>` | | | | | | | |

Stress set per text-bearing component: longest string · unbreakable string · zero items ·
320 px · 200 % zoom · RTL `<if localised>` — results per component in the cases above.

## 4. Run summary

- Cases: `<total>` · passed `<n>` · failed `<n>` · blocked `<n>` · not run `<n>`
- Defects: blocking `<n>` · warning `<n>` · note `<n>`
- Release gate: `<pass | fail — open blocking defects: …>`
- Top three defects: `<ID — rule — severity — one-line repro>`
- Not covered: `<devices, assistive technology, unreachable states>`
- Design problems handed to a review: `<…>`
