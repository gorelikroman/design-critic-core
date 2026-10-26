# Language of the output

> The skill's own files are written in English. The people using it may write in any
> language. This file fixes what is translated and what is not, so reports of the same review
> in two languages can still be counted, grepped and compared.

## The rule

1. **Answer in the language of the request.** The chat report, the screen cards, the
   findings, the brief, the spec, the test plan and the build note are written in the
   language the request was written in. A mixed request follows the language of its
   instructions, not of its quoted material.
2. **Keep the counting tokens in English, untranslated**, in every language:
   - rule citations: `lens NN · <exact entry heading>`, catalog IDs (`A-03`), log rows;
   - results: `pass` · `partial` · `fail` · `not-applicable` · `not-reviewed`;
   - tags: `ok` · `debt` · `context` · `decision-needed` · `rule-candidate`;
   - severity: `blocking` · `warning` · `note`; confidence: `high` · `medium` · `low`;
   - test results: `passed` · `failed` · `blocked` · `not-run`;
   - state names: `default` · `loading` · `empty` · `validation_error` · `server_error` ·
     `success` · `permission_denied` · `custom`;
   - file names, folder names, JSON keys and values of `review.json`.
   These are what the method counts across screens and reviews; a translated tag is a
   second tag.
3. **Everything else is translated**: observations, interpretations, recommendations, the
   verdict, table headings, template headings and comments.
4. **Terms of the method** (dominant, route, spacing cascade, reading mode, colour budget,
   state matrix, decisions log, …) are translated consistently within one deliverable; on
   first use, the English term may follow in brackets so a reader can find it in the lenses.
5. **Quotes stay verbatim.** The project owner's words and the interface's own copy are
   quoted in the original language; a translation, if needed, follows in brackets.
6. **Interface copy is judged in the interface's language**, whatever the report's language
   (lens 07).
