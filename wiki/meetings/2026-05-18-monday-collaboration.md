---
tags:
  - graph/leaf
---
# Monday Collaboration — May 18, 2026

**Type:** meeting
**Last updated:** 2026-05-18
**Source:** [[raw/teams-transcript-monday-collaboration-2026-05-18]]
**Date:** 2026-05-18 · **Transcript window:** 12:40–14:33 UTC (~1h 52m captured)
**Organizer:** [[wiki/people/jacob-oluwole|Jacob Oluwole]]
**Attendees:** [[wiki/people/jacob-oluwole|Jacob Oluwole]] (616 cues), [[wiki/people/adeleke-tolulope|Adeleke "Steve" Tolulope]] (325 cues), [[wiki/people/abiodun-solomon|Abiodun "Ablad" Adekanmi]] (357 cues), [[wiki/people/taiwo-ola-balogun|Taiwo Ola-Balogun]] (21 cues), Andres Urrego (6 cues — joined briefly, left for daughter's school 01:10)
**Related:** [[wiki/projects/fitlogic]], [[wiki/projects/meridian-buda]], [[wiki/concepts/moil360]], [[wiki/people/travis-sutherland]], [[wiki/people/megan-miller]]

---

> ⚠️ **Transcript quality caveat (from raw header):** Microsoft Teams' speech-to-text struggled heavily — strong Nigerian-English accents, simultaneous speech, music playback, intermittent network drops. Many cues are unintelligible. Decisions and action items below are extracted conservatively only from clear segments. Confirm with Jacob before treating any as binding.

## Summary

Standing Monday team working session. **Andres' opening (00:00–01:10) is the only high-confidence intelligence**: three project handoffs before he stepped out for his daughter's school. The remaining 110 minutes was Jacob × Adeleke × Abiodun × Taiwo working through (1) the new **brand-DNA / image-generation feature on staging** that scrapes a customer's website and extracts fonts/colors/voice to generate a mini-website + branded images; (2) **Request-a-Demo flow** missing from moilapp.com (Jacob raised this multiple times — clear repeated ask); (3) **generative content QA** — Abiodun read sample AI-generated marketing copy aloud; (4) an **email-delivery bug** for the business-plan PPT (download works, confirmation email doesn't arrive).

This is the **first Monday Collaboration where Andres did not stay** — pattern shift from his usual heavy engagement (Apr 13, Apr 20, May 4, May 11).

## Andres' opening directives (high confidence)

Three handoffs before he left:

1. **FitLogic ("Feed Logic" in transcript) — hold production push until website rebuild is complete.** *"We need to go on my feed logic.com or the other website. We're not going to push that out anytime soon until our website is completed by someone else."* Cross-ref to [[wiki/projects/fitlogic]] open question (Electric Bricks redesign / marketing site).
2. **[[wiki/projects/meridian-buda|Meridian]] — ready it, test it, partner pushes when comfortable.** *"We need to have it ready, we need to test it, and then he'll be able to push, you know, whenever he's ready and feels good about the testing."* The partner is [[wiki/people/travis-sutherland|Travis Sutherland]] (Meridian-Buda owner); push timing is Travis-side, not Moil-side.
3. **PowerPoints + HTML design — "Stevie" (Adeleke) finishes.** *"Stevie's gonna work on a couple of things for the PowerPoints and the design, and then we should be good to go."* Adeleke owns the design polish; Andres flagged *"the HTML thing is already good to go."*

## Decisions (extracted from clear segments — confirm with Jacob)

- **Hold FitLogic production push** until the new marketing-site build is complete (Andres directive).
- **Meridian** to be readied + internally tested; [[wiki/people/travis-sutherland|Travis]] triggers the push when comfortable.
- **Add manual brand-DNA input** (company name + description + colors + fonts) as a first-class alternative to website-scrape on the staging brand-DNA flow. Adeleke confirmed this exists under "Generate Branding" but is untested end-to-end.
- **Add Request-a-Demo / Schedule-a-Demo entry point** on moilapp.com. Jacob raised this multiple times (~37:00 and ~58:50) — repeated ask, clear signal it's missing today.

## Action Items (tentative — confirm with Jacob)

| Owner | Action | Timing |
|---|---|---|
| Taiwo | Send testing-account emails + passwords for the three projects to Jacob | This week |
| Jacob | Test Meridian + brand-DNA flow on staging; give feedback to Adeleke | This week |
| Adeleke | Ship the manual color/customization control on brand-DNA; resolve multi-step ↔ coach token mismatch | This week |
| Adeleke | Finish PowerPoint + HTML design work (Andres' opening directive) | This week |
| Jacob / team | Add Request-a-Demo flow on moilapp.com | TBD — confirm priority with Andres |
| Team | Investigate business-plan PPT email-delivery bug (download works, confirmation email doesn't arrive) | Soon |
| Team (end of week) | Sit on a deployment call with each of the three test customers | EOW 2026-05-23 |

## Side threads (low-to-medium confidence)

- **Brand-DNA / image-generation feature walkthrough (~03–13 min).** Adeleke walked Jacob through a new staging feature: scrapes customer's website HTML, extracts brand tokens (fonts, colors, voice), generates a "mini website" preview, and feeds image generation. Open issue: the multi-step and "coach" steps aren't fully aligning on the extracted tokens; Adeleke is adding a manual color-customization control. Replicates an experiment Andres ran on the side.
- **Crawler / scraping concern (~17 min).** Abiodun asked whether prod prevents AI/bots from crawling. Adeleke clarified the architecture: **public pages are intentionally SEO-open** (so crawlers can find Moil); **the authenticated app is protected**. Architecture note worth capturing — not a vulnerability.
- **Social / outreach channels (~40 min, ~1:04).** Jacob discussed using his personal LinkedIn business account for outreach and customizing cold messages by location. Continues the May 11 *"10 real DM conversations/day"* + May 15 LinkedIn-SMB outreach assignment lines.
- **Generative content QA (~1:28–1:51).** Abiodun read aloud sample AI-generated marketing copy: "Social Metrics Pro" demo, social-media best-practices script, "Launch your startup" pitch, plus a **satirical critique** about *"40-page business plan in 6 seconds … 12 strategies, 11 of which are the same strategy reworded."* This was apparently QA of Moil's content-generation output — worth surfacing whether the satirical critique is real customer feedback or an LLM-generated piece of meta-commentary.
- **Email-delivery bug (~1:50).** Jacob can download the business-plan PPT but is not receiving the confirmation email. Suspected delivery issue. **Pairs with the May 14 standing item** on outbound deliverability — could be the same root cause (sender domain reputation) hitting transactional email too.

## Notable absences / signal

- **Andres present for only ~70 seconds.** First Monday Collaboration where he handed off and left immediately. Worth tracking whether this becomes a pattern or was one-off (daughter's school commitment).
- **Adeleke participated heavily (325 cues).** Breaks the May 11–14 silence anomaly that had hit 7+ days with three stacked escalations (xAI Grok 4.3 re-forward, Anita Lansing console errors, Gemini 3.1 Flash Lite). Today he was lead on the brand-DNA feature walkthrough and design hand-off — meaningfully back online.
- **Taiwo light participation (21 cues).** Stayed quiet beyond the testing-account credential commitment; consistent with the May 14 heads-down on FitLogic Outlook migration + Meridian setup the night before.

## Why this matters

- **First Andres-absent Monday Collaboration on record.** Watch whether the team self-organizes the agenda or drifts. Today's transcript suggests **drift** — most of the 110 minutes was demo + content read-alouds rather than structured ship-status review.
- **Adeleke is visibly active again** after the 7-day silence flagged in [[wiki/people/adeleke-tolulope|his page]]. Reduces escalation pressure on the three stacked items but doesn't close them — confirm xAI / Anita / Gemini deprecation items individually.
- **Request-a-Demo flow is the loudest repeated ask on the call.** Jacob raised it twice. This is a marketing-site gap that connects to the May 15 marketing reset (LinkedIn-SMB outreach + Friday cadence) — without a demo capture flow, the cold-outbound work has no in-product conversion surface.
- **Brand-DNA + manual-input fallback is a foundational Moil 360 feature** — when a customer doesn't have a website, the platform needs to still generate branded assets. Adeleke's manual-input path is the gap-fill; ship discipline matters because every Moil 360 onboarding without a website depends on this.

## Connections

- [[wiki/projects/fitlogic]] — Andres directive: hold production push until website rebuild done
- [[wiki/projects/meridian-buda]] — Andres directive: ready + test internally; Travis pushes when comfortable
- [[wiki/concepts/moil360]] — brand-DNA / image-generation feature lives here
- [[wiki/people/adeleke-tolulope]] — owns brand-DNA token mismatch fix + PowerPoint/HTML design polish + visibly back online after silence
- [[wiki/people/jacob-oluwole]] — Request-a-Demo ask repeated; will test Meridian + brand-DNA; receiving Taiwo's test-account credentials
- [[wiki/people/taiwo-ola-balogun]] — sending test-account credentials for three projects
- [[wiki/people/abiodun-solomon]] — content QA read-aloud + crawler/scraping clarification
- [[wiki/people/travis-sutherland]] — partner-side push trigger on Meridian
- [[wiki/meetings/2026-05-11-monday-collaboration]] — prior week pattern (Andres heavily engaged)
- [[wiki/meetings/2026-05-15-moil-marketing-team-reset]] — Friday cadence start; LinkedIn-SMB outreach assignment
