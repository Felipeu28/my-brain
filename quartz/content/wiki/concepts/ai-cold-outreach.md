---
tags:
  - graph/spoke
---
# AI-Powered Cold Outreach

**Type:** concept
**Last updated:** 2026-05-07
**Source:** [[raw/x-bookmarks-2026-04-11]], [[raw/email-digest-2026-05-06]], [[raw/email-digest-2026-05-07]]
**Related:** [[wiki/moil/gtm]], [[wiki/moil/icp]], [[wiki/concepts/linkedin-gtm]], [[wiki/concepts/smb-ai-audits]], [[wiki/concepts/content360]], [[wiki/concepts/moil360]]

---

## Overview

Multiple X creators published full guides on using Claude and AI agents for cold email, LinkedIn lead generation, and outbound systems during the Mar 26 – Apr 11 period. This is a rapidly maturing playbook.

## Key Resources

- **@adriannalakatos** — "The Cold Outreach Bible" (Apr 10) — X Article
- **@itsalexvacca** — "I Gave AI One URL and Asked It to Build a Cold Email Campaign From Scratch" (Apr 6) + follow-up: "Cold outbound has been definitively solved" (Apr 8)
- **@dimitarangg** — "How I Abuse Claude to Write Emails That Book Fortune 500 Companies" (Apr 6)
- **@draprints** — "How to retardmaxx your outbound in 2026" (Apr 5) — aggressive optimization playbook
- **@levikmunneke** — "Claude Code + Google Maps = 7-figure outbound team" (Mar 20) — uses Maps API to find local businesses and auto-generate personalized outreach
- **@DeRonin_** — "Claude + LinkedIn = 11 clients" (Mar 26) — unlimited lead generation via LinkedIn

## The "One URL" Campaign Build (@itsalexvacca)
Workflow: Give Claude one URL (your target company's website) → Claude analyzes the company → generates a full personalized cold email campaign (subject lines, body, follow-up sequence). No manual research. This is the minimum viable AI outbound system.

## The iMessage/SMS Play (@coreyganim, @startupideaspod)
- "Most business owners already text more than they email" — SMS outreach via iMessage is underused as a channel
- Lindy integration for iMessage as AI executive assistant (@startupideaspod, Apr 6)
- The hypothesis: SMS reply rates are 5-8x email reply rates for local business outreach

## Relevance to Moil

Moil's GTM is currently community-led + PLG. At $15-$75/mo ACV, traditional outbound doesn't pencil. **However**, the Claude + Google Maps pattern (@levikmunneke) is directly applicable: find local service businesses in Texas → auto-generate personalized Moil pitch → feed into email sequence. This could be a low-cost experiment to test alongside community events.

The key insight from the GTM doc: outbound doesn't work at Moil's price point with manual effort. But AI-automated outbound at near-zero marginal cost changes the math entirely.

**Moil-specific plays to test:**
1. **Google Maps play:** Use Claude + Maps API to find dental offices, gyms, and med spas in Austin/Buda/Round Rock → generate personalized "do you have an AI Co-Founder?" pitch → test 100-email batch, measure response
2. **One-URL campaign builder:** Give Claude a target company's website → auto-generate personalized Moil pitch email — could be run as a Cowork scheduled task
3. **SMS test:** Andres texts 10 warm contacts directly about Moil. Compare reply rate to email.

See also [[wiki/concepts/linkedin-gtm]] for the LinkedIn warming layer that makes cold email convert better.

## May 6–7, 2026 — SMB cold-outbound campaign live (Content360 pitch)

Source: [[raw/email-digest-2026-05-06]], [[raw/email-digest-2026-05-07]]

The first SMB-pivot outbound batch began **2026-05-06** and continued **2026-05-07** with ~12+ Content360 pitches sent across construction, real-estate, food-service, and animal-control SMBs. Three rotating subject lines in active test:

| Subject line | Frame | Sample recipients (May 7) |
|---|---|---|
| *"30 days of content in 20 minutes"* | Time-savings hook | Brian Anderson (Anderson Roof Repairs), Cynthia Thigpen (Newcastle TX), Jose Mendoza (Axxon Services), Joe Justice (Lanterra Group), Yaniv Dotan (NewEdge RE), Lisa Gallagher (CHG) |
| *"Most SMB owners tell us the same thing…"* | Pain-mirror hook | Joseph Ortega (Skytex Construction), Gabriel Lopez (BLS Construction Mgmt), Jerry Blaricom (Kari King), Wilson Maclin (Omega Animal Removal), Leonor Ramirez (Barista Kats) |
| *"Business owners don't expect it to sound this good"* | Voice/brand angle | Savannah Carter (Tiello), Design Dept (Kevin Wood Landscapes), Simon Dockey (Tiello) |

**Operating reads:**
- This is the **first sustained day-over-day cold outbound campaign at SMB ICP** (vs. the chamber/EDC cold campaign from April). It marks the operational shift from B2G replication → SMB direct.
- Three subject-line variants under live A/B test — track open and reply rates by variant. The *"Most SMB owners tell us the same thing"* pain-mirror frame is the closest cousin to the @itsalexvacca / @dimitarangg hook patterns above.
- All sends from `andres@moilapp.com`. **Deliverability risk:** the same address that bounced FitLogic test emails to Gmail spam in April. Watch for reply-rate floor that suggests inbox-placement issues; if response rate < 1%, evaluate domain-warmup or rotation to a secondary outbound domain.

## May 6–7, 2026 — Chamber-breakup follow-ups continuing

Source: [[raw/email-digest-2026-05-07]]

Four *"Should I close this out?"* breakup follow-ups sent **2026-05-07 12:12–12:43 UTC** to silent April chamber/EDC contacts: Hunterdon County Chamber (Christopher Phelan), Point Pleasant Beach Chamber (Carol Vaccaro), UCEDC (Erich Peter), Jefferson County WV Chamber (Heather McIntyre). This is the breakup template (4-of-4) of the [[wiki/concepts/chamber-outreach-2026-04|chamber/EDC cold campaign]] firing on schedule — track which contacts reply to a breakup email vs. which stay silent. Charles DeBow (NBCC) Apr 29 reply established that breakups *do* surface signal from at-most-warm contacts.
