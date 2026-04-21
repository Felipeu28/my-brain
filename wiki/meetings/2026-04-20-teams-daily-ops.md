---
tags:
  - graph/spoke
---
# Apr 20, 2026 — Teams Daily Operations

**Type:** meeting
**Last updated:** 2026-04-20
**Source:** [[raw/teams-2026-04-20]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/moil/active-projects]], [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/people/inna-benyukhis]], [[wiki/meetings/2026-04-18-teams-daily-ops]]

---

## Summary

36 Teams messages Apr 19–20 across 5 threads (1:1 Jacob, 1:1 Taiwo, 1:1 Adeleke, Moil Marketing, Moil Team). Monday Collaboration call convened in the afternoon with internet trouble from Jacob; meeting ran two tracks — content/growth strategy (Inna's social performance, converting long-form interviews → IG clips, face-led educational direction) and a production-fixes track where Adeleke worked the `business_plan_beta_prod` codebase and pushed fixes. Jacob opened a process-improvement proposal for a Project Requirements Document per new dev/demo/feature. Abiodun confirmed week-ending content delivery (Apr 17/18/19/21 for Inna; Moil Apr 20/22 flyers + videos). Taiwo re-engaged on FitLogic + Meridian for the day; Andres sent FitLogic.docx and Taiwo shared personal Gmail `taiwotriumphant@gmail.com`. Jacob opened the Instagram tagging problem (can't tag accounts from Meta Business — needs IG access from Inna or send-and-post model).

---

## Decisions

1. **PRD process proposed (Jacob, Apr 19 11:21 PM).** Jacob asked that every new development project, demo, or feature begin with a Project Requirements Document — to help the team "move faster, iterate well, deliver properly, and clear tasks off our table efficiently." Awaiting Andres sign-off. If adopted this becomes a standing gate for new work.
2. **Memory-mode onboarding over static onboarding.** Andres told Adeleke to review the "new memory one" first because it's less invasive than the static onboarding — review-first, then decide whether to ship (Apr 20 11:41 AM). Adeleke agreed.
3. **Adeleke pushing production fixes without a branch-review gate.** Adeleke said he'd already fixed bugs on prod (`business_plan_beta_prod`). When prompted, he said the workflow will still create a new branch — he'll review and push from there. Accepted.
4. **Claude Code session handed off for review again.** Andres shared `https://claude.ai/code/session_0156Da69uG1W8jSEof5V2xgb` to Moil Team at 5:02 PM — continues the pattern of Andres running Claude Code sessions and handing verification to Adeleke.
5. **Instagram tagging handling — two options offered to Inna.** Jacob framed the options: (a) Inna gives Moil access to her IG/LinkedIn so they can post + tag directly; (b) Moil creates content and sends to Inna to post herself (since IG blocks tagging accounts from Meta Business). Awaiting Inna's choice.

## Action Items

| Owner | Action | Deadline | Status |
|---|---|---|---|
| Andres | Respond to Jacob's PRD proposal — adopt / modify / decline | Apr 21 | Open — direct founder decision needed |
| Adeleke | Push `business_plan_beta_prod` prod fixes on new branch, review, then merge | Apr 20–21 | In flight — Adeleke already fixed bugs |
| Adeleke | Review the new "memory" onboarding variant (less invasive than static onboarding) before Andres decides ship direction | Apr 20–21 | Open — Andres explicit ask |
| Adeleke | Review Claude Code session `session_0156Da69uG1W8jSEof5V2xgb` (latest Andres handoff) | Apr 21 | Open |
| Taiwo | Walk through FitLogic + Meridian with Andres (Taiwo explicitly asked) | Apr 20 | In progress — Andres sent FitLogic.docx 5:57 PM |
| Jacob | Get Inna's decision on IG/LinkedIn access vs. send-and-post workflow; confirm whether LinkedIn tagging is in-scope | Apr 21 | Open |
| Jacob | Fix internet connectivity for Monday calls (he missed the start, team waited) | Ongoing | Recurring blocker |
| Abiodun | Confirm Monday Apr 21 + Moil Apr 22 assets are captioned with Jacob's copy (already delivered: Struggling-to-keep-up.png, Connect-with-GenZ.mp4, Posting-Consistently.mp4, Ask-Moil.mp4) | Apr 21 | Open — assets in, captions with Jacob |
| Andres | Respond to Jacob on the "Posting Consistently.mp4" reviewed thoughts | Apr 21 | Open |

## Key Signals

- **Jacob escalated to process owner** (PRD proposal). First time Jacob has proactively pushed a team-wide operating framework rather than just executing. Signal of intent to stabilize delivery after the Apr 15–18 testing-pace escalations. This extends the pattern from Apr 18 where Jacob took ownership of the Connectex + Business Coach slip.
- **Adeleke is fixing production bugs without waiting for tasks** — proactive mode. He said: "I already fixed some bugs though" (Apr 20 4:38 PM) in response to Andres starting a project for the same work. Healthy overlap but worth formalizing ownership on `business_plan_beta_prod`.
- **Taiwo re-engaged fully on Apr 20** — despite the Apr 18 time-zone boundary, he proactively asked to go through FitLogic + Meridian in the morning ("Hoping we can go through fitlogic and meridian today"). Taiwo also shared a personal Gmail `taiwotriumphant@gmail.com` — likely for a dev-tool / account invite (context: GitHub, Supabase, or tool access, not confirmed).
- **Monday Collaboration call structure (per Jacob's meeting summary at 4:36 PM):**
  - Track 1 — Content & growth: Inna's social media performance; turning long-form recorded interviews into IG clips; improving follower growth + lead gen via more intentional educational content; "face-led educational content" was the proposed direction; reviewed performance data and post types that drove views
  - Track 2 — Production: Adeleke's proactive prod fixes on `business_plan_beta_prod`; Andres' parallel project for the same workstream reconciled mid-meeting
- **Abiodun hit Sunday Apr 19 deadline.** Content delivered as set in the [[wiki/meetings/2026-04-18-teams-daily-ops|Apr 18 review]]:
  - For **Inna**: Apr 17, 18, 19, 21 in ANIMATED FLYERS; Apr 21 and Apr 30 Women's mental-health videos in CREATED VIDEOS
  - For **Moil**: Apr 20 (Struggling-to-keep-up.png — caption with Jacob); Apr 22 (Connect with GenZ.mp4 — caption with Jacob, content-calendar-.png); Ask Moil.mp4 (+ cover); Posting Consistently.mp4
- **Instagram tagging problem surfaced** as a new business-of-content friction. Meta Business no longer supports tagging arbitrary accounts from the Moil publishing side — this forces the team to either take over Inna's IG directly or hand back to her for tagging + posting. Broader signal: the platform-access model for Moil360 / content delivery needs an explicit SOP.
- **Team internet / connectivity remains a recurring blocker** — Jacob missed the Monday call start ("I am having issues with internet connection" at 4:22 PM). Team was waiting. This is the third month running that Jacob's bandwidth has disrupted ops.

---

## Context / Threads

- **1:1 Jacob ↔ Andres (5 msgs):** PRD proposal opens Apr 19 night; Apr 20 afternoon check-ins on Monday call; late-night (6:30–6:38 PM) drafts of the Inna IG-tagging message (Jacob iterated the message twice — classic "working out what to say" moment).
- **1:1 Taiwo ↔ Andres (4 msgs):** Good-morning → FitLogic + Meridian ask → personal Gmail shared → Andres sent FitLogic.docx late afternoon.
- **1:1 Adeleke ↔ Andres (5 msgs):** Morning check-in → Andres's "review memory one first, it's less invasive than the static onboarding" → Adeleke concurs.
- **Moil Marketing (2 msgs):** Abiodun's weekly content manifest; Jacob asking the channel for thoughts on "Posting Consistently.mp4."
- **Moil Team (20 msgs):** Monday Collaboration logistics (pre-call waiting), Jacob's internet issues, Jacob's meeting summary, Adeleke's prod-fixes thread, Andres's Claude Code session handoff.

## Referenced Artifacts

- `Monday Collaboration (1).docx` — shared by Jacob Apr 20 4:22 PM (Teams attachment; not pulled into raw/)
- `FitLogic.docx` — shared by Andres Apr 20 5:57 PM to Taiwo
- `Posting Consistently.mp4` — Jacob asked the Marketing channel for thoughts
- Claude Code session: `https://claude.ai/code/session_0156Da69uG1W8jSEof5V2xgb` (for Adeleke review)
- `business_plan_beta_prod` codebase — Adeleke's active fix branch target
