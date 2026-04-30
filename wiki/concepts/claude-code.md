---
name: claude-code concept
description: Anthropic's CLI/agent for software engineering tasks — core to Andres's Brain + Moil dev workflows
type: concept
tags:
  - graph/spoke
---

# Claude Code

**Type:** concept
**Last updated:** 2026-04-24
**Source:** [[raw/x-bookmarks-2026-04-11.md]], [[raw/x-bookmarks-2026-04-11.md]], [[raw/brain-guide.md]], [[raw/x-bookmarks-2026-04-24]]
**Related:** [[wiki/concepts/claude-cowork]], [[wiki/concepts/managed-agents]], [[wiki/concepts/llm-knowledge-bases]], [[wiki/concepts/openclaw-hermes]], [[wiki/concepts/brain-architecture]]

---

## Summary
Anthropic's official CLI agent for software engineering and knowledge work. It's the runtime for Andres's Brain, his coding workflow, and most of the "second brain" and "Claudeopedia" patterns going viral in the X ecosystem.

## Key Points
- **Hidden features thread** (@bcherny) — 3.9M views, 52K bookmarks: mega-guide to under-used capabilities.
- **Skills** — Markdown-packaged prompts that Claude Code invokes on demand. Viral examples: `claude-ads` (190 audit checks), Google Ads audit, SEO audit.
- **Hooks** — shell commands triggered on events (pre/post tool call, prompt submit). See "8 Claude Code Hooks" (zodchiii, 2M views).
- **Plugin marketplace** — install Codex plugin via `plugin marketplace add openai/codex-plugin-cc`.
- **Monitor tool** — lets Claude create background scripts that wake the agent later.
- **Knowledge base patterns** — Karpathy-inspired wiki + /last30days + /wiki skills (@alliekmiller "Claudeopedia"; @NickSpisak_ rebuilt in 20 min).
- **Obsidian integration** — Claude Code + Obsidian = viral "second brain" pattern (@defileo 3.9M views, @aiedge_ Ultimate Guide).
- **Security gotchas** (@coreyganim) — Claude has access to `~/.ssh/config`, AWS creds, `.env` files by default. Audit permissions.
- **Self-improvement** — Meta Harness (@MatthewBerman, @yoonholeee): Claude Code + Cursor that improve themselves autonomously.

## Connections
- **Claude Cowork** sits on top of Claude Code for scheduled/background workflows → [[wiki/concepts/claude-cowork]].
- **Managed Agents** is the deployment layer for persistent agents → [[wiki/concepts/managed-agents]].
- **OpenClaw / Hermes** are the open-source parallel ecosystems to Claude Code → [[wiki/concepts/openclaw-hermes]].
- Andres uses Claude Code as the runtime for the entire [[wiki/concepts/brain-architecture]].

## Moil Relevance
- Moil's entire dev + content pipeline could run on Claude Code skills (SEO, blog posts, ads audits, customer support triage).
- The `claude-ads` pattern could inspire a "Moil-ads audit" skill for Moil customers' ad accounts.
- Security audit is a real todo — Andres should know what permissions Claude Code has on the Mac Mini M4 before running autonomously.

## Apr 14–24 update — automation runtimes converging

From [[wiki/summaries/x-bookmarks-2026-04-24]]:

- **Routines vs Schedules vs /loop** — three distinct ways to run Claude work automatically (@coreyganim, @NickSpisak_, @claudeai Apr 14). **Routines** = cloud, no laptop required (research preview). **Schedules** = local cron-like. **/loop** = current-session iteration. Decision matrix relevant to whether the Brain's launchd jobs ([[wiki/concepts/brain-architecture]]) should migrate to Routines.
- **Recaps** (@bcherny Apr 16) — short summaries of what an agent did + what's next, native to long sessions.
- **Adaptive thinking on Opus 4.7** (@bcherny Apr 16) — tune effort level for speed vs intelligence; replaces budget-based thinking.
- **Claude Doctor** (@aidenybai Apr 15) — reads `~/.claude` to find where Claude keeps messing up and writes new CLAUDE.md rules. Quarterly hygiene candidate.
- **Boris Cherny's full Claude Code skill collection** (@NainsiDwiv50980 Mar 27) — installable as one skill bundle.
- **Compound Engineering v3** (@trevin Apr 22) — naming cleanup, plan/brainstorm artifacts with idea→commit paper trail. Worth comparing to `/brain-ingest` + `/brain-query` flow.
- **Setup rots over time** (@itsolelehmann Mar 24) — one detox prompt deletes bloat and improves output. Schedule a quarterly pass.
