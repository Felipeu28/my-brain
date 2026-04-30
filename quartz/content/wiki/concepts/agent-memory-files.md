---
tags:
  - graph/spoke
---
# Agent Memory Files (SOUL.md / MEMORY.md / DREAMS.md Pattern)

**Type:** concept (AI architecture pattern)
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11]]
**Related:** [[wiki/concepts/brain-architecture]], [[wiki/concepts/claude-code]], [[wiki/concepts/managed-agents]]

---

## Summary
The pattern of using structured markdown files as persistent memory and identity for AI agents. Emerged independently from multiple creators in the bookmark period and crystallized into a small set of canonical files: SOUL.md, MEMORY.md, DREAMS.md, AGENTS.md, and design-system.md variants. @vincent_koc (Apr 5) gave this the clearest framing: "A Theory of Mind in Three Files."

## The Canonical File Set

### SOUL.md — Identity
"Who I am" — the agent's (or human's) enduring values, operating principles, communication style, and non-negotiables. Stable; rarely changes. Forces explicit articulation of what the agent stands for.

### MEMORY.md — What You've Lived  
"What I've lived" — running log of past decisions, outcomes, lessons learned, things to remember. Grows over time. Is the "working memory" that prevents the agent from making the same mistake twice.

### DREAMS.md — Direction
"What I'm becoming" — aspirations, long-term goals, the direction of growth. Helps the agent make consistent decisions when priorities conflict.

### AGENTS.md — Operational Context
Loaded by Pi and Claude Code at startup. Contains role, business description, key contacts, priorities, tone preferences, rules. The practical operating briefing that SOUL.md/DREAMS.md provide the values foundation for.

### design-system.md (@jasondoesstuff)
Step 1: Claude Code creates design-system.md from your current app. Step 2: reference it everywhere. Prevents visual entropy across AI-generated UI components — the design equivalent of SOUL.md for aesthetics.

### agentskills_ai "7 Text Files" (Apr 8)
"These 7 text files will run your business in 2027" — the agent harness approach. These 7 files collectively encode enough context for an AI agent to operate a business function autonomously:
1. AGENTS.md (role + context)
2. MEMORY.md (history)
3. SOUL.md (identity)
4. DREAMS.md (direction)
5. A skills/ directory (capabilities)
6. A context/ directory (domain knowledge)
7. Workflow triggers (automation hooks)

## The @davemorin Observation
@vincent_koc quotes @davemorin's "A Theory of Mind in Three Files" — the philosophical claim is that SOUL + MEMORY + DREAMS is sufficient to reconstruct a person's (or agent's) decision-making. This maps to how human psychology thinks about identity (values + experience + aspiration).

## Why This Matters Beyond Philosophy
The files-as-memory pattern solves the statelessness problem of LLMs: without external state, every conversation starts from zero. With structured memory files, the agent accumulates context across sessions and improves over time without any vector database or embedding infrastructure.

## Connections
- The AGENTS.md in `~/My Brain/knowledge-base/pi-workspace/AGENTS.md` is already implemented
- MEMORY.md at `~/My Brain/knowledge-base/MEMORY.md` is the running actions/context file
- [[wiki/concepts/brain-architecture]] implements this pattern as its Storage layer
- The "7 text files" are the minimum viable agent harness — [[wiki/concepts/openclaw-hermes]] is one implementation

## Moil Relevance
The SOUL.md / MEMORY.md / DREAMS.md pattern could be packaged as a Moil onboarding product: "Complete Moil's 21 questions and we generate your business's SOUL.md, MEMORY.md, and DREAMS.md — the three files that let your AI Co-Founder know exactly who you are and where you're going." This would make the onboarding feel more meaningful and create a durable artifact the customer owns. The Karpathy-style wiki pattern (this Brain) is the enterprise version; these three files are the MVP version any SMB can understand.
