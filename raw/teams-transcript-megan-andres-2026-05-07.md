---
source: Microsoft Teams transcript
captured: 2026-05-07
meeting_date: 2026-05-07
meeting_id: MSpjYzZhZWNhNS0xMjUxLTQ0ZGYtYjg2Mi05MmE5ODM3MWQ4N2IqMCoqMTk6bWVldGluZ19NRE01WVdFeU5XVXRNelF3TXkwMFlUQXhMV0pqWldJdE5EbGlPRE5rT0RrMU1HUXpAdGhyZWFkLnYy
ingested: true
ingested_at: 2026-05-07
---

# Megan & Andres — 2026-05-07

**Subject:** Megan & Andres
**Date:** 2026-05-07
**Time:** 3:30 PM – 4:55 PM CT (20:30–21:55 UTC) — ~1h 21min (transcript started 14 min into meeting)
**Organizer:** Andres Urrego (Andres@moilapp.com)
**Attendees:**
- Andres Urrego — Moil CEO
- Megan Miller — Active Moil customer, owner of FitLogic Functional Medicine + new LLC "My Life on Purpose"

## Context

This was a working session with a key Moil customer. Two parallel threads: (1) FitLogic business operations update, and (2) live demo + setup of the custom CRM/sequence tool the Moil team is building for Megan, including configuring a new business email address for outbound campaigns.

## Key decisions

1. **Email strategy:** Megan created `connections@myfitlogic.com` via GoDaddy's Microsoft 365 email add-on (cheaper than Gmail Workspace, ~$5/mo vs $12). This will be the dedicated outbound/lead-comms email — separate from the existing `practicemanager@fitlogicfunctionalmedicine.com` clinic ops email.
2. **Domain workaround:** The `fitlogicfunctionalmedicine.com` domain is locked behind a Cloudflare config Megan can't access (an old vendor likely set it up). Decided **not** to fight the Cloudflare lock — instead, run all outbound from `myfitlogic.com` where DNS is manageable in GoDaddy.
3. **CRM delivery:** Andres ships Megan login credentials and configured email tomorrow morning (2026-05-08). Megan will start with low-volume testing (a few emails per day, not bulk) using the "test contact" flag while Michelle learns the system.
4. **Landing pages — defer:** Don't build landing pages yet. Wait until the FitLogic website is fully launched, then build SEO-targeted conversion pages for specific services (ear acupuncture, hormone treatment, men's testosterone) — only when ROI is clear.
5. **Mastermind subscription:** Megan is canceling — she doesn't think she needs it.
6. **Trigger-based emails (open question):** Megan asked for click-triggered automation ("if they clicked, send X"). Andres wants to think through the UX so it doesn't feel spammy — deferred, not committed.

## Action items

### Andres / Moil team
- **[2026-05-08 AM]** Configure Microsoft 365 email for `myfitlogic.com` in GoDaddy using credentials Megan sent.
- **[2026-05-08 AM]** Send Megan CRM login credentials (tied to the new `connections@myfitlogic.com` email).
- **[Next week]** In-person visit to FitLogic to walk Megan + Michelle through the CRM. Andres to schedule.
- **[Open]** Design the "clicked-link" trigger flow for the CRM. Decide manual vs automated, and how to keep tone non-spammy.
- **[Ongoing]** Clean up the imported Keap contact list (~5,341 contacts) — remove duplicates and obvious fakes (`sample@email.com` etc.).

### Megan
- **[Done during call]** Sent GoDaddy credentials + new `connections@myfitlogic.com` info to Andres.
- **[This week]** Send Andres his lab order (fasting bloodwork via LabCorp, 8–10 vials) — Megan is debating switching labs from LabCorp to a different vendor. She'll text when the order is in the Charm portal.
- **[Q2]** Add monthly in-person **Women's Vitality Group Circle** to FitLogic membership offering (Megan's patient base is ~90% women).
- **[Later]** Consider quarterly equivalent for men — Megan asked Andres for input on format.
- **[Ongoing]** Continue rewriting website pages (currently going through every page; pricing page already redone — moved away from a la carte/piecemeal pricing toward standard membership programs).

## FitLogic business update (context for the Brain)

- **Hire / training:** Megan is training **Michelle** (new operations / patient connection role). Michelle is excelling at the relational side — one new patient asked Michelle to be physically present in her appointment because she had no one else to bring. Megan flagged this as a strong organic-fit signal.
- **AI-driven leads working:** ChatGPT and Claude AI Search are sending real leads. Megan reported 4–5 calls Tuesday alone, two confirmed conversions, and a small waitlist forming (Megan is intentionally protecting her schedule from overload).
- **New LLC approved:** "My Life on Purpose" finally got LLC approval. Megan is shopping for a new bank + payment processor (not top priority, but on her list). This LLC is separate from FitLogic and likely the home for the menopause/andropause coaching certification course she's planning.
- **New product idea — coaching certification:** Menopause and andropause coaching certification course. Coaches get certified to support clients through hormonal transition. Larger market for women but men included.
- **Book draft in progress** — no fixed deadline, working on it as time allows.
- **Pricing rewrite:** Megan rewrote the FitLogic pricing page after finding it was structured like a blog post listing a la carte service costs. Repositioned around the membership model. Notable competitive data point: she found a competitor charging **$1,600 for a 60-minute initial consultation**.

## CRM tool — features demoed

- Drag-and-drop pipeline stages (leads → contacted → qualified)
- ~5,341 contacts imported from Megan's old Keap export (dirty data, needs cleanup pass)
- Manual campaigns + sequences (drafts until contacts are added)
- Templates with reusable CTA links (saved buttons, e.g., "get started today")
- Variables for personalization (first_name, email, company, city, last_name, etc.)
- File attachments (lead magnets supported)
- Per-campaign analytics (deliver / open / clicked) — newly added per Megan's prior feedback
- Lead source tracking (ChatGPT, Claude AI Search, email, etc.) added based on Megan's feedback
- Auto-send default: 8 AM daily, one batch per contact per day
- "Test contact" flag so Michelle can practice without sending real emails

## Notable quotes

- Megan, on a longtime patient she coached today: *"I asked her, 'what do you need to feel heard, supported, seen?' She said, 'Just keep doing what you're doing — that's exactly why I'm here.'"*
- Andres, on landing pages: *"Anybody can sell you something to create a landing page. It's being able to create a landing page the right way — one that converts."*
- Andres, on time tradeoffs: *"In one hour, I guarantee you can make more than $150. So it comes down to, do I want to do it myself and spend 5 hours, or convert that time into money?"*

## Cross-references

- Megan Miller is listed as an active Moil customer + product feedback source in `pi-workspace/AGENTS.md`. This call is direct evidence of that feedback loop in action — multiple Megan-requested features (analytics, lead source tracking) shipped in this CRM build.
- Possible wiki targets: `wiki/people/megan-miller.md`, `wiki/orgs/fitlogic-functional-medicine.md`, `wiki/moil/pipeline.md` (Megan as live customer + custom-tooling reference account).
