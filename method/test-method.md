# The test method — UX test cases and bug reports from the same rules

> How QA turns the rules into a test plan, runs it on a build, and files defects that
> design and development can act on without a meeting. The difference from a review: a
> review judges a design and grows the project's decisions log; a test run executes
> defined cases on an implementation and reports each as passed or failed. Both cite the
> same rules, so a failed case and a review finding about the same problem carry the same ID.
>
> Output: a test plan with cases (`templates/test-plan.md`), a CSV of cases for the team's
> test management tool (`scripts/catalog_to_tests.py`), bug reports
> (`templates/bug-report.md`), and a run summary.

---

## 0. Inputs, and what they allow

| Input | Cases come from | Can execute |
|---|---|---|
| UX spec (`templates/ux-spec.md`) | its scenarios, state matrix and acceptance criteria | nothing yet: plan only |
| Build note (`templates/build-note.md`) | its states delivered, deviations and "needs review" list | nothing yet: plan only |
| Design file | the states drawn, the copy, the static rules | static checks only (contrast, target size, labels, states present) |
| Staging URL, app build, device | all of the above | everything: mouse, keyboard, touch, screen reader, network, zoom |

The strongest plan starts from the spec, adds what the build note says was deviated from or
not checked, and adds the catalog rows for the components on the screen. Without a spec,
QA writes the scenario model itself from lens 05 §1 (as in `method/spec-method.md` §2).

---

## 1. Scope the run

- **What**: the screens, the flow, the components; the platform and the devices.
- **Which lenses and catalog sections**: route as a review does (`SKILL.md` · Routing), then
  pick catalog sections by what is on the screen: A and B always; C for selection controls;
  D and E for forms; F for anything that loads; G for navigation and search; H for overlays;
  I for lists and tables; J for touch; K and L always on web and apps; M for content, money
  and localisation; N for motion and network.
- **Level**: REQUIRED rows always; RECOMMENDED rows for a release gate; CONTEXT-DEPENDENT
  only when the project's log has made them rules.

---

## 2. Write the cases

A case is observable, has one expected result, and cites the rule that defines "correct".

| Field | Content |
|---|---|
| ID | `<flow>-TC-NN` |
| Title | what is checked, in one line |
| Rule | catalog ID and/or `lens NN · entry`; an acceptance criterion from the spec (`AC3`) |
| Scenario | the spec's scenario (`S2`) or the dimension values: persona, data, environment |
| Preconditions | the state to start from |
| Steps | numbered, with the input method (mouse / keyboard / touch / screen reader) |
| Expected | the observable result, from the rule's Check or the criterion's "then" |
| Severity if failed | from the rule (the lens entry's Severity; the catalog's REQUIRED at the floor = `blocking`) |

Sources, in order:

1. **Acceptance criteria** of the spec: one or more cases each.
2. **Scenario coverage**: one case per scenario path, checking every screen reaches its
   declared state (lens 05 · Scenario coverage rules). Pairwise is enough for standard
   dimensions; every value of a `critical` dimension gets its own case.
3. **The state matrix**: every required state is reached on the build, not only drawn
   (lens 05 · Coverage is declared, not executed).
4. **The catalog rows** in scope: their "Check" column is the steps, their "Rule" column is
   the expected result. `scripts/catalog_to_tests.py` exports them as a CSV to import and
   trim: `python3 scripts/catalog_to_tests.py --sections A,B,D,E,K,L --platform web
   --level REQ -o cases.csv`.
5. **The stress set** per text-bearing component: longest string, unbreakable string, zero
   items, 320 px, 200 % zoom, RTL where localised (lens 05 · The reviewer's minimum stress
   set).
6. **The acceptance checklist** of the catalog, all twenty items, for a release gate.

Do not write cases for rules that cannot apply (a gesture rule on a desktop-only web app); do
not write the same check twice under two rules.

---

## 3. Execute

- Use the input the rule requires: a keyboard rule is run with the keyboard, a screen-reader
  rule with a screen reader, a network rule with throttling or offline (review method §2,
  Live URL).
- Record per case: `passed` · `failed` · `blocked` (cannot be run: the state is unreachable,
  the environment is missing) · `not-run`. A `blocked` case is a finding about testability,
  never a pass.
- Keep the evidence next to the result: a screenshot, a recording, the DOM or the
  accessibility-tree excerpt, the network log.
- A visible element is not proof of behaviour: the focus ring must be seen moving, the
  announcement must be heard, the retry must be observed working.
- Measurable cases can run unattended. `scripts/live-checks.js` measures a rendered page
  (overlapping targets, target sizes, clipped and spilling text, sideways scroll) and maps
  axe-core results (contrast, names, labels, alt, the 24 px floor) to catalog IDs; each finding
  is evidence for the case, not its verdict. Screenshot regression against reference images
  answers a different question, what changed: every changed image is triaged with the review
  method before it is accepted or filed. A runner such as Testplane can do both over every
  story of a Storybook.

---

## 4. File defects

One defect per problem (`templates/bug-report.md`), even when it fails several cases; list
the cases. Every defect has:

- the **rule** (catalog ID and/or lens entry), so design, development and the next review
  speak about the same thing;
- the **severity** from that rule, never raised or lowered by how annoying it is; the fix
  priority is the team's, set separately (review method §8);
- the **minimal repro**: start state → action → observed, and the expected result from the
  rule;
- the **environment**: build, device, OS, browser, assistive technology, network;
- the **owning discipline** when the break is visible: typography, layout, writing,
  accessibility, colour (lens 05 · Look once, report what visibly broke, name the owning
  discipline).

A problem that is a design decision rather than an implementation defect (the build matches
the design, and the design breaks a rule) is filed against design and flagged for a review,
not closed as "works as designed".

---

## 5. Report the run

Lead with the verdict, then the defects that matter:

- cases: total · passed · failed · blocked · not run; defects by severity;
- the release call against the gates: any open `blocking` defect fails the gate;
- the top three defects with rule, severity and repro;
- what was not covered (devices, assistive technology, states unreachable on this build),
  so silence is not mistaken for a pass;
- design problems found, handed to a review.

Re-test a fixed defect with the same case, the same environment and the same evidence
(review method §9).
