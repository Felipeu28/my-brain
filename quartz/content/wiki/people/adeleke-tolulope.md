---
status: active
last_contact: 2026-04-13
tags:
  - graph/hub
  - person/team
---
# Adeleke Tolulope (Steve)

**Type:** person
**Last updated:** 2026-04-15
**Source:** [[raw/meetings/]] (multiple meeting transcripts), [[raw/teams-2026-04-12]] (415 messages, Apr 5–12 2026), [[raw/teams-transcript-monday-collaboration-2026-04-13]], [[raw/teams-2026-04-15]] (84 messages, Apr 14–15 2026)
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

## Gaps

- Full legal name vs. nickname (Steve) — Steve appears to be a team nickname
- Exact location (likely Nigeria based on power outage context)
- Compensation terms unknown
- Facebook account access issue (Apr 7–8) — may still be unresolved
