---
tags:
  - graph/spoke
---
# Apr 21, 2026 — Megan Miller × Andres FitLogic Working Session

**Type:** meeting (customer working session)
**Last updated:** 2026-04-21
**Source:** [[raw/teams-transcript-megan-miller-2026-04-21]]
**Related:** [[wiki/people/megan-miller]], [[wiki/orgs/fitlogic]], [[wiki/moil/customers]], [[wiki/moil/product-roadmap]], [[wiki/concepts/moil360]]

**Duration:** 89 min (3:00–4:00 PM CT; Teams transcript 20:00–21:01 UTC)
**Attendees:** Andres Urrego (Moil), Megan Miller NP (Fit Logic Functional Medicine owner), Michelle (clinic staff, in-room)

---

## Summary

Working session where Andres walked Megan through Moil's CRM (campaigns, sequences, contact list, sales pipeline) on a test instance, then reviewed the in-progress redesign of Megan's website by **Electric Bricks** (her current external vendor). Megan exported her Keap CRM contacts (~5,000 rows) for import into Moil. Session doubled as deliverability debugging — the test email Moil sent her from `partners@moilapp.com` landed in Gmail spam with a 404 link inside.

This was the first hands-on CRM tour with a paying Moil 360 customer. Megan immediately understood and got excited about the **sequences feature** ("This is what I've been wanting") — specifically: drop a new initial-consult patient into a pre-built 3-email sequence and let it run. That is the killer use case for her.

---

## Key Decisions

1. **Sales CRM and patient CRM stay separate.** Megan keeps Keap (or whatever holds patient records); Moil CRM is purely sales pipeline + outbound campaigns. Outbound emails go from a sales address, not her patient communication address.
2. **50 cold-outreach emails/day per email account throttle** — avoid spam jail on cold sends.
3. **Plain-text emails only.** No heavy HTML/branding — better deliverability, feels like a personal note from the clinic.
4. **Default nurture sequence: 3 emails over 6 days** for new-lead / initial-consult follow-up.
5. **Push back on Electric Bricks on the website redesign.** Too text-heavy, too busy, too similar to Megan's current site. Andres's written feedback email is the punch list. If they can't deliver, ask for a refund.
6. **FAQ is its own page** (separate from service pages). Long-form education lives in articles, not on landing pages.
7. **Wait for Electric Bricks to finish before Andres touches their code.** Do not pay them to add the CRM form, quiz form, or `/CRM` route — their per-change fees are too high.
8. **Build a quiz natively in Moil** (replace Thrive Quizzes WordPress plugin) so leads flow directly into Moil CRM. Build after Electric Bricks ships.
9. **Test campaigns with 100 leads before mailing the 5,000-contact list.** Validate which campaigns convert, then scale.

---

## Action Items

### Andres — this week

- [ ] **Tonight (Apr 21):** Code updates so Megan's full 5,000-contact CSV imports in one pass, with cleanup tooling so she can bulk-flag clients vs. non-clients
- [ ] **Tonight (Apr 21):** Wipe test contacts from the CRM instance
- [ ] **Deploy Moil CRM to `fitlogicfunctionalmedicine.com/CRM`** using the GoDaddy login Megan shared during the call
- [ ] **Connect `Megan@fitlogicfunctionalmedicine.com` as the sending address** (currently sends from `partners@moilapp.com`, lands in spam)
- [ ] Verify deliverability after the new sender is wired — re-test that emails don't land in spam
- [ ] Surface **per-campaign click-rate / open-rate dashboard** cleanly (Megan asked; partly visible today)
- [ ] Once Electric Bricks ships, build the quiz form inside Moil and embed on FitLogic site so leads flow into Moil CRM

### Megan — this week

- [ ] **Forward Andres's website-feedback email to Electric Bricks** as the required-changes checklist before she accepts the redesign
- [ ] Ask Electric Bricks for the **logic/reasoning behind the heavy text** on each page — give them a chance to explain before hard pushback
- [ ] Walk her Keap contact list and **mark her actual current clients** — easier to mark the ~real clients than untag the false ones (most "client" tags in Keap are wrong — old massage clients, kids, Charm imports)
- [ ] Pull **remaining contacts from the EHR** not yet in Keap and add to the final CSV before import
- [ ] Send Andres her **quiz questions / current Thrive Quizzes setup** so he can rebuild natively in Moil later

### Joint / pending

- [ ] **Workshop co-planning:** Megan mentioned it to one interested person; Andres has only told Justin K. **Decide whether to push the window or postpone** — timing is tight
- [ ] Andres still owes Megan **ear acupuncture** with Michelle and Anita once Michelle is ramped

---

## Product Feedback — Megan as the Moil 360 customer voice

| Issue | Severity | Notes |
|---|---|---|
| First test email landed in Gmail spam; sender was `partners@moilapp.com` displaying as "FitLogic" | 🔴 Blocker for cold outreach | Needs real sender domain + deliverability fix |
| Link inside the test email returned 404 ("not found") | 🔴 Blocker | Campaign link wiring incomplete |
| User couldn't switch active business plan once one was "stuck" — Megan had an old "for my life" plan that wouldn't switch to FitLogic | 🔴 Previously blocked her — Andres manually intervened | Core bug in plan-switching UX; hit Megan weeks ago |
| Per-campaign aggregate click-rate visibility gap | 🟡 Feature ask | "Is this doing what we want it to do?" — benchmark per campaign |
| Duplicate-contact detection on CSV import | 🟡 Parity ask | Keap has this; Megan expects Moil to as well. Andres confirmed Moil supports it |
| Sequences feature (3-email drip over 6 days, per-segment variants) | 🟢 Killer feature | "This is what I've been wanting." Male vs. female initial-consult variants, auto-trigger on new patient add |

---

## Website Redesign — Electric Bricks Review

**Andres's verdict (written feedback, ~27:30 in):** "It's too busy. Way too much text. Nobody will read this. FAQ should have been its own page. I get what they're trying to do — SEO positioning — but if someone comes here and doesn't know what to do, you're going to lose that client either way."

**Andres's hard-line framing to Megan:** "Either you go 'here's a report, this is all the changes we want or we won't take it' and they say 'we're not doing any of that' and you're like, OK, give my money back. Or they make all the changes and you get what you want."

**Specific defects (from Andres's formal email to Electric Bricks, sent from Megan & Andres chat Apr 21 8:59 PM):**
- **Every image on the site is missing alt text** — sitewide SEO and accessibility failure
- **The homepage has no H1 tag**
- Three blog posts have **chiropractic-themed URL slugs** (wrong vertical — Megan is functional medicine, not chiro)
- FAQ collapsed into service pages instead of being its own page
- Site feels too similar to the current FitLogic site that Megan explicitly wanted replaced

**Decision:** Megan forwards Andres's email to Electric Bricks as the blocker list. Moil does not touch Electric Bricks' code until they deliver.

---

## Personal / Relationship Context

- Megan shared a moving story about **Carla** — a former patient who came to her with terminal colon cancer asking for quality-of-life help rather than treatment. Carla passed about a month after Megan visited her at home. Core patient-relationship story that defines why Megan practices this way.
- Megan recounted catching a **25-year-old male patient's brain tumor early** on a gut-check from his lab work early in her career. Reinforces her clinical instinct as a personal brand asset.
- Michelle is early in clinical training — months before fully ramped.
- Megan handed Andres her **GoDaddy credentials** ("I must really trust you"). Andres reassured her he only logs in during their joint calls.

---

## Key Signals

1. **Megan is the first Moil 360 customer to get a live CRM tour** — feedback is disproportionately load-bearing for product direction. The sequences reaction ("this is what I've been wanting") is the clearest customer pull signal yet for outbound automation.
2. **Deliverability is the week's gating bug.** Partners domain lands in spam for at least two recipients (Megan confirmed; Roxana didn't get her PureSerenity link Apr 20 night — Jacob said devs "can't optimize it more"). This is a **product blocker, not a support ticket**. Either rotate sender infrastructure or move to per-customer domains.
3. **Electric Bricks handoff pattern matters for Moil 360.** Customers come with existing agencies. Moil's play is to wait for the agency to finish, then layer the CRM + quiz + forms on top. If Moil inserts too early it pays the agency's per-change fees. If Moil inserts too late the customer loses confidence. Apr 21 set the pattern: wait, then layer.
4. **Megan trusted Andres with domain credentials** on the first CRM call — relationship depth is meaningfully above the average Moil 360 customer. She is the best case-study candidate in the current roster.
5. **Business-plan switch bug hit a paying customer.** Megan already experienced it; Andres had to manually intervene. Appears again in the Apr 21 Moil Team thread (single plan not connected to business coach). Escalate into product.
6. **Native quiz replaces Thrive Quizzes.** Important product scope — Thrive is a WordPress plugin used by the agency-style customer base. A native quiz + form builder turns Moil into the go-to replacement.

---

## Referenced Artifacts

- Andres's formal feedback email to Electric Bricks (drafted inside Teams "Megan & Andres" chat, Apr 21 8:59 PM, "Subject: Fit Logic Website — Outstanding Items Before Delivery")
- Keap CSV export (~5,000 contacts) — Megan to finish cleanup before final import
- Full WebVTT transcript (89 min, ~2,745 lines) — summarized; raw kept alongside `raw/teams-transcript-megan-miller-2026-04-21.md`
- GoDaddy credentials for `fitlogicfunctionalmedicine.com` — shared during call (to be used only on joint sessions)
