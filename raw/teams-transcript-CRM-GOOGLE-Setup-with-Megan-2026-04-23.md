---
ingested: true
ingested_at: 2026-05-04
---
# Teams Transcript — CRM / Google Setup with Megan

- **Date:** 2026-04-23
- **Time:** 14:15–14:58 CT (19:15–19:58 UTC)
- **Meeting subject:** CRM - GOOGLE Setup with Megan
- **Organizer:** Andres Urrego (Moil)
- **Attendees:**
  - Andres Urrego (Moil, founder)
  - Taiwo Ola Balogun (Moil, developer)
  - Megan Miller (customer — FitLogic Functional Medicine)
  - Michelle (Megan's team, joined briefly near end)
- **Source:** Microsoft Graph `/me/onlineMeetings/{id}/transcripts/{id}/content` (VTT)
- **Transcript duration captured:** ~40 minutes

## Context

Working session to finish wiring Megan's standalone Moil-built CRM so it can be handed off from Moil's environment to her own. Goal: set up Megan-owned Google Cloud OAuth, GitHub, Supabase, and Resend accounts so Taiwo can deploy the CRM to `fitlogicfunctionalmedicine.com/crm` on her GoDaddy. Also a secondary thread on Megan's website agency dispute (30-page SEO build) and a brief catch-up on Moil 360 being back online.

## Key decisions

- **CRM will be deployed to `fitlogicfunctionalmedicine.com/crm`** on Megan's GoDaddy domain. Vercel will host the site; Supabase will host her contacts database. Both free tiers — no cost to Megan.
- **OAuth scopes finalized in Google Cloud Console** for Megan's project: Gmail `send`, Gmail `readonly`, Gmail `compose`, Calendar `readonly`. Authorized redirect URIs will hold multiple entries (local / staging / production) so the same client works across environments.
- **Megan's `hello@` email** is the Gmail account the CRM will authenticate against (same password Michelle already had).
- **GitHub repo will be created under Megan's account** so she owns the code. Taiwo added as collaborator to push.
- **Resend used for outbound email** from the CRM; tied to Megan's GitHub login.
- **Gemini API key to be set up for Megan at deploy time** so she pays her own monthly usage going forward.
- **Next handover meeting: Wed 2026-04-29 at 9:30 AM CT.** Taiwo will join. Goal for that meeting is the full walkthrough with Megan so she can start sending CRM emails from her side.
- **Go-live target: Monday 2026-04-28** — Moil tests through the weekend, Megan starts sending real emails Monday or Tuesday.
- **Multi-user (Michelle login) is not shipping yet.** For now Michelle just shares Megan's FitLogic login. Multi-user is planned as a feature for the $75/year tier.
- **Moil 360 / Moil Coach is working again for Megan** (Jacob emailed her this morning confirming the fix).

## Action items

| Owner | Action | Timing |
|---|---|---|
| Taiwo | Test the CRM build tonight after pushing code to the new GitHub repo | Tonight (2026-04-23, evening Nigeria time) |
| Taiwo | Continue migration / deploy work tomorrow morning | 2026-04-24 |
| Andres | Send Megan a status update tomorrow (what's done, what's left, testing plan) | 2026-04-24 |
| Andres | Possibly attend Megan's meeting with the website agency (30-page SEO dispute) | Fri 2026-04-24 (note: Megan said Friday 12:30 — double-check date) at 12:30 PM CT |
| Megan | Start forwarding every meeting invite to Andres so they land on his calendar (she admitted she keeps missing meetings because they only live in her head) | Ongoing |
| Megan | Log into Moil 360, upload her logo + brand colors, and play with image editing — but **do not create the content calendar yet** until everything is uploaded | Before next Wed |
| Andres + Taiwo | Verify testing works through the weekend so Megan can send real emails Monday | Sat–Sun 2026-04-25/26 |
| Everyone | Reconvene for full handover | Wed 2026-04-29, 9:30 AM CT |

## Side threads worth flagging

- **Website agency dispute.** Megan is frustrated with her website vendor. They built a 30-page SEO/AIO-optimized site and included references to "doctor" alongside "health coach" (compliance risk for her). The agency pushed back claiming 30 pages is required to rank in Buda, TX. Megan has a meeting with them Friday at 12:30 PM. Andres offered to attend. Andres' own take in the call: bulk SEO text that no human reads isn't obviously helpful, but the non-negotiable is that **nothing on the site can confuse a patient** about Megan's scope of practice.
- **Connection surfaced:** Michelle (Megan's team member) knows **Daniel D. Mann** ("Firefly"). Andres speaks highly of Daniel — called him "the man" for referrals and connecting people, and said he'd like to pursue a project with him. Michelle said Daniel speaks equally well of Andres. Worth a direct follow-up text from Andres to Daniel.
- **Calendar hygiene.** Megan missed an 11 AM meeting during this call. She's committing to forward all meeting invites to Andres so the Brain can track them. This is a standing behavior change, not a one-off.

## Full transcript (cleaned)

> Timestamps are MM:SS from start of the recorded transcript (~14:16 CT). Speaker tags preserved from the VTT. Minor duplicate/overlap lines collapsed for readability; content not altered.

**[00:53] Andres:** Hello, my brother, how are you? … Can you hear me again? I think you might be muted.

**[02:04] Andres:** No, I can't hear you if you're talking. I can't hear you at all. … Okay, there you are. Ty, so she's about to join. Once she joins, I'll let her know you're on the call. My goal, Ty, was just to really get her to give me the access — I'll set it all up for her, but then have her in the call while we set it up so it doesn't take longer than it needs to.

**[02:38] Andres:** I'll just say, hey, she has a private chat with me, so I'll be like, send me that there while I log in, set everything up, and that way we move a lot faster. … She needs a Resend and a Supabase account too. Then you'll be able to move everything over yourself.

**[03:15] Taiwo:** Yes, I'll move everything over.

**[07:35] Megan:** Thank you. … Hey, so sorry about that. I ran over with my last patient and had to send her a prescription before UPS picked everything up.

**[07:53] Andres:** That's right. I mean, if there's a better time, we can do that another time too.

**[07:57] Megan:** My God, I totally forgot about a meeting I had at 11 today. No, this is fine. We can see what we can get done.

**[08:04] Andres:** Okay, perfect. So a couple of things. I have Taiwo on the call — he's our developer that's working on finalizing the project. We just need to set up three things: one, where your website will be hosted, which will be Vercel. The second is Supabase, where your contacts / own database lives. None of that is going to cost you anything — both are absolutely free. And then we need to connect your platform to your email so we can actually get everything up and running. So I'm going to need the login for that email account. Send it in the private chat so it stays private and you can delete it after we're done.

**[09:33] Andres:** Taiwo, we probably need a GitHub account for her as well, so she can own her code, have it in the repo. We'll create a repo for it. Megan, thank you. Once everything is ready and deployed, we'll move it.

**[09:55] Andres:** I'm going to keep the GitHub in an incognito page. OK.

**[10:07] Andres:** Taiwo, are we connecting the integration to Gmail directly through here?

**[10:12] Taiwo:** Yes, the integration is going to be done here.

**[10:18] Andres:** Perfect. Let me do that right now. I've got the login stuff, and then we'll go directly to creating the other accounts.

**[10:29] Taiwo:** Let's start from the Google Cloud Console.

**[11:04] Megan:** We might have changed the password.

**[11:28] Megan:** That's the last password I have. Do you have a password for the hello email? I can see what Michelle has if it's the same.

**[11:59] Megan:** It's good — that's the same password Michelle has.

**[12:38] Megan:** I really got to start sending you everything so you can put it on my calendar, because I'm not good. Is there a way to share your calendar? It's not even on there — it's in my head. Well, because I missed something. Yeah, I'm just going to send you a message every time I get a meeting, so you can put it on there.

**[12:57] Andres:** Yeah, I think that's a good idea.

**[14:09] Megan:** Do you have to leave early for anything today? I should be good. No games today — just practice. But if I leave by 4:30 I should be good. [Side conversation about her son's baseball practice.]

**[14:46] Megan:** Hey, I emailed the website people. I was just a little frustrated because of those little typos and because they're using the word "doctor" and "health coach."

**[15:12] Megan (reading agency's response):** "You hired us to give you an SEO / AIO optimized website with 30 pages to get your ranking in Buda, Texas. To rank, you need more content than you as the lead practitioner think you need. From my experience with other clinics, this is what's required to make patients feel safe enough to proceed. This is my professional expertise from over 10 years. If you want to remove content, you can remove content. I'm happy to discuss in tomorrow's meeting."

**[15:42] Andres:** My question to them is always — I get it, but how does a bunch of text that nobody will ever read help? I get SEO is important, but how will it actually help? And more importantly, it can't confuse him [the patient]. That it doesn't confuse him at all.

**[16:13] Megan:** Right. Yeah.

**[16:17] Andres:** Sorry about that, I just joined from the other computer. All right, I'm going to share my screen real quick so you see what we're doing. All right, Taiwo, so we need to go…

**[17:09] Taiwo:** So I think first is creating new clients.

**[17:16] Andres:** We can use this one. What do you need from here?

**[17:19] Taiwo:** I can't see your screen.

**[17:23] Andres:** Oh, okay, hold on. … There we go.

**[17:34] Taiwo:** First thing is to put in new clients. … Let me send the URL — it's OAuth clients.

**[17:58] Andres:** Oh, so you just need the authentication part — the OAuth consent screen.

**[18:04] Taiwo:** Yes, this one. I'm going to do the branding, the audience, and clients — the desktop from overview. OK, let's move to branding and let me see if the branding is already there.

**[18:34] Andres:** What are the settings that you need from here? Because you and I can go through everything else, but I need to know what you need so we can set it up and get Megan back to her work — she doesn't have to just watch us connect accounts.

**[18:54] Megan:** I got other stuff I can do, just like you do.

**[18:56] Andres:** That's what I mean, yeah.

**[19:01] Andres:** I already have a client. What do you need from here? The client ID, right?

**[19:05] Taiwo:** Yeah, client ID and secrets.

**[19:10] Andres:** Perfect — they set those up last week.

**[19:24] Andres:** I think we might have to change this — you and I can look into it in a bit, but these are the current authorized redirect URLs. So we'll have to change those.

**[19:36] Taiwo:** OK, let me send it to you. Those things are very important.

**[19:46] Andres:** And I'll give you a new secret.

**[20:19] Andres:** That's until it gets deployed to her. Because once we push it to her GoDaddy and take it out of Vercel, then we'll need to redirect it. I think on that, we're waiting a little bit.

**[20:38] Taiwo:** Yes — you can add multiple links, so for local development, for staging, and for production, so we can have multiple links at once.

**[20:51] Andres:** All right, so you've got the secret, you've got the authentication — I've added those here. What else do we need?

**[21:01] Taiwo:** What should I be [doing]? … Switch to me.

**[21:10] Andres:** Oh, the scopes, yeah, okay.

**[21:40] Taiwo:** You are going to do that on the console itself — the consent screen.

**[22:38] Andres:** What scopes do you need?

**[22:41] Taiwo:** Gmail — so type `gmail.send`.

**[22:45] Andres:** That's already done.

**[22:49] Andres:** It has email, Gmail. Let's add more. Gmail.

**[22:54] Taiwo:** Gmail send only. OK. Let's add that with send only.

**[23:01] Taiwo:** Give me `gmail.send` only.

**[23:15] Andres:** Which one do you need?

**[23:19] Taiwo:** I just need send and readonly.

**[23:25] Taiwo:** Yeah, send, and then also read only, another one is read only.

**[23:35] Taiwo:** Then also the calendar. Calendar. And I will do `also`.

**[24:10] Taiwo:** `full` [access], readonly.

**[24:20] Andres:** Yeah, we already have calendar readonly and send email, so we're good.

**[24:23] Taiwo:** Yeah, there's still `compose` only for Gmail, which is for transfer.

**[24:28] Andres:** What's that?

**[24:28] Taiwo:** Compose only for Gmail.

**[24:34] Andres:** It's read-only right here. Oh, Gmail.

**[24:36] Taiwo:** No, for Gmail — Gmail, Gmail.

**[24:42] Andres:** Got it. Perfect Gmail.

**[24:51] Andres:** There is no read-only for Gmail.

**[24:53] Taiwo:** Okay, type `gmail.compose` only.

**[25:17] Andres:** All right, done.

**[25:18] Taiwo:** Okay, that is all. So I think you can proceed to creating the GitHub and Supabase.

**[25:26] Megan:** I can't find the teams [tab]. … It's not here. Oh, your tabs.

**[25:39] Andres:** Megan, you're going to get a few emails for these new account creations, so …

**[25:43] Megan:** Okay, I just can't find you on … I lost you.

**[25:51] Andres:** No worries, no worries. You'll get a few emails like "this account was created, this account was created."

**[26:01] Megan:** I gotcha. Real gen [Resend].

**[26:08] Andres:** Okay, we got a GitHub, Taiwo. I'm going to add you as a person who can actually commit to it. We'll come back and add it — we need to create the repo first.

**[26:52] Andres:** The good thing is we have mostly everything we need from here, which is great.

**[27:12] Andres:** All right, Ty, we just sent you the invite so you can push the GitHub. It's a collaborator on there. When you get a minute, can you please send me your GoDaddy stuff? I know you sent it a couple of days ago, but I couldn't find it.

**[27:29] Andres:** That way whenever it's good to go, we'll just push it to like `fitlogicfunctionalmedicine.com/crm`, and then that allows you to sign in yourself.

**[27:39] Megan:** If you go to Connect Team and scroll up, it's in there.

**[27:46] Andres:** Oh, the GoDaddy stuff? Okay, perfect. So it's in there. Good, good, good. Awesome.

**[28:20] Andres:** And what's your phone number?

**[28:23] Megan:** My personal number?

**[28:24] Andres:** Yes, please.

**[28:33] Andres:** Hey, can you share with me that four-digit text you just got, please?

**[28:45] Megan:** 0702.

**[28:59] Andres:** Beautiful. OK, continue with GitHub — we're going to connect GitHub, that way we can just push the repos and upload them directly into here.

**[29:21] Andres:** Imported. Done. Perfect. All right. GitHub.

**[29:29] Andres:** Google, done.

**[29:32] Andres:** What else? We've got FitLogic there.

**[29:40] Taiwo:** Resend.

**[29:41] Andres:** Oh, he had it Resend so he could send the emails.

**[29:46] Andres:** Connect it all directly through GitHub, log in, get started.

**[30:04] Andres:** Beautiful. Okay, perfect. API keys — I'm going to send you this one right now.

**[30:39] Andres:** Once we're ready to deploy, Taiwo, we'll have to help her set up an API key for Gemini so she can use that every month directly from hers.

**[30:52] Taiwo:** Okay, sir.

**[30:53] Andres:** This one is Resend.

**[31:12] Andres:** My FitLogic uses shared click tracking. Interesting.

**[31:25] Andres:** Interesting. Okay, we'll have to work on here. Perfect — so all accounts are ready to go, Taiwo.

**[31:29] Taiwo:** Mhm.

**[31:32] Andres:** Megan, I think that is it. I have everything I need. We've got everything so we can now move our data — start moving it over to you, setting everything up so we can run a couple of tests. Most of the tests I'm going to try are going to be from that email account directly to our email accounts, and then the replies will come from there. So if you see a little bit of movement from those email accounts, don't worry — that's just us testing. But this is now the final stretch of actually getting it deployed and you actually starting to send emails out.

**[32:09] Andres:** For Taiwo right now, it's almost 11 PM, so I know him — he'll probably work a little bit on this today, but tomorrow morning he'll definitely work on it, Megan, so we can move everything from us directly to you, set up all of your accounts. We were logged in; now we need to go set everything up. You'll hear from me tomorrow again — hey, here's where we're at, here's what's done already. Let us test through the weekend, and then Monday you can start sending your emails. That will be our goal.

**[32:49] Megan:** Awesome.

**[32:49] Andres:** I'll do the walkthrough, start setting everything up so you can actually start sending those emails. We did start testing yesterday with the uploads, making sure we're able to import everything as you needed.

**[33:05] Andres:** Moil 360 / your coach should now be working. Jacob sent you an email this morning letting you know that had been resolved. Please let me know what questions come up from there.

**[33:26] Megan:** Okay. Monday and Tuesday are a little busy, but Wednesday — would Wednesday work?

**[33:36] Andres:** Okay, perfect. Let's put it on the calendar now. That way we both have it set up.

**[33:44] Andres:** Wednesday looks fantastic. What do you want to do — 10?

**[33:53] Megan:** Can we do 11? Let me back up — 10. Or even 9:30 — would 9:30 work?

**[34:16] Andres:** Yes.

**[34:36] Andres:** Boom, and we said 9:30?

**[34:38] Megan:** 9:30. Yeah.

**[34:49] Andres:** Boom, I just sent it. So we've got ourselves a meeting for next Wednesday at 9:30.

**[34:55] Megan:** And hey, just FYI — I'm meeting with the website people tomorrow at 12:30.

**[35:04] Andres:** Do you want to send me that invite? Thursday, Friday — yeah, I think I should be able to make it.

**[35:23] Megan:** Have not seen [the calendar invite], but I will. Well, I booked it with them. I have the email confirming. Oh, no, I did get it. Do you want — I'll send the link.

**[35:54] Andres:** You can forward it, Megan. If they send you an actual invite, forward it to me, I'll just save it.

**[36:04] Megan:** They just sent me a link. I can still forward you the email. It's going to be easier if I just send you the link. I'm going to send it to you.

**[36:28] Megan:** In the Connect team, but do you want me to email? That's fine.

**[36:29] Andres:** Next [Teams] is fine.

**[36:42] Megan:** Friday 12:30. Okay, we'll get to your 3 o'clock.

**[36:50] Megan:** Andres, this is Michelle. I'm supposed to say hello to you from Daniel D. Mann.

**[36:52] Andres:** Hi, Michelle. Oh, you know Daniel, I love it. Daniel is the man.

**[37:03] Megan:** He is the man, isn't he? He's very particular about the D. in there.

**[37:06] Andres:** Yeah, I always tell him his mom set him up for success. He just needs to make something of that brand, you know, because he is the man. When it comes to referrals, connecting people — great guy. I've got a couple ideas of projects that I told him would be good for us to work on. Amazing guy when it comes to connecting people, and he's so fun to talk to. You get a good feeling from him. Please tell him I say hello back, and to not be shy and shoot me a text.

**[37:44] Megan:** I will tell him. He says all those same things about you, by the way. Smart guy, very well connected. I've heard lots of good things.

**[37:54] Andres:** That's awesome. Well, I'm glad.

**[37:59] Andres:** All right, guys — thank you very much for your time. Megan, please, please, please — if you have a little bit of time, go into Moil 360, check it out. I was doing a demo with a client this morning — she does red light therapy. She said, "I created an image with Moil. I wanted to create an image for red light therapy, but the one he created was just like a localized therapy." So she added one of the pictures of her machine and said, "just give me this image of a person inside of the machine." And he did. Now she gets to brand it — edit those images with her own images as reference. The idea is you now have Moil 360 that you can start posting. If you run into obstacles, let me know, because I want you to do it right. Don't create a calendar until you feel like everything's good, because I need you to upload your colors, your logo. We can do these things together — just kind of play around with it, make sure you have access to everything. As soon as we're ready, then every day: copy, paste, download, post it for the day. Okay?

**[39:13] Megan:** Awesome. How can I add a user so Michelle can have a login?

**[39:21] Andres:** Not yet — but you can give her access for now to the My FitLogic account. We do want to add a feature where, for example, if you have the $75 yearly license, you can add someone that gets access to just kind of manage it with you. That's coming soon.

**[39:50] Megan:** OK, alright.

**[39:52] Andres:** Alrighty, as always it's been an absolute pleasure seeing you and talking to you. Talk to you tomorrow.

**[39:52] Megan:** Well, see you tomorrow, I guess. All right, see ya.

**[40:01] Taiwo:** Have a good one.

**[40:03] Andres:** Thank you, Taiwo.

**[40:07] Andres:** Thank you, brother. So we're good, right? I think we're good to go.

**[40:10] Taiwo:** Yes — I did push the code to GitHub. I'll test it this night. If I have any issues with testing, I'm going to get back to you.

**[40:26] Andres:** Perfect.

**[40:30] Andres:** All right, man — sounds good. So we have until next Wednesday to finish this one up real good, okay?

**[40:36] Taiwo:** Okay, sir.

**[40:37] Andres:** Thank you, my brother. Talk to you later.
