# Finding — `<cluster>.<#>` `<title>`

<!-- One block per finding. Fields are always all present; write "—" rather than leaving one
     out. Method: method/review-method.md §4 (results, tags, guardrails) and §8 (severity). -->

- **Location:** `<node id | file path:line | route + selector | screenshot + pin>`
- **Rule:** `<lens NN · Entry name>` or `<catalog ID>` or `<log row: archetype · decision>`
  <!-- several rules may be cited, comma-separated; the problem is still one finding -->
- **Observation:** `<What is there — measured or seen. One sentence. Numbers from the structure;
  "est." when read from a screenshot.>`
- **Interpretation:** `<What it means against the rule. One sentence.>`
- **Recommendation:** `<What to do, as a proposal: delete → use the platform → reuse an existing
  pattern → correct the value → add something new. One sentence. Only a blocking finding says "must".>`
- **Result:** `<pass | partial | fail | not-applicable | not-reviewed>`
- **Tag:** `<ok | debt | context | decision-needed | rule-candidate>`
- **Severity:** `<blocking | warning | note>`
- **Confidence:** `<high | medium | low>`
  <!-- high: proved by structure or measurement · medium: read from a screenshot or inferred from
       code without a render · low: rests on an assumption about the task or the platform -->
- **Evidence:** `<shots/<key>-<slug>.png + pin N | node id | path:line | route + selector>`
  <!-- blocking, and any contested warning: add the minimal repro — start state → action → observed -->
- **Also on:** `<other screens with the identical problem, by key, or —>`

## Grouping findings

One problem is one finding, even when it cites several rules; the same problem is never
written twice under two rules. When the identical fix applies on several screens, write one
finding, put the clearest instance in Location and Evidence, and list the rest under "Also
on" ("…and 4 more"); the debt table gets one row, not one per screen. A problem that needs a
different fix on a different screen is a separate finding.
