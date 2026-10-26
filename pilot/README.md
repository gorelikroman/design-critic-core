# design-critic pilot — without a product layer

Goal: in one to two weeks, find out whether the skill helps in real work for designers, PMs,
QA and developers, and what to improve before the products are connected. Participants: one
or two people per role.

During the pilot the skill works on **universal rules only**: it does not know your
components, tokens or the decisions your products have made. Every deliverable starts with
"Product: none — universal rules only". Comments like "it suggests a component we don't have"
are expected and are not a skill failure; comments on logic, hierarchy, states,
accessibility and copy are exactly what the pilot tests.

## 1. Install

You need Claude Code and read access to the `gorelikroman/design-critic-core` repository on GitHub.

```bash
claude plugin marketplace add gorelikroman/design-critic-core
claude plugin install design-critic@design-critic-core
```

Or inside a session: `/plugin marketplace add gorelikroman/design-critic-core`, then
`/plugin install design-critic@design-critic-core`. Start a new session afterwards. Updates:
`claude plugin update design-critic@design-critic-core`.

On first use Claude may ask for permission to read the skill's folder — allow it; otherwise
it works from the short summary and says so in the report.

Smoke test: write "Review this screen" and attach any screenshot. The answer should have a
verdict, findings citing rules (`lens 01 · …`, `B-04`) and the line "Product: none".

## 2. How to ask

In plain words, in any language; the answer comes back in the same language. The skill picks
the mode itself; to force one, name it: "in review mode", "in build mode", "write a spec",
"test cases".

- Attach the material: screenshots, a Figma frame link, code files, a staging URL. Without
  material the skill asks for it first.
- Say what the screen is for and on which platform: "mobile app, the user is in a hurry to
  pay". It improves the result a lot.
- If an answer is too general, ask "show me the rule you cite" or "run the full catalog".

## 3. Tasks per role

Use real tasks from the current sprint. At least three tasks per person.

**Designer**
1. Review before handoff: "Review this mockup before handoff" + a Figma link or screenshots.
2. Build: "Design the <…> screen; start with the brief and the state matrix" — judge whether
   the brief helps thinking, not only the result.
3. Feedback translation: paste a real stakeholder comment ("make it cleaner", "no air") and
   ask "translate this into a concrete axis and propose changes".

**Product manager**
1. "Write UX requirements and acceptance criteria for this story" + the story or PRD.
2. "What states does this flow need?" — compare with the original ticket.
3. "Is this ready for release?" + staging or screenshots — the release gates check.

**QA**
1. "Write UX test cases for <screen>, web", plus the catalog export (the plugin folder is
   listed by `claude plugin list`; copied skills live in `~/.claude/skills/design-critic`):
   `python3 <skill folder>/scripts/catalog_to_tests.py --sections A,B,D,E,K,L --platform web --level REQ -o cases.csv`
2. "Test <screen> accessibility on staging: keyboard and screen reader" + URL.
3. Take a bug you already found and ask "write this up with the bug report template" —
   compare with your usual report.

**Developer**
1. "Build the <…> component to our design rules" — check that every state is there.
2. Scan changed files before a PR:
   `git diff --name-only main | python3 <skill folder>/scripts/ui_tells.py --stdin`
3. "Review the UI in this branch", in the repository with your branch checked out.

## 4. Feedback — after every task

Copy, fill in, send to the pilot organiser (or the pilot chat).

```
Role:
Task (what you asked, one line):
Material (screenshot / Figma / code / staging / text):
Mode the skill chose (shown in the answer): review / build / spec / test / unclear
Time spent:
Usefulness, 1–5:
What was useful (1–3 points):
False findings (flagged for nothing) — how many, one example:
Missed (a problem you know of that it did not find):
What was unclear in the answer:
Would you have done this without the skill? Faster / same / slower:
```

Especially valuable: answers in the wrong language, the wrong mode chosen, citations of rules
that do not exist, and advice that contradicts your platform (phone rules on desktop, etc.).

## 5. When the pilot succeeds

- Average usefulness ≥ 4 for every role.
- On average no more than one false finding per review.
- At least one case per role where the skill found something the person would have missed.
- The right mode is picked without a hint in 9 cases out of 10.

## 6. After the pilot

1. Feedback triage → changes to rules and wording (a separate PR, version 1.1.0).
2. Product layers for the three products (`products/README.md`): the product's names, the
   Figma library, the tokens, 5–10 reference screens per product.
3. Real screens with agreed findings → `evals/<product>/`, so every rule change can be
   checked for regressions.
