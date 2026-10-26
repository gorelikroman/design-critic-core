# Sources

The skill's rules are paraphrased and merged from the material below. No file in the
skill names an author; this page is the single record of origin and licence. Where a rule
appears in several sources, the skill keeps one entry and the strongest check.

## The project's own material (the doctrine, the method, the review evidence)

- A design doctrine compiled from 23 design-school lectures and a four-day colour
  intensive: perception mechanisms, composition, hierarchy, typography, modular grids,
  colour. Compiled as a law graph with a critic rubric.
- The screen-review method used on 85 shipped screens and the 266-screen typography
  review: clustering by user task, the seven-field card, the ok / debt / context /
  decision-needed / rule-candidate tags, the rule lifecycle (candidate → confirmed →
  decision-needed), the decisions log, the visual pin page.
- Expression axes (density, tension, task-verb profiles) validated by transfer on lab
  screens; the corner-case coverage method; the error-state system; the typography
  role system and its findings; the handoff conventions.
- The decision-board mechanism (`board/`): a published page where every finding is a
  numbered item with pins on a screenshot and a per-item ok / fix / skip verdict, adapted
  from the project's own decision-board tooling with its design-system-specific typefaces
  and palette replaced by a neutral, theme-aware one. The build script and page shell are
  the project's own; nothing in them is third-party.

## The project's knowledge bases

- **UX/UI Rules Catalog — English Edition, v2.0 (2026-07-14).** 266 rule cards in 14
  sections (A–N) with rationale, examples, exceptions, design-stage checks,
  implementation checks and acceptance criteria; the AI review protocol (three modes,
  the pass / partial / fail / not-applicable / not-reviewed scale, the nine-field
  finding, the guardrails). Evidence base: WCAG 2.2, WAI-ARIA Authoring Practices,
  platform human-interface guidelines (Apple, Android, Material 3, Fluent 2), GOV.UK
  Design System, USWDS, web.dev, Nielsen Norman Group research.
- **How We See** — a book on perception science for interface design: optics, retina,
  visual pathways, contrast, colour, depth, eye movements, attention, recognition,
  memory, mental models, heuristics and biases, prospect theory, choice architecture,
  human error, aesthetics, consciousness. 160 graded scientific claims, 79 myths and
  oversimplifications, about 285 terms, about 216 cited sources.
- **UX Book** — an internal product-UX standard: screen principles, evidence and
  measurement, performance targets as a UX responsibility, number and date formats,
  forgiving inputs, mobile mechanics, kiosk / POS / handheld rules, the unified approval
  gate.

## Open-source skills (MIT licence unless stated)

- emilkowalski/skills — animation and design-engineering guidance: frequency gate,
  duration and easing, springs and gestures, properties and performance,
  interruptibility, reduced motion, feedback, overlays, mobile-native feel, the review
  bar for motion. MIT, © 2026 Emil Kowalski.
- jakubkrehel/skills — interface craft: surfaces and radius, icons, typography
  rendering, colour systems, accessibility essentials (WCAG 2.2), layout, product
  writing, state polish, the "break" stress test, the interface review. MIT,
  © 2026 Jakub Krehel.
- kylezantos/design-motion-principles — the three motion lenses (restraint,
  production polish, playful experimentation) distilled from the published work of
  Emil Kowalski, Jakub Krehel and Jhey Tompkins; the motion audit checklist; the
  anti-AI-slop motion tells. MIT, © 2026 Kyle Zantos.
- Dammyjay93/interface-design — design-review dimensions, the deslop cleanup pass,
  the design-direction vocabulary, "consistency beats perfection". MIT,
  © 2026 Damola Akinleye.
- vercel-labs/web-interface-guidelines (reached through the `web-design-guidelines`
  skill in vercel-labs/agent-skills) — 100+ testable web interface rules on
  accessibility, forms, feedback, performance, typography and copy. MIT,
  © 2025 Vercel Labs.
- LottieFiles/motion-design-skill — motion purpose taxonomy, choreography, duration
  and easing tables, property selection, motion personality archetypes, quality rules.
  MIT, © 2025 LottieFiles.
- rastian/interaction-design-skills — micro-interaction anatomy (trigger → rules →
  feedback → loops and modes), affordance and feedback principles. No licence file in
  the repository; only long-published principles (Norman, Tognazzini, Nielsen Norman
  Group) were taken from it, paraphrased, never quoted.

## Usability-motion techniques and animation research (added 2026-09-26)

Drives lens 09 · "Motion serves one of four usability jobs" and "Twelve usability techniques",
and foundations · object constancy. All paraphrased; nothing quoted beyond technique names.

- **Issara Willenskomer, "Creating Usability with Motion: The UX in Motion Manifesto."**
  UX in Motion (Medium), 31 March 2017.
  https://medium.com/ux-in-motion/creating-usability-with-motion-the-ux-in-motion-manifesto-a87a4584ddc
  — the four ways motion supports usability (expectation, continuity, narrative,
  relationship), the realtime / non-realtime distinction, and the 12 principles (easing,
  offset & delay, parenting, transformation, value change, masking, overlay, cloning,
  obscuration, parallax, dimensionality, dolly & zoom). Read from an archived 2018 snapshot
  of the Medium page and the UX Magazine republication
  (https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto).
  © the author; the skill paraphrases and renames. The job assigned to each technique follows
  the wording of its own definition; the manifesto gives no evidence beyond examples, and its
  "always ease" and its value-change, parallax, dimensionality and dolly & zoom
  recommendations are reconciled in the lens with the frequency gate, the keyboard rule, the
  registers and reduced motion.
- Heer, J. & Robertson, G. (2007). Animated transitions in statistical data graphics. IEEE
  TVCG 13(6), 1240–1247. doi:10.1109/TVCG.2007.70539 — two controlled experiments; animated
  and staged transitions vs static; design principles (congruence, apprehension, staging,
  object constancy and its abuse). Principles, results and conclusion read.
- Tversky, B., Morrison, J. B. & Bétrancourt, M. (2002). Animation: can it facilitate?
  International Journal of Human-Computer Studies 57, 247–262. doi:10.1006/ijhc.2002.1017 —
  review; congruence and apprehension principles; little benefit of animation over
  equivalent static graphics for explaining systems; exception for real-time reorientation.
  Abstract and sections 1–3 read.
- Chang, B.-W. & Ungar, D. (1993). Animation: from cartoons to the user interface. UIST '93,
  45–55. doi:10.1145/168642.168647 — design and system paper (no controlled study): solidity,
  exaggeration, reinforcement; no sudden materialisations or disappearances; slow in and slow
  out; follow-through. Abstract and principle sections read.
- Chevalier, F., Henry Riche, N., Plaisant, C., Chalbi, A. & Hurter, C. (2016). Animations 25
  years later: new roles and opportunities. AVI '16, 280–287 — taxonomy of 23 roles in 5
  categories (keeping in context, teaching aid, user experience, data encoding, visual
  discourse), revisiting Baecker & Small (1990, not read directly). Abstract, role table and
  the keeping-in-context section read.
- Bederson, B. B. & Boltman, A. (1999). Does animation help users build mental maps of spatial
  information? IEEE InfoVis '99, 28–35 (read as HCIL technical report 98-11) — 20
  participants; animated viewpoint changes improved reconstruction of the space, no time
  penalty, no difference in satisfaction.
- Klein, C. & Bederson, B. B. (2005). Benefits of animated scrolling. CHI '05 Extended
  Abstracts. doi:10.1145/1056808.1057068 — task time up to 5.3 % faster (reading, 300 ms) and
  up to 24 % (symbol counting, 500 ms); reading errors down up to 54 %. Abstract read.
- Chalbi, A., Ritchie, J., Park, D., Choi, J., Roussel, N., Elmqvist, N. & Chevalier, F.
  (2020). Common fate for animated transitions in visualization. IEEE TVCG 26(1), 386–396
  (arXiv:1908.00661) — crowdsourced grouping study; common motion outranks dynamic luminance,
  size and luminance. Abstract and introduction read.
- Cockburn, A. & McKenzie, B. (2002). Evaluating the effectiveness of spatial memory in 2D
  and 3D physical and virtual environments. CHI '02, 203–210. doi:10.1145/503376.503413 —
  performance fell as freedom to use the third dimension rose; 3D judged more cluttered.
  Abstract read.
- Frederick, D., Mohler, J., Vorvoreanu, M. & Glotzbach, R. (2015). The effects of parallax
  scrolling on user experience in web design. Journal of Usability Studies 10(2), 87–95 —
  86 participants; parallax significantly more fun, no difference in perceived usability,
  satisfaction, enjoyment or visual appeal; two participants reported motion sickness. The
  journal page returned 404 in this pass; findings taken from the summary in Sharma, S. &
  Murano, P. (2020), "A usability evaluation of Web user interface scrolling types", First
  Monday — treat as secondary.
- Harrison, B., Ishii, H., Vicente, K. & Buxton, W. (1995). Transparent layered user
  interfaces: an evaluation of a display design to enhance focused and divided attention.
  CHI '95, 317–324 — semi-transparent layers: background awareness vs foreground
  interference, level depends on task and content. Summary read, not the full text; no
  numbers taken.

Platform guidance (publisher terms apply; paraphrased):
- Material Design motion transition patterns — container transform, shared axis, fade
  through, fade — as documented in Material Components for Android, docs/theming/Motion.md
  (Apache 2.0).
- Apple Human Interface Guidelines — Motion (purposeful motion, optional motion, realistic
  feedback, avoid motion on frequent interactions, let people cancel motion).
- Microsoft Fluent 2 — Motion (functional, natural, consistent, appealing; enter/exit,
  elevation, top-level fade, container transform; staggering and hierarchy).
- W3C, Understanding WCAG 2.2 · SC 2.3.3 Animation from Interactions (AAA) — motion animation
  triggered by interaction can be disabled; parallax named; vestibular disorders. W3C
  Document Licence.

Implementation references for the "In code" lines (platform APIs, not library content):
- MDN Web Docs — View Transition API; CSS scroll-driven animations; `clip-path` animation
  type (CC BY-SA 2.5).
- Paul Lewis, "FLIP Your Animations", aerotwist.com, 11 February 2015.
- Apple Developer Documentation — SwiftUI `matchedGeometryEffect(id:in:properties:anchor:isSource:)`
  (iOS 14), `NavigationTransition.zoom(sourceID:in:)` and `matchedTransitionSource(id:in:)`
  (iOS 18).
- Android Developers — Shared element transitions in Compose (`SharedTransitionLayout`,
  `Modifier.sharedElement`, `Modifier.sharedBounds`, `clipInOverlayDuringTransition`).
- Motion (motion.dev) — React layout animations, `layout` and `layoutId`.

## What was deliberately left out

- Every design-system-specific value: fonts, hexes, tokens, spacing ladders, component
  names, node ids, brand rules. They belong in a project's own `design-decisions.md`.
- Framework- and library-specific animation skills (GSAP, Framer Motion, Animate.css,
  Lottie runtime) — implementation, not review. The one-line "Implementation" fields in lens
  09's technique entries name platform APIs and generic library options only.
- A third-party research-first design skill whose content is not the project's own.
