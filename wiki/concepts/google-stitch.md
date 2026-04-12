# Google Stitch (Design-to-Code Tool)

**Type:** concept (AI tool)
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/concepts/claude-code]], [[wiki/concepts/vibe-coding]]

---

## Summary
Google Stitch is a design-to-code tool launched by Google in late March 2026. The workflow: describe or sketch your UI in Stitch → Stitch generates production-ready frontend code → hand off to Claude Code for backend logic. It's positioned as the design layer that Claude Code shouldn't be doing. Tutorial video by @stitchbygoogle got 684K views.

## Key Points
- **Official launch:** Stitch 2.0, March 2026 (@stitchbygoogle tutorial, 684K views)
- **Use case:** "STOP asking Claude Code to design your apps" (@PrajwalTomar_) — Claude Code is better at logic than aesthetics; Stitch handles aesthetics
- **Integration:** Stitch output → Claude Code input; they complement rather than compete
- **The design-system.md pattern:** @jasondoesstuff's workflow: Stitch/Claude creates design-system.md → reference that file in every future UI conversation → prevents design entropy across sessions

## The Design Layer Problem
Without a dedicated design tool:
- Every vibe-coding session starts fresh on UI decisions
- Inconsistent button styles, spacing, color usage accumulate across sessions
- AI-generated UIs look "AI-slop" (recognizably AI-generated, uncanny)

With Stitch + design-system.md:
- UI language is defined once
- Every subsequent build references the same design language
- The product looks coherent even across dozens of AI sessions

## Connections
- Complements [[wiki/concepts/vibe-coding]] by solving the UI consistency problem
- The design-system.md output is the design equivalent of AGENTS.md — a persistent context file the agent reads before every UI task
- Lovable (animation guides from @damienghader) occupies a similar niche for animated components

## Moil Relevance
If Moil's frontend development uses Claude Code, Stitch could be valuable for:
1. Establishing a consistent design-system.md for moilapp.com
2. Prototyping new UI features before committing to Claude Code implementation
3. Reducing the "AI slop" aesthetic in any AI-generated Moil UI

**Action:** Create a design-system.md for Moil's current app UI as a one-time exercise. Use it as a CLAUDE.md companion file that's referenced in every frontend development session.
