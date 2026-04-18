---
tags:
  - graph/spoke
---
# Apr 18, 2026 — Teams Daily Operations

**Type:** meeting
**Last updated:** 2026-04-18
**Source:** [[raw/teams-2026-04-18]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/moil/customers]], [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/meetings/2026-04-15-teams-daily-ops]]

---

## Summary

51 Teams messages across 4 threads (Apr 17–18, Saturday end-of-week review). Delivery pace tension from Apr 15 escalated — Andres repeatedly called out that only 2 of 6 projects were tested this week. Business Coach bug surfaced (not responding). Jacob sent Alloy ATX Moil 360 invite Apr 18 (late — was supposed to be sent Apr 15). Connectex remains untouched despite top-priority label. Taiwo asked for delivery calls not at 11pm or 2am his local time. Andres challenged Abiodun Adekanmi directly on content production pace for Inna + Moil next-week content.

---

## Decisions

1. **Content rhythm shift — Tue push / Sun review.** Going forward, content for the following week should be submitted earlier so there's a cushion; Andres wants to use Sunday to review the prior week's output. Abiodun pushed back that if the full week is submitted at the start of the week, he'd already be working on the following week — Andres clarified he wants content ready ahead, not trickled daily.
2. **Next week's Moil + Inna content due Sunday Apr 19.** Andres: "I want to see all the content for next week by tomorrow as I have made clear is my expectation for the last year!"
3. **Demo fix owner = Taiwo.** Taiwo acknowledged the "messed up" demo and asked Andres for better business context to add to prompts to generate desirable results (context was previously defined in Lovable, can't replicate in current flow).
4. **Claude Code audit shared with Adeleke.** Andres ran an audit/fixes on a different project via Claude Code (session `session_01PP9t1m41A2snaRRACs3TNs`) and asked Adeleke to review — "make sure nothing was broken or revert if it was."
5. **Application flow regression acknowledged.** Andres pointed out that the current build doesn't flow like the prior version — previous code used the business plan as a single source of truth that drove everything. Implicit ask: restore that pattern.

## Action Items

| Owner | Action | Deadline | Status |
|---|---|---|---|
| Jacob | Fix Business Coach "not responding" bug (major bug flagged while Jacob was testing) | ASAP | Open — blocks Jacob's own testing loop |
| Jacob | Send follow-up emails to Moil 360 license recipients who have NOT activated | This week | Open — Andres pushing |
| Jacob | Start Connectex work (flagged as "one of top priorities that we have not looked at") | ASAP | Open — slipped past Apr 18 |
| Jacob | Share Apr 17 call transcript with Andres (Jacob asked) | Apr 18 | Open |
| Jacob | Confirm Moil 360 license activation shows on partners' dashboard after invite | Apr 18 | Confirmed — Alloy ATX invite sent late Apr 18 |
| Taiwo | Rework demo prompt context — ask Andres for business-specific context to add to prompts | Next work session | Open |
| Taiwo / Andres | Reschedule delivery calls to reasonable hours for Taiwo's time zone (not 11pm / 2am his time) | Ongoing | Taiwo raised; Andres acknowledged |
| Adeleke (Steve) | Review Claude Code audit fixes (`session_01PP9t1m41A2snaRRACs3TNs`) — confirm nothing broken; revert if so | Apr 18–19 | Open |
| Abiodun | Deliver next week's content for Moil + Inna | Sun Apr 19 | Open — Andres's explicit deadline |
| Abiodun | Clarify content rhythm expectations with Andres (daily submission vs. weekly batch) | Apr 19 | Open — Abiodun asked for clarification |
| Andres | Confirm which non-activated partners get follow-up emails | Apr 18–19 | Open |

## Key Signals

- **Delivery pace is the #1 tension this week.** Andres repeatedly escalated: "WE ARE VERY BEHIND and I didn't see the same commitment this week that we need to be successful!" / "It's taken us a full week to test 4 projects I built in one week!" / "Did everyone take yesterday off?"
- **Testing throughput is the bottleneck.** Only 2 of 6 active projects tested this week — focus was Meridian + FitLogic. Connectex, Business Coach (broken), and others untouched.
- **Business Coach is broken.** Jacob: "One major bug I encountered was with the business coach not responding." Jacob also reported being "offline" — couldn't test his own assignments.
- **Jacob missed Alloy ATX license invite** until Apr 18. Originally expected Apr 15 per the earlier license distribution push. Andres: "I asked to send emails to moil360 to multiple users their one year license!! 🫠"
- **Time-zone conflict surfaced.** Taiwo explicitly asked for delivery calls outside 11pm/2am his time. First formal boundary signal from the Nigeria team on scheduling.
- **Content tension with Abiodun.** Andres: "I need to see content and less fees in this group every single day!!" Abiodun asked what "fees" Andres meant — miscommunication around expectations and terminology. Andres wants visibility into content production daily even if submission is weekly.
- **Architectural regression.** Andres flagged that the current application doesn't use the business plan as the single source of truth the way the prior version did — implicit rebuild/restore ask sitting with engineering.
- **Moil 360 license activation flow confirmed** — partners' dashboard will show when they have activated their license.

---

## Context / What Was Working This Week

- **Meridian** — tested + shipped updates (from Apr 15 run).
- **FitLogic** — focus of the week, on track for Apr 18 deadline (see [[wiki/meetings/2026-04-15-teams-daily-ops]]).
- **Moil updates pushed to prod** — Jacob reported all updates pushed to prod except Conectex, testing in progress.

## Context / What Slipped

- **Connectex** — explicitly named by Jacob as top priority not looked at.
- **Business Coach** — bug blocks Jacob's own testing.
- **Alloy ATX Moil 360 invite** — sent Apr 18, 3 days late.
- **Apr 17 (Friday) appears to have been a low-output day** — Andres: "Did everyone take yesterday off? 😆"
