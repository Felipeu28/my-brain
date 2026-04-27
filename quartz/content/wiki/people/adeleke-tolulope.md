---
status: active
last_contact: 2026-04-26
tags:
  - graph/hub
  - person/team
---
# Adeleke Tolulope (Steve)

**Type:** person
**Last updated:** 2026-04-26
**Source:** [[raw/meetings/]] (multiple meeting transcripts), [[raw/teams-2026-04-12]] (415 messages, Apr 5–12 2026), [[raw/teams-transcript-monday-collaboration-2026-04-13]], [[raw/teams-2026-04-15]] (84 messages, Apr 14–15 2026), [[raw/teams-2026-04-18]] (51 messages, Apr 17–18 2026), [[raw/teams-2026-04-20]] (36 messages, Apr 19–20 2026), [[raw/teams-2026-04-21]] (161 messages, Apr 20–21 2026), [[raw/teams-2026-04-24]] (Moil Team + 1:1 Apr 24), [[raw/teams-2026-04-26]] (1 message 1:1, Apr 26)
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/moil/positioning]], [[wiki/moil/product-roadmap]]

---

## Role

**Lead AI/ML Engineer at Moil** — known as "Steve" within the team. The most technically capable member. Responsible for training custom AI models, building the OpenAI agent, and all backend AI pipelines.

## Background

Nigerian developer (references to power outages, network changes in Lagos/Nigeria context). Works remotely. On team since at least Jan 2025.

## What He Does

- Fine-tuned DeepSeek models for Moil's internal code generation
- Built the **OpenAI Agent** for automated business plan generation (major milestone, Apr 2025)
- Manages AI stack: Gemini (resume extraction), DeepSeek (resume generation), OpenAI agent (business plans), o3-mini/o4-mini (business insights)
- Runs Azure compute instances for model training
- Uses Postman for API testing
- Handled job matching algorithm improvements
- Backend for business plan creator, interview tool, employer account creation

## Key Contributions (Chronologically)

| Date | Contribution |
|---|---|
| Jan 2025 | Fine-tuned DeepSeek R1 for code generation — first working internal model |
| Mar 2025 | Backend for resume builder (completed) |
| Apr 2025 | Built OpenAI agent → eliminates repeated prompt character charges |
| Apr 2025 | AI-generated brand identity testing |
| May 2025 | Two-model pipeline: o4-mini (insights) + o3-mini (business plan) |
| May 2025 | Social media job post automation design |

## Personality in Meetings

- Methodical and technical — explains clearly when pressed
- Will push back gently when requirements are unclear ("I don't know what you mean")
- Has power outage and connectivity issues in meetings (infrastructure constraint)
- Used "Dr. Jenner babe" as a playful sign-off to Andres (warm relationship)
- Discusses finances and investments with Jacob casually off-agenda

## Azure Access Issue (Ongoing)

As of May 2025, Adeleke lost access to Azure resources for ~2 weeks. Andres submitted a support case.

## April 2026 Activity (from Teams chats, Apr 5–12)

**Most active team member** — 181 messages in 1:1 with Andres, the highest volume of any chat thread. This is the primary engineering communication channel.

### Work completed this week:
- Pushed multiple updates to staging for Content360 (Moil 360) and Business Coach
- Fixed publish functionality bug (Monday Apr 7)
- Fixed strategy document generation bug (validation error — strategy data not being sent to backend)
- Pushed Business Coach updates to staging for testing
- Fixed 503 image creation error in Moil 360 (resolved same night, Apr 10)
- Monitoring Qwen model failures and coordinating model switches

### Key technical threads:
- **OpenAI cost spike:** Discovered that the `gpt-4o` alias silently upgraded to `gpt-5_4-2026-03-05` snapshot (March 5, 2026), causing unexpected billing. Andres investigating where GPT-5 is used.
- **Grok 4.1 Fast identified** as breakout cost saver: $0.20/$0.50 with 2M context, 30x cheaper than current GPT-5.4 billing
- **Qwen Turbo 3.5 exhausted free tier** — Andres moved to paid. Adeleke set reminders to monitor next Tuesday + Friday
- **Model switching discussion:** Evaluating moving from Qwen to Gemini or xAI for speed; can't sacrifice speed even if cost is better
- **Edge functions** pushed for performance improvement
- **Facebook login issue:** Could not record app review video due to FB account sending login codes to mobile failing. Issue persisted Apr 7–8

### Relationship with Andres:
- "You the man! Get some rest" (Andres, 9:13 PM)
- "AI at work!" (Adeleke, responding to Claude Code implementation)
- Adeleke monitors Claude Code sessions Andres shares, reviews implementations, pulls code to staging
- Adeleke said "AI is doing sh*t now, something that would have taken like 3-5 days" — genuine excitement about speed
- Andres shares X/Twitter links for inspiration (AI video tools, etc.)

## April 13, 2026 — Monday Collaboration

Steve reported on PDF/PowerPoint document generation testing:
- First PDF test produced output but **formatting needs significant work**
- Logo generated; needs a non-colored background version
- **Action:** Create a testing folder in the repo branch with reference PDFs for Claude Code to iterate on
- **Action:** Continue fixing formatting issues and feed results back to the AI
- Also pushed updates to staging: image creation in Business Coach, monitoring improvements

See [[wiki/meetings/2026-04-13-monday-collaboration]].

## April 15, 2026 — API Cost Audit + Staging Push

Source: [[raw/teams-2026-04-15]]

- **Assigned: full codebase audit for OpenAI API spend.** Andres discovered token refill frequency exploded from monthly to 3x/week. Adeleke's initial hypothesis: heavy Business Coach testing as the primary driver.
- Will find all remaining `gpt-4o` references in codebase and migrate to `gpt-5-mini`
- After audit, API keys will be rotated
- Completed all pending Claude Code chats from last week — pushed results to staging
- PDF/PPT generation quality "really improved" (confirmed by Adeleke)
- Claude service was having issues — Adeleke confirmed "not working" around 3:45pm
- Andres noted 4 people simultaneously logged into Claude Code may be contributing to issues

See [[wiki/meetings/2026-04-15-teams-daily-ops]].

## April 18, 2026 — Claude Code Audit Review Assigned

Source: [[raw/teams-2026-04-18]]

- Andres ran a Claude Code audit/fixes on a different project (session `session_01PP9t1m41A2snaRRACs3TNs`) and asked Adeleke to review: "make sure nothing was broken or revert if it was."
- Adeleke acknowledged Andres's early-morning (Apr 18 12:08 AM) check-in about starting to play with the business-side onboarding restructuring: "Yes sir" (Apr 18 5:21 AM).

See [[wiki/meetings/2026-04-18-teams-daily-ops]].

## April 20, 2026 — Production Fixes + Memory-Mode Onboarding Review

Source: [[raw/teams-2026-04-20]]

- **Proactively fixed bugs on `business_plan_beta_prod`** ahead of Andres starting a parallel project for the same workstream. Told Andres "I already fixed some bugs though" (4:38 PM). Planned workflow: create a new branch, review, push. Andres accepted.
- **Morning check-in (11:39–11:48 AM):** Asked whether to review and push the current item before the prior chat. Andres directed "review the new memory one first, it's less invasive than the static onboarding. Do a review and let me know what you think first! If all good we can start there!" Adeleke concurred. This is the "memory-mode" onboarding variant vs. the static onboarding flow — review-first, not ship-first.
- **Claude Code session handed over again.** Andres shared `https://claude.ai/code/session_0156Da69uG1W8jSEof5V2xgb` (5:02 PM) for Adeleke to review — continues the pattern from Apr 18 (session `session_01PP9t1m41A2snaRRACs3TNs`) of Andres running Claude Code audits and Adeleke verifying.
- **Codebase-selection snag surfaced.** "oh, we hav to select the codebase with prod / the business_plan_beta_prod" (4:37 PM) — signal that Claude Code / tool configuration needs to target prod codebase explicitly; default was wrong.

See [[wiki/meetings/2026-04-20-teams-daily-ops]].

## April 21, 2026 — Moil 360 Launch-Day Firefight + Multi-Model Fallback

Source: [[raw/teams-2026-04-21]]

- **Prod image-generation regression debugged all afternoon.** Image creation went from "happen right away" to "taking a minute+" — Adeleke restarted his system mid-debug ("Omg Please I need to restart my system so I can fix this, it's going to take few minutes" 5:12 PM). Confirmed template intermittently failing.
- **Claude Code pushed fixes to AWS same-day.** Quote: "Claude already pushed the update, it deploying right now on AWS" (5:29 PM) → "Fixes deployed already" (5:31 PM). Continues the Apr 20 pattern: Andres reports, Adeleke fixes via Claude Code, deploys same day.
- **Multi-model fallback architecture decision.** Adeleke wants Gemini video generation to **fall back to Grok** on error even if the user didn't select Grok. Added a Qwen backup layer too. Andres: "Great, and add a qwen model for backup as well." First on-prod multi-provider routing decision for Moil — important for reliability and cost at scale. Architectural pattern: primary (user-selected) → Grok (fallback) → Qwen (backup).
- **Codebase-selection snag fixed after Apr 20's surfacing** — Adeleke explicitly targeting `business_plan_beta_prod` for the Claude Code session on the Gemini-fallback work.
- **Force-assigned Megan FitLogic's Moil 360 license** after the Jacob/Andres debug loop confirmed the plan-switching bug had trapped her. Steve was the gate to unblock the customer.
- **Asked for `cs@moilapp.com` password** openly in Moil Team channel at 11:31 AM — Jacob responded with the plaintext password in the channel. Credential hygiene needs a vault.

See [[wiki/meetings/2026-04-21-teams-daily-ops]].

## Gaps

- Full legal name vs. nickname (Steve) — Steve appears to be a team nickname
- Exact location (likely Nigeria based on power outage context)
- Compensation terms unknown
- Facebook account access issue (Apr 7–8) — may still be unresolved

## April 24, 2026 — Auto-Assign License (Staging) + Onboarding-Guide Routing

Source: [[raw/teams-2026-04-24]], [[wiki/meetings/2026-04-24-teams-daily-ops]]

- **Auto-assign Moil 360 license is on staging.** Andres asked the Moil Team channel at 8:37 PM (Sun Show event in progress) for a way to give a free month to anyone signing up over the weekend. Adeleke flagged the constraint: *"That will be on staging and it's going to take a while before we can push to prod"* — feature exists, ship-readiness gap on a real-world conversion event.
- **Proposed routing the existing in-app guide for new-user onboarding.** When Andres surfaced the customer-feedback gap (*"they logged in and didn't know what to do next?"*), Adeleke responded: *"On Moil? We have guide already there"* + *"But if they ask the little guide, it can direct them tho"* + *"It can ask them what they want to do and then guide them"* — first articulated routing pattern for the existing in-app guide. Andres agreed on the redesign-for-discoverability angle.
- **AI-iteration on prod work confirmed by Jacob.** Jacob's status to Andres at 12:05 PM: *"Steve began work on it yesterday... he said the AI is not doing exactly what he is asking it... so He is doing it again."* Confirms the Apr 21 Claude-Code-pushed-fix pattern but with first-pass-clean as the unmet bar — multiple iterations needed to land output to spec.
- **Acknowledged the chats Andres sent.** *"Okay sir"* (11:22 AM) — chats-review still pending follow-through.

See [[wiki/meetings/2026-04-24-teams-daily-ops]].

## April 26, 2026 — High-Value-Asset Model Cost Evaluation Asked

Source: [[raw/teams-2026-04-26]]

- Andres pinged Adeleke 1:1 at 12:36 AM Apr 26 with `https://x.com/gdb/status/2048162286838444511` (Greg Brockman / OpenAI post): *"Have we reviewed the cost of this model? We should definitely start using for high value assets… and maybe even for Moil360 depending on cost"* — first explicit founder-driven ask for a cost/quality evaluation on a new model specifically scoped to "high value assets" first, Moil 360 second. Continues the Apr 15 OpenAI cost-audit thread; this time the framing is *which assets justify a premium model* rather than *cut spend everywhere*.
- No reply on record yet — action sits with Adeleke for a written cost-vs-value comparison before Moil 360 production usage.
