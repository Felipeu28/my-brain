---
tags:
  - graph/spoke
---
# Apr 24, 2026 — Teams Daily Operations

**Type:** meeting (async team-chat digest)
**Last updated:** 2026-04-24
**Source:** [[raw/teams-2026-04-24]]
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/abiodun-solomon]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/adeleke-tolulope]], [[wiki/people/megan-miller]], [[wiki/orgs/fitlogic]], [[wiki/meetings/2026-04-23-megan-crm-google-setup]], [[wiki/meetings/2026-04-21-teams-daily-ops]]

---

## Summary

99 Teams messages across 5 threads on Apr 24. Three story arcs:

1. **Andres ↔ Abiodun (Ablad) — first deep documented AI-adoption clash.** A 38-message exchange in Moil Marketing triggered by a tweet about GPT Image 2. Abiodun called the tweet "rage-bait"; Andres took it as evidence of a wider AI-resistance pattern: "Everytime we have ever talked about AI for two years, you have a attitude towards it that is dismissing!" Andres ended with the threat — *"I'm this close to closing our full marketing department"* (12:00 PM, 1:1 with Jacob) — and the framing as a leadership growth conversation: *"As your leader my goal is to make sure you can grow, and growth can be uncomfortable! But I can say I am happy I have pushed you beyond..."* This is the first time the Andres ↔ Ablad AI-adoption tension has surfaced as a structured argument with both sides on record.

2. **Founder-built Clio demo videos.** Andres has been creating product demo videos using AI tools (HeyGen + ChatGPT image2 + Capcut) — `clioremembers.com/demo` is the artifact. Quote: *"I am creating demo videos for Moil that we haven't created over the last 2 years (clioremembers.com/demo) without ever designing anything or even knowing exactly how to do it!"* Used at the Sun Show event tonight. Andres stated explicitly: *"I am building the workflow so we can actually reproduce this videos for all other aspects of Moil! This is what happens when people make me mad! I build."*

3. **Sun Show event Apr 24 evening — free-month license ask.** Andres asked the Moil Team channel (8:37 PM) for a way to give a free one-month license to anyone who signs up over the weekend. Adeleke flagged this as a staging-only build, not pushable to prod by tonight: "That will be on staging and it's going to take a while before we can push to prod." Implementation gap surfaced live during the event.

Other threads of note:
- **Megan FitLogic handover confirmed Wed Apr 29.** Jacob asked if it happened yesterday (Apr 23); Andres clarified *"Not a handoff, we are doing that next Wednesday!"* — confirming the [[MEMORY]] sprint plan from Run 19.
- **Taiwo committed weekend work** on Inna and Connectex; opened Supabase for FitLogic Apr 23.
- **Jacob's outbound messaging flagged as low-conversion** — Andres said the Apr 23 group post "missed opportunity to convert over 2000 businesses" and pushed Jacob to think strategy-first ("How were they driven to convert?").
- **Onboarding UX gap re-surfaced** — client feedback: "they logged in and didn't know what to do next?" Adeleke proposed routing the existing in-app guide to ask new users what they want to do; Andres committed to redesigning the guide so it's discoverable.

---

## Decisions

1. **Megan FitLogic handover = Wed Apr 29** (not Apr 23, not Apr 30). Confirmed by Andres explicitly in 1:1 with Jacob 4:00 PM. Aligns with the existing FitLogic CRM handoff sprint in [[MEMORY]].
2. **Taiwo weekend sprint Apr 25–26: Inna + Connectex.** First explicit weekend commitment from Taiwo. Quote: *"I have the weekend to work on Inna and connectex"* (6:57 PM). Andres asked status on Inna; Taiwo previously thought it was complete.
3. **Free-month license for Sun Show weekend signups — deferred (staging-only).** Adeleke confirmed the auto-assign-license feature is on staging, not pushable to prod by tonight. Andres asked the question in real-time during the event; manual workaround (admin assignment after signup) implied.
4. **Andres will redesign the in-app guide** so new users discover it on login. Adeleke + Andres aligned that the existing guide can route users to the right starting point ("ask them what they want to do and then guide them") — but discoverability is the gap.
5. **Demo-video workflow is being built as a reproducible system.** Andres committed to building the workflow so all Moil aspects get demo videos using the Clio template. Adds to the "Daily video production" technical-debt item in [[MEMORY]] (Apr 5–12 carryover).
6. **HeyGen subscription scrutiny.** Abiodun: HeyGen "cannot lift from our website. It doubles the work." Andres pushed for HeyGen hyperframes specifically. Login expired during the day — Abiodun asked for re-auth. Open: do we keep HeyGen, switch to ChatGPT image2 + Capcut workflow, or both?

---

## Action Items

| Owner | Action | Deadline | Status |
|---|---|---|---|
| Andres | Build reproducible demo-video workflow (Clio template applied to all Moil features) | Ongoing | In progress — Clio first artifact live at `clioremembers.com/demo` |
| Andres | Redesign in-app onboarding guide for discoverability | Next week | Open — Adeleke aligned |
| Taiwo | Inna — finish remaining work this weekend | Apr 25–26 | Committed |
| Taiwo | Connectex — start build this weekend | Apr 25–26 | Committed |
| Adeleke | Push auto-assign-Moil-360-license feature from staging to prod | Asap | In progress — already in dev |
| Adeleke | Review chats Andres sent earlier in the week | Today/tomorrow | Acknowledged "Okay sir" 11:22 AM |
| Jacob | Rework outbound messaging to be conversion-driven, not vague — strategy first | Before next batch | Open — Andres flagged Apr 23 batch missed 2000+ business conversions |
| Jacob | Re-auth HeyGen login for Abiodun (expired Apr 24) | Today | Open — Abiodun asked 12:47 PM |
| Abiodun | Maximize HeyGen credits — stop wasting monthly allocation | Ongoing | Open — Andres flagged repeatedly |
| Andres + Ablad | Reach a working agreement on AI-tool adoption pace; revisit after Andres's "won't hear it from me anymore" cooldown | This week | Open — argument unresolved, both retreated |

---

## Key Signals

1. **Andres ↔ Ablad clash is now on the record.** Two years of background AI-adoption tension turned into a structured public argument (Moil Marketing channel, 38 messages, 11:42 AM – 12:47 PM). Both positions visible: Andres = "we are an AI company, we are slow to adopt, we waste credits, we miss opportunities"; Abiodun = "I use AI all the time, the tool [HeyGen] doesn't fit our work, you are dismissing opinions, repeating past arguments." Andres ended with *"You don't have to believe me, you just won't hear it from me anymore!"* — first time he has signaled disengagement from the persuasion attempt. The "I'm this close to closing our full marketing department" quote to Jacob is the direct escalation.

2. **Founder-built artifact bypassing the marketing team.** `clioremembers.com/demo` exists because Andres built it himself using AI tools without Ablad. Used at tonight's Sun Show event. The implicit message inside the team: the founder can ship a polished demo video faster than the design team can — which is exactly the AI-adoption gap Andres has been flagging.

3. **Megan FitLogic handover date confirmed Apr 29 (not Apr 30).** Removes ambiguity from the [[MEMORY]] sprint timeline. Apr 24 was *not* a handoff (Jacob's mistaken assumption); the formal handover is the Wed Apr 29 9:30 AM CT meeting.

4. **Sun Show event = first real-world conversion test for Moil 360 sign-up flow.** Andres asked at 8:37 PM (event in progress) whether sign-ups tonight could get a free month. The fact that the auto-assign-license feature is still on staging during a live conversion event = product-readiness gap on what is supposed to be the primary acquisition channel for license-based growth.

5. **Taiwo's first explicit weekend-work commitment.** Until now Taiwo has worked late-night-Nigeria but not weekends. *"I have the weekend to work on Inna and connectex"* (6:57 PM) is volunteered, not pushed. Pace shift continuing from Apr 21–23 momentum.

6. **Onboarding gap re-surfaces as customer-feedback signal, not internal hypothesis.** Andres at 12:09 PM: *"Client feedback, they logged in and didn't know what to do next?"* The onboarding-revamp work Andres sent "last week" is now justified by an external complaint, not just a founder hunch. Discoverability of the existing in-app guide is the immediate fix.

7. **Jacob's outreach messages = strategy gap, not effort gap.** Andres reviewed Jacob's Apr 23 group post: *"none of them really sell or give the buyer any insight into anything we are offering!! Completely missed opportunity to convert over 2000 businesses but we have to do it right."* Pushed Jacob to articulate the strategy *before* sending: *"What was the strategy you used to make the decision for the comments you sent and posted? How were they driven to convert?"* Pattern: Jacob executes fast but strategy-thin; Andres's coaching focus shifts toward upstream thinking.

8. **HeyGen subscription is at decision-point.** Abiodun: "cannot lift from our website. It doubles the work." Andres: pushed for HeyGen hyperframes and re-shared the link. Login expired same day. Working capital + workflow-fit decision pending — keep HeyGen, drop, or replace with ChatGPT + Capcut.

9. **The "build when angry" pattern is now founder-self-aware.** Andres: *"This is what happens when people make me mad! I build"* (6:25 PM). The Clio demo videos are the direct product of frustration with marketing-team pace — and Andres is naming the pattern in the team channel, not just in private. Implicit signal to the team: shipping > venting.

10. **Steve (Adeleke) is doing AI-driven feature work hands-on.** Jacob: *"Steve began work on it yesterday... he said the AI is not doing exactly what he is asking it... so He is doing it again."* The bottleneck Andres asked about ("We have been working on this… yet hasn't been fixed! What's the bottleneck?") is now articulated as: AI agent output not matching spec on first pass, requiring re-runs. Pattern: Claude-Code-style iteration on prod work is not yet first-pass-clean.

---

## Context / Threads

- **1:1 Jacob ↔ Andres (39 msgs):** Megan handoff clarified Apr 29; Steve's AI-iteration bottleneck on a feature; the Ablad escalation ("I'm this close to closing our full marketing department"); auto-assign-Moil-360-license feature in dev; Jacob's Apr 23 group-post conversion gap; Andres pushing Jacob on strategy-before-execution; voiceover decision on the Clio demo video; mobile-format ask from Jacob; SharePoint video share (~241MB); HeyGen + tools talk.
- **Moil Marketing (38 msgs):** The Hewar GPT Image 2 thread → Andres ↔ Abiodun AI-adoption clash. Both sides on record. Abiodun: HeyGen doesn't fit, the tweet is rage-bait, repeating past arguments is dismissive. Andres: AI gap is real, demo videos are proof, growth is uncomfortable. Abiodun praised Clio demo video at the end ("AMAZING!!! Now I'd like to know how you did it") — partial reconciliation. HeyGen login expired; re-auth requested.
- **1:1 Taiwo ↔ Andres (9 msgs):** Taiwo confirmed Supabase opened for FitLogic Apr 23; volunteered weekend Apr 25–26 for Inna + Connectex; Andres clarified GitHub is the universal login.
- **Moil Team (11 msgs):** Sun Show free-month-license ask (Andres 8:37 PM); auto-assign feature is staging-only per Adeleke; client-feedback onboarding gap; in-app guide discoverability work.
- **1:1 Adeleke ↔ Andres (2 msgs):** Andres asked if Adeleke had reviewed the chats sent earlier; "Okay sir" acknowledgment.

## Referenced Artifacts

- `clioremembers.com/demo` — founder-built Clio demo video (referenced multiple times Apr 23–24 as proof of AI-tool capability)
- SharePoint video shared by Jacob 6:53 PM (~241MB, `moilapp-my.sharepoint.com/:v:/p/andres/...`)
- Hewar GPT Image 2 tweet (`x.com/1littlecoder/status/2047331869319184798`)
- HeyGen hyperframes (Andres's recommended next-gen workflow)
