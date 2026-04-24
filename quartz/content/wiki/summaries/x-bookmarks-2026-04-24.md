---
tags:
  - graph/leaf
---
# X Bookmarks Summary — 2026-04-24

**Type:** summary
**Last updated:** 2026-04-24
**Source:** [[raw/x-bookmarks-2026-04-24]]
**Period:** Feb 4 – Apr 24, 2026 (82 bookmarks, captured by gstack /browse, account `@roarkittys`)
**Related:** [[wiki/concepts/claude-code]], [[wiki/concepts/managed-agents]], [[wiki/concepts/openclaw-hermes]], [[wiki/concepts/llm-knowledge-bases]], [[wiki/concepts/linkedin-gtm]], [[wiki/concepts/ai-org-design]], [[wiki/concepts/managed-agents]], [[wiki/concepts/self-learning-gtm-brain]]

---

## Why this digest exists

This is the first bookmark capture since the deep compile of 2026-04-12 ([[wiki/summaries/x-bookmarks-deep-compile-2026-04-12]]). 82 saved items spanning Feb 4–Apr 24. Themes are grouped by Andres's working domains — not by author or chronology — so this becomes a routing layer for downstream concept-page updates.

## Theme 1 — Claude harness engineering matures

The most consequential signal cluster. Tooling that was rough in March is now opinionated and shareable.

- **Routines vs Schedules vs /loop** — three distinct mechanisms for running Claude work automatically (@coreyganim Apr 14, @NickSpisak_ Apr 14, @claudeai Apr 14). Routines = cloud, no laptop needed (research preview). Schedules = local cron-like. /loop = current session. Decision matrix worth adding to [[wiki/concepts/claude-code]].
- **Recaps feature** (@bcherny Apr 16) — short summaries of what an agent did + what's next, for long sessions. Native to Claude Code now.
- **Adaptive thinking on Opus 4.7** (@bcherny Apr 16) — tune effort level for speed vs. intelligence; replaces budget-based thinking.
- **Claude Doctor** (@aidenybai Apr 15) — reads `~/.claude` to find where Claude keeps messing up and writes new CLAUDE.md rules. The "self-tuning harness" pattern.
- **GBrain v0.10.0** (@garrytan Apr 15) — RESOLVER.md, SOUL.md, ACLs, 24 fat skills with end-to-end tests + evals.
- **Clawputer** (@garrytan Apr 21) — GBrain in the cloud, the hosted alternative to self-hosting OpenClaw.
- **Boris Cherny's complete Claude Code skill collection** (@NainsiDwiv50980 Mar 27) — installable as one skill.
- **Compound Engineering v3** (@trevin Apr 22) — naming cleanup, plan/brainstorm artifacts with paper-trail "idea → commit." Approach worth comparing to Andres's `/brain-ingest` + `/brain-query` flow.
- **Stitch 2.0 + Claude Code via MCP** (@PrajwalTomar_ Apr 21) — the workflow that "stops apps looking like AI slop." [[wiki/concepts/google-stitch]] candidate update.
- **DESIGN.md spec open-sourced** (@stitchbygoogle Apr 21) — usable across any tool/platform. Could become a Moil internal convention.
- **Claude setup rots over time** (@itsolelehmann Mar 24) — one detox prompt deletes bloat. Quarterly hygiene worth scheduling.

## Theme 2 — Managed Agents ecosystem hardening

Three weeks after the Apr 8 launch, the use cases are settling.

- **What people actually use Hermes Agent for** (@mvanhorn Apr 19) — pre-call research, proposal writing, CRM sync. Concrete workflow list, not hype. Direct relevance to [[wiki/concepts/openclaw-hermes]].
- **Claude Managed Agents quietly killed AI startups** (@voxyz_ai Apr 9) — "doing real work for users" — pattern repeats from the Apr 12 deep compile, now with three-week-out evidence.
- **OpenClaw real use cases** (@voxyz_ai Mar 28) — social media ops + email automation, 5 posts/day vs 1.
- **OpenClaw security audit** (@coreyganim Apr 9) — SSH, .env, AWS exposure with 3-level fix (sandbox / allowlist / .gitignore). Reinforces the strategic action item already in [[MEMORY]].
- **Claire** (@coreyganim Apr 2) — OpenClaw agent generating content + scheduling posts, 21M views/mo on X.
- **Chief of Staff on OpenClaw** (@rsarver Apr 6) — "better than any human EA I've hired" from a VC.

## Theme 3 — AI for SMB / vertical AI

- **Mark Cuban's framing** (@WorkflowWhisper Apr 18) — "real AI money is 1 vertical, 1 workflow, 1 painful problem." Direct ammo for Moil's "narrow ICP" thesis.
- **$1T agent-first opportunity** (@gregisenberg Apr 18) — 10,000+ niches, SaaS going headless in 18 months.
- **Sequoia $1T thesis** (@hamudinaanaa Apr 16) — must measure economic outcomes, not tooling. Aligns with Moil's outcome-selling positioning.
- **Ramp 99% AI tool adoption then stuck → built per-employee AI coworkers** (@sebgoddijn Apr 9) — pattern Moil customers will hit when they go from "we use AI" to "we *staff* with AI."
- **From Hierarchy to Intelligence** (@jack Mar 31) — speed is the best predictor in the agent era.
- **$3M revenue from 20 Claude Code agents** (@Mitchell Mar 23) — concrete revenue per agent benchmark.
- **AutoAgent** (@aakashgupta Apr 3) — first open-source self-optimizing agents library. Watch list.

## Theme 4 — GTM / outbound reality check

- **🔥 LinkedIn algorithm 2026: AI content is dead** (@paolo_scales Apr 21) — tactics from 6 months ago killing reach now. Direct conflict with Moil's content engine assumptions; needs a deep look. Update [[wiki/concepts/linkedin-gtm]].
- **Meeting-to-pipeline gap** (@itsalexvacca Apr 14) — 847 AI SDR meetings → 11% converted vs 312 human → 35%. Quantified case against full-AI SDR motion.
- **Cold outbound definitively solved** (@itsalexvacca Apr 8) — 23M-send study reduces to 5 bullets.
- **Connect Claude to LinkedIn in 1 click** (@pierreeliottlal Apr 18) — 300+ skills, finds leads + writes messages.
- **Cold Outreach Bible** (@adriannalakatos Apr 10) — first-person cold-emailed-into-Buildspace template.
- **Self-learning GTM Brain** (@pierreeliottlal Mar 31) — learns from every campaign, compounds. Already covered in [[wiki/concepts/self-learning-gtm-brain]] — fresh source citation.
- **Multi-channel GTM where every channel makes every other better** (@MichLieben Mar 31) — $90k/month breakthrough framing. Already covered in [[wiki/concepts/gtm-system-multi-channel]].

## Theme 5 — Local inference + open-source models

- **Nvidia 80 free hosted AI models** (@dhruvtwt_ Apr 22) — MiniMax, GLM, Kimi, DeepSeek, GPT-OSS-120B. Possibly relevant to Moil's multi-model fallback (Apr 21 Adeleke decision).
- **Locally This, Locally That** (@leopardracer Apr 22) — full AI app running on-device with Qwen.
- **Grok Speech-to-Text API** (@xai Apr 17) — multi-speaker, 25 languages, "best market price." Worth comparing to Moil's current Groq Whisper choice.
- **Gemini 3.1 Flash TTS** (@OfficialLoganK Apr 15) — scene direction, audio tags, 70 languages.
- **27B Qwen3.5 distill on Claude Opus 4.6 traces beats Sonnet 4.5** (@TheCraigHewitt Apr 1) — local inference quality climbing.
- **Gemma 4 on MLX** (@neural_avb Apr 2) — 125 quantized models from Prince Canuma. Direct Mac Mini M4 relevance.

## Action items surfaced (not auto-added to MEMORY)

The following are *candidate* MEMORY items — not added automatically because none has a clean owner/date yet. Andres should triage during weekly review.

- Investigate Claude Routines / Schedules vs current launchd jobs — could simplify [[wiki/concepts/brain-architecture]] automation tier
- Read Paolo Scales LinkedIn-2026 thread before next [[wiki/concepts/linkedin-gtm]] revision; assumptions may be stale
- Evaluate Hermes Agent vs Pi for the proposal-writing / pre-call-research use case (matches @mvanhorn Apr 19 list)
- Consider DESIGN.md spec adoption for Moil-built sites (Stitch + Claude Code workflow)
- Schedule a quarterly "Claude Doctor" / "detox prompt" pass on `~/.claude`
- Test Grok Speech-to-Text API against Groq Whisper for transcript quality + cost

## Cross-reference

Concept pages that should be updated (not done in this digest — would expand scope):
- [[wiki/concepts/claude-code]] — Routines / Schedules / /loop trio, Recaps, adaptive thinking, Claude Doctor
- [[wiki/concepts/managed-agents]] — Hermes use case list (mvanhorn), Clawputer
- [[wiki/concepts/linkedin-gtm]] — Paolo Scales 2026 algorithm shift
- [[wiki/concepts/ai-org-design]] — Ramp 99% adoption pattern, "per-employee AI coworker"
- [[wiki/concepts/openclaw-hermes]] — Hermes-specific use cases, OpenClaw security 3-level fix
