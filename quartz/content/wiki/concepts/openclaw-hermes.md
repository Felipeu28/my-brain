---
name: openclaw-hermes concept
description: The open-source parallel ecosystem to Claude Code — gstack, Superpowers, Compound Engineering, gbrain
type: concept
tags: [concept, moil, seed]
---

# OpenClaw / Hermes Ecosystem

**Type:** concept
**Last updated:** 2026-04-11
**Source:** [[raw/x-bookmarks-2026-04-11 copy.md]], [[raw/x-bookmarks-2026-04-11.md]]
**Related:** [[wiki/concepts/claude-code]], [[wiki/concepts/claude-cowork]], [[wiki/concepts/managed-agents]]

---

## Summary
A growing parallel open-source ecosystem around OpenClaw and Hermes — community-built agent harnesses, second-brain tools, and plugins that deliver Claude-Code-like workflows on any LLM (including local models). Strongly trending in Andres's X bookmarks.

## Key Projects
- **gstack** — harness with skills (browse, qa, design, ship, land-and-deploy, codex, cso, etc.). Comparable to Claude Code skills but open.
- **Superpowers** — 121K ⭐ (@Voxyz_ai comparison).
- **Compound Engineering** — sibling to Superpowers / gstack.
- **gbrain** — @garrytan: "OpenClaw/Hermes total-recall brain" at [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain).
- **Clawdex** — Telegram-operated Yolo Codex machine (@swader).
- **openclaw-codex-app-server** — control Codex from Telegram & Discord (@huntharo, pwrdrvr).
- **Paperclip** — orchestration tool behind 30K ⭐ (referenced by @startupideaspod).

## Key Points
- **Run OpenClaw on local models** — @JulianGoldieSEO: Qwen 3.6 Plus via Alibaba API.
- **27B Qwen3.5 on Mac Mini** (@TheCraigHewitt) — near-Opus-level local inference is real.
- **Gemma 4 on MLX day-0** (@neural_avb) — Mac Silicon is a first-class agent target.
- **Community meta** — @IndraVahan: "Drop your Hermes / OpenClaw use cases" as a community thread.
- **Chief-of-staff pattern** — @rsarver: "Chief of staff on OpenClaw better than any human I've hired" (Apr 6).
- **Assistant pattern** — @ryancarson: "Turn OpenClaw into the world's best assistant" (1.2M views).

## Voxyz comparison
gstack vs. Superpowers vs. Compound Engineering — see @Voxyz_ai Mar 29 article. Three overlapping harnesses, different philosophies.

## Connections
- **Alternative runtime** to [[wiki/concepts/claude-code]] — same shape, different governance/pricing.
- **Works with local models** → ties to Moil Brain architecture running on M4 Mac Mini (Gemma 4 via LM Studio per `~/My Brain/CLAUDE.md`).
- **Competes with** [[wiki/concepts/managed-agents]] in the persistent-agent niche.

## Moil Relevance
- **Evaluate gstack-style harness** for Moil agent workflows — Andres is already using `/browse`, `/ship`, `/review` skills via gstack.
- If Moil ever builds its own agent orchestration, OpenClaw/Hermes is the open-source base to fork — cheaper than building from scratch.
- Community is where the new playbooks emerge first; track @Voxyz_ai, @coreyganim, @garrytan.
