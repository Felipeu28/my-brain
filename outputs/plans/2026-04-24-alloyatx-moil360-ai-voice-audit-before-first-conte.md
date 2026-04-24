---
date: 2026-04-24T00:00:00.000Z
type: implementation-plan
plan_type: feature
appetite: 1w
topic: AlloyATX Moil360 AI-voice audit before first content batch ships
state: under_review
active_repos: []
tags:
  - graph/leaf
approved_at: '2026-04-24T16:33:42.545Z'
---

# Plan: AlloyATX Content-Voice Gate — audit before Week 1 batch posts

**Thesis.** AlloyATX is Moil's first $75/mo Market Pro retainer; if the opening content batch reads as AI-uniform, LinkedIn's 2026 algorithm actively punishes it and the relationship is at risk before Month 2 billing hits — audit and rewrite for human voice before Abiodun posts anything.

## The compounding signal

1. **Operating brief 2026-04-24** names this explicitly: *"Before Abiodun posts AlloyATX's first Moil360 content batch, audit for AI-voice uniformity… if Week 1 content performs poorly, the relationship is at risk before it starts."* Owner assigned: Andres → Abiodun.
2. **@paolo_scales · Apr 21** (editorial 2026-04-24): LinkedIn's algorithm now *punishes* AI content in 2026, not just ignores it. Tactics from six months ago are actively killing organic reach.
3. **Editorial 2026-04-24**: Content360's volume-and-pattern output is exactly the signal LinkedIn now flags — the machine is generating content the platform is trained to suppress.
4. **Pipeline + MEMORY.md**: AlloyATX closed Apr 11–14 on a monthly retainer. Onboarding call done; 21-question flow is the next deliverable. MEMORY carries an open item: verify 21 questions + assets completed by Apr 18. Status unknown — batch may ship before this is confirmed.
5. **Operating brief 2026-04-24** (watch list): *"Track Roxana's LinkedIn engagement on first batch. Flat or declining = AI-voice problem; adjust Abiodun's delivery before Month 2 billing cycle."* — the brief already treats this as a leading indicator for churn risk.

## Scope

- **In:**
  - Pull every draft post Abiodun has queued for AlloyATX Week 1 before any go live
  - Run a 5-point voice-uniformity check on each post (pattern phrases, em-dash clusters, passive openers, generic hooks, filler CTAs)
  - Rewrite or return for rewrite any post that fails 2+ checks
  - Confirm Roxana's 21-question intake is complete before scheduling; missing brand voice context is the root cause of AI-sounding output
  - Establish a one-line brand voice brief (AlloyATX: gym culture, Austin audience, owner-voice) that Abiodun uses as a system prompt prefix going forward

- **Out (not doing):**
  - Do not rebuild the Moil360 content generation pipeline (no code changes this week)
  - Do not delay the AlloyATX relationship to run a longer brand discovery — use what exists from the onboarding call
  - Do not apply this gate retroactively to other Moil360 clients this week (Inna, FitLogic) — AlloyATX is the priority because it is the first Market Pro retainer

- **Deferred (maybe later):**
  - Systematize the voice audit as a checklist inside the Moil360 delivery workflow (could become a feature in `Moil-Code/Moilapp_business` post-stabilization)

## Appetite

1w — roughly 2 focused hours for Andres + Abiodun sync, then Abiodun owns execution. Calendar constraint: Sun Show tonight (Apr 24) is AlloyATX-adjacent; use the Roxana conversation there to confirm voice preferences live if she attends.  
Stop condition if overrun: if the 21-question intake is still incomplete by Apr 28, ship a 3-post minimum batch that Andres has personally reviewed rather than holding indefinitely.

## Execution

**Step 1:** Andres pulls all queued AlloyATX posts from Abiodun (Slack/Teams DM today, Apr 24) · Owner: Andres · ~15 min · Acceptance: draft list received.

**Step 2:** Andres runs 5-point voice check on each post — flag posts that hit 2+ of: generic hook ("Are you struggling with…"), em-dash overload, passive voice opener, filler CTA ("DM me to learn more"), no specific Austin/gym detail · Owner: Andres · ~30 min · Acceptance: each post marked pass/revise.

**Step 3:** Andres writes a one-paragraph AlloyATX brand voice brief (gym culture, Austin community, Roxana's owner-voice, specific program names) from the onboarding call notes and tonight's Sun Show conversation · Owner: Andres · ~20 min · Acceptance: brief is one paragraph, shareable in a Teams message.

**Step 4:** Abiodun receives flagged posts + brand voice brief; revises flagged posts using the brief as a rewrite prompt · Owner: Abiodun · ~Apr 25–26 · Acceptance: revised posts resubmitted to Andres for a single final pass.

**Step 5:** Andres does final pass on revised batch; approves for scheduling · Owner: Andres · ~20 min · Acceptance: green-light message sent to Abiodun with schedule dates.

**Step 6:** Confirm 21-question intake completion with Roxana (if not done — MEMORY item is open) before scheduling Week 2 batch · Owner: Andres · ~Apr 28 · Acceptance: Roxana confirms or intake session booked.

## Success criteria

- **Week-2 proof:** AlloyATX Week 1 posts are live with no AI-pattern flags visible on manual review; Roxana has not flagged voice concerns.
- **Day-60 outcome:** AlloyATX renews Month 2 retainer without negotiation; becomes a reference case for Market Pro LinkedIn results.
- **Kill signal:** Roxana's Week 1 LinkedIn posts get below 5% of her historical organic reach baseline OR Roxana proactively flags that the content doesn't sound like her — if either happens, pause Month 2 batch and run a live brand voice session before any more posts go out.

## Repo note

This plan has no code changes. The Moil360 product lives in `Moil-Code/Moilapp_business` and `Moil-Code/Business-plan-beta-prod` (both active), but the fix this week is operational — audit and delivery process, not a feature build. If the voice audit surfaces a repeatable workflow worth encoding, the checklist feature belongs in `Moil-Code/Moilapp_business`.

## Alternatives considered (rejected)

1. **Ship Week 1 as-is and monitor:** The operating brief already identified the risk; monitoring after shipping means eating a bad first impression with a new $75/mo client — too expensive.
2. **Full brand discovery call with Roxana before any content:** Adds delay that risks Roxana perceiving Moil as slow; tonight's Sun Show conversation is the faster path to the same information.

## Decision needed

**Andres must confirm: pull Abiodun's AlloyATX queue today (Apr 24) before anything posts.** If Abiodun is already scheduled to post this weekend, that needs to be paused now. If the queue is empty and Week 1 hasn't been drafted yet, this plan converts to a pre-production brief (lower urgency, same steps).
