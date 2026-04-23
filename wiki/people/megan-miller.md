---
tags:
  - graph/hub
  - person/customer
status: active
last_contact: 2026-04-23
client: "[[wiki/orgs/fitlogic]]"
---
# Megan Miller

**Type:** person
**Last updated:** 2026-04-23
**Source:** [[raw/imessages-people-2026-04-09]], [[raw/email-history-6months-2026-04-14]], [[raw/teams-transcript-megan-miller-2026-04-21]], [[raw/teams-2026-04-21]], [[raw/email-digest-2026-04-20]], [[raw/email-digest-2026-04-21]], [[raw/teams-transcript-CRM-GOOGLE-Setup-with-Megan-2026-04-23]], [[raw/email-digest-2026-04-22]]
**Related:** [[wiki/orgs/fitlogic]], [[wiki/moil/customers]], [[wiki/moil/gtm]], [[wiki/concepts/smart-hiring]], [[wiki/concepts/moil360]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]], [[wiki/meetings/2026-04-23-megan-crm-google-setup]]

---

**Email:** meganmillernp@gmail.com (personal), `Megan@fitlogicfunctionalmedicine.com` (clinic — to be Moil sender)
**Title:** Nurse Practitioner (NP) — Functional Medicine & Hormone Specialist
**Business:** Fit Logic Functional Medicine (see [[wiki/orgs/fitlogic]])
**Relationship:** Active Moil 360 customer — CRM onboarding in progress (Apr 21 live tour)
**Trust level:** Shared GoDaddy credentials Apr 21 ("I must really trust you")

---

## Profile

Megan Miller is a Nurse Practitioner specializing in functional medicine with a focus on hormone optimization and women's health. She runs an online community and holds live educational sessions for clients. She is currently onboarding with Moil for hiring support.

## Onboarding Timeline

- **Mar 29–30:** Scheduling back-and-forth — Megan told Andres "this week is packed" (covering front desk + leading 3rd live session Thursday). Suggested 9am or 1:45pm Wednesday.
- **Apr 1, 2026:** Onboarding call — *"Megan & Andres @ Wed Apr 1, 2026 9:20am–10am CDT"* — first meeting held.
- **Status thread:** "We are almost ready!" — active onboarding email thread.

## Why She Uses Moil

Megan is hiring through Moil's platform — posting jobs through [[wiki/orgs/fitlogic|FitLogic]]. As a solo NP running a practice, she needs to find clinical or admin staff without the overhead of traditional recruiting.

## Product Feedback (Original — from iMessage history)

Megan surfaced two UX issues when she first used the platform:

1. **Applicant contact info not visible** — She found an application (from applicant Michelle) but couldn't see the applicant's phone number or email anywhere
2. **Notification system unclear** — Sent a message through Moil but didn't know how the applicant would respond or how she'd be notified

These were active bugs/gaps in the employer experience. Andres handled support personally via iMessage.

## Active Deal (Apr 2026)

- **FitLogic GitHub repo:** [Moil-Landingpages/fit-logic](https://github.com/Moil-Landingpages/fit-logic) — ✅ active
- **First hire imminent** as of Apr 12, 2026
- **Moil 360 CRM onboarded Apr 21, 2026** — first hands-on CRM tour with a paying Moil 360 customer
- See [[wiki/orgs/fitlogic]] for deal status

## April 21, 2026 — Moil 360 CRM Working Session

Source: [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]] (89 min, 3–4 PM CT)

- **Exported her Keap CRM** (~5,000 contacts) for import into Moil. Acknowledged most "client" tags in Keap are wrong (old massage clients, kids, Charm imports). Will walk the list and mark real clients before final import.
- **Sequences are the killer feature for her:** "This is what I've been wanting." Wants to drop every new initial-consult patient into a 3-email auto-drip with male / female variants.
- **Shared GoDaddy credentials for `fitlogicfunctionalmedicine.com`** — Andres to deploy `/CRM` route tonight and wire `Megan@fitlogicfunctionalmedicine.com` as the sending address (currently sends from `partners@moilapp.com` which lands in spam).
- **Pushed back on Electric Bricks** (her external website agency) — site too text-heavy, too busy, too similar to her current site. Andres drafted the formal "Fit Logic Website — Outstanding Items Before Delivery" email (alt-text missing sitewide, no H1 on homepage, chiropractic-themed blog URL slugs); Megan forwards it as the punch list.
- **Open items for her:** forward feedback email to Electric Bricks, mark actual clients in Keap, pull remaining EHR contacts, send quiz questions for Andres to rebuild natively in Moil.
- **Personal moment:** shared story of patient Carla (terminal colon cancer, chose quality of life over treatment, passed a month after Megan visited her at home) — core patient-relationship story that defines why Megan practices this way. Also recounted catching a 25-year-old's brain tumor early on gut instinct — her clinical intuition is the brand.

## Product Feedback from Apr 21 Session

| Issue | Severity | Notes |
|---|---|---|
| Test email from `partners@moilapp.com` landed in Gmail spam | Blocker | Deliverability bug |
| Link inside test email returned 404 | Blocker | Campaign link wiring incomplete |
| Couldn't switch "stuck" business plan — old "for my life" plan wouldn't move to FitLogic | Already hit her | Same bug surfaced again Apr 21 in Jacob/Andres debugging session |
| Per-campaign aggregate click-rate not clearly surfaced | Feature ask | "Is this doing what we want?" |
| Campaign link editing lives only in sequences, not campaigns | Feature-parity gap | Andres caught during same-day debugging |

## Apr 19 — Payment Plan Renegotiation Ask

Source: [[raw/email-digest-2026-04-20]]

Megan emailed Apr 19 asking to switch from **$500/mo × 3 to $250/mo × 6** (same total, stretched). Also requested a website update in the same thread. Needs a collection/revenue decision + reply. Context: Apr 21 CRM tour went well, deliverability issues surfaced — the payment ask is on the table alongside product firefighting.

## License / Activation Issue (Apr 21)

Megan had been asking for her Moil 360 license for ~2 weeks ("Two weeks asking and we don't have it for a demo call" — Andres to Jacob, 7:26 PM). Root cause: license was assigned via Buda but she needed a fresh license specifically on Moil 360. Andres and Jacob spent 20+ minutes debugging her profile — plan-switching flow was broken (30% profile completion block). Steve (Adeleke) involved to force-assign. Surfaced the partner-dashboard license UX as next redesign target.

## April 23, 2026 — CRM / Google Setup Session (40 min)

Source: [[wiki/meetings/2026-04-23-megan-crm-google-setup]] (Teams transcript, 2:15–2:58 PM CT)

Two days after the Apr 21 working session, Andres + Taiwo + Megan wired up the infrastructure accounts so the Moil CRM can be handed off from Moil's environment to Megan's own. Megan shared hello@ Gmail credentials in private chat; Andres drove the Google Cloud Console OAuth config (Gmail `send`/`readonly`/`compose` + Calendar `readonly`) while Taiwo instructed from the Nigeria side.

**Key decisions for deployment:**
- **Megan owns everything:** Google Cloud project, GitHub repo, Supabase, Resend, Gemini API key (at deploy time). Taiwo added as GitHub collaborator.
- **CRM will deploy to `fitlogicfunctionalmedicine.com/crm`** on Megan's GoDaddy. Vercel hosts the app; Supabase hosts contacts DB. Both free tiers.
- **Go-live target: Mon 2026-04-28** — Moil tests through the weekend, Megan starts sending real emails Monday/Tuesday.
- **Handover meeting: Wed 2026-04-29 at 9:30 AM CT** — full walkthrough so Megan can send from her side.
- **Multi-user (Michelle login) deferred** — for now Michelle shares Megan's login. Multi-user planned for the $75/year tier.

**Calendar hygiene commitment (behavioral change):** Megan admitted she missed an 11 AM meeting during the call itself — "I totally forgot about a meeting I had at 11 today." She committed to forwarding every meeting invite to Andres going forward so the Brain calendar tracks them. *"I'm just going to send you a message every time I get a meeting, so you can put it on there."* This is a standing pattern, not one-off.

**Website agency dispute — Andres to attend.** Megan meets her website vendor Fri 2026-04-24 12:30 PM CT to resolve the "doctor vs. health coach" compliance issue + 30-page SEO buildout. Vendor's defense: "10+ years experience, 30 pages is what it takes to rank in Buda, TX." Andres's position: bulk SEO text nobody reads isn't obviously helpful, but the non-negotiable is that nothing on the site can confuse a patient about Megan's scope of practice. Megan sending the link; Andres plans to join.

**Moil 360 / Coach status for Megan:** Working again as of Apr 23 — Jacob confirmed the fix via email Apr 23 morning. Andres gave her the open homework: log in, upload logo + brand colors, play with image editing (with her own machine photos as references, per the red-light-therapy customer demo), **do not build the content calendar yet** until all brand assets are uploaded.

**New network connection surfaced:** Michelle (FitLogic clinic staff) was in the call briefly and mentioned she knows [[wiki/people/daniel-mann|Daniel D. Mann]] — "Firefly." Andres responded warmly ("Daniel is the man … amazing guy when it comes to connecting people") and asked Michelle to relay a hello. Michelle confirmed Daniel speaks equally well of Andres. This is a second-degree social proof loop through Moil's #1 referral partner — worth a direct text from Andres to Daniel to acknowledge + reinforce.

## Why She Matters

Megan represents the solo/small-team healthcare practitioner segment — a high-value Moil ICP. Her practice requires specialized hiring (clinical credentials, flexible hours) that job boards don't serve well. Her early UX feedback shaped the employer dashboard improvements. First confirmed hire through FitLogic = product proof point. As of Apr 21, she is also the **first Moil 360 customer to receive a live CRM tour** — her feedback (sequences excitement, campaign editing gap, deliverability, plan-switching bug) is disproportionately load-bearing for product direction, and she is the **strongest current case-study candidate** given relationship depth (GoDaddy credentials on the first call).

<!-- AUTO-ACTIVITY:start -->
## Recent Activity (auto)

*Auto-generated by entity-graph-builder · last refreshed 2026-04-21. Entries capped at 12, pruned at 30 days. Do not edit inside the markers.*

- **2026-04-21** · `teams` · 89-min CRM onboarding; exported Keap contacts and reviewed website redesign · also: email-digest
- **2026-04-23** · `teams` · 40-min Google Cloud OAuth + GitHub/Supabase/Resend account setup; Apr 29 handover scheduled; Apr 28 go-live target
<!-- AUTO-ACTIVITY:end -->
