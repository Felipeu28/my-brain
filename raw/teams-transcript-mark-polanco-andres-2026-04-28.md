---
type: meeting-transcript
source: Microsoft Teams
date: 2026-04-28
ingested: true
ingested_at: 2026-04-28
---

# Teams Transcript — Mark Polanco & Andrés (2026-04-28)

**Meeting subject:** Mark Polanco & Andrés
**Date:** 2026-04-28 (1:45 PM – 2:20 PM CT)
**Organizer:** Andres Urrego
**Attendees present:** Mark Polanco, Andres Urrego, Taiwo Ola Balogun (joined for technical portion)

---

## Context

Working session with Mark Polanco to review the ConnectX CRM/website Andres's team is building for him. Mark is a Moil business collaborator (Buda network, Airtable project background; daughter Faith). He sells phones / connectivity through Verizon and Yealink under the ConnectX / connectex.net brand, and is migrating off Airtable + a generic site (connectex.com / .net) onto a custom CRM + landing page Andres is building. Goal of this call: confirm what's been built, lock down go-live for early next week, settle payment terms, and capture remaining requirements (Squarespace login, Airtable column scope, troubleshooting docs).

## Topics covered

- **Site reaction.** Mark loves it — "100x better than connectex.com," called it "modern, elegant, efficient, professional." Already showing it to AT&T / channel partners and an AppDirect channel manager. Has matching ConnectX-branded merch (techno design on the back).
- **Airtable migration scope.** Mark walked Andres through which columns to import: everything from the leftmost column up through (but not including) the reporting / documents columns on the right. Reporting stays in Airtable for now since he uses its existing reporting flow.
- **BuiltFirst marketplace billing issue.** The marketplace page on Mark's existing site is blacked out due to an unpaid bill at BuiltFirst. Mark plans to pay it off, but Andres advised him to first apply for the Buda EDC reimbursement so he doesn't lose eligibility.
- **Buda EDC reimbursement.** Up to $10K total split across categories (marketing / equipment / software). Mark previously only got $1K (or never picked up the rest). Andres committed to providing a full invoice up front so Mark can submit for reimbursement. Mark will resubmit the application ASAP.
- **Payment structure.** Agreed: 1 down payment + 3 quarterly payments over 9 months. Andres explicit that support is unconditional during those 9 months — "we'll tweak as we go," not pay-locked support tiers.
- **Quoting flow.** Mark does NOT need a quote builder — his channel partners (AT&T, Verizon, etc.) handle quotes via their own portals. He uses their experts; he just needs faster turnaround. (He lost some deals to AT&T slowness recently — channel partner side, not Moil's.)
- **Phone number on site.** Change to Mark's business cell: **330-812-5750**.
- **CRM walkthrough (`/CRM`, `/ticketing`).** Andres walked Mark through tabs: Contacts, Leads, Tickets, Knowledge Base, Campaigns, Blogs. Knowledge Base is where Verizon/Yealink troubleshooting docs go so AI can resolve tier-1 tickets before they reach Mark. Ticketing portal (`connectex.net/ticketing`) will be left **publicly open** — capture lead info from anyone who lands there.
- **Resources / blog section.** Andres committed to having it live next week so Mark can write SEO-backed blog posts after every training he attends.
- **Campaign builder API key.** Gemini key needs to be added (Taiwo to handle); Mark was about to test a Verizon T77 LTE campaign when they paused for the API key.
- **Side topic.** Patrick (mutual contact) hosting an event tonight at "back nine" on Davis Lane in South Austin. Mark can't attend (kids' boxing + swim team afternoon schedule). Lunch tentatively scheduled mid-May.

## Key decisions

- **Go-live: early next week.** ConnectX site pushes to Mark's Squarespace once login is provided. Mark redirects traffic from connectex.com/.net to the new site.
- **Phone number on site → 330-812-5750.**
- **Ticketing portal stays publicly open** to capture inbound leads from anyone who finds it via Google.
- **Payment terms:** 1 down + 3 quarterly over 9 months; full invoice issued up front so Mark can claim Buda EDC reimbursement.
- **Knowledge Base seeded with Mark's troubleshooting docs** (Verizon, Yealink) before tier-1 AI ticket triage tests next week.
- **Resources / blog section live next week.**
- **No quote builder needed** — channel partners handle quoting.
- **Lunch mid-May.**

## Action items

- **Mark:** Send Squarespace login. Contact BuiltFirst about the marketplace billing block. Refile Buda EDC reimbursement application ASAP. Send 4–5 troubleshooting documents (e.g., Verizon T77 LTE, Yealink LTE deck station coming end-of-month).
- **Andres:** Update site phone to 330-812-5750. Build Resources/blog section live by next week. Push site to Squarespace once login arrives. Issue full invoice for Mark's EDC reimbursement claim. Schedule lunch mid-May.
- **Taiwo:** Add Gemini API key to ConnectX campaign builder so the test campaign can run.
- **Engineering team (Andres + Taiwo):** Import Airtable contacts (left-side columns up to but not including reporting/documents columns); finish ConnectX contacts tab to match Airtable schema; load troubleshooting docs into Knowledge Base for AI tier-1 ticket testing next week.

---

## Full transcript

**Mark Polanco:** Man, you should have come over here. It's a nice day to be outside over here at Progress and Buda.

**Andres Urrego:** Oh, you're a progress.

**Mark Polanco:** Yes, sir.

**Andres Urrego:** Nice. Did you work out out of there today?

**Mark Polanco:** Yes, sir.

**Mark Polanco:** Yeah, I decided to come out here because it was a, it was just, I can't concentrate with it at home sometimes, you know? My wife's working from home and so she likes to come downstairs and watch TV sometimes and it's just kind of distracting, you know, so I get out of the house.

**Andres Urrego:** Nice, nice.

**Mark Polanco:** Yeah, how about yourself?

**Andres Urrego:** Not much, man. I mean, just super busy, lots of work, but good stuff, man. I mean, I literally earlier, I thought I had a call, like a workshop at 7 A.m., but I had done the math wrong. It was in Arizona time, so it was actually 11 A.m. So that completely threw off my entire day, man. But it is what it is. It is what it is. We do what we can, right? I mean, we made it happen.

**Mark Polanco:** Yeah.

**Mark Polanco:** Yeah.

**Mark Polanco:** That's right.

**Andres Urrego:** You know, got all the appointments done. We got two more the rest of the day up to you, but man, I'm just, I'm excited that we get to chat today and go through this, man. How's work?

**Mark Polanco:** Mhm.

**Mark Polanco:** Yeah, I'm ready to go, man. I'm ready to launch this bad boy. I've been looking it over, and I actually was showing it to my channel partner at AppDirect, and I was showing them all the good work that she did. So, yeah.

**Andres Urrego:** Good.

**Andres Urrego:** What do they think? I mean, how are you feeling about it so far? We're working. We're literally right now is just on a call with the team. We're finalizing the so that we can just get all the data imported from from Airtable.

**Mark Polanco:** I love it.

**Mark Polanco:** Uh-huh.

**Andres Urrego:** So I will keep you posted so that we can get the latest file. I have a small sample that I downloaded last time from you. And we're working on making sure that we, you have a lot of like, there are a lot of columns. So I want to make sure I don't miss any of them when we import them.

**Mark Polanco:** Mmh.

**Mark Polanco:** Gotcha.

**Andres Urrego:** So at least the ones that you have that are filled out most of the times, I want to make sure that you have all of those inside of your CRM.

**Mark Polanco:** Mm.

**Mark Polanco:** Yeah, and I can I can tell you which ones for sure that we need to have, right?

**Andres Urrego:** I love it.

**Mark Polanco:** So, everything from the left-hand side all the way to, if you go right.

**Mark Polanco:** To.

**Mark Polanco:** I don't even need that reporting section.

**Mark Polanco:** Any of that stuff? Okay, so past column, what column is this?

**Mark Polanco:** or the documents column.

**Andres Urrego:** You want to share your screen with me? That way I can take a quick look.

**Mark Polanco:** Yeah, yeah, sure. I'm sorry. Let me go ahead and...

**Andres Urrego:** Thank you. Thank you. Thank you. No, you're good.

**Mark Polanco:** I do that real quick.

**Mark Polanco:** Surprised you can't see.

**Mark Polanco:** Let me see, hold on real quick, share, share, there we go.

**Mark Polanco:** Mm.

**Mark Polanco:** Here we go. All right. You see that?

**Andres Urrego:** Now I do it, perfect.

**Mark Polanco:** So really, all this reporting information right here, so anything from this column.

**Mark Polanco:** to the right. I really don't need because I don't use it now because I have that on the other airtable part.

**Mark Polanco:** So, that's why I do my reporting, because they can do it all at once, right? This one I have to like copy and paste everything and put it into an email format, unless I feel them, I just click a button and boom, it sends all the information, so I don't even fill this part out anymore.

**Andres Urrego:** Got it.

**Mark Polanco:** So, yeah, so everything from here to the left is what I need.

**Andres Urrego:** Beauty.

**Mark Polanco:** Yeah.

**Andres Urrego:** Okay, good, good, good. Yeah, yeah, because that's what I, you know, that's what we're working on. Make sure that we don't miss anything in any of those tabs that we need for sure.

**Mark Polanco:** Yeah, I need the rest.

**Mark Polanco:** And the rep there, those are the reps, the Verizon reps.

**Andres Urrego:** Let me add, let me add real quick. I'm gonna, I'm gonna add.

**Mark Polanco:** I don't know where they are.

**Andres Urrego:** Um...

**Andres Urrego:** my developer and my project manager so they can listen in.

**Mark Polanco:** Okay.

**Andres Urrego:** They can listen in and we make sure that we don't miss anything before the delivery. I'm pushing for delivering next week, early next week, for us to like literally start testing, for you to actually give it a try. You know, go push out a couple of emails for testing and make sure that everything's working.

**Mark Polanco:** Okay.

**Mark Polanco:** Yeah, that.

**Mark Polanco:** That actually works out for me because I still need to contact built first who did the marketplace for me because there was a billing issue. So I need to figure out what went wrong. So I'm going to go ahead and get that squared away.

**Andres Urrego:** Okay, so is it not loading right now?

**Mark Polanco:** Today, but it'll be, it'll be ready to go. Huh?

**Mark Polanco:** I'm sorry?

**Andres Urrego:** Is it not working right now, that marketplace?

**Mark Polanco:** Let me double check. Last I checked earlier, I didn't see it.

**Mark Polanco:** Yeah, excuse me.

**Mark Polanco:** Excuse me.

**Mark Polanco:** Did I see it?

**Mark Polanco:** Yeah, so it's usually right here, but see how it's all blacked out.

**Mark Polanco:** I don't know if you can see that. Can you see this?

**Andres Urrego:** Ohh, are you talking about that? Ohh, no, no, no, no, no, it, it, I think you're only sharing one tab.

**Mark Polanco:** That's good.

**Mark Polanco:** Okay.

**Mark Polanco:** Let me see, Alan.

**Mark Polanco:** So here's the marketplace.

**Mark Polanco:** Yeah, see how you can, you can see it.

**Andres Urrego:** Yes, yes, and it's not loading. Yeah, okay.

**Taiwo Ola Balogun:** Yeah.

**Mark Polanco:** Yeah, it's not loading, but you can kind of see there's something that looks like it wants to be there, right?

**Mark Polanco:** You can barely see some.

**Andres Urrego:** But that is coming, so that's not on an end, right? On our end it was loading is just because of that billing issue.

**Mark Polanco:** Yeah, yeah, and I'll take care of that. I'll take care of that. I had it budgeted anyway. And you know what, now think about it. I think what I need to do is I'm going to go ahead and take care of this and then I'm going to submit, I need to submit the thing through the EDC. That way I can get reimbursed for it.

**Andres Urrego:** OK, alright.

**Mark Polanco:** See, they'll reimburse me for it, right?

**Andres Urrego:** Okay, good.

**Andres Urrego:** Yeah, there is, and you gotta do that application ASAP.

**Mark Polanco:** Yeah.

**Andres Urrego:** Because I know you only got 1000 bucks last time, so, or you maybe never even picked it up, so I don't.

**Mark Polanco:** Yeah.

**Mark Polanco:** What, what's the what's the max on that anyway, on that payout? Do you remember?

**Andres Urrego:** Well, it's 10,000 total, but you have to be very specific. Like, there's like a certain part for marketing, there's a certain part for, you know, equipment and software, you know, so you gotta...

**Mark Polanco:** Yeah.

**Mark Polanco:** Right.

**Mark Polanco:** Mhm.

**Mark Polanco:** And then I gotta have the receipts for it.

**Andres Urrego:** Right. So like marketing, for example, your website qualifies for marketing, software and solutions, you know, like, like Moil 360 qualifies for, you know, for that. Like, so a lot of it, but you have to spend the money up front or you have to have the invoice.

**Mark Polanco:** Okay.

**Mark Polanco:** You know.

**Mark Polanco:** Yeah.

**Mark Polanco:** Okay.

**Mark Polanco:** Right.

**Andres Urrego:** So like, if you like, and again, you know, you said, okay, Andres, I'll pay you quarterly. I'm okay with that. Which I wanted to talk to you about. You tell me when I was thinking we could, if you're cool with it, we could do like first payment and then three, right? I mean, so first payment and then another, you know, three more payments over what, nine months? Is that what you're thinking?

**Mark Polanco:** Right.

**Mark Polanco:** Yeah.

**Mark Polanco:** In.

**Mark Polanco:** Yeah, that'll work. That'll work.

**Andres Urrego:** Perfect, and then, but I can give you.

**Andres Urrego:** the full invoice, like if you already paid it kind of thing. So then that way you can get that up front and you know, just just.

**Mark Polanco:** Mhm.

**Mark Polanco:** Okay.

**Mark Polanco:** Yeah, and then, and then once I get that payment, I could just pay off the rest of it.

**Andres Urrego:** Because, unless you suspend it.

**Andres Urrego:** Exactly, exactly, so.

**Mark Polanco:** In fact, in fact, I'm thinking about this bill first. They're allowing me to pay it off in two payments. I may just go ahead and pay the whole thing and then just submit this and get that payment.

**Andres Urrego:** For the other, the other guys.

**Mark Polanco:** Yeah.

**Andres Urrego:** Well, but then you got to take a look and see how and if you're going to be able to use this as a write-off, because I don't want you to pay it off right away. And then they're like, yeah, no, sorry, Mark, we can't give you the three grand for that. You know what I mean? So,

**Mark Polanco:** Oh, okay, I see. Yeah, yeah.

**Mark Polanco:** Okay.

**Mark Polanco:** Look up.

**Andres Urrego:** So spend it where you're going to be able to get it back, and we'll just kind of have to, I mean, number one thing, Mark, would be sit down and fill out that application again ASAP.

**Mark Polanco:** Okay.

**Mark Polanco:** I would definitely do that. I would definitely do that.

**Andres Urrego:** Um...

**Andres Urrego:** And if you need, you need to, if you need some help, obviously we can sit down and go over it.

**Mark Polanco:** All right, so this right here is fantastic. I like the this right here, local.

**Andres Urrego:** Good, yeah, yeah, I changed, and yes, exactly, and I, those are kind of like what you wanted, you had asked for. You know, I added them on there, obviously we can continue to add more.

**Mark Polanco:** Yeah.

**Mark Polanco:** And how do I go about adding more anyway?

**Andres Urrego:** Yeah, man.

**Andres Urrego:** What's that?

**Mark Polanco:** How do I go about adding more? Because I talked to my channel provider, she's going to give me some suggestions what I can add to this list.

**Andres Urrego:** Oh, just let me know, we'll add him right away.

**Mark Polanco:** Okay, cool. That'll work.

**Andres Urrego:** Yeah, man, I mean, you're going to have nine months for us to trick these things around and for us to work on it. Yeah, I mean, it's not one of those things, Mark. I'm not the kind of person that is like, look.

**Mark Polanco:** Tweak it around. OK, perfect.

**Andres Urrego:** You're going to pay me this over nine months, but you only get the support they want. You know, in love. That's not how it works. You know, we got you. So like, we will tweak things as we go. We'll make sure that everything works. My main concern today is, okay, let's push everything over to, let's bring the contacts over and then let's start sending some outbound campaigns. Make sure you can track it on here, but then let's start doing some real marketing.

**Mark Polanco:** Yeah.

**Mark Polanco:** Alright.

**Mark Polanco:** Right, yeah, I definitely want to get that going ASAP, so.

**Andres Urrego:** Um...

**Mark Polanco:** And I also talked to my channel manager earlier today because I was telling them that I really need a faster turnaround when it comes to getting quotes and getting, you know, some of this because I want to make sure that when we go full go and people start submitting, you know, orders and things like that, that we can turn it around fast. Because the experience I had, and particularly it was with AT&T, to tell you the truth,

**Mark Polanco:** They've been dragging, dragging, dragging, dragging, and I lost a couple of deals because of that, so yeah, and it wasn't it wasn't our guys' fault, it was actually AT&T's fault.

**Andres Urrego:** Okay.

**Andres Urrego:** No.

**Andres Urrego:** So is it like, so what are you thinking? Like adding quotes? Do you want us to build like a quote builder kind of thing? Or what are you thinking? How do you, how do you foresee us? So like the, okay, good.

**Mark Polanco:** What's that?

**Mark Polanco:** No, I got a quote builder. Yeah, no, no, let's not worry about that. They have that on their website. And I like to use their website anyway, because what so essentially what it is, is I get, let's say for instance, you're looking for something, you know, from my for my my connections. And so I said, OK, you know, Andres is looking for an AI, a Gentic AI for

**Andres Urrego:** Good.

**Mark Polanco:** you know, let's say troubleshooting or something like that. And so I'll send it to those guys and say, I need a quote. And so I can, I have somebody I send it to, and then I can just say, okay, send me the quote, send me the quote, and I can bug them about it, right? And then they'll find me the right person. They'll find me the right solution. I don't.

**Andres Urrego:** Bride.

**Mark Polanco:** I have to go look for the solution. They're my experts, right? I have experts there that do all that for me. So, and they'll get me the quote and I'll list up. I just told them I need that to be a little bit more expedited, a little bit more faster when it comes to getting quotes and stuff. Yeah, so.

**Andres Urrego:** Beautiful.

**Andres Urrego:** Okay, very good.

**Andres Urrego:** What other comments do you have, Mark? Like, I know you've kind of gone to the website. What else do we need to change? And then we can jump into the CRM section just to kind of, kind of, again, on there, we're finishing up some of the touches. I wanted to go over, you know, at least what your website is.

**Mark Polanco:** Uh-huh.

**Andres Urrego:** and I'm going to need access. Like I think honestly today, this is, and I don't mean this in a rude way, please forgive me, but I think this is already better than what's already sitting at connectex.com.

**Mark Polanco:** Oh yeah, definitely. No, no, no. Oh yeah, 100 times better.

**Andres Urrego:** Or.net, so I'll need your your login, yeah, so I'll need your login info for like GoDaddy or whatever you're hosting this site, so that Squarespace perfect, and I got Tywo here on the call with me, so that way, once you say that to me, we'll be able, because this is good, this is good to go, other than the than the little billing thing, but, and again, Mark.

**Mark Polanco:** Oh, Squarespace, okay.

**Mark Polanco:** Yep.

**Mark Polanco:** Oluwole.

**Andres Urrego:** I mean, you already have a contract with them, right? So I mean, if you don't have to pay them right away, just delay it a little bit if you can, but just make sure that they get it back up so that it shows. If for some reason there's a delay there, let me know. We'll move it away from it. It's okay. We'll take it out.

**Mark Polanco:** Yeah.

**Mark Polanco:** Yeah, yeah.

**Mark Polanco:** Yeah, we can we can hide the page, really.

**Andres Urrego:** That's what I mean, yep.

**Mark Polanco:** Yeah, we can just hide the page here. That's fine. So this right here, can you change that number to my 330 number?

**Andres Urrego:** Yes, so change phone number, perfect.

**Mark Polanco:** Yeah, change that to, because that's my, that's, I mean, I rather, I guess I just use my cell phone number, my business cell phone number, 330812.

**Mark Polanco:** 5750.

**Andres Urrego:** Perfect. Can you do me a favor? Okay, what was that number again?

**Mark Polanco:** Okay, 330.

**Andres Urrego:** Yep.

**Mark Polanco:** 812.

**Mark Polanco:** 5750.

**Andres Urrego:** Five 750 - perfect.

**Mark Polanco:** Hey, do you want to see something cool?

**Andres Urrego:** Yes, Sir.

**Mark Polanco:** I have to show you this.

**Mark Polanco:** So, let me stop sharing my screen.

**Andres Urrego:** OK.

**Mark Polanco:** So, it's called...

**Mark Polanco:** Running, alrighty.

**Mark Polanco:** Can you see my camera? Where's my camera at?

**Andres Urrego:** Uh, not yet.

**Mark Polanco:** I turn it on, yeah.

**Andres Urrego:** Huh.

**Andres Urrego:** Ooh, I love it.

**Mark Polanco:** Look at that. It matches my website. Yeah. Check it out. And I even have the techno on the back. It matches the website, dude. Yeah, I'm ready to go.

**Andres Urrego:** Daddy, ohh, yeah, yeah, baby, I love it.

**Andres Urrego:** Well done. Well played. Well played. It matches your side now. I love it. I love it. And see how it looks modern, right? So I think we, I think we picked the right design for it. You know, it looks good. It, yeah, yeah, yeah. I like it. I like it.

**Mark Polanco:** Mm-hmm.

**Mark Polanco:** Yeah.

**Mark Polanco:** Mm-hmm. Yep.

**Mark Polanco:** Yeah?

**Mark Polanco:** Additive.

**Mark Polanco:** And the number I have on there is the 330 number. That's why I want that one changed. So.

**Andres Urrego:** Okay, perfect. I love it. I love it. Oh, that is so awesome. That makes me very happy. That makes me, that tells me that you did, you know, that you like what we're working on so far.

**Mark Polanco:** Yeah, I...

**Mark Polanco:** It's fantastic, dude. I love it. Love it. I mean, I've been bragging to everybody and I've been showing some of the reps that I work with. I said, here, check this out. I know it hasn't been launched yet, but it's almost ready to go. And I'm like, boom, this is it. And they love it. I mean, it looks fantastic. It looks super modern. It looks very elegant. It looks very efficient.

**Mark Polanco:** And it looks very professional. I mean, just fantastic. I'm totally happy with it. Totally happy with it.

**Andres Urrego:** I love it. I love it. I absolutely love it. Thank you for the feedback.

**Mark Polanco:** Yeah.

**Mark Polanco:** Definitely. And then also, go ahead. I was just going to say, I.

**Andres Urrego:** Uh, alright.

**Andres Urrego:** Go to the other page, but...

**Mark Polanco:** Yeah, yeah, just send me a link later on to leave a review for your website and stuff, so I can do that.

**Andres Urrego:** Oh, thanks man. I'll send you the link to Moil. I'll send you a link to Moil and then that would be awesome.

**Mark Polanco:** Yeah, I need, I need that.

**Mark Polanco:** Yeah.

**Mark Polanco:** Yeah, everything else looks fantastic. You know, we'll probably need to put some more here into the resources.

**Andres Urrego:** Yes, that will be, and I build that, that we'll make sure that it's live by next week so you can test it, you know, create as many blogs as you want. My goal is that, right? You're going to be, like, for example, you went to a training this week, right? Or you took a training online and you're like, oh ****, I really want to write about this subject. So you go.

**Mark Polanco:** Mmh.

**Mark Polanco:** Hello?

**Andres Urrego:** Type a few notes, create your article, you push it, and now you got an extra SEO article hitting your website.

**Mark Polanco:** OK, and that's and that's one of the things that you were showing me last time, right? How they create articles and all that.

**Andres Urrego:** Yeah, so do me a favor right up here on the on the on the URL, I want you to type forward slash CRM.

**Mark Polanco:** There we go. That's what I was looking for last week.

**Andres Urrego:** Yeah, baby. Let's go. So everything's going to be here again. This is going to change a little bit because we're finishing up those, because we're finishing up the, you know, the contacts tab so that it matches what you, what we already have, you know, so that it can import what you have. But go ahead and click through them, right? So if you click through them, you're going to have your contacts tab.

**Mark Polanco:** There we go.

**Mark Polanco:** Gotcha.

**Andres Urrego:** Yeah, you're going to, oh, and again, you know, so there you go. So you're going to be able to, your leads, you're right, you're going to be able to, you're tracking through here. I'll make sure that this matches better what you have on our table. On tickets, so check out the tickets one. So tickets are going to come here.

**Mark Polanco:** Perfect.

**Andres Urrego:** But guess what? We're going to build a knowledge base. So click down here where it says knowledge base. That's where we're going to upload all those documents about the devices, right? That's where we're going to start adding the documents. And here's why. Because then when people submit a ticket, if the documentation already has it available, it will respond to that.

**Mark Polanco:** Gotcha.

**Andres Urrego:** ticket so that you don't have to touch it just yet. Anything that actually requires your attention will go to your email, but anything that can be resolved, troubleshooting, a lot of that, we're going to test this next week so that you can see exactly how it works. So if you have a few documents, Mark, that you can please share with me, like...

**Mark Polanco:** Perfect.

**Andres Urrego:** I don't know, 5 documents of some of the devices. Just send it to us in an email and I'll upload them here so that we can run those tests.

**Mark Polanco:** Okay, like the documents on how to do certain stuff or what are we talking about?

**Andres Urrego:** Like, like the troubleshooting document, like I know, for example, devices have a, like the phone Verizon 4433, you know, that probably has a document that tells you how to troubleshoot it.

**Mark Polanco:** Okay, yeah, yeah, okay. Yeah, I can do that.

**Andres Urrego:** To see all of those little things, like, and I want you to think, what are the main things people call you about? Remember, as we build this, and this is the beauty of the fact that we have nine months, you know, is...

**Mark Polanco:** Yeah.

**Mark Polanco:** Mmh.

**Andres Urrego:** as we go is, okay, what are the things that you most, that take a lot of the time on the tickets? You said, okay, tickets take some time. I got to troubleshoot these things. Okay, well, what if we can create, well, not what if, we are going to create that filter of, okay, this person can actually be helped with the troubleshooting. Here's some information you need. AI helps him out.

**Mark Polanco:** Mm.

**Andres Urrego:** And then there's other people that you'll just say, okay, no, this one definitely needs Mark's attention.

**Andres Urrego:** But they're all being tracked directly in your CRM.

**Mark Polanco:** Okay.

**Mark Polanco:** Okay, perfect.

**Mark Polanco:** Perfect.

**Mark Polanco:** Excellent, and here's the campaigns.

**Andres Urrego:** Yes, okay, so let's take type on new campaign and I think we had added, I think we had already added the.

**Andres Urrego:** the API key that we're using for testing, but it could be, all right, so let's test this out real quick just to make sure if not, I was on the call, maybe we can add a quick API to it. Do me a favor, type here.

**Andres Urrego:** What do you want to say in a campaign about? A campaign about our new Verizon phones that are $25 a month or something.

**Mark Polanco:** Mmmm.

**Mark Polanco:** Let's talk about, yeah, the T77 LTEs.

**Andres Urrego:** Yeah, try that. And be very vague just so we can test it. I always like to test to break things. I really do because...

**Mark Polanco:** Yeah.

**Mark Polanco:** Okay.

**Andres Urrego:** If we test just for the things that work, then you know we run into bugs later. OK. All right, so that's on me. All right, let me.

**Andres Urrego:** Taiwo, can we add an API key real quick to the campaign builder?

**Taiwo Ola Balogun:** Yeah, I'm going to check the model. I'm going to check the Gemini model, but I think we can, but let me get that.

**Andres Urrego:** Perfect.

**Andres Urrego:** Thank you.

**Andres Urrego:** And I'm literally, as I have you on the call, Mark, I'm literally running, you know, half of these things that we're working on for your CRM. So it's literally what we're running on it right now because we were in a meeting before you and I met. Okay, so homework for you before we get this key updated and we test it just so you can see it a little bit, but.

**Mark Polanco:** Perfect.

**Andres Urrego:** Number one thing, we'll push this out to your Squarespace or whatever you have it today. So I'll need that access. That way you can just start telling people to go to connectx.net instead of giving them this website.

**Mark Polanco:** Mm.

**Mark Polanco:** Okay.

**Mark Polanco:** Gotcha.

**Andres Urrego:** There is another page that is not available yet for you to for people to see, but I want you to try this. So delete that on the on the yeah, delete CRM and campaigns and then type ticketing.

**Mark Polanco:** Okay.

**Andres Urrego:** This one will come live. But this is something that you're going to give to people, to your clients. When you send an email, you say, if you ever need to open a ticket, here's where you come to open your ticket.

**Mark Polanco:** Mmm.

**Mark Polanco:** Sweet. So it's going to say connect text.net slash ticketing or how's it going to say?

**Andres Urrego:** So, right?

**Andres Urrego:** Yes, yes, it's going to be connected. But it's up to you. If you want me to make it available to anyone, I can. If you want to just be a link that you share with people, that's okay. But that's the beauty of this, right? It's...

**Mark Polanco:** Okay.

**Mark Polanco:** Gotcha.

**Mark Polanco:** Yes.

**Mark Polanco:** Yeah.

**Mark Polanco:** So let me ask you this. So if we make it available to anybody, right?

**Andres Urrego:** Young.

**Mark Polanco:** And they have to fill out this information, full name, email, all that stuff. And that's going to be captured in a CRM, correct?

**Andres Urrego:** Yeah, so go, yes, so as soon as they, yeah, so as soon as they type on here, they submit that request, it goes to your CRM. If I, if a client exists, it's going to match it to that client. If a client doesn't exist, then it will it will walk you through the process of creating the new the new user.

**Mark Polanco:** Leave it open. Leave it open.

**Mark Polanco:** Perfect. Yeah, let's leave it open for everybody. That way if somebody Googles it and finds it and they want to see, hey, can I use this for my own phone? Fine. At least I get their information and I can reach out to them.

**Andres Urrego:** Exactly. Very good.

**Mark Polanco:** Yeah, yep, yep.

**Andres Urrego:** All right, love it, love it. Yeah, this is kind of what I wanted to show you, right? Like, there's four parts to this. There's your landing page, there's your CRM, there's your ticketing, and then everything else, the campaigns, and then the blogs.

**Mark Polanco:** So I need to send you my login for Squarespace. I need to figure out what that is. Some 4 to 5 troubleshooting documents.

**Andres Urrego:** But...

**Andres Urrego:** Yeah, yeah, yeah, because...

**Andres Urrego:** Yes, perfect. And then that way we'll test this, we'll test this ticketing. So for example, right here, once we have those documents, I'll ask a question about that Verizon device and say, my Verizon device isn't working, I'll upload an image and the chat should give me a message back that says,

**Mark Polanco:** Okay.

**Mark Polanco:** And what else do you need from me?

**Mark Polanco:** Okay.

**Andres Urrego:** Please try this, blah blah blah blah. OK, if you can't fix it, then he click here and this goes to Mark.

**Mark Polanco:** Perfect.

**Andres Urrego:** And it will give them those troubleshooting steps first. It will be directed to that specific device. We can add an API key before we move it over to you. And then that way, if the document doesn't exist, then the API will pick it up. Like the AI will know that we don't have documentation on that product.

**Andres Urrego:** So now we go out and try and find as much as we can that is recent on that device to help them troubleshoot.

**Mark Polanco:** Gotcha.

**Andres Urrego:** I, I, of course, if you have the the the documents, is much easier for us to upload them and then just have them there, because these are the devices you sell, but if you don't, then we'll do the live searches.

**Mark Polanco:** Mm.

**Mark Polanco:** Well, I mean, keep in mind, you know, there's, you know, Verizon has new products coming out, right? Or Yealink, that's the manufacturer. So, like, they've got a new LTE deck station coming out this month, end of this month, beginning of next month. So that's something that we're going to definitely put in there. So.

**Andres Urrego:** Nice, there you go. So as soon as they send you that documentation, you're going to be able to download them, save them to your knowledge, and then people can ask questions from them.

**Mark Polanco:** Perfect.

**Andres Urrego:** Right? It makes it fun, it makes it simple, it makes it, I mean, and that's what it is, right, Mark? I mean, my goal is...

**Andres Urrego:** you're going to own this and it gives us the next six, nine months to truly build it and make it exactly everything you wanted so that you're no longer ever having to pay for all of these solutions or, you know, separately. Right? You're paying 200 bucks for this, you're paying 200 bucks for that, you're paying 200 bucks for that. Well, that's already $7,200 a year.

**Mark Polanco:** Mhm.

**Mark Polanco:** Right, right, yep. And that's huge.

**Mark Polanco:** Mm.

**Andres Urrego:** You know, but if you own it, this is for many years to come. It's yours. You can build on top of it. You can build in it. You can do whatever you want because it's your product.

**Mark Polanco:** Perfect.

**Mark Polanco:** Perfect.

**Mark Polanco:** Trying to find my Squarespace. I'm gonna have to look for it. I know I had it somewhere.

**Andres Urrego:** That's okay, that's okay.

**Andres Urrego:** Any questions, Mark? Next week's test will be much better. Next week's test, we'll put everything together. We'll finish up your...

**Andres Urrego:** And.

**Andres Urrego:** We'll finish up the CRM today so that we can import those Airtable documents. Once we have that ready, then everything else is just making sure that we got everything connected and ready for you to go.

**Mark Polanco:** Perfect, alrighty.

**Mark Polanco:** That works for me. And as soon as I find this login for you, I will send it over to you.

**Andres Urrego:** Thank you. Perfect. I love it.

**Mark Polanco:** Thank you very much, my friend. Hey, you going tonight to, I think Patrick's doing some kind of event in South Austin. Did you hear about it?

**Andres Urrego:** Oh, yes, I had no idea. I messaged him a couple, like, like a month or so ago, and I was like, hey, man, I hope to see you at this event. I didn't hear back from him, so I just assume he's busy. But I had no idea. Where's the event at?

**Mark Polanco:** No, he's super busy if he, yeah.

**Mark Polanco:** It's at the back nine right there on Davis Lane. It's in South Austin.

**Andres Urrego:** Okay, okay, and you going?

**Mark Polanco:** And I was, no, I can't, I got too many things. So my kids, I just started them. So one of them has been boxing, the other one just started on the swim team. So my afternoons are just shot. And this is right in the middle of the afternoon, so I can't go. I mean, I need to call him anyway. So, yeah, but I need to get together with him. But hey, let's grab some lunch soon.

**Andres Urrego:** Okay.

**Mark Polanco:** Probably mid-May.

**Andres Urrego:** Yeah, yeah.

**Mark Polanco:** Yeah. And then we'll go from there, man. We'll celebrate.

**Andres Urrego:** Yeah, let's...

**Andres Urrego:** Yeah, I know it, my friend. I know it. So let's, yeah, let me, I'll meet with the team today. Once we get those things, we'll push your website, the regular website out. That way it's live. I'll add some of those documents. We'll test throughout the week. We'll make sure the CRM works. And then I'll let you know as soon as possible. And we'll find a time next week. We'll sit down, meet.

**Andres Urrego:** Get it, make it happen.

**Mark Polanco:** Yeah.

**Mark Polanco:** Okay, sounds like a plan.

**Andres Urrego:** I know you're ready to start deploying this, so I'll make sure we can make that happen.

**Mark Polanco:** Okay, I'm going to find this login and get it to you real quick so we can get that go ahead and launch it. So.

**Andres Urrego:** Alright, my brother sounds good.

**Mark Polanco:** Thank you, sir. Appreciate your time.

**Andres Urrego:** I appreciate you, my friend.

**Mark Polanco:** Alright, thank you. Bye, guys.

**Andres Urrego:** Thank you, bye, bye.
