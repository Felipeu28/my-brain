---
tags:
  - graph/spoke
---
# Vibe Coding

**Type:** concept (programming paradigm)
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/concepts/claude-code]], [[wiki/concepts/openclaw-hermes]], [[wiki/concepts/brain-architecture]]

---

## Summary
"Vibe coding" is the emergent pattern of software development where humans describe intent in natural language and AI (Claude Code, Cursor, Codex) generates the actual implementation. The term captures both the freedom (no syntax memorization) and the risk (accumulating dead code, inconsistent patterns, unreviewed logic) of this approach. It's gone from niche meme to mainstream practice in the March–April 2026 bookmark window.

## Key Points
- **Spec-based workflow** — @buildwithhassan + @trq212: "Write rough spec → let Claude interview you until it knows exactly what to build." This is the disciplined version of vibe coding.
- **Dead code risk** — @gabriberton: "Vibe coding creates lots of dead code. Run a delete-dead-code prompt often." The entropy problem is real and growing.
- **design-system.md pattern** — @jasondoesstuff: "Step 1: Tell Claude Code to create a design-system.md from your current app. Step 2: reference it everywhere." Prevents visual entropy.
- **Invoice builder as demo** — @Timmysofine built a free invoice builder with Claude for freelancers using this pattern (620K views).
- **Non-developer access** — vibe coding is moving coding from an expert skill to a general-purpose tool; non-developers are shipping real products.

## The Spec-Based Upgrade
The best practitioners aren't just vibing — they're writing specs:
1. Write a rough spec (what you want + who it's for)
2. Let Claude ask clarifying questions until it fully understands scope
3. Claude generates the build plan
4. Approve → Claude codes
5. Review output, iterate

This catches ambiguities before code is written, not after.

## Connections
- Runs on [[wiki/concepts/claude-code]] and alternatives ([[wiki/concepts/openclaw-hermes]])
- The design-system.md pattern is the same metadata-file philosophy as CLAUDE.md, MEMORY.md, SOUL.md in the [[wiki/concepts/brain-architecture]]
- At scale, vibe coding becomes the first step of [[wiki/concepts/openclaw-hermes]] workflows

## Moil Relevance
Andres's team ships via vibe coding (Claude Code + Cursor, likely). The dead-code pattern is a real operational risk — if Moil's codebase has accumulated vibe-coding entropy, a cleanup sprint (dead code scan, test coverage audit) is worth scheduling. More importantly: Moil's SMB customers are now vibe-coding their own tools — this shifts the competitive landscape (if SMBs can build their own hiring + marketing tools cheaply, Moil needs to stay ahead on workflow depth and data, not just feature presence).
