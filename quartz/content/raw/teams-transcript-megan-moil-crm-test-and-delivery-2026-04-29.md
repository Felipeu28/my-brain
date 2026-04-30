---
tags:
  - graph/leaf
  - source/teams-transcript
date: 2026-04-29
---

# Teams Transcript — Megan & Moil — CRM test and delivery

- **Meeting subject:** Megan & Moil - CRM test and delivery!
- **Date:** 2026-04-29
- **Time (UTC):** 14:30 – 15:58 (transcript end)
- **Source:** Microsoft Teams (Graph API transcript export, VTT)
- **Meeting ID:** `MSpjYzZhZWNhNS0xMjUxLTQ0ZGYtYjg2Mi05MmE5ODM3MWQ4N2IqMCoqMTk6bWVldGluZ19PV00wWVRkaVlUVXRPRE0xTVMwME1qWTFMV0UwWkdFdE16TTFZelppTWpNNE1USTRAdGhyZWFkLnYy`

## Attendees

- **Andres Urrego** — Founder & CEO, Moil (organizer)
- **Megan Miller** — owner, FitLogic functional medicine practice; Moil customer (`meganmillernp@gmail.com`)
- **Michelle** — Megan's practice manager (joined mid-meeting; new staff to be added to FitLogic Moil account)
- **Taiwo Ola Balogun** — Moil developer (`Taiwo@moilapp.com`; briefly unmuted)

## Context

Walkthrough/training session delivering Moil's custom build for FitLogic: contact CRM, AI campaign creator (email), and Content360 30-day social calendar with image and video generation. Megan is migrating from Charm (medical) and Keap as source CRMs; ~5,000 contacts to import, mostly cold leads with a smaller subset of active patients. Module already wired to Megan's Gmail. Brand colors and logo in Brand DNA partially configured.

## Key decisions

- **Posting cadence:** Daily, not weekly. On days with both image and video, post twice (one for each asset).
- **Email rollout strategy:** Don't blast all 5,000 cold leads on the same email. ~10/day cadence; rotate variants until one performs.
- **Tone for AI-generated emails:** Hook-style opener (e.g., "You may be wondering…", "Are you still struggling with…") instead of "I wanted to share…". Patient-focused, not founder-focused. Megan and Michelle will edit per-send via the free-form prompt box rather than asking the AI for rewrites (avoid unnecessary API calls).
- **Lead segmentation taxonomy agreed:** cold / previous client / active patient / inactive patient / IC-only (initial consultation only) / massage-only legacy. Andres extracts patient vs. non-patient from the 5,000-row export; Megan handles the manual IC-only tagging on her side.
- **Bulk-tag shortcut:** Megan will identify the day Jill's contact list was imported and mass-tag those rows (good-enough segmentation without per-row review).
- **Default image format:** Stories layout (vertical) — performs best on Facebook/Instagram per Andres.
- **API key for AI email generation:** Megan continues using Moil's test API key during testing; switch to FitLogic's own key at launch (~$2–3/month expected).
- **Testing rule:** Test sends only against newly-created test contacts, never existing customer contacts.

## Action items

### Andres / Moil engineering

- [ ] Extract patients vs. non-patients from FitLogic's 5,000-contact export (Megan already shared the patient list earlier — Andres to retrieve from prior call).
- [ ] Add "Last contacted" filter/tab on contacts so Megan can see who's been touched and who hasn't.
- [ ] Add a `previous client` option on lead source / pipeline so prior-but-inactive patients can be segmented and emailed differently.
- [ ] Customize the lead-source drop-down to include: social media, website, driving by, friend/family referral, networking event, other (with free-text on "other").
- [ ] **Bug:** pipeline stage updates in the pipeline view don't propagate back to the contact card. Fix so a contact moved to "won" displays as "won" in the card and rolls into analytics.
- [ ] **Bug:** Content360 calendar defaulted to February dates instead of current month — investigate (may be a stale date param when Megan started).
- [ ] **Bug:** "Edit image" action in Content360 appears to constrain regeneration to the original image rather than producing a new image from the new prompt — investigate.
- [ ] Verify Brand DNA colors are propagating into the Content360 image generator (Megan suspects they aren't because she set up the calendar before saving colors).
- [ ] Add closed-captioning support for generated videos (accessibility — flagged as good feedback).
- [ ] Send Megan today: platform access details, list of what she needs, and confirmation Michelle can be added as staff.
- [ ] Build chat/FAQ widget tied to FitLogic's website once the website is deployed; include "book a call" link to Square calendar.
- [ ] Add ability to paste/manage links centrally so they can be reused across emails.

### Megan / FitLogic

- [ ] Bring brand color hex/RGB values from home notebook and enter in Brand DNA.
- [ ] Export active-patient list from Charm; identify any inactive names she doesn't recognize.
- [ ] Manually tag IC-only patients (people who came for an initial consultation but never converted).
- [ ] Add Michelle as staff via Settings → Add Staff.
- [ ] Reach out to her Austin business friend re: how they added closed captions for accessibility on Instagram videos.

## Notable observations

- Phone interruption mid-meeting for a Buda Drug Store medication refill — patient-care work bleeding into the training; Megan's practice manager hand-offs are real-time.
- Michelle joined ~2/3 through and immediately gave the most useful copy feedback ("we need a hook"); she should be the primary day-to-day operator of the platform.
- Megan is uncomfortable with the word "I" in cold-email openers ("I don't care what you want") — wants reader-centered copy. This is a tone signal worth baking into the FitLogic brand voice config.
- Taiwo (developer) was on the call with hot mic playing audio — minor professionalism issue; worth a note for future client-facing calls that internal devs should stay muted.

## Full transcript

**Andres Urrego:** which is, we're going to add that little section, which is, okay, someone called in or, you know, I had a, you know, they stopped by, you know, whatever you want to do, you can add those notes. Right now, you can add them directly here into the contact. But I want it to be actually separate, like, okay, they came in three different locations that I was able to just.

**Andres Urrego:** log in three different, or one was a call, one they stopped by, one we email them, you know, so that you can log all of those separately.

**Megan:** Yeah.

**Megan:** Perfect.

**Megan:** Is there a way when we do that to?

**Megan:** To then go in and like...

**Megan:** download a report or see like how many in like how many people in the last month called or stopped in or like how we're getting leads.

**Andres Urrego:** How many people in the, so say that again, sorry.

**Megan:** Yeah, that would be good to know.

**Megan:** Is there a way for us to track in this system how we are getting new leads? So if we do it, if we put them in and add a tag that, you know,

**Megan:** drove by and saw the sign or walked in or, you know, however they found us, is there a way for us to then look back and so we can track, oh, look, we got this many people who called based on, and by the way, we've had at least three people call and say that they found us.

**Andres Urrego:** Okay, very good.

**Andres Urrego:** Absolutely.

**Megan:** through ChatGPT or Claude.

**Andres Urrego:** Very nice. Okay, that's good. That's good. And what are they searching for? Did they say?

**Megan:** It.

**Megan:** What are they? You know what? The search is functional medicine. Oh, okay. Yeah.

**Andres Urrego:** Yeah, yeah, yeah, yeah, very good.

**Megan:** So, we had one functional medicine and then local, yes.

**Andres Urrego:** Yeah, and that's exactly what I meant the other day with the guy on the call is, I mean, I don't know that always more is better, right? I mean, it's yes, more pages, but you have 30 pages, you know? You hide all the extra text that people don't need to see inside of Q&As rather than having it all displayed, but then you actually let...

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** Ohh, mhm.

**Andres Urrego:** people navigate your website. Because if we need to know they just kind of get, oh, whoa, what's happening here?

**Megan:** Yeah.

**Andres Urrego:** But very good, very good. Yeah, so we can add it inside of the edit contacts so that you can come in here and for example, just add something like, you know, how did they, how did you hear about us or, you know, source of lead.

**Megan:** Mhm.

**Andres Urrego:** Oh, well actually it's here, but maybe other...

**Megan:** Yeah. Can we customize that drop down to include like social media, website, driving by, you know, friend or family referral, networking event. Can we customize that drop down or is it set?

**Andres Urrego:** Yeah, okay.

**Andres Urrego:** Perfect.

**Andres Urrego:** Yeah, yeah, yeah, absolutely. You, yeah, I mean, if I'll add those that you just mentioned, we can add those, and then, and then if you guys want to add any more, just let me know.

**Megan:** Okay.

**Megan:** Just put it in a connecting.

**Andres Urrego:** Yeah, most people, what they'll do is, you know, like, you know, if we have like 10 or 15, they'll just do other, and then we add an extra box of like other. And then that way you keep it clean, you keep the top ones that you typically see. And then under other, it opens up an extra box where you type what other was.

**Megan:** But it is, yeah. That's how, I don't know if I've shown you that in Charm yet. But every time we click on, so they are all in there. How, well. You do have a list like that already. In Charm. Yeah, I'll show you.

**Andres Urrego:** Yeah, so then you have your pipeline stage, right? It's a sales cycle, so contacted, qualified, proposal, negotiation, won and lost. You'll be able to update those as well.

**Megan:** Yeah.

**Andres Urrego:** Phone.

**Megan:** And then how do we see like how many we won and how many we lost, for example?

**Andres Urrego:** Okay.

**Andres Urrego:** Right. Well, I mean, that's that. So what I tell people is unless the client says stop emailing me or, you know, I mean, I just think is as long as you continue to do it periodically, you know, and as long as it's not like, oh, I'm going to send you 5000 emails over the next two months, I think, you know, you can nurture these clients and it becomes a thing of

**Andres Urrego:** you know, of have it. Okay, oh, this was nice. I got to read this this month or, you know, maybe, oh yeah, this was a good reminder that I should come in. And unless someone says, hey, stop emailing me. Well, that point is not yet lost, right? And then, you know, when you're tracking it, so when you say, for example, okay,

**Megan:** Mhm.

**Megan:** Right.

**Andres Urrego:** Right here. So cold, right? So maybe it's an active lead. Maybe they replied and they said, okay, yeah, I think I'm going to stop by. Other than that, they're cold, right? They're cold leads because you're just emailing and they're not warm until, you know, like something has actually happened or replied from them.

**Megan:** I think.

**Andres Urrego:** If, you know, if someone said, hey, one would be okay, we moved it over to you as a client, right? You've already moved it over into your system. But then I think other than that, just to keep your other system clean and keep this very organized, then you move them alongside this, right? So qualified, contacted, right? Okay.

**Andres Urrego:** they got an email, so it's going to move to contacted, but then qualified would be they replied and with established conversation, right? Once they come in, you make a proposal. If you obviously, they say, yes, I want to get started today, then obviously that's a won lead and now you know you've won that lead and it's been moved over to your new system. Does that make sense?

**Megan:** Thank you for calling Fit Project. This is Michelle. How may I help you?

**Megan:** Hey.

**Megan:** Yes, just one second.

**Megan:** Yeah, so if, here, I'm gonna move you because Michelle had to take a phone call. If, so we have, when they come in for like an initial consultation, and after that, if then they sign.

**Megan:** Sign up for a program.

**Megan:** That would be considered like a converted, right? Converted from so.

**Andres Urrego:** Yeah.

**Andres Urrego:** Of course, I mean, well, I mean, honestly, the moment they come in from an email, that, I mean, you got the client, now it's can we convert it inside of the store, right? So, because the job, at that point, the job of the email has been done. The client came in.

**Megan:** Yeah, so I'm just wondering.

**Megan:** Yeah, and so is there a way to like...

**Megan:** To track that, like, if if they came in and then converted, like, how many of how many of those happened, you know, per month? Is there a way to just...

**Megan:** I don't know, see a screen of how many or download a report or...

**Andres Urrego:** Well, yeah, you're going to be able to see, yeah, yeah, and we'll look at the analytics and then see if we don't have it yet, so that it shows you like, oh, so far this month, this many, you know, this many have actually, but we'll have to do a good job at making sure that, okay, if the person came in, right, and then, you know, we know, okay, now I know this is actually $1400, right?

**Megan:** Do you know what I'm saying?

**Megan:** Yeah.

**Megan:** OK.

**Andres Urrego:** And then, okay, it's one, then I'm gonna update it, right? I'm gonna update it, boom, it's one, perfect. And then now in my pipeline.

**Megan:** Okay.

**Megan:** Mm.

**Megan:** K.

**Andres Urrego:** Up to you, uh, okay, there we go.

**Andres Urrego:** I thought I updated it.

**Megan:** So.

**Megan:** Sure, the entire Friday.

**Andres Urrego:** Actually, ohh, newly one.

**Megan:** Anything here?

**Megan:** Yes.

**Andres Urrego:** Interesting.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** OK, I see.

**Megan:** The.

**Megan:** I will.

**Megan:** Best.

**Megan:** Fat people.

**Andres Urrego:** Okay, so right here is where I'll make sure not referrals one. I'll add one that it says one deals. Okay, so in the sales pipeline and in the analytics, I'll make sure that.

**Megan:** Ohh.

**Megan:** Okay. Okay.

**Andres Urrego:** because that one deal that I just moved over should actually show here in your analytics. So in your analytics, you already have your one deal, right? You're going to see your open opportunities, click rate, bounce rate, open rate.

**Megan:** Bean.

**Megan:** Actually.

**Andres Urrego:** And this, and right here, it's obviously showing you the one deal, but I want to make sure that it is updating. I think that's just a connection error in the database, but it now.

**Megan:** Pop.

**Megan:** Starting.

**Andres Urrego:** Yeah, because this one's already one. See, see, it's because it's not updating in the contact itself. The pipeline stage is not updating, even though in the pipeline it is. So I'll fix that so that that person now starts showing as one, right? That's a one deal. And then that's the way you'll be able to track it.

**Megan:** So.

**Megan:** Yes.

**Megan:** K.

**Megan:** Okay, hold on one quick second. Andres, is she, she's out of all of her medications and so Buda Drug Store sent us something just 3 minutes ago and so to refill it. Well, what I would do is...

**Andres Urrego:** Yeah.

**Megan:** Due to Drugstore said they sent it to us on Monday. I know, we don't.

**Megan:** The patient, they send it in a way that I never check. I'll show you that. But what I would do is call them and ask them if they can have it ready for her today or what's the soonest they can have it ready for her. And if they can't have it ready for her by tomorrow, then I really would like to refer to use Grace.

**Megan:** But if they can't, then just, and also I have some, if Chelsea wants to come in and pick up, I can give her a couple. Okay, so if we can get this signed, can they fill it today? And then if not.

**Megan:** We'll find another, and if if they can fill it.

**Megan:** today, then just give him a verbal and tell him that you're the practice manager. OK. I know all of them. OK. So yeah.

**Megan:** Mm.

**Megan:** Okay.

**Megan:** We have a...

**Megan:** I'm back. Moving over, so Michelle can make that call.

**Andres Urrego:** Alright, perfect.

**Andres Urrego:** So now I'll show you the, again, we'll just kind of make sure we go to the AI campaign creator. The only thing that we have left to do is just change. And again, you know, you can test this while you're in testing. You can continue to use our test API key. Once this is done, we'll add your API, you know, we'll help you create an API key that you can add on here.

**Andres Urrego:** And then again, that's going to be, at most, honestly, probably a couple bucks a month that you will spend on actual API calls to create all of your emails and stuff. So the API key is the connection to any of the language models to be able to use.

**Megan:** Awesome.

**Megan:** I like.

**Megan:** The.

**Megan:** What is an API key?

**Andres Urrego:** All the AI that happens behind your application.

**Megan:** Okay.

**Andres Urrego:** So, is the cost of running the the the the AI right? So, every call you make, so as people as personal, you know, on our personal level, we use just we just pay for a membership and then we use that, but as a business, you pay for API calls. So, if you have a Gemini key or a Grok or or ChatGPT, whatever.

**Megan:** And I.

**Megan:** Yeah.

**Andres Urrego:** you know, to be able to connect to their product, you have to pay for that API key. You know what I mean?

**Andres Urrego:** Does that make sense?

**Megan:** Kind of.

**Andres Urrego:** Okay, so yeah, I mean when you consume so if

**Andres Urrego:** Your website or your product today uses AI.

**Andres Urrego:** That AI has to come from somewhere.

**Megan:** Okay.

**Andres Urrego:** Does that make sense? The language model that is producing everything has to come from somewhere, and that's about a couple dollars a month.

**Megan:** Yeah, yeah.

**Megan:** Yeah.

**Megan:** Yes.

**Andres Urrego:** Depending on how many you use, you know, how many times you...

**Megan:** Oh, so each for each.

**Megan:** Send.

**Megan:** I have a reason over.

**Andres Urrego:** No, $2, a couple dollars a month total, period.

**Megan:** Okay.

**Andres Urrego:** Does that make sense?

**Megan:** Yeah.

**Megan:** Is it possible to get those?

**Andres Urrego:** Just a second.

**Megan:** I was.

**Megan:** Before you can get to the screen.

**Andres Urrego:** So, the.

**Andres Urrego:** Okay, so you're going to create it. And again, this, it could might be a dollar. You know, just again, it depends how often you're going to create, how many different emails you're going to create. But I would never expect you to spend more than $3 in a month on this.

**Andres Urrego:** Um, okay, so you can't see my screen, right?

**Megan:** Yes.

**Andres Urrego:** Perfect. All right, so we've created the email, right? So we're going to, here's where you're going to be able to edit your email, right? You're going to be able to make changes. Here you can preview the email, right? It has been a while since we last spoke, and I wanted to share a quick thought on why functional medicine often works in traditional approaches for short.

**Andres Urrego:** Most care focused on suppressing symptoms, but we focus on finding the root cause of your health challenges. Whether you're dealing with persistent fatigue, gut issues, or hormonal imbalances, we look at your body as a whole system by addressing the underlying triggers rather than just masking the effects. We help you achieve health that actually lasts. And then it will use their first name. Are you still looking for deeper answers to your health questions? You can learn more about our personalized approach here.

**Megan:** Thats.

**Megan:** I want to see your process.

**Megan:** To go to that site.

**Megan:** Okay.

**Megan:** Up.

**Andres Urrego:** And then I am we are adding the the for you to be able to add edit the links, right? So like you'll be able to just paste the link and then use them for and then use them for any of the emails.

**Megan:** Okay.

**Megan:** Okay.

**Andres Urrego:** Like, whatever you want to take them, right?

**Megan:** I.

**Andres Urrego:** What did you think about that email? Like the language? Does it feel like we've made sure that we create something that speaks kind of the language, that it feels natural, that it feels not pushy, and that it kind of goes along with your brand?

**Megan:** The.

**Megan:** Um...

**Megan:** Mostly, it's pretty good. I just, and I'd like Michelle to look at it when she's finished doing what she's doing. But the I wanted to.

**Megan:** I'm not a fan of that wording, but I know that's...

**Megan:** just because it's pretty common. So for the most part, it's pretty good.

**Megan:** I would just probably change that to like, um...

**Megan:** more about not what I, not that I want to share, but more about what them, you know.

**Andres Urrego:** Well, but it is you, the you are the brand, you are, you are the...

**Andres Urrego:** The person they see.

**Megan:** I know, I know, I'm just particular about wording.

**Andres Urrego:** OK, but tell me more, like, when, when...

**Megan:** So, like, instead of...

**Andres Urrego:** How do they how do they feel like it's you and not just another generic any email you're sending anyone and everyone?

**Megan:** No, I mean, because it's saying what I want. I want it to be about what they want. So it's been, Michelle can probably, let Michelle read it real quick. She's better at putting my thoughts into words.

**Andres Urrego:** Well, but you wanted to share a quick thought.

**Andres Urrego:** Okay, okay, thank you.

**Andres Urrego:** Where is Michelle then?

**Megan:** Yeah, she's right here. Oh, thank you.

**Andres Urrego:** OK, OK, sorry, sorry, I wasn't sure I thought she was bringing a call.

**Megan:** Yeah, I'm right. Oh, yeah, I'm right here. I'm just I'm reading the second sentence, paragraph one.

**Andres Urrego:** Perfect.

**Megan:** And who is the target audience for this email?

**Andres Urrego:** This one was, I think it was something like cold emails or, you know, people that we haven't talked to or reached out in a while.

**Megan:** Cold emails, OK.

**Megan:** So what I was trying to say, Andres, is maybe something like, instead of I wanted to share a quick thought, I would probably change that to something like, you might be wondering why.

**Megan:** instead of I wanted to share, you may be wondering.

**Megan:** It's a small change, but... Yeah, it's like we need an attention getter to start it off with, get them thinking, like a question. Like if you were doing even a presentation, you would start with, you know, like a thought-provoking question to get them to read the rest of the email.

**Megan:** A hook? A hook? Yes, a hook. We need the hook.

**Andres Urrego:** Just you, OK. Perfect. No, that's good feedback.

**Andres Urrego:** I, okay, perfect, perfect. Now, when it comes to re-engaging, and I, and I just honestly, I just, I have to say, when it comes to re-engaging clients, you know, it has to come from you and it has to feel personal. If not, we're going to fall into the same thing that every other email reads like.

**Megan:** Yeah.

**Megan:** Mhm.

**Megan:** Oh yeah, for sure.

**Andres Urrego:** and it's generic, right? So when, you know, just keep in mind that saying, I wanted to share this with you, I mean, it doesn't take away from anything from them. It's not, look, this is the practitioners emailing me and saying, I wanted to reach out and just share a little bit on why traditional

**Megan:** Exactly.

**Andres Urrego:** I mean, why functional medicine afterwards when traditional approaches fall short? All right, OK, so OK.

**Megan:** You know, this might be this might be a personal thing for me, because...

**Megan:** Of the I want like.

**Megan:** And maybe you can tell me, Michelle, if it's different because sometimes I'm like, well, I don't care what you want. That's exactly what I was going to say. You know, so I don't want to make it about what I want. It's like, what do they need? Yeah, right now. And it still can be very personal. Like here's.

**Andres Urrego:** But you don't know though. See, that's what I mean. You don't know what they mean.

**Megan:** Right, so you could say you may, you may be wondering.

**Megan:** Or are you still struggling with?

**Megan:** Or so, for example, we had a...

**Andres Urrego:** But we don't know that. We don't know that, right? This is a complete, these are 5,000 people that we, most of them, we've never talked to.

**Megan:** They've never met us.

**Andres Urrego:** Yeah, so like you, you, you, this entire list that we're building this off of is mostly because we don't we don't have the full or I don't think we have the full keep the list of actual patients because we wanted to keep those separate, but we can we are going to add them as a category on here, but the list of 5000 people we're going to upload, those are from

**Megan:** Um...

**Andres Urrego:** Or I think you were going to send me the patient list so we could extract them, I think.

**Megan:** We did and you downloaded it on the call. I shared it with you.

**Andres Urrego:** Okay, okay, okay, yes, so then I need to, okay, so I don't have that yet where I've extracted them from the from the outreach list, because yeah, so if it's cold, I mean that.

**Andres Urrego:** Again, you have your 5,000 that you need to work on to bring those as new clients, and then everybody else that's already a client needs to be treated differently.

**Megan:** So here's a different way to say that. Instead of I wanted to share, maybe just I'm sending this email to share.

**Megan:** Just the I wanted to thing is I don't like it.

**Andres Urrego:** And that's fine. I mean, and that's what you guys are going to be able to make those edits. So that, yeah, absolutely. So it just needs to sound like fit logic. Now, you know, when it comes to, you know, the things of.

**Megan:** Yeah, tweak it.

**Megan:** Yeah.

**Megan:** And then?

**Andres Urrego:** you know, we wanted or you know this thing, I mean, we can probably make those changes.

**Andres Urrego:** As we can hard code some of those changes, but some others, you know, we'll just have to maybe edit manually, right?

**Andres Urrego:** But because if we, I mean, unless you want me to add a way for you to be able to just ask the AI, like make this change, but I think sometimes that's an unnecessary API call for something that could be changed semantically. Does that make sense? Financially is what I do.

**Megan:** Yeah. Yeah. I just don't know that the first part, if we want it to sound like Megan, like you were saying, we want this to sound like you, it would sound like a personal email coming from her. And I, just having only been here a couple weeks, I don't think this is how she would write an email, that first part.

**Andres Urrego:** Yeah.

**Megan:** It may seem really, really minor or, you know, picky, but words really do matter. And so it may be just a couple, you know, words that we want to tweak in that for a second sentence. Am I speaking out of turn like that? No. Okay.

**Andres Urrego:** Absolutely, and look, that that's what it is exact.

**Andres Urrego:** And that's why this exact box is for, right? This is so we just did a one-click like test, right? But this is what that exact box is for. I wanted to sound like this. I wanted to say this. I wanted to mention that, right? This is the, you know, you have the quick options and those are, you know, just if you ever needed something to kind of get started.

**Megan:** That's why I want you here. Okay.

**Megan:** Mhm.

**Megan:** Mhm.

**Megan:** Okay.

**Megan:** Mhm.

**Andres Urrego:** You know, you can pick, introduce this, and then from there we add more detail to it. And this is where it gets to be personalized, right? This is where it gets to sound. What we've built on the back end is the brand, bit logic, right? The company, the product, you know, it understands the company, it understands the system.

**Andres Urrego:** Now, this is the area where we can imprint Megan. Does that make sense?

**Megan:** Mm-hmm.

**Andres Urrego:** Does that work?

**Megan:** Yeah, I think if we just we can put in there.

**Megan:** to make it more about them.

**Andres Urrego:** Absolutely, and you can, right? You can't, don't.

**Megan:** Well, I think we can, you know, make that make the person reading the email feel very special, and that it's, yeah, it's patient focus.

**Taiwo Ola Balogun:** F.

**Taiwo Ola Balogun:** Yeah.

**Taiwo Ola Balogun:** Nothing without tickets, a transit file of 20,000 Tairan. Trading and fighting are really smoking and are not allowed.

**Andres Urrego:** Oh, sorry, just a second.

**Andres Urrego:** I wasn't muted. Okay. All right, make it personable.

**Megan:** Make the person reading it feel like it's about them.

**Taiwo Ola Balogun:** If you would like to listen to music, action video, or only use headphones.

**Andres Urrego:** S.

**Megan:** What?

**Megan:** What is that? I don't know.

**Andres Urrego:** I don't know why Taiwo keeps unmuting himself. That's our developer.

**Megan:** Yeah.

**Andres Urrego:** Yeah, so perfect, done.

**Andres Urrego:** So yeah, and this is again, this is where you get to have fun with AI, right? To say, you know, if you liked it, if you loved it, then you can use, you know, you can go, you know, you can use it. If you didn't love it, you can go back and try the new one.

**Megan:** That's better.

**Andres Urrego:** But that's the entire point, right? That we, that we, that you guys have something that you can completely personalize, that it, that you can guide, that you can tell it, my personal style is this, I want it to sound like that. So it gives you, good, good.

**Megan:** Yeah.

**Megan:** There, that first paragraph.

**Megan:** Okay.

**Megan:** Yeah, this is much better. Yeah.

**Megan:** That's much more engaging. Yeah.

**Megan:** and relatable.

**Megan:** For sure.

**Andres Urrego:** Beautiful. Awesome. Very good. And so you say safe campaign.

**Andres Urrego:** And your campaign's here, it's ready to go.

**Andres Urrego:** Give us your email.

**Megan:** So you don't have any of our contacts in there right now?

**Andres Urrego:** Some tests, yeah, we have 26 contacts right now for testing.

**Megan:** Oh, I see. I know I recognize a couple of them. One's my neighbor.

**Andres Urrego:** Yeah, and that's the thing, right? So whenever you guys are going to start sending the emails, I would honestly recommend two things. We're going to add a tab that kind of tells you last contacted so that you can filter by like, okay, these are the last ones I contact or the ones that I haven't. So that every time, like if you guys are going to do your, do it weekly or every day or.

**Andres Urrego:** If you want to add 10 people every day to your contact list and send it to them, that's absolutely fine. Again, remember, just stay within the limits, you know, make sure we're not going to spam people. And then, so I'll make it so that you guys can see who has actually been contacted and who hasn't.

**Megan:** Mhm.

**Andres Urrego:** And then as you're selecting them, make sure that it is people that you want to email, right? If there are people on there that you know you shouldn't, because maybe there are, again, I haven't extracted the actual patients from this. So I would be careful on adding all 5,000 of them.

**Megan:** Mhm.

**Andres Urrego:** Okay, so we'll take care of that today of extracting the ones that haven't that are not patients.

**Megan:** Is there, I see a few in there that were previous patients. I don't know what a good tag would be for that, but.

**Andres Urrego:** Ohh.

**Megan:** Just to change them to like newly to like.

**Andres Urrego:** Oh yeah, so for example, let's say it's Jennifer, so let's look at options.

**Megan:** Yeah.

**Andres Urrego:** Yeah, we could add on the pipeline stage, we could call it.

**Andres Urrego:** Or maybe it could be part of the lead source or status. It could be previous client. We could add it somewhere on here, so it's like previous client, so that you can tag them that way. And then if you ever want to select a group of previous clients, you know, you send them a direct email that way.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** You.

**Megan:** Yeah.

**Megan:** Yeah, that would be great, yeah.

**Andres Urrego:** OK, perfect. Awesome. I love it.

**Megan:** And then that would, would that allow us to send them a different type of customized email then? Yeah. Okay. Okay.

**Andres Urrego:** Oh, 100%. When it comes to your emails, you can create any type of email. You know, that's the beauty of this is there's no templates. It's all free flow. You're going to think of something you want to send people and you create it. See, it's complete flexibility for you as a business to from now on not have to do.

**Megan:** Okay, yeah.

**Andres Urrego:** Oh, I have to create an entire campaign for 5,000 people with just these three emails. Now, you know what? I'm going to do 10 a day. And honestly, that's what I would do with a tool like this. I'll do 10 a day, and then I send them a different one until I figure out which one works. Because sometimes, you know, we spend, yeah, sometimes we spend 1000 emails.

**Megan:** And.

**Megan:** Okay.

**Andres Urrego:** And, on the same email, and then we now we know we now we now burned out that opportunity to reach out to that 1000 customers, and we didn't realize that maybe everything went to spam or maybe not, you know, they weren't reading any of them, so that it's important right that that that we that we test, and that's what this gives you that ability to do that.

**Megan:** Okay. And of that 5000, you may have already gone over this, but I just want to ask, because I'm not familiar with the system, of that 5000, at any time, if she wanted to run, you know, a different type of campaign, would we be able to cluster like prior patients, current patients, future patients we want to target?

**Andres Urrego:** Then, um, you want...

**Megan:** So it's not always just the 5,000? Yes. Okay.

**Andres Urrego:** Yeah, so we...

**Andres Urrego:** Right, so right now I'm adding, so basically once I extract those patients or the patient list, I'll be able to keep like your cold. So these are going to be completely cold, people we haven't talked to in the past. And then you have your clients or previous clients, right? So you have those boxes. So then whenever you say,

**Andres Urrego:** Okay, I want an email a segment. You're going to be able to select from here a segment of, okay, this is my previous client segment.

**Megan:** We really set up, set like a male campaign, just yeah, yeah, yeah, you know, yeah, hormone for that women campaign. OK, awesome, that'll be great.

**Andres Urrego:** Yeah, so then when you say like, for example, if you say these are my previous line segment, you select those lines that are in that segment, and then it sends that email to all those lines, or however many emails you want to send.

**Megan:** There's an.

**Megan:** So there's another segment or category that I don't know what we should call it, but it would be people who came in for the initial consultation and then and then never came back. So I don't know what to call them, but.

**Andres Urrego:** Okay.

**Andres Urrego:** Okay, good.

**Andres Urrego:** How do you have them today in your, like, how do you have them?

**Megan:** They're just...

**Megan:** We don't have a tag or name for them right now, but like I see only.

**Andres Urrego:** Okay.

**Andres Urrego:** I mean, because if you mark in your list, if there's any way to mark, and then we can actually just import them the right way so that you don't have to do the cleanup now inside of here. So I would honestly suggest.

**Megan:** Yeah.

**Megan:** have to because I mean all those contacts and keep, they're not.

**Andres Urrego:** Yeah.

**Andres Urrego:** No, no, no, but that's what I mean. Like, like I can extract, or we can extract clients from non-clients, but then in your client list, you probably also have your no longer client, or maybe they didn't continue to come. That's where we need to, you know, make it pretty in your.

**Megan:** Mhm.

**Megan:** Go home.

**Andres Urrego:** Client list and it's and previous clients, or if everything else is a cold, you know, they're cold and they get moved, you know, through your pipeline as you contact them or they tell you to stop, but everything that already exists, we need to, we need to make everything that's already exists that's clean in your, you know, in your client base, that we need to make sure we bring it in.

**Megan:** Yeah.

**Megan:** Hey, man.

**Andres Urrego:** very clean, you know, so that you have this looking great from the beginning, your segments are clean, you can send your targeted emails to everyone.

**Megan:** Well, what I'm saying is...

**Andres Urrego:** Yeah.

**Megan:** I don't know if we, that hasn't been done. So like in Charm, there's the referral source that we put in. When they make an appointment, we know how they found us. But

**Andres Urrego:** Hey.

**Megan:** Then if they come in for initial consultation and for whatever reason they don't convert, then we don't have anything in place right now to.

**Megan:** Label or tag or...

**Megan:** There's just nothing. So Michelle mentioned maybe like IC only, that would be a good category or tag for them if that for those people. But I'm going to have to go through and just because I know the names and I'm just going to have to go through and do it.

**Andres Urrego:** Yeah.

**Andres Urrego:** Of course, yeah.

**Andres Urrego:** Yeah, and there's probably a way you can filter inside of your the other CRM to see people who only have done an initial consultation and then you can, there might be an option to edit those, tag them, right, as like, okay, I see only. No, the other one where you have your.

**Megan:** You talking about keep?

**Andres Urrego:** Because I assume you, if they did an initial consultation, that are they on keep or are they in the medical system?

**Megan:** Well, there, some of them are in both. So the last full export from Charm and to keep was probably in.

**Megan:** I don't know if it was April or September, but...

**Megan:** I don't know, we'd have to look at charm and see if we can, when we export the list, if they're tagged with anything, because it just, the only thing it asks for in charm is the referral source. So, and we can either, it's either an active or inactive patient. So there's no way that I know of.

**Andres Urrego:** Right.

**Megan:** To say, like, to to label that in charm or track it in charm, but in keep.

**Andres Urrego:** Right, but it's active and then inactive. Okay, so then we would add it. Okay, so as long as patience is clean and we have active and inactive, then we can tag inside of your platform, your new platform, then we can build it so that you can tag.

**Megan:** Yes.

**Andres Urrego:** so that you can tag those as IC only, for example, like that, then, you know, patients and non-patients.

**Megan:** Well, some of them are never came in and some of them are massage clients. Like we used to have a...

**Andres Urrego:** Ohh, the initial consultations is the is the document online.

**Megan:** Yeah, we had a massage therapist for a couple of years that used Charm to schedule. So we have some clients in there that are only massage therapy and never came in. Or we have some that are like only ear acupuncture or maybe they had an injection or something like that. So.

**Andres Urrego:** Right in.

**Megan:** And.

**Megan:** Yeah, I think if we just exported the list of all active and inactive patients,

**Megan:** And.

**Megan:** And then any in any inactive patients names that I am not familiar with, we can look and see if they ever came in because sometimes.

**Megan:** I had an applicant for this position who came in for initial consultation and I didn't remember her name. So we could look at, we could, I mean, it's going to be manual labor on my end. And that's okay because it just.

**Andres Urrego:** And that's what I want to do before we move those over. Does that make sense? Like, so that is, yeah, okay. And so I can work.

**Megan:** Sure, yeah.

**Megan:** We'll have to do it in heat.

**Andres Urrego:** Right, I'll move. So for now, what I'll do is I'll move what's patient and non-patient, right? I'll look, I'll extract them, kind of keep whatever's really cold on one side, and then you can work on your actual patient data so that whenever you move it over, it comes over to like patient or this was just initial consultation.

**Andres Urrego:** I mean, we're not probably going to catch them all, honestly. Some people that are...

**Megan:** Well, yeah.

**Megan:** What we can do is.

**Andres Urrego:** Right.

**Megan:** I think, I'm pretty sure in Charm we can export a list of active patients. And I know those are updated. So those can be imported here as active. And then beyond that, I'll just have to, we'll have to import them then again to keep and I'll have to go through.

**Andres Urrego:** Okay.

**Megan:** Because I don't think they're tagged with, I mean, with anything. I can look on the day that we imported all the, all of Jill's contacts and that, because that was all done on one day and I can.

**Andres Urrego:** Okay.

**Andres Urrego:** Oh, that's interesting. That's a good idea. Yeah, yeah, yeah.

**Megan:** Just probably tag all those with one.

**Andres Urrego:** Yes, okay, I understand. Okay, that's good. That's actually a really good idea, because then everything else, you know, you've kind of had some contact with, or at least the majority, and that point, you know, I mean, we...

**Megan:** Yeah.

**Andres Urrego:** Yeah, I mean, I think it's okay.

**Megan:** Yeah.

**Megan:** Yeah, there'll still be some massage clients on there from, you know, 2018 or whatever, but...

**Andres Urrego:** That's okay. You know, I mean, again, remember open rates, we know we got to shoot for 10%, you know, 5%, 3% sometimes, you know, so it.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** Eat breakfast.

**Andres Urrego:** Sometimes we worry about the five or six people, but we really got, we got to worry about the almost four or 5000, you know, leads that are out there. Because the goal is, can we convert 2 a month? Can we convert 3 a month? Can we, because that's, you know, that at that point, you know, everything's paying for itself, you know, like, okay, two, three clients a month or, you know, 5, 10 clients, 20 clients the first year. I mean, that's

**Megan:** Yeah.

**Megan:** Singh.

**Megan:** Yeah.

**Andres Urrego:** massive, so that this gives you an opportunity to do it right, to make sure that it feels personable, small, you know, local. So yeah, yeah. So for example, here's some ideas for you guys. So for clients that if you don't want to just send like spammy emails and stuff like that, you can do, you know, creating the newsletter every month. So you don't have to now schedule your newsletter in advance 12 months.

**Megan:** Yeah.

**Andres Urrego:** You can kind of go, you know, based on recent data or anything you wanted to do. So, for example, if we did, let's create a newsletter for Mother's Day in May.

**Andres Urrego:** With A twenty-five percent offer.

**Andres Urrego:** Or.

**Andres Urrego:** new clients or something. I mean, this obviously just making stuff up, but for new clients.

**Megan:** Yeah.

**Megan:** That's a pretty heavy discount.

**Andres Urrego:** I know.

**Andres Urrego:** OK, but still, it's still a mock email, so...

**Megan:** I know.

**Megan:** I don't even know what we can do for Mother's Day.

**Andres Urrego:** Thinking about bombs.

**Andres Urrego:** Okay.

**Megan:** The.

**Megan:** And square.

**Megan:** But they're not tagged with anything.

**Megan:** We could start, I think we could put a, yeah, I don't know how to do that in Square, but we could figure it out, yeah, if you wanted to, that's what I was saying, right? It is an idea, only if they're local, you know, I mean, I guess we could put them on the gut health stuff, but...

**Megan:** Well, that's not true. If they're in Texas, I can tell them. Because the guy that bought the testosterone, was that what he bought? DHEA, yeah. He, on his way out, he's like, if this works, if it doesn't work, I'd be interested. I should have told you that yesterday. He's like, you know, we'll see if there's maybe more shaking. I'm like, yeah.

**Megan:** Well, I wonder what he means by works. I... We have his phone number. I didn't know. I don't know how to talk to him about that. We can talk about that and you can give him a call. So, yeah. Okay.

**Megan:** I'm trying to remember his name. But that made me think like, oh, that, because yesterday is like you booked that appointment.

**Megan:** the woman, right? So I'm like, maybe they're here. If, you know, maybe we have a son. I don't know. I just started thinking like, okay, that's a target. Yeah. I mean, yeah. I just know if you, if you can target them, like if that would be a conflict, but.

**Andres Urrego:** Hey.

**Megan:** If they are, I mean, how many of them are looking at the? They are there, they all do, and so, yep.

**Megan:** Just got me thinking. Yeah.

**Andres Urrego:** So what do you think about emails like this, right? So this is what I think of, like guided in the right direction. If you want a newsletter like email, you ask it for a newsletter. If you want an educational email, an informational email, again, tailor it as much as you can, guys. Have fun with it because that's the entire point for this is to really go and try as many as you possibly can until they work. But you know,

**Andres Urrego:** you know, again, continue to make sure that it sounds like you, that it is your voice, that it is your, that it feels like FitLogic. Again, from the back end, you know, we guide it based on the research and we guide it based on your brand. But again, it makes sure that you get creative when it comes to, okay, you know what, this one should be a newsletter. Or every month you have a little reminder and you come here

**Megan:** Yeah.

**Andres Urrego:** And you saw how fast that was. It was just literally 4, 5, 10 words. And you know, we got our newsletter for the month. And then you pick all females or all moms and send it out. Or you send it to everyone, honestly, because it's a newsletter and you're just letting them know, hey, by the way, Mother's Day.

**Megan:** Yeah.

**Megan:** Yeah.

**Andres Urrego:** But...

**Andres Urrego:** questions so far. I am taking notes or, well, I am have the transcript on, so I am taking notes of all the feedback, so I will make sure that I work on that.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** We have access to this now. Yeah, I think so. That's the thing we have to, we have to just go in and and see what we can do, get our hands on.

**Andres Urrego:** Yeah.

**Andres Urrego:** Yeah, and I'll keep it, I'll keep it. Here's the only thing, make sure that whenever you guys are testing, I'll send you guys access today, a little list of like what you need, da da da. Just make sure when you're testing, create yourselves as new contacts. Don't test yet with any existing contacts. And yeah.

**Megan:** Yeah.

**Megan:** Yeah.

**Andres Urrego:** Perfect, okay, good. And...

**Andres Urrego:** You can add Michelle from here.

**Andres Urrego:** Okay.

**Megan:** Mhm.

**Megan:** Oh, Etter.

**Megan:** Oh, in the settings? Add staff, okay.

**Andres Urrego:** Yeah, and then campaigns, integrations, integrations, you are connected to your Gmail already. So...

**Andres Urrego:** In your inbox, you'll see this.

**Megan:** Wonderful.

**Andres Urrego:** And you'll be able to save from contacts once those contacts start emailing you back, if they're going to start showing back on, they're going to start showing on here as contacts inside of this platform. That's how we're keeping it separate from your regular email.

**Megan:** Okay.

**Megan:** So you can just check email right in there? So we can just check our email right from in here.

**Andres Urrego:** Yeah, there you go.

**Andres Urrego:** That is correct.

**Megan:** my next question. Awesome. Another question that I have, Andres, is, will this link to the website? So when someone requests, like completes a quiz or on the website or, you know, okay.

**Andres Urrego:** Yes.

**Andres Urrego:** We are going to do that once the website is done, correct, Megan? Once the website is done. Yeah, so once the website is completed and deployed, then we'll be able to connect to that. And then I also want to, I told Megan I would help out with making sure that we can create a way for her to update her Q&As.

**Megan:** Yeah.

**Andres Urrego:** you know, if you wanted to, or add more Q&As. Or we could add a separate page where people just ask questions and then they get automatically, yeah, it's a little chat bot basically. So in here, and I still have it right here. So these are all, you know, FAQs.

**Megan:** That's up.

**Megan:** Mhm.

**Andres Urrego:** that are actually industry SEO driven FAQs. So we will create a chat that whenever people come to the chat, they can ask questions. And then from there, it answers them from here, right? Basically. So you can add as many as you want and then the answers will always be there.

**Megan:** Mhm.

**Andres Urrego:** You know, when the conversation is ready, it will move, it will move the conversation to the sale or, you know, always with a call to action to talk to Megan or call or email or set an appointment or fill out a form.

**Megan:** Perfect. And then that will be...

**Megan:** We talked about also if they are not getting, if they're not getting the answer, they want to schedule or call, have a time like they could schedule a conversation with you. Great. Then we can figure out how to do that.

**Andres Urrego:** All right.

**Andres Urrego:** All right.

**Andres Urrego:** Absolutely.

**Megan:** And we can even use the square calendar. We can, so it can be.

**Megan:** I mean, we could use them.

**Andres Urrego:** Yeah, you just add a link. So we'll make it so that you can have a link that is hard-coded. So whenever it gets to the conversation, they select book a call, then it immediately takes them to the link, they book the call, done.

**Megan:** Yeah.

**Megan:** Perfect. I love it.

**Andres Urrego:** You can add FAQs, right? You're going to be able to add them, just simply add them. You know, what others will charge you $10 for FAQ. You're just going to be able to add them for free. So, yeah, yeah, I mean, what questions you guys have so far? I'll send you this over today.

**Megan:** Mhm.

**Andres Urrego:** You know, you have access to Moil, so I added it on there so that you can just get to it straight from there with one click. You do have a license on there already. Your referrals is going to be here. You can add a referral link. We'll have to add this to like, we'll have to figure out how this is going to work, right? You can create a referrer name now, and then you can give him a link.

**Megan:** Thank you.

**Andres Urrego:** that they can share so that when someone comes and buys from you, you can use that at checkout or something so that you can track.

**Megan:** Yeah.

**Megan:** It would be like.

**Megan:** if they buy it, if they sign up, not just for the initial consultation.

**Andres Urrego:** Ohh, 100% right, so...

**Andres Urrego:** Yeah, so whenever someone crimes and they buy, then they give you this, they can literally just give you the referral code or they can tell you, well, Andres referred me. You copy the referral code, you add it, and then that way you keep tracking them and then you know who you're going to pay out for the referrals and who not.

**Megan:** Mhm.

**Megan:** Mhm.

**Megan:** Um...

**Megan:** The only, I have to go in about 10 minutes, but I was wondering, can you run through the social media? I started doing that, but I don't know if it was ready to go.

**Andres Urrego:** Yeah, me too.

**Andres Urrego:** Uh, did you, were you able to complete the...

**Andres Urrego:** Were you able to go? Oh yeah, you have the business plan and then you have...

**Andres Urrego:** All right, let me do that one.

**Andres Urrego:** I.

**Megan:** Ouch. Is it just me or just the music come in and out?

**Megan:** Yeah, some of the volume is different depending on the song or at all. OK, then it's not just me. Yeah.

**Andres Urrego:** ****.

**Andres Urrego:** All right, let me show you. Sorry, that was my bad.

**Andres Urrego:** So...

**Megan:** It's like that.

**Andres Urrego:** Okay, so where are you? So you created your business plan, you have it, that's done.

**Megan:** Is this mine?

**Andres Urrego:** And no, this is mine. I can't access yours, no.

**Megan:** Oh.

**Megan:** Do you want me to pull it up and share my screen?

**Andres Urrego:** Yeah, absolutely.

**Megan:** That.

**Andres Urrego:** But, but I guess my question is, have you...

**Andres Urrego:** So...

**Andres Urrego:** You have the plan, so have you started this part right here?

**Megan:** I started.

**Andres Urrego:** Because if not, I can show you exactly how to do it.

**Megan:** I, oh well, let me, I'll show you what I started.

**Andres Urrego:** Perfect. Let me stop.

**Andres Urrego:** Perfect.

**Megan:** Yeah.

**Megan:** Okay, here's this where I am.

**Andres Urrego:** Beauty, okay, okay, perfect.

**Megan:** But I didn't, I was a little nervous to like do it all because I didn't know what I was doing.

**Andres Urrego:** Okay, so let's try something. Go ahead and close out of this little guy. And let's go look at your brand. No, no, no, I mean, I mean this little pop-up right here.

**Megan:** What pop up?

**Andres Urrego:** The one that's in the middle of says choose your content type.

**Megan:** Oh.

**Andres Urrego:** Yeah, okay, and then go ahead and click on Brand DNA. And then let's see, where you, did you add anything on here yet, your logos or?

**Megan:** I don't think so. I don't remember. It was more than a day ago, so.

**Andres Urrego:** Okay, go ahead and scroll down a little bit, please. All right, so yeah, there is a logo. Are these your colors? We need to...

**Megan:** Oh, I own my logo, okay.

**Megan:** But I didn't know how to do the colors because I don't know the...

**Andres Urrego:** Just like, what?

**Andres Urrego:** Oh, you don't have them?

**Megan:** I've got him. Oh, Sean has him.

**Andres Urrego:** Okay, perfect. Okay, so let me show you. So click on, click on the actual one of the colors.

**Andres Urrego:** There you go. Or click on the box where it says primary.

**Andres Urrego:** On the actual, yeah, the color code. Okay, you can type the color code on there too.

**Megan:** Down.

**Megan:** She's getting them.

**Andres Urrego:** You did.

**Megan:** This weekend.

**Megan:** Where do I say that? She's trying to find it. I'm trying to find it, yeah.

**Andres Urrego:** Okay.

**Andres Urrego:** It's more like that, yeah, like, yeah, I think that's closer to it, yeah.

**Megan:** Value is.

**Megan:** You.

**Megan:** Yes.

**Megan:** As close as I can get.

**Megan:** And what do I need to put anything?

**Andres Urrego:** Well, but you actually have white now, your secondary, yeah, yeah, we need to look at, yeah, I think your third color is white.

**Megan:** Yeah.

**Megan:** I think I might have left it at home. I was working on something. I can't find it. I think I have it in my home notebook. But yeah, I do have the hex code and then the RGB that I was able to pull for the logo. So I have it. I just don't have it in my phone. I have it on a notebook at home. Sorry. Okay. I think this will be good.

**Andres Urrego:** Haha.

**Andres Urrego:** Perfect.

**Andres Urrego:** Very good, OK.

**Megan:** Fine, for I mean, can we we can can we come back in and change it?

**Andres Urrego:** Yeah, so let's try it. We'll just say brand colors. Absolutely.

**Megan:** Okay.

**Megan:** That's OK.

**Andres Urrego:** Okay, so let's scroll down a little bit more.

**Andres Urrego:** Beautiful. Okay, you don't need anything from here. Just go ahead and click on go back, go ahead and click that close up the DNA or just go click right there. We're gonna go to the to the calendar.

**Megan:** I.

**Andres Urrego:** All right, perfect. All right, so you can go ahead and close the guides, use on your guide today.

**Andres Urrego:** And let's go ahead and click on February 28th since that was, oh, okay. So this got started. It says February for some reason. So I wonder if the date, yeah, if the date was okay.

**Megan:** Yeah, that's weird.

**Megan:** I probably clicked on the wrong date. It's probably what happened because it's...

**Andres Urrego:** And that's okay, but if it doesn't say February, you can still use it. So that's not a massive problem. Or I can have the team probably maybe reset it. But let's practice first. So if you go ahead and click on God Health Reset.

**Megan:** Okay.

**Andres Urrego:** Okay, and then we're going to scroll down a little bit. Yeah, you got your, go ahead and scroll down a little bit more. Go ahead and click on the image dimension you want, if you want an Instagram image or a story or for squared. Typically I pick stories. Those are like that size that Facebook likes the most.

**Andres Urrego:** And then you have Squirrel landscape and then just click generate visual, yes. Now if you have any reference images, I'll show you in just a second, but images that you've done in the past, that you've used in the past, and you want to use those as reference because you like some of it, you can actually add them to guide the AI to create them.

**Megan:** Yeah.

**Andres Urrego:** So, you've got you got a first image here for your God. I think this was a God reset on Lucy.

**Andres Urrego:** The quality of the video.

**Andres Urrego:** Okay, so if you click on the T, everything looks blurry, but if you click on the T.

**Megan:** Yeah.

**Andres Urrego:** Yes, perfect. Then here, now if you go click on the text, you can either move the text down, up, you can move the text around. Now if you go down a little bit more, you're going to be able to, on the left side,

**Megan:** One second.

**Andres Urrego:** Yes, so if you go down a little bit, you're going to be able to right here. You can delete, change the text, update it, you know, just.

**Andres Urrego:** Write whatever you want into the image.

**Andres Urrego:** Oh, nice.

**Andres Urrego:** Okay, so then I would even remove if you know where to start. I would just say one call to sort it takes to be to be a noticeable God help reset.

**Andres Urrego:** Makes it a little bit shorter.

**Megan:** What did you say?

**Andres Urrego:** Yeah, and I would just delete everything else after health, you know, keep it punchy. Yeah, I mean, it just go up and then you're going to see it, obviously changes happen live. So it's there, you can go ahead and move it down or again, add it, whatever you want.

**Megan:** Can you change the color, the colors?

**Megan:** I think so, on the left, right below where that is the...

**Andres Urrego:** The colors or the text? Oh yeah, absolutely. So go down a little bit more. There they are. Yeah, you can change colors, you can change backgrounds, you can play with fonts and different fonts. Yeah.

**Megan:** Yeah.

**Megan:** Yeah, yeah.

**Megan:** Ugh.

**Megan:** I don't even know. I'm terrible at this.

**Andres Urrego:** So, I...

**Megan:** I will help you. This looks like fun.

**Megan:** Okay, well I think white was probably the best, but okay.

**Andres Urrego:** Good. I'm glad. You can edit your images. So for example, if you wanted to like, no, I wanted this one to be of a person. I like that image, of course, but if you wanted to do, I want it to be of a person, then you can click where it says edit image and you can type whatever your request is and then it will help you create that image next. Now, see where it says reference images below?

**Megan:** Just.

**Andres Urrego:** That's where he would... Oh, what did you write?

**Megan:** I just wrote happy gut. I want to see what it shows.

**Andres Urrego:** Okay, but you're going to have to be able to guide it a little bit better than that, okay? So like, just tell it exactly what you want. So like, okay, I want a person that, you know, or an image of a happy god. I don't think that created a happy god.

**Megan:** Okay.

**Megan:** And.

**Andres Urrego:** or change the background, add my colors.

**Megan:** generate a person.

**Andres Urrego:** And we'll test and see if the brand callers are coming through, since we did create the calendar first, but I'll look at that.

**Megan:** It's happening.

**Megan:** Is that better?

**Andres Urrego:** I can't read it because everything's blurry. What does this say?

**Megan:** Yeah, it says image of a person who is happy and feels relief.

**Andres Urrego:** Okay, all right, yeah, let's try it. It should work.

**Andres Urrego:** No, we didn't. Okay. All right, so let me make that note.

**Megan:** Mm.

**Megan:** Oh wait, well, I think it might be working slowly. There's like, do you see the person, the face on the bottom? There's a face and then the hand is above the face.

**Andres Urrego:** No.

**Andres Urrego:** Yeah.

**Megan:** work out the, work out some prompts. Can you see that? Work on prompts.

**Andres Urrego:** Interesting. No, I don't think it, I'm not sure, I'll look on my end too, but I don't think it's the prompt. I think what's happening is trying to edit that specific image and it didn't let you create a new image. So let me see. Yeah, I think that's exactly what it is. So it's really trying to force what you're asking for.

**Megan:** Mm.

**Andres Urrego:** as part of that image.

**Megan:** I've gotta get going.

**Andres Urrego:** Let me see. All right, sounds good. But does that answer some of those questions? Just play around with it again. You have the entire calendar to create these images. Let's just go up a little bit real quick. I want to show you something. Once you find the days where you really love the image, you really love the concept, can you go up a little bit more?

**Andres Urrego:** See the little camera, I can't see it, but if you see the little camera on the post on the days, there's like a little camera logo or camera icon. Go ahead and click on it. Okay, go ahead and turn that one off because you probably don't want an image of that, a video of that image. But you can, what you do is you select the one that you love and then you click on the video, go ahead and

**Megan:** Yeah.

**Megan:** Mm.

**Andres Urrego:** So let's just test with that one just to test. It's not going to automatically create it, but on the first one, go ahead and click on the first one on the first day. And then go scroll down. You get six of those, six or seven. Scroll down, scroll down, and then you can generate motion from that image. Now, you could probably do it from the salad on the first one, and it will add audio and

**Megan:** No.

**Andres Urrego:** And it would add, you know, it would add motion to it. So it would actually do a good job at creating a good video from it.

**Megan:** I go. Okay, do you want me to keep going? I'm going to let Michelle take over. I'm going to, I got to go. Okay.

**Andres Urrego:** All right.

**Andres Urrego:** Perfect. All right, Michelle, so right here, and we're almost done, but you, once you have the image that you love.

**Megan:** Okay.

**Megan:** Mhm.

**Andres Urrego:** And you want to create a video from, you see how in the bottom you have your three versions.

**Megan:** Yes.

**Andres Urrego:** Okay, so you would just basically use the version that you like the best, and then you click on render to premium video. And then that will create, if it's Gemini, you see how it says Gemini video? If you use the Gemini video 3.1, it does 8 seconds. If you do Grog, it does 10 seconds. So test them out, test out the quality.

**Megan:** Okay.

**Andres Urrego:** 10 to 12 seconds, yeah. So check out the quality, which one you love most, and then that way you can continue to use it.

**Megan:** Can I click on this now just to see what it looks like?

**Andres Urrego:** I picked, yeah, let's go up real quick. So let's go up real quick and do another day. Let's create an image for another day. That way you can see a little bit better. So there's pick like perimenopause, hormone shifts. Go ahead and click on that one. And then...

**Megan:** Okay.

**Andres Urrego:** Yeah, go ahead and click on that one and then if you want to, yeah, and then go ahead and click on the day so it takes you down.

**Andres Urrego:** No, you gotta click on the actual on the actual day, um, so...

**Megan:** Oh, I see. So I'll click on this.

**Andres Urrego:** Perfect.

**Megan:** Did it register?

**Andres Urrego:** Go ahead and click on it, and it should take you down. It selects it.

**Megan:** I think it's still on the gut health.

**Andres Urrego:** No, it definitely, yes, so it should change once you click on it.

**Andres Urrego:** There you go. Okay, perfect. Okay, fantastic. So now let's scroll down and then we're going to select again the stories layout just for this test.

**Andres Urrego:** First thing you do is you pick the image that I mentioned. Good.

**Andres Urrego:** Perfect. If we scroll down a little bit and then we just click generate AI visual.

**Andres Urrego:** Yeah.

**Andres Urrego:** It auto loads the hook on it, so you can remove it. So if you click on T, you're going to click on the T to edit the tags.

**Megan:** Okay.

**Megan:** Okay, and I can move it down.

**Andres Urrego:** And then you can move it down. Yeah, you can move it down. And you can change the length, right? So you obviously, if you want to make it easier, I mean, shorter, you can definitely do that. Scroll down a little bit on the left side on that team.

**Andres Urrego:** On the left side, please.

**Megan:** Ohh, sorry.

**Andres Urrego:** No, no, that's okay. That's okay. And then for your image on the video, we don't, we don't, typically you don't want the text on there, but.

**Andres Urrego:** If you scroll down a little bit more on...

**Megan:** Ohh, do you want me to remove it? Do you want me to remove the text? OK.

**Andres Urrego:** No, no, no, no, no. The text is not going to come up in the video. It will show up for your image. So now you get 2 assets. You get the image and the video. But yeah, you can shorten your text right here on the left side at the bottom. You know, you can remove the text, you can change it, replace it. Do you see that little box right there?

**Megan:** These over here.

**Andres Urrego:** For the text on the left, no, if you go scroll down a little bit more.

**Megan:** Oh, here we go, layer text, right?

**Andres Urrego:** Perfect, yes, that's it.

**Megan:** This box.

**Andres Urrego:** Yeah, and then you have font and colors. Yeah, but anyway, so if you want to keep it that long, you can. If you want to make it shorter, you can. But then to do the video, let's say we like this image of this specific person right now. So I think we can actually just click on generate a video and then and see how that video goes.

**Megan:** Okay.

**Andres Urrego:** If you scroll up on the right.

**Andres Urrego:** Yeah, perfect. And then we're going to click at the bottom, we're going to click where it says generate video.

**Megan:** Okay.

**Andres Urrego:** And if go ahead and click rock, for example, on this one.

**Megan:** And then render to premium motion video.

**Andres Urrego:** Yes, please.

**Megan:** Oh, this is exciting.

**Andres Urrego:** Yay, good. And look, we're pushing updates every single week. So I think you guys will see them coming live. You guys will see those changes week after week. Well, you can't create all 30 days of content all in one sitting. You know, I recommend people just do it week after week because you're honestly going to see the changes. You're going to see the updates, the improvements.

**Andres Urrego:** Okay, can you scroll up a little bit on the right and then Desco click play? Yes, perfect.

**Andres Urrego:** I can't hear it.

**Andres Urrego:** Is there is there sound in it?

**Megan:** Yes.

**Andres Urrego:** Okay, how did it go? I can't hear anything on the sound.

**Megan:** Oh, okay. I turned the volume all the way up for you, but...

**Andres Urrego:** I think it's just the way.

**Andres Urrego:** Let me see, this just might be the way that it's sharing, sharing without audio.

**Megan:** Okay, I'm trying to stop it. There we go. So question, who is running social media? Megan? So like you've, just so I understand, because I haven't been in your conversations. So you've provided the Moil 360. So when you said we're going to be running this once a week, does that mean Megan is generating the content in here?

**Megan:** Here, or you are.

**Andres Urrego:** Oh yeah, absolutely. You, our, no, our company does.

**Andres Urrego:** the access to the platform. You guys do your social media.

**Megan:** Okay, I see. That's what I thought, but I just wanted to make sure when you were saying we, I just want to make sure. Okay.

**Andres Urrego:** I.

**Andres Urrego:** Okay, okay, perfect. Yeah, no, no, no, yeah, you guys have the access to the platform. Again, it gives you the 30 days of, you know, and it takes about 3:00 to 4:00 minutes to create the 30 days for you. And then it helps you or guides you week after week to create the content you need. How was that video? How was the audio? I couldn't hear it, so I'm not sure.

**Megan:** How often do you say that?

**Megan:** I thought it was great. I thought it was good.

**Andres Urrego:** Okay, I love it. I love it. Good.

**Megan:** Yep, it was running on repeat, so she kept saying the same thing over and over again until I hit pause.

**Andres Urrego:** Oh yes, yes, yes. Once it's done, okay. Interesting.

**Megan:** And I think that's fine. You know, I think that's okay. I wanted to ask you how, yeah, how often do you suggest posting? You said weekly, right?

**Andres Urrego:** Good. Well, that's exciting. So, yeah, go ahead.

**Andres Urrego:** Well, you guys have 30 days, so I mean daily, right? Yeah. Oh, absolutely. You guys have, that's where we create the full 30-day calendar so you can post daily. And then on days where you get the image and the video, I would post twice.

**Megan:** Daily. That's what I thought. Yeah.

**Megan:** Mhm.

**Megan:** Okay, that's what I was thinking, but I just wanted to make sure I didn't misunderstand that about the weekly thing. Okay.

**Andres Urrego:** If...

**Andres Urrego:** No, no, no, you're good. You're good. And then you can regenerate. So let me, yeah, so if you scroll up a little bit, for example, the days you're going to do image and video, I would regenerate the text so that you don't use, go left on the left side, please go scroll up a little bit on the left side. Yes, there we go. Okay, right here. So

**Andres Urrego:** You can click rewrite on right next to copy post. Oh, and by the way, Michelle, so once you say, let's, I love that video, I'm ready. So you click on download, you download your video, you download your image, then you're going to click right here on copy post. And just like that, you're going to take it over to Facebook and.

**Megan:** Yeah.

**Megan:** Mhm.

**Andres Urrego:** an Instagram or whatever and then just click paste. It's going to paste everything, the caption, the hook, the hashtags. So you just paste it and then insert the image or video that you just downloaded. Now if you want.

**Megan:** Cat.

**Megan:** Can we practice that? Can I do that in Facebook right now? Copy post to Facebook.

**Andres Urrego:** Absolutely, yeah, yeah.

**Megan:** Okay, let's try that. I just want to make sure I understand so I can teach Megan too. You know, I don't want to...

**Andres Urrego:** Absolutely, and then download the video right here, for example. So scroll down on the right side and download the video.

**Megan:** Not know what to do.

**Andres Urrego:** If you scroll down on the little box on the right side, yeah, but...

**Megan:** I see it there.

**Andres Urrego:** Yeah, there we go. So there should be a download button right below the video.

**Andres Urrego:** There we go. So we're going to click download. Perfect.

**Megan:** Ah, here it is. So just because it's there, it doesn't mean it's downloaded.

**Andres Urrego:** No, no, because I mean, yeah, it doesn't automatically download it to your computer because, you know, we don't want to, we want you to download it once you, once you want it, once you're ready. And then now you can go to Facebook. You already at the top, did you already copy the caption? Like did you, did you click on copy post?

**Megan:** I clicked on copy post, yes.

**Andres Urrego:** Perfect. So let's go to Facebook and now you can paste it and then insert the video.

**Megan:** Where do I pay steps? Where?

**Andres Urrego:** Ohh, you go to Facebook.

**Megan:** Oh, you're saying like the Facebook tab here, right here?

**Andres Urrego:** No, like on Facebook, inside of Facebook, you just...

**Megan:** Oh, I see.

**Megan:** I don't want to pull up her Facebook, but...

**Andres Urrego:** Oh, okay, but okay, so it will be like the fit logic one, but yeah, so it will be like copy and then just...

**Megan:** Oh, okay, so she does have a FitLogic one? Oh, yeah, I'm on it.

**Andres Urrego:** Ohh, I assume so, yeah, yeah.

**Megan:** Yeah, I'm on it, so I bet she's got that. I just didn't want to pull up her personal one, you know.

**Andres Urrego:** That makes sense.

**Megan:** But yeah.

**Andres Urrego:** And you can switch it over here on the top right. Yeah, there you go.

**Megan:** Okay.

**Andres Urrego:** So yeah, let's go ahead and post like if you're doing a new post.

**Andres Urrego:** Scroll down.

**Andres Urrego:** Yeah, we're gonna do...

**Andres Urrego:** Oh, you need to switch to fit logic. Yeah, so switching to fit logic to manage and start. It says sweet right here. No, it says switch now right here on the blue.

**Megan:** I think I am.

**Megan:** Oh, I see.

**Andres Urrego:** Perfect, now it's gonna let you post.

**Megan:** Oh, I see, and then I would just...

**Andres Urrego:** Yep, so what's on your mind? Go ahead and if you just click on what's on your mind and you just Control-V to paste.

**Andres Urrego:** Perfect. So now your postage, it's.

**Andres Urrego:** Good, so if you scroll up a little bit, you'll see the rest of the post, and then now you can add the video that it should that be downloaded to your.

**Andres Urrego:** I just click on add photos or videos.

**Andres Urrego:** No, you don't wanna do a live video? No, no live video.

**Megan:** This one?

**Andres Urrego:** Yeah, yeah, yeah.

**Andres Urrego:** And then it downloads, probably.

**Andres Urrego:** Um...

**Andres Urrego:** Did, did you, did you click download on the video?

**Megan:** I did, yeah.

**Andres Urrego:** Okay. Can we go back to that page real quick? If you went ahead and click cancel, let's try that again. I'm not sure where it's downloading to, so we'll take a quick look. All right, scroll down a little bit to the video. Let's find that download button again.

**Megan:** Sure.

**Andres Urrego:** This is true.

**Andres Urrego:** Go ahead and click download.

**Andres Urrego:** Allow.

**Andres Urrego:** Yeah, let's see where it saved it.

**Andres Urrego:** Go ahead and click on it and then let's see. Oh, it is in downloads. Okay, so C360 day two. Okay, let's try and find it that way. It might be the way she has her.

**Andres Urrego:** downloads filtered, but let's see. So if you click on that one, let's try again.

**Andres Urrego:** That's interesting. Okay, you see the little menu here for, okay, yeah, there you go. Maybe that works. There we go. Boom.

**Andres Urrego:** Awesome.

**Megan:** There it is. I'm not going to post it, but I just wanted to go through the process, you know.

**Andres Urrego:** OK.

**Andres Urrego:** Very cool.

**Megan:** Okay.

**Andres Urrego:** Yeah, then once you hang the hat, the hang of it is literally click, click, post, click, click, post, click, click.

**Megan:** Yeah, yeah, OK.

**Andres Urrego:** All right, Michelle, any questions for me?

**Megan:** No, I don't think, oh, I know. We do need to have, for accessibility reasons, we do need, I think it's important that we have closed captioning on our videos. Is that possible? And if so, where do I click to add closed captioning?

**Andres Urrego:** We don't have closed captioning on it, but I think, if I'm not mistaken, Facebook ads them now, or you can add them on Facebook, but let me look into that. But yeah, but right now there is no option for you to add closed captions, but I'll look into that. That's a good feedback.

**Megan:** Ohh.

**Megan:** Okay.

**Megan:** Okay.

**Megan:** Yeah, no, it's just people will, you know, people with disability, hearing disabilities comment that a lot. I see that a lot that they need to have that. But you're right. I think, I think, I don't know about Facebook, but I have seen posts on Instagram where

**Andres Urrego:** OK, perfect.

**Megan:** Because I have a friend that runs a business in Austin, and because of overwhelming customer feedback, she had to figure out a way to make her videos accessible. And so I could reach out to her and ask her how she did that on Instagram. And so I don't know if she had to make...

**Andres Urrego:** Okay.

**Andres Urrego:** Absolutely, yeah.

**Andres Urrego:** Because I believe you can add it, if I'm not mistaken, it can be added inside of.

**Megan:** Yes.

**Megan:** Yeah, I'll need to ask her if Instagram, if there's a way to do that or if she had to maybe purchase something, but I can reach out to her and find out about that.

**Andres Urrego:** Okay.

**Andres Urrego:** Yeah, yeah, we're gonna look into it as well, for sure.

**Megan:** Oh, perfect. Okay. Is she wanting to do things on LinkedIn as well or just Instagram, Facebook?

**Andres Urrego:** I am not sure. It's an option for everyone in case they want it and then they can, you can regenerate the text on each one of those days. So yeah, yeah, yeah.

**Megan:** I see LinkedIn as an option here. Okay, I just wanted to ask.

**Megan:** Yeah, that's excellent. I like that. I use LinkedIn A lot. And so I like that that's an option there. It's just a very different approach. You know what I mean? And so I like that, you know, Facebook, Instagram can be the same, but that you can maybe do it different.

**Andres Urrego:** Okay, good. It is great.

**Andres Urrego:** A 100%.

**Megan:** you know, a very different type of message on LinkedIn. So that, or you can do it the same. So I like that a lot. This is great.

**Andres Urrego:** A 100%, 100%.

**Andres Urrego:** Good. Yay. I love the feedback. I love it. Thank you. And again, always, I'm open, you know, you send me an email, you know, if you have any feedback that you think, you know, we should definitely implement, please share it with us. We try to make sure that we implement changes very quickly, as long as you know that they can be scalable, that help everybody. And I think a lot of the stuff you've mentioned to me does help everybody. So I appreciate it.

**Megan:** Yeah, yeah.

**Megan:** Oh, good. Where is it that, I know I have those, I was able to get the RGB and the HEX number. So where is it that when I get those numbers from home, where do I change that? All the way up, okay.

**Andres Urrego:** Yeah, so let's go all the way up. Yeah, let's go all the way up to the top. And then you're gonna, oh, actually, yeah, up here, you're gonna click on go back to, let me just, I can't see your screen, it's really, really, I think it's a network issue on my end probably, but let me tell you.

**Megan:** Okay.

**Andres Urrego:** I'm gonna tell you exactly what you're gonna do.

**Megan:** Is that under replace logo?

**Andres Urrego:** You just need to go back to.

**Andres Urrego:** I'm done.

**Andres Urrego:** back to Hub. So at the top you click Hub and you go back to Hub.

**Megan:** Ohh.

**Andres Urrego:** And then brand DNA and then in here in the brand DNA is where you'll be able to make your updates.

**Megan:** Colors, I'm guessing.

**Andres Urrego:** Correct, colors, logos, if you have older logos that are, you know, clear background, anything you're going to be able to change and upload in here.

**Megan:** Oh, yeah, yeah, yeah.

**Megan:** Oh, perfect. Yeah, I have these. I thought I for sure have put them in my phone, but I was working on it this weekend and I must have just kept them in my notebook. So, oh, that'll be, that'll take two seconds to update. So hub and then, yeah, this is a very user-friendly system.

**Andres Urrego:** Hey, it's all good, not a problem.

**Andres Urrego:** Good, thank you. That makes me very happy. Of course.

**Megan:** Once you understand the terminology, yeah, once you understand the terminology, it makes sense.

**Andres Urrego:** Thank you, thank you. And we're trying to, again, every week try to make it even more user-friendly, you know, something that more and more people can use and have access to. So thank you.

**Megan:** Mhm.

**Andres Urrego:** It.

**Megan:** How is it if this is a thirty-day plan? How do you how are you able to do multiple posts on the same day if there's only one button for each day?

**Andres Urrego:** Well, you can do the video and the image. So on the days that you have video and image, you can do video and image and then do 2 posts. One for the video, one for the image. If you edit an image and you like both, you can use both images for different messaging for that day. So you can regenerate the text.

**Andres Urrego:** You can create new tags, improve the tags, change the tags, and then just literally create a separate post from the same day.

**Andres Urrego:** Yeah.

**Andres Urrego:** K.

**Megan:** Got it. Yep.

**Andres Urrego:** All right, Michelle, I do have to run, but thank you very, very much for your time. I really appreciate you. Anything you need, please, please let me know, okay?

**Megan:** Thank you.

**Megan:** Yes.

**Megan:** Yes, sir. Thank you so much for your time and training as well. Have a good day.

**Andres Urrego:** Fantastic. No, thank you.

**Andres Urrego:** I appreciate you talk to you later. Bye bye.

**Megan:** Bye.

**Megan:** You.