# Snippet for a product repository's CLAUDE.md

<!-- Paste the block below into the CLAUDE.md of a repository that ships UI, replace the
     <placeholders>, delete what does not apply. It tells Claude Code in that repository to
     use design-critic while writing UI, not only when asked for a review. -->

```markdown
## UI work — design-critic

This product's UX/UI rules come from the `design-critic` skill; product layer: `<slug>`
(`<path to .design-critic/product.md, or "products/<slug>/ in the skill">`).

- Creating or changing UI: use design-critic in **build** mode. Write the brief and the
  state matrix first; build from the product's components and tokens; every required state
  (loading, empty, errors, success) ships with the change.
- Before handing over a UI change: run the tells scan on the changed files and look at every
  hit (a tell is not a verdict):
  `git diff --name-only <base> | python3 <skill folder>/scripts/ui_tells.py --stdin`
  where `<skill folder>` is `~/.claude/skills/design-critic` or the installed plugin's folder.
- Put the build note (design-critic `templates/build-note.md`) into the pull request
  description: rules applied, deviations with reasons, states delivered, what needs review.
- Reviewing a UI branch or PR: use design-critic in **review** mode with code input; load
  lens 09 and lens 10 in full.
- Never edit `design-decisions.md` or the product layer from a feature branch; propose rows
  in the build note or the review's decisions delta.
```
