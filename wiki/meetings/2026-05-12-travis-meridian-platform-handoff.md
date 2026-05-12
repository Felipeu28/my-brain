---
tags:
  - graph/leaf
date: 2026-05-12
type: meeting
attendees:
  - "[[wiki/people/travis-sutherland]]"
  - Andres Urrego
location: Meridian Buda
---
# 2026-05-12 — Travis × Andres: Meridian Buda platform handoff

**Type:** meeting (Teams + in-person at Meridian Buda, ~31 min)
**Time:** 1:30 PM – 2:01 PM CT (18:30–19:01 UTC)
**Source:** [[raw/teams-transcript-travis-andres-2026-05-12]]
**Related:** [[wiki/people/travis-sutherland]], [[wiki/orgs/meridian-buda]], [[wiki/orgs/zoiwell]], [[wiki/people/taiwo-ola-balogun]], [[wiki/moil/active-projects]]

---

## Context

End-to-end product walkthrough of the **event-management / ticketing platform** Andres has been building for Meridian Buda (Travis's coffee/live-music venue). Andres demoed the full lifecycle: events (incl. recurring), ticketing tiers, customizable RSVP, check-in flow (QR or name search), analytics dashboards, bookings inbox, menu management, and the automated email flow (confirmation → 7-day → 24-hour → post-event follow-up). The session ended with **credential transfer** — Travis created his own GitHub account and shared GoDaddy admin so all production artifacts now live under Travis's accounts, not Andres's.

## Key decisions

1. **All deployment artifacts live under Travis's accounts.** Andres explicitly avoided creating anything under his own login. Code → Travis's GitHub repo. Hosting → Travis's Vercel (free tier). Email → Travis's Resend (free under 1,000/day). Rationale: Travis keeps full ownership even if he later hires a different developer.
2. **Primary admin email: `travis@zoiwell.com`.**
3. **Staff check-in account: `info@meridianbuda.com`** — Andres will provision this as an additional team-member login so door staff can check guests in without using Travis's password.
4. **Image/design approval gates the push.** Andres will not push to production without Travis's prior approval on hero/page images. Workflow: Andres sends image options → Travis picks → Andres pushes.
5. **Recurring events:** the platform supports "weekly until cancelled" so Meridian doesn't have to recreate the same weekly event manually.
6. **Email-flow customization** is Travis's quasi-"send custom email" tool — he can rewrite the 24-hour or follow-up emails on the fly. (Ad-hoc one-off email creation is captured as a future feature request.)
7. **Custom ticket-tier names confirmed** — Travis can rename "general admission" to "RSVP" on free events to capture headcount without the paid-ticket framing.

## Bugs identified live during demo

| # | Symptom | Root cause / status |
|---|---|---|
| 1 | Artist-autofill (Gemini-backed) didn't populate when Travis tried "Kiltoni" comedian example | **Gemini model deprecated; API key needs replacement.** Andres: *"Gemini replaced this model, so we just need to upgrade it to the new model."* |
| 2 | Check-in button stayed disabled after moving event start time to make it live | UI didn't refresh after the time change. Same underlying issue as #3. |
| 3 | Event-update form continued to display the stale 6:30 opening time after Andres changed it | Travis caught it: *"Yeah, looks like it still has the 6:30."* Time-change isn't propagating to UI state. |

## Action items

| # | Owner | Action | Due |
|---|---|---|---|
| 1 | Travis | Sign up for GitHub.com with `travis@zoiwell.com` (email+password, not Google) and send credentials to Andres | ✅ Done in-meeting |
| 2 | Travis | Send Andres GoDaddy admin invite to `Andres@moilapp.com` for site deployment access | ✅ Done in-meeting (after second invite — first attempt didn't land) |
| 3 | Andres | Replace API key + upgrade to current Gemini model | Today (May 12) |
| 4 | Andres | Fix check-in button not enabling when event start time is changed | Tomorrow (May 13) |
| 5 | Andres | Push landing page (with new hero / Stan Martinez images) to production | By tomorrow (May 13) |
| 6 | Andres | Provision `info@meridianbuda.com` as additional staff login for door check-ins | Next |
| 7 | Andres | Text Travis when the Gemini API key is replaced so he can re-test artist autofill | After fix |
| 8 | Andres | Send Travis a credentials doc with all relevant logins (GitHub, Vercel, Resend, GoDaddy) | After landing-page push |
| 9 | Travis | Pick which hero/page images he wants from the Stan Martinez batch — Andres swaps them in for review | Ongoing |

## Feature requests captured (future)

- **On-the-fly custom email to upcoming event attendees.** Today Travis can only edit the templated 24-hour or follow-up email; he asked for an ad-hoc email-creation tool. Andres: *"we can look at that."*
- **Search check-ins by guest name, not ticket number** — Andres self-flagged: *"I can actually change that to be the name so that you guys don't have to type this entire thing."*

## Platform features demoed (for KB synthesis)

- **Event creation:** image, description (auto-filled from artist name via Gemini — currently broken), opening time + show times (e.g. 7:30 / 9:00), free or paid tickets, max 10 per purchase, multiple tiers, custom tier labels.
- **Organizer/artist accounts:** add organizer email → they log in to their own dashboard to see real-time tickets sold.
- **Check-in:** QR scan via phone camera *or* search by ticket number/name. Live attendance % + single-tap check-in.
- **Multi-user staff access:** invite team members by email (e.g. `info@meridianbuda.com`) — they activate via emailed link, then can check in guests.
- **Analytics:** revenue by event, tickets sold by tier (VIP, GA, etc.), event attendance, no-shows, recent orders, in-flight (started-but-not-completed) orders with ping-by-email follow-up.
- **Bookings inbox:** form submissions land here with status pipeline (new → contacted → confirmed/declined).
- **Menu management:** add/edit/remove menu items.
- **Email flows:** confirmation (with PDF ticket attached) → 7-day reminder → 24-hour reminder → post-event follow-up. All editable, all toggleable on/off, variable inserts (name, event title, event date, CTA).

## Notable signals (for Brain synthesis)

- **First explicit credential-discipline handover under the May 11 Monday-Collaboration rule.** Three days after Andres' *"if you create a new account, tell us — we have 10 @moilapp.com emails, we shouldn't be using personal Gmail accounts, especially with client data"* directive, **Andres himself ran the rule on a client**: GitHub + Vercel + Resend + GoDaddy all under Travis's accounts before any production push. Pattern: the rule applies both directions — Moil-side credentials go under Moil-owned emails, **and** client-side credentials go under the client's own accounts. Capture as the canonical pattern for every venue/website client handoff going forward.
- **Image-approval gate before push** is now an explicit rule for Travis — first time Andres has named *"I won't push until you say push"* as a per-client workflow. Reduces the trust-debt that built up at FitLogic/Inna when proactive design changes landed without sign-off.
- **Stan Martinez (photographer)** surfaces for the first time as the source of Meridian's hero/page images. New person worth tracking if his name appears again on other client visual assets.
- **Same-day client tour at Meridian Buda** — Andres was in Buda for the Perseus Defense meeting at 8 AM, and the Travis handoff was the 1:30 PM follow-on. Two YC-adjacent and venue-client wins on one Buda visit; replicable cadence (bundle Buda visits to compound venue presence).

(Meeting ends 19:01 UTC / 2:01 PM CT.)
