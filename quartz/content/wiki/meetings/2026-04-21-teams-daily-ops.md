---
tags:
  - graph/spoke
---
# Apr 21, 2026 — Teams Daily Operations

**Type:** meeting (async team-chat digest)
**Last updated:** 2026-04-21
**Source:** [[raw/teams-2026-04-21]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/moil/active-projects]], [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]], [[wiki/people/megan-miller]], [[wiki/orgs/fitlogic]], [[wiki/meetings/2026-04-20-teams-daily-ops]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]]

---

## Summary

161 Teams messages across 6 threads on Apr 21 (single busiest ops day of the week). The day ran three parallel tracks: (1) **Moil 360 launch day** — Andres did a live Moil360 demo to Megan Miller (see [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]]), and spent the evening debugging FitLogic email deliverability, campaign editing UX, and the Moil 360 activation funnel; (2) **Prod-stability firefight** with Adeleke — image-creation latency (used to be instant, now taking a minute+), Gemini API errors on video generation, templates failing sometimes, Claude-pushed fixes deployed mid-day; (3) **License distribution catch-up** — multiple customers still haven't received their Moil 360 licenses (Megan, Siren, Roxana, Jill/PureSerenity), partners@moilapp.com emails landing in spam ("devs said they can't optimize it more"), and Andres escalating that Buda cohort licensees also need the upgrade email.

Taiwo confirmed he's ready to start Connectex tomorrow — the first time the long-deferred Connectex has a committed owner and day. Jacob began redesigning the partner dashboard's license section mid-day.

---

## Decisions

1. **Adeleke: add Grok fallback for Gemini video generation** — "when this happens it falls back to grok even tho the user didn't select grok" (Adeleke, 4:12 PM). Plus a Qwen model as additional backup, since video gen has been failing sporadically. Accepted by Andres.
2. **Coach: restore day/light mode** — removed in a prior build; Andres asked Taiwo to re-add it (6:08 PM). Taiwo will check and restore.
3. **Cold-outreach email sending defaults (from Megan session, applied team-wide):** plain-text only, max 50/day per sender account, 3-emails-over-6-days default sequence. See [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]].
4. **FitLogic domain deployment tonight.** Andres has the GoDaddy creds, will deploy `fitlogicfunctionalmedicine.com/CRM` and wire `Megan@fitlogicfunctionalmedicine.com` as the sender. Fixes the spam-folder problem for Megan specifically.
5. **Taiwo starts Connectex tomorrow (Apr 22).** Taiwo asked for the CRM URL and explicitly said "I need to move on to other projects so we can start getting paid" (10:10 PM). Andres agreed — FitLogic has to finish first but Taiwo works Connectex in parallel starting tomorrow.
6. **Campaign link-editing UX gap:** Moil lets you edit links in **sequences** but not in **campaigns**. Andres flagged this as a required feature — "we need option to edit the links attached to the email" (8:34 PM). Taiwo confirmed the edit path exists via "editing the campaign" but hidden; needs to surface.
7. **Partners email spam issue acknowledged as unresolved.** Jacob reported the dev team said "they can't optimize it more" — Andres pushed back ("I don't think they are getting the emails lol"). Escalation path: move per-customer to their own domain (applied for FitLogic tonight). Default `partners@moilapp.com` sender remains broken.

---

## Action Items

| Owner | Action | Deadline | Status |
|---|---|---|---|
| Andres | Deploy Moil CRM at `fitlogicfunctionalmedicine.com/CRM`; wire Megan@fitlogicfunctionalmedicine.com as sender | Tonight Apr 21 | In progress — GoDaddy access confirmed |
| Andres | Wipe test contacts + import 5,000-contact Keap CSV for FitLogic in one pass | Tonight Apr 21 | In progress |
| Andres | Surface per-campaign click-rate / open-rate dashboard for FitLogic | This week | Open — Megan asked |
| Andres | Finalize FitLogic with Taiwo so Megan can go live and Moil moves on | Apr 22 | Open — Andres: "finish fitlogic so we can get her all switched over" |
| Andres + Jacob | Send Moil 360 upgrade email to **every Buda cohort licensee** with new feature updates | Apr 21–22 | Open — Jacob will pull emails of Buda license recipients; Andres prompted Apr 21 12:21 PM |
| Adeleke | Implement Grok fallback + Qwen backup for Gemini video generation failures | Apr 22 | In progress — Adeleke already pushed fixes mid-day |
| Adeleke | Root-cause slow image creation (minute+ vs. prior instant) and template-intermittent-fail on prod | Apr 22 | In progress — Claude Code session pushed update to AWS |
| Taiwo | Restore day/light mode on coach | Apr 22 | Open |
| Taiwo | Start Connectex — needs CRM URL from Andres, will build in parallel to FitLogic finish | Apr 22 | Committed |
| Taiwo | Surface campaign link-editing in Moil (currently only in sequences) | This week | Open |
| Jacob | Fix license-assignment flow — Megan FitLogic has not gotten her Moil 360 license despite 2 weeks of asking; Siren Beauty needs the email too | Apr 21 | In progress — redesigning partner dashboard license section mid-day |
| Jacob | Resend PureSerenity license link to Jill (signed up + paid $75 Apr 20, didn't receive link) | Apr 21 | Open — Andres escalated at 6:27 PM |
| Jacob | Confirm activation status on Moil 360 dashboard for all P1 licensees (Megan, Mark, Becky, Roxana, Jill, Alloy ATX) | This week | Open — carryover |
| Andres | Respond to Jacob's PRD-proposal (from Apr 19) | Apr 22 | Open — carried from Apr 20 |

---

## Key Signals

1. **Moil 360 launch day friction, not launch day success.** Despite Andres's "MOIL 360 BABY!!" (5:18 PM, Moil Marketing), the actual launch felt like triage: license emails landing in spam, Megan didn't have her license at call time ("Two weeks asking and we don't have it for a demo call"), PureSerenity / Roxana missing their links after paying. The product works; the distribution layer is broken.
2. **Partners-domain deliverability is now a P0 product blocker.** Second customer in two days confirmed `partners@moilapp.com` → spam. The engineering team's answer ("they can't optimize it more") is not acceptable — tonight's workaround is to move FitLogic to its own domain sender. This doesn't scale if every Moil 360 customer needs a custom sender.
3. **Business-plan switching bug hit another customer.** Jacob and Andres spent 20 minutes debugging why Megan's profile wouldn't let her switch business plans — she had multiple plans and then one plan, neither let her activate Moil 360. Same bug class as the "stuck plan" issue Megan hit weeks ago. Escalate as a real product fix, not manual DB intervention.
4. **Connectex finally has a Tuesday start date.** After three weeks of slipping (Apr 15 push, Apr 18 "top priority that we have not looked at," Apr 20 still open), Taiwo committed to Apr 22 start and asked for the CRM URL. First concrete progress.
5. **Adeleke's prod-fix mode persists.** Pattern from Apr 20 continues — Adeleke pushes a Claude-authored fix to AWS same-day (5:29 PM "Claude already pushed the update, it deploying right now on AWS"; 5:31 PM "Fixes deployed already"). The human-in-the-loop review is now: Andres reports, Adeleke fixes via Claude Code, deploys same day.
6. **Multi-model fallback architecture surfaced on prod.** Adeleke wants Gemini video → Grok fallback + Qwen backup so a Gemini API failure doesn't block the user. First on-prod multi-provider routing decision for Moil — architecturally important for reliability and cost.
7. **Andres frustration signal is back.** 9:12 PM "Come on!!! Why is this still the image and messaging for our links?? FUCK!" — the OG image on the Moil links was still wrong. Taiwo acknowledged he forgot the OG image differed from the landing page. Small execution miss on a high-visibility surface (Moil 360 demo day).
8. **Campaign vs. sequence feature-parity gap is visible to the founder.** Andres caught that sequences can edit email links but campaigns can't. This will happen to every customer. Feature-parity audit warranted.
9. **Buda cohort licensees need the upgrade email loop.** Andres: "can we please gather all the emails for everyone who got a Buda license last cohort? We need to send them an email as well with all the updates!" (12:21 PM). Moil 360 ship-day is also a re-engagement opportunity for cohort alumni — not yet systematized.

---

## Context / Threads

- **Moil Team (67 msgs):** Prod firefight (Adeleke + Jacob + Andres); Gemini/Qwen fallback architecture decision; FitLogic demo prep; password for `cs@moilapp.com` disclosed as `Pr0ud**2023$` in the open channel (**security issue — move to vault**); Moil 360 activation email template issues; Taiwo + Andres on FitLogic finalization; Taiwo's Connectex commitment to start tomorrow.
- **1:1 Jacob ↔ Andres (55 msgs):** Megan's missing license (2-week delay); PureSerenity not receiving license link after paying $75; Siren Beauty license email questions; business-plan-switch bug debugging in Megan's profile; partners-domain spam-folder issue; Jacob redesigning the partner dashboard license section; "had to confirm with Steve" (Adeleke) whether Megan's license was assigned.
- **1:1 Taiwo ↔ Andres (11 msgs):** Taiwo worked overnight on FitLogic bugs; ready to review new fixes morning Apr 21; asked for Connectex CRM URL; auto-schedule behavior of email sequences (sends regardless of checkbox state) clarified; campaign vs. sequence link-editing gap surfaced.
- **1:1 Adeleke ↔ Andres (22 msgs):** System hang / restart mid-afternoon; image-creation latency debugging (minute+ vs. instant); template failing intermittently; Claude Code pushed an update that deployed to AWS same-day; fixes confirmed deployed 5:31 PM.
- **Megan & Andres (1 msg):** Andres drafted the formal "Fit Logic Website — Outstanding Items Before Delivery" email to Electric Bricks at 8:59 PM — alt-text missing sitewide, no H1 on homepage, chiro-themed blog URL slugs, etc. Serves as punch list.
- **Moil Marketing (5 msgs):** "MOIL 360 BABY!!"; Abiodun proposed using unrelated materials to grab attention in messages; Andres liked it but asked for "better text."

## Referenced Artifacts

- Claude Code session(s) used to push prod fixes to AWS on Apr 21 (not explicitly shared this day — implicit in Adeleke's "Claude already pushed the update" message)
- Email draft to Electric Bricks (full text in `raw/teams-2026-04-21.md`, Megan & Andres thread, 8:59 PM)
- `cs@moilapp.com` password: `Pr0ud**2023$` — **leaked in Moil Team channel at 11:31 AM by Jacob** (Adeleke asked publicly for the password; security hygiene fix needed)
- `partners.moilapp.com/moil-admin/dashboard` — partner license dashboard (Jacob's link, 7:19 PM)
