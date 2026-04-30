---
type: meeting-transcript
source: microsoft-teams
ingested: true
ingested_at: 2026-04-21
ingested_run: 17
---

# Teams Meeting Transcript — Megan & Andres
**Date:** 2026-04-21
**Time:** 20:00–21:01 UTC (3:00–4:00 PM CT, 89 min recorded)
**Subject:** Megan & Andres
**Source:** Microsoft Teams transcript (auto-captured via Graph API)
**Meeting ID (Graph):** `MSpjYzZhZWNhNS0xMjUxLTQ0ZGYtYjg2Mi05MmE5ODM3MWQ4N2IqMCoqMTk6bWVldGluZ19NVEkwTnpKbFpEWXRObU15TWkwME1XUmpMVGd3WmpBdE1UWm1Oekk0WVRaaE16RXdAdGhyZWFkLnYy`

## Attendees

- **Andres Urrego** — Founder/CEO, Moil (organizer)
- **Megan Miller, NP** — Owner, Fit Logic Functional Medicine (active Moil customer)
- **Michelle** — Megan's clinic staff (in-room with Megan, partial participation)
- **Lori** — clinic staff, briefly mentioned
- **Cassandra** — clinic staff, briefly mentioned
- Brief background interactions with patients (Leslie, Ina, Carla in Megan's clinic)

## Context

Working session: Andres walked Megan through Moil's CRM (campaigns, sequences, contact list, sales pipeline) using a test instance. Also reviewed the in-progress redesign of Megan's website by **Electric Bricks** (her current website vendor). Megan exported her Keap CRM contacts for import into Moil.

---

## Key Decisions

1. **Sales CRM and patient CRM stay separate.** Megan keeps Keap (or whatever holds patient records); Moil CRM is purely for sales pipeline + outbound campaigns. Outbound emails will go from a sales address, not her patient communication address.
2. **Throttle: max 50 cold-outreach emails/day per email account** to avoid spam jail.
3. **Plain-text emails only** (no heavy HTML/branding) — better deliverability, feels like a personal note from the clinic.
4. **Sequence default:** 3 emails spread over 6 days for nurturing leads (e.g., new initial-consultation patients).
5. **Push back on Electric Bricks** on the website redesign — too text-heavy, too busy, looks too similar to Megan's current site. Andres' written feedback email serves as the punch list. If they can't deliver, ask for a refund.
6. **FAQ should be its own page** (separate from main service pages); long-form education should live in articles, not on landing pages.
7. **Wait for Electric Bricks to finish the website** before Andres touches their code to add the CRM form, quiz form, or `/CRM` route. Don't pay them to do it — their per-change fees are too high.
8. **Build a quiz natively in Moil** (replace the Thrive Quizzes WordPress plugin) so leads flow directly into Moil CRM with no go-between. Build it after Electric Bricks delivers the new site.
9. **Test with 100 leads before mailing the 5,000-contact list.** Use the 100 to validate which campaigns convert before scaling.

---

## Action Items

### Andres (this week)
- [ ] **Tonight:** Make code updates so Megan's full 5,000-contact CSV can be imported in one pass (with cleanup tooling so she can flag clients vs. non-clients in bulk).
- [ ] **Tonight:** Wipe the test contacts from the CRM instance.
- [ ] **Deploy CRM to `fitlogicfunctionalmedicine.com/CRM`** using the GoDaddy login Megan sent during the call.
- [ ] **Connect `Megan@fitlogicfunctionalmedicine.com`** as the sending address (currently sending from `partners@moilapp.com`, which lands in spam).
- [ ] Verify deliverability after the new sender is wired up — re-test that emails don't land in spam.
- [ ] Add **per-campaign click-rate / open-rate dashboard** as a feature (Megan asked; Andres confirmed it's already partly visible but agreed to surface it cleanly).
- [ ] Once Electric Bricks delivers the new site, build the quiz form inside Moil and embed it on the FitLogic site so leads flow into the Moil CRM.

### Megan
- [ ] **Forward Andres' website-feedback email to Electric Bricks** as a checklist of changes required before she'll accept the redesign.
- [ ] Ask Electric Bricks for **the logic/reasoning behind the heavy text on each page** — give them a chance to explain before pushing back hard.
- [ ] Walk through her Keap contact list and **mark her actual current clients** (most existing "client" tags in Keap are wrong — many are old massage clients, kids, or imports from Charm that never got cleaned up). Easier to mark the ~real clients than untag the false ones.
- [ ] Pull the **remaining contacts from the EHR** that aren't yet in Keap and add them to the CSV before final import.
- [ ] Send Andres her quiz questions / current Thrive Quizzes setup so he can rebuild it in Moil later.

### Joint / pending
- Workshop they're co-planning: pushed timing is tight (today is Apr 21, target window is soon). Megan told one interested person about it; Andres has only mentioned it to Justin K so far. **Need to decide whether to push or postpone.**
- Andres still owes Megan **ear acupuncture** with Michelle and Anita once Michelle is more confident in the technique.

---

## Notable Customer Insight (product feedback)

- Megan immediately understood and got excited about the **sequence feature** ("This is what I've been wanting"). Specifically: drop a new initial-consult patient into a pre-built 3-email sequence and have it run automatically. This is the killer use case for her.
- Megan flagged that the **first test email landed in her Gmail spam folder** — sender was `partners@moilapp.com` displaying as "FitLogic". The link inside the email returned a 404 ("not found") because it wasn't wired up yet. Both are blockers for cold outreach until fixed.
- Megan asked specifically for **per-campaign aggregate click rate** so she can benchmark campaign performance ("is this doing what we want it to do?").
- Megan was previously stuck with an old "for my life" business plan in Moil that wouldn't switch to FitLogic — Andres had to manually intervene with the team. **Bug:** users can't easily switch their active business plan once one is "stuck."
- Megan wants the ability to **recognize duplicate contacts on CSV import** (Keap has this; she expects Moil to as well). Andres confirmed Moil supports it.

---

## Personal / Relationship Context

- Megan shared a moving story about a former patient (Carla) who came to her with terminal colon cancer and asked Megan to help her improve quality of life rather than pursue treatment. Carla passed away about a month after Megan visited her at home. This is the kind of patient relationship Megan describes as core to why she does this work.
- Megan also recounted catching a 25-year-old male patient's brain tumor early in her career on a gut-check from his lab work. Reinforces her clinical instinct as a personal brand asset.
- Michelle is still in early training — months before fully ramped on the clinical side.
- Megan trusts Andres enough to hand over her **GoDaddy credentials** ("I must really trust you"); Andres reassured her he only logs in during their joint calls.

---

## Full Transcript (verbatim, WebVTT)

The complete transcript was captured via Microsoft Graph (`OnlineMeetingTranscript.Read.All` scope). Stored separately because of size; key passages are summarized above. Full VTT is preserved at:

- Source: Microsoft Graph `transcripts/{transcriptId}/content` (DOCX/VTT)
- Full WebVTT file (89 min, ~2,745 lines): retained at `/tmp/megan_transcript.vtt` during ingestion; should be archived to long-term storage if Megan-call transcripts are kept as-corpus.

### Transcript excerpts (key segments)

**On the website redesign feedback (~27:30 in):**
> Andres: "It looks good, but a couple of things. It could use a little bit more interactivity, but the main thing is it's too busy. It's got way too much text. Nobody will read this. ... FAQ should have been its own page. ... I get what they're trying to do, which is position you well on SEO. But if you're positioned well on SEO and someone comes here and doesn't know what to do, you're going to lose that client either way."
>
> Megan: "Yep, that's the whole reason why I wanted a new website is because my current one is too busy."
>
> Andres: "Either you go completely 'here's a report, this is all the changes we want or we won't take it' and then they're like 'we're not doing any of that' and you're like, OK, give my money back and we're done. Or they make all the changes and you get what you want."

**On the contacts mess in Keap (~36:30 in):**
> Megan: "I know the name of everybody who is here. ... but there's a lot of these who are marked as clients who are not clients. I don't know why."
>
> Andres: "Interesting. It was probably the way they were imported."

**On the sequence feature (~1:18:30 in):**
> Megan: "Is there a way... let's say we have 3 emails that we want to go out to every single initial consultation, one for women, one for men, depending on what they're coming in for, like what to expect. ... and then we just put the person in and then a series is going..."
>
> Andres: "Literally, yeah. ... You create them up front. Now what you're going to do is, every time a new client that needs to go into that sequence, you just add him right here."
>
> Megan: "This is what I've been wanting."

**On the test email landing in spam (~1:06 in):**
> Megan: "I got one today from FitLogic, 'a different way to think about your health.' But it is in spam. It says fit logic and then partners at Moilapp.com. Yes, it is in spam."

**On the quiz integration (~1:24 in):**
> Megan: "Is the functionality possible in Moil to build a quiz that when... it's possible for the website to link with a quiz hosted here so that the information gets dumped right in the CRM, and there's not an extra step? Then we can eliminate, you know..."
>
> Andres: "Right, right. No, absolutely. Once they submit there, the contact gets created here for sure. But we have to wait for the current company that's doing the website to deploy that once they're done."
