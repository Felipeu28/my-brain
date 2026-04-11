---
name: claude-code-changelog
description: Append-only changelog of Claude Code features, launches, and ecosystem shifts
type: radar
---

# Claude Code — Running Changelog

**Type:** radar (append-only — newest on top)
**Last updated:** 2026-04-11
**Purpose:** A single place to see Claude Code's trajectory without rereading old bookmark digests. Updated during weekly X bookmark sweeps and whenever Anthropic ships.
**Related:** [[wiki/concepts/claude-code]], [[wiki/minds/dario-amodei]], [[wiki/concepts/managed-agents]], [[wiki/concepts/claude-cowork]]

---

## How to use this file
- Add new entries at the **top** with date, feature name, 1-line summary, and source link.
- Group by month. Keep each entry tight — deep context lives in concept pages.
- When an entry becomes load-bearing, promote it to `wiki/concepts/*` and backlink.

---

## 2026-04

### Apr 9 · Monitor tool
Lets Claude create background scripts that wake the agent later. New primitive for long-running / scheduled work inside a single session.
- Source: @noahzweben, @trq212 · [[wiki/summaries/x-bookmarks-2026-04-11-copy]]

### Apr 8 · Claude Managed Agents (GA) 🔥
Official launch — persistent managed agents you build and deploy. 20M views on the announcement. Dominated the X feed for a week.
- Source: @claudeai · [[wiki/concepts/managed-agents]]
- Ecosystem response: @NickSpisak_ "First working Managed Agent" (Apr 8), @sharbel "Deploy in 10 minutes" (Apr 9), @coreyganim "No Docker/orchestration needed" (Apr 9)

### Apr 8 · "7 text files will run your business in 2027" meme
@agentskills_ai's framing of the agent-harness approach went viral — skills + memory + identity files as the minimum runnable agent.
- Source: @agentskills_ai

### Apr 7 · Cowork "4 layers in one weekend" framework
@rubenhassid published a tiered-adoption framework for Claude Cowork.
- Source: @rubenhassid

### Apr 3 · 8 Claude Code Hooks That Automate What You Keep Forgetting
@zodchiii · 2M views. Comprehensive hooks guide.
- Source: @zodchiii

### Apr 2 · LLM Knowledge Bases (Karpathy)
Not a Claude Code feature — but the viral post that created the "Claudeopedia" wave that's now the dominant way people organize Claude Code projects. 19.3M views.
- Source: @karpathy · [[wiki/minds/andrej-karpathy]] · [[wiki/concepts/llm-knowledge-bases]]

---

## 2026-03

### Mar 30 · Codex plugin for Claude Code
`plugin marketplace add openai/codex-plugin-cc` — OpenAI's Codex integrated as a Claude Code plugin. 941K views on the reach_vb announcement.
- Source: @reach_vb, @dkundel · github.com/openai/codex-plugin-cc

### Mar 30 · Meta Harness — self-improving agents
@MatthewBerman + @yoonholeee: Claude Code + Cursor that improve themselves autonomously.
- Source: @MatthewBerman

### Mar 29 · Hidden Claude Code features mega-thread
@bcherny's thread hit 3.9M views, 52K bookmarks — the canonical reference for under-used features.
- Source: @bcherny

### Mar 27 · Non-developer Claude Cowork guide
@NickSpisak_'s 10-things-to-set-up-first for non-devs. Still referenced as the baseline onboarding.
- Source: @NickSpisak_

---

## Pending / watch list

- **Claude Code security audit** — Andres's todo per [[MEMORY]]. What does Claude Code actually have access to on the Mac Mini M4?
- **Managed Agents pricing** — still unclear what the cost structure looks like at scale.
- **Skills marketplace maturity** — claude-ads (190 checks), Google Ads audit, SEO audits all shipped privately. When does Anthropic formalize a skills marketplace?
- **Codex + Claude Code convergence** — if the plugin deepens, is the "Claude vs OpenAI" binary even meaningful for coding agents?
