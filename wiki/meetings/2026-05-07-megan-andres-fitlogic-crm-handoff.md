---
tags:
  - graph/leaf
date: 2026-05-07
type: meeting
attendees:
  - "[[wiki/people/megan-miller]]"
  - Andres Urrego
---
# 2026-05-07 — Megan × Andres: FitLogic CRM handoff + email-domain workaround

**Type:** meeting (Teams, ~1h 21min — transcript started 14 min in)
**Time:** 3:30 PM – 4:55 PM CT (20:30–21:55 UTC)
**Source:** [[raw/teams-transcript-megan-andres-2026-05-07]]
**Related:** [[wiki/people/megan-miller]], [[wiki/orgs/fitlogic]], [[wiki/people/michelle-fitlogic]], [[wiki/concepts/moil360]], [[wiki/meetings/2026-05-06-andres-taiwo-ongoing-projects]], [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]

---

## Context

Working session immediately downstream of the May 6 Andres × Taiwo internal test. Two parallel threads:
1. **FitLogic business operations update** — practice manager training (Michelle), AI-driven inbound leads, new LLC ("My Life on Purpose"), product-direction signals (coaching certification course, book draft, pricing rewrite).
2. **Live demo + setup of the custom Moil CRM/sequence tool** — including configuring a new sending email address that bypasses the multi-week `fitlogicfunctionalmedicine.com` Resend domain-verification block.

This is also the meeting that resolves the Resend/GoDaddy domain blocker that has been open since the [[wiki/meetings/2026-04-21-megan-fitlogic-working-session|Apr 21 working session]] — but **via a workaround** (new domain), not by unblocking the Cloudflare-locked original domain.

## Key decisions

1. **New sending domain → `myfitlogic.com`.** Megan created `connections@myfitlogic.com` via GoDaddy's Microsoft 365 email add-on (~$5/mo vs. Gmail Workspace's $12). This becomes the dedicated outbound/lead-comms email — separate from the existing `practicemanager@fitlogicfunctionalmedicine.com` clinic-ops mailbox.
2. **Don't fight the Cloudflare lock.** `fitlogicfunctionalmedicine.com` is locked behind a Cloudflare config Megan can't access (likely an old vendor). Decision: do not chase access — run all outbound from `myfitlogic.com` where DNS is manageable in GoDaddy. Closes the multi-week Resend verification thread without resolving the underlying access problem.
3. **CRM delivery target: tomorrow morning (2026-05-08).** Andres ships Megan login credentials + the configured `connections@myfitlogic.com` sender. Megan starts low-volume only (a few emails per day, not bulk) using the **test-contact flag** while Michelle learns the system.
4. **Defer landing pages.** Don't build them yet. Wait until the FitLogic website is fully launched, then build SEO-targeted conversion pages for specific services (ear acupuncture, hormone treatment, men's testosterone) — only when ROI is clear. Andres's framing: *"Anybody can sell you something to create a landing page. It's being able to create a landing page the right way — one that converts."*
5. **Megan canceling Mastermind subscription** — doesn't think she needs it.
6. **Trigger-based emails: deferred, not committed.** Megan asked for click-triggered automation (*"if they clicked, send X"*). Andres wants to design the UX so it doesn't feel spammy before committing.

## Action items

### Andres / Moil team
- [ ] **[2026-05-08 AM]** Configure Microsoft 365 email for `myfitlogic.com` in GoDaddy using the credentials Megan sent during the call
- [ ] **[2026-05-08 AM]** Send Megan the CRM login credentials wired to the new `connections@myfitlogic.com` sender
- [ ] **[Next week]** In-person visit to FitLogic to walk Megan + Michelle through the CRM together (Andres to schedule)
- [ ] **[Open]** Design the "clicked-link" trigger flow for the CRM — manual vs. automated; how to keep tone non-spammy
- [ ] **[Ongoing]** Clean up the imported Keap contact list (~5,341 contacts) — remove duplicates and obvious fakes (`sample@email.com` etc.)

### Megan
- [x] **Done during call:** Sent GoDaddy credentials + new `connections@myfitlogic.com` info to Andres
- [ ] **[This week]** Send Andres his lab order (fasting bloodwork via LabCorp, 8–10 vials). Megan is debating switching labs from LabCorp to a different vendor — she'll text when the order is in the Charm portal
- [ ] **[Q2]** Add monthly in-person **Women's Vitality Group Circle** to FitLogic membership offering (patient base is ~90% women)
- [ ] **[Later]** Design quarterly equivalent for men — Megan asked Andres for input on format
- [ ] **[Ongoing]** Continue rewriting website pages — pricing page already redone (moved away from a la carte/piecemeal pricing toward standard membership programs)

## FitLogic business update

- **Hire / training:** Megan is training **[[wiki/people/michelle-fitlogic|Michelle]]** as the operations / patient connection role. Michelle is excelling at the relational side — one new patient asked Michelle to be physically present in her appointment because she had no one else to bring. Megan flagged this as a strong organic-fit signal.
- **AI-driven leads working:** ChatGPT and Claude AI Search are sending real leads. Megan reported **4–5 calls Tuesday alone, two confirmed conversions**, and a small waitlist forming (Megan is intentionally protecting her schedule from overload). First quantified AI-search-traffic data point at FitLogic.
- **New LLC approved:** "**My Life on Purpose**" finally received LLC approval. Megan is shopping for a new bank + payment processor (not top priority). This LLC is separate from FitLogic and likely the home for the menopause/andropause coaching certification course she's planning.
- **New product idea — coaching certification course:** Menopause and andropause coaching certification. Coaches get certified to support clients through hormonal transition. Larger market for women but men included. Likely lives under "My Life on Purpose," not FitLogic.
- **Book draft in progress** — no fixed deadline; working on it as time allows.
- **Pricing rewrite:** Megan rewrote the FitLogic pricing page after finding it was structured like a blog post listing a la carte service costs. Repositioned around the membership model. **Notable competitive data point:** Megan found a competitor charging **$1,600 for a 60-minute initial consultation** — orders of magnitude above FitLogic's current pricing.

## CRM tool — features demoed

- Drag-and-drop pipeline stages (leads → contacted → qualified)
- ~5,341 contacts imported from Megan's old Keap export (dirty data, needs cleanup pass)
- Manual campaigns + sequences (drafts until contacts are added)
- Templates with reusable CTA links (saved buttons, e.g., "get started today")
- Variables for personalization (first_name, email, company, city, last_name, etc.)
- File attachments (lead magnets supported)
- **Per-campaign analytics** (delivered / open / clicked) — newly added per Megan's prior feedback
- **Lead-source tracking** (ChatGPT, Claude AI Search, email, etc.) — added based on Megan's Apr 29 feedback
- **Auto-send default:** 8 AM daily, one batch per contact per day
- **Test-contact flag** so Michelle can practice without sending real emails

## Notable quotes

- **Megan**, on a longtime patient she coached today: *"I asked her, 'what do you need to feel heard, supported, seen?' She said, 'Just keep doing what you're doing — that's exactly why I'm here.'"*
- **Andres**, on landing pages: *"Anybody can sell you something to create a landing page. It's being able to create a landing page the right way — one that converts."*
- **Andres**, on time tradeoffs: *"In one hour, I guarantee you can make more than $150. So it comes down to, do I want to do it myself and spend 5 hours, or convert that time into money?"*

## Patterns observed

1. **Cloudflare workaround closes a 16-day blocker via second domain, not access fix.** The `fitlogicfunctionalmedicine.com` Resend block has been open since Apr 21 (Megan handed over GoDaddy credentials but the Cloudflare layer was never accessible). Rather than escalate further, Megan registered a second domain (`myfitlogic.com`) where she controls DNS end-to-end. **The architectural lesson:** when a customer hands over credentials to one layer of their stack but a deeper layer is locked, the right move is sometimes to stand up a parallel asset they fully own, not to chase the missing access. Worth capturing for the Moil 360 onboarding playbook.
2. **AI-search inbound is now a measurable lead channel for FitLogic** — ChatGPT + Claude AI Search → 4–5 calls Tuesday + 2 conversions + a small waitlist. First on-record quantified data point. If it holds, it strengthens the pitch to other practitioner customers and informs the lead-source taxonomy that was added per Megan's Apr 29 ask.
3. **Megan is now operating in dual-business mode.** FitLogic remains primary, but "My Life on Purpose" LLC creates a second business surface (coaching certification course is the leading candidate). Track both — the certification course in particular is a Moil 360 surface candidate (course-website + email + CRM).
4. **The "owner trains a manager" pattern is operating.** Michelle continues to be the de facto day-to-day operator (consistent with Apr 29 delivery walkthrough). Andres scheduled a next-week in-person visit explicitly to walk both of them through the CRM together — **the manager is now the primary trainee, not the owner.**
5. **Megan's competitive data points are unusually load-bearing.** $1,600/60-min IC competitor benchmark is significant: it widens the visible price ceiling in functional medicine and suggests FitLogic is under-priced. Worth surfacing back to Megan if she ever revisits pricing.
