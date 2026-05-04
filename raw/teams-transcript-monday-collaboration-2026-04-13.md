---
type: transcript
ingested: true
ingested_at: 2026-05-04
---

# Teams Transcript: Monday Collaboration — 2026-04-13

**Meeting:** Monday Collaboration
**Date:** April 13, 2026, 8:17am–10:00am CT (13:17–15:00 UTC)
**Organizer:** Jacob Oluwole
**Attendees:** Andres Urrego, Jacob Oluwole, Abiodun Adekanmi (Ablad), Adeleke Tolulope (Steve), Taiwo Ola Balogun

---

## Key Decisions & Action Items

### Brain / Knowledge Base Demo (First ~30 min)
- Andres demoed the Moil Brain (Obsidian + Quartz knowledge base) to the full team
- Showed team profiles, customer profiles, org connections, project tracker, and the visual graph (143 nodes, 699 connections, 187 wiki pages, 78 raw sources ingested)
- Brain ingests transcripts weekly on Fridays; also ingests emails, X bookmarks, and meeting data
- **Decision:** Andres wants to clone the Brain repo for each team member so they can have their own personal "brains" once the system is stable
- **Action:** Andres to fix client project connectors in the knowledge base (FitLogic and others not linking properly)

### Inna Benyukhis — 10am Meeting Prep
- Andres has a 10am meeting with Inna today
- Reviewed Inna's CRM (Empowered Wellness with Inna) — looks good visually
- **Issue:** CRM not reading contacts in the pipeline
- **Issue:** Campaigns API key not yet added for Inna's account
- **Action:** Need to verify and fix contact pipeline display and campaigns API key before or after the meeting

### PDF/PowerPoint Document Generation (Steve/Adeleke)
- Steve tested PDF generation — first test produced output but formatting needs significant work
- Logo was generated; needs a non-colored background version added
- **Action:** Steve to create a testing folder in the repo branch to upload reference PDFs for Claude Code to iterate on
- **Action:** Steve to continue fixing formatting issues and feed results back to the AI
- Steve also pushed updates to staging: image creation in Business Coach, monitoring improvements

### Meridian Buda — Stripe Webhook (Taiwo)
- **Blocker:** Stripe webhook URL not configured for Meridian's ticketing system — ticket confirmation emails not sending
- Taiwo will send the endpoint URL to Andres to add in Stripe's developer section (Meridian test account)
- **Issue:** Cron job secrets in Vercel are using placeholder values, not real secrets
- **Action:** Taiwo to update the Vercel secrets and send Andres the Stripe webhook endpoint
- **Action:** Andres to configure the webhook in Stripe test mode as soon as he gets the endpoint
- Meridian email sending works via Resend (partner email, limited to 100/day) — sufficient for now

### Content Calendar (Ablad/Abiodun)
- Ablad sent content links to the group but is behind on video format content
- Ablad testing Business Coach and flyer creation tool — finding issues with image dimensions and formatting
- **Action:** Ablad must keep detailed testing notes open while testing (reiterated from Friday)
- **Goal:** Get content for the following week ready by Friday so Mondays are for strategizing, not catching up

### New Client — Massage Place
- Andres added a new client project (massage business) — website is nearly done, just needs images
- **Action:** Taiwo to create a client handoff document listing everything clients need before project handover (Vercel accounts, Supabase, Resend, login instructions, etc.)

### Sun Show Event (Next Week)
- Moil invited to showcase at a local event series next week (likely Travis Sutherland's "Sun show")
- Will have a table to demo Moil products

### Google Alloy Image Testing
- Andres meeting with someone about Alloy (Google image generation) tomorrow
- **Action:** Jacob to start testing Alloy image generation inside Moil — if it works, could charge clients without extra work

### General Team Direction
- "Big week" — many projects in flight, Andres urged the team to stay connected and not disappear
- Emphasis on speed: if one project is blocked, immediately start on another
- Andres encouraged team to actively learn and engage with AI tools and links he shares

---

## Full Transcript (VTT)

WEBVTT

00:00:03.478 --> 00:00:23.398
<v Andres Urrego>You know, recorded calls, emails, messages, they create, so let me show you how much detail this has, right? So, you know, Jennifer, it's related to Jennifer Storm, Joshua Edmund, Jackie Martinez, ADO, positioning, go to market, right? So, all of this, it...</v>

00:00:23.478 --> 00:00:37.078
<v Andres Urrego>This is how it's related to positioning, for example. Moil positioning, blah, blah, blah, blah, one line pitch, right? And so it basically is connected to our entire business and our entire operation.</v>

00:00:38.918 --> 00:00:59.958
<v Andres Urrego>So it's connected to basically, so it's my brain replicated. So now let me show you how it works for you guys. So, by the way, I didn't type any of this. This is all automatically created based on the data that on all the touch points and every email and every message and every, there's gaps. And I've noticed because it's, I don't think it's ingested everything yet.</v>

00:01:00.198 --> 00:01:10.118
<v Andres Urrego>But now, he has done such a good job so far that I can only imagine where this will be in two years after he continues to know me, after he continues to understand what I do, what I learn, what I...</v>

00:01:11.798 --> 00:01:30.518
<v Andres Urrego>So, right, so it, it, what's the strategic value of the Buda Buda EDC or Buda High for us? Revenue per seat model licenses, social proof is a city CT EDC as a customer plus generator for storm endorsement expansion pad replicate with other cities EDC.</v>

00:01:30.638 --> 00:01:39.078
<v Andres Urrego>Product, product placement, entrepreneurs become more power users, positioning Andres is respected coach, not just a founder selling software.</v>

00:02:15.038 --> 00:02:23.398
<v Andres Urrego>Ta da, Steve has his own Wikipedia page, or my own. You have your own page in my brain. Of course, we all do, right? We all have.</v>

00:02:35.318 --> 00:02:45.558
<v Andres Urrego>So some of the things, again, are going to be inconsistent, but it will continue to fix them, to learn them every week, because now every week it will ingest new things about Moil.</v>

00:03:00.998 --> 00:03:10.518
<v Adeleke Tolulope>Okay, how is it going to ingest information about us on a weekly basis? Is it connected to Teams Chats or...</v>

00:03:10.518 --> 00:03:31.918
<v Andres Urrego>So it's connected to like, like our transcripts. So like I'm feeding it our transcripts every week. So after our calls, you know, we're going to get our transcripts and then every Friday it's going to run everything like the transcripts from the calls. It will, you know, see what I'm saying? So it will run like, it will, it will even know what projects, what projects you work on.</v>

00:03:34.838 --> 00:03:59.598
<v Andres Urrego>Yeah, like you will even know as we continue to go. Again, remember, this is just a few, probably, I don't know how many emails is read on you, you know, from the emails that I share or yeah, where I give access to my email and then our transcripts. So so far is what it knows, right? But again, it's from here forward, it will continue to ingest it once a week.</v>

00:10:37.638 --> 00:10:45.718
<v Andres Urrego>Okay, so like what concepts I'm interested in. So like for example, Moil 360, bam, bam, let's go to Moil 360. There we go.</v>

00:10:47.158 --> 00:11:05.238
<v Andres Urrego>There you go. So see, like, I'll never have to even, if I say I need a pitch deck for investors, it will know exactly everything I need, everything about the business. So AI is most full service marketing hiring package for SMBs, turn around.</v>

00:13:15.078 --> 00:13:33.318
<v Andres Urrego>Yeah, so I mean, it is, look, the Moil positioning, right? One line pitch, Moil is an AI co-founder of a small business it serves. Market research, business plan, 30-day content engine, smart hiring across 10 plus platforms and 24-7 coaching, all from 21 questions starting at $15 a month.</v>

00:20:13.158 --> 00:20:22.678
<v Andres Urrego>All right, guys, back to work. So I think honestly this is, and let's get this right, and I think everyone of you guys should have.</v>

00:20:23.878 --> 00:20:44.518
<v Andres Urrego>your own little brain to dump in. Let me just get it right. And then what we'll do is we just clone the repos and then you guys just have your own little brains. The cool thing is from here on, like weekly, I can give it personal things if I want to. I can, you know, talk about my family. I can do whatever, whatever, anything I need, right?</v>

00:21:07.638 --> 00:21:14.038
<v Andres Urrego>It has 100 and eighty-seven wiki pages, and Roll sausage ingested seventy-eight so far out there.</v>

00:21:10.358 --> 00:21:14.038
<v Andres Urrego>699 connections, 143 nodes.</v>

00:22:31.238 --> 00:22:35.318
<v Taiwo Ola Balogun>I was it was this one on the because I saw it article on cloud and obsidian.</v>

00:22:42.518 --> 00:22:48.358
<v Taiwo Ola Balogun>Okay, you is it is it from the article you did this? I think I saw that on X on cloud and obsidian.</v>

00:22:47.718 --> 00:23:09.878
<v Andres Urrego>So, I, I, I, yeah, I did it from from actually the so Andrew Karpathy is the so this this has, so there's two things on the background it has the repo from from that guy which was an an ex-Tesla, one of the guys that you know helped to build Tesla and has done other amazing things.</v>

00:24:15.478 --> 00:24:32.118
<v Andres Urrego>in these large machines that they have, so they can actually use their own AI with their own information and never have to worry about anything, right? For us, it's more of like, okay, we're collecting the data today so that we can do exactly that very soon.</v>

00:27:06.998 --> 00:27:09.958
<v Andres Urrego>Right, so it it literally does.</v>

00:28:51.038 --> 00:29:13.398
<v Andres Urrego>when you don't even have to look at it or worry about it because you know it's just absolutely ingesting your mind, your brain, absolutely learning from everything that I'm doing, that I'm working on. Yeah, pretty cool, pretty cool. I mean, I'm sure it's gonna take a little while to probably set it up all the way correctly for it to learn everything it needs to learn, everything I need to teach it, but.</v>

00:33:11.318 --> 00:33:33.478
<v Andres Urrego>And it's so cool that, again, we're already there. So it's almost like we're living in the future, guys. We are at the beginning. Maybe we were early. You know, maybe we started building early when AI was still kind of slow, but it's not there anymore. And that gives us an amazing advantage because everybody else got stuck behind thinking AI wasn't going to work.</v>

00:34:07.918 --> 00:34:12.198
<v Andres Urrego>Now we have, how many projects did I say, 12 projects, 10 projects?</v>

00:34:14.278 --> 00:34:21.158
<v Andres Urrego>We might, we might close all of them, and all of them will buy Moil 360, and all of them will buy all the products that we're gonna build for them.</v>

00:35:56.918 --> 00:36:13.718
<v Andres Urrego>So anyways, all right guys, so lots of work for this week. I got two meetings, one at 10, one at 11, a meeting at 10 with Inna. So I want to look at Inna CRM. How is Inna CRM looking? Did we, I, this just needs to be.</v>

00:36:17.958 --> 00:36:24.438
<v Andres Urrego>This just needs to be something that I can show her, that's all. Okay, very good. Yeah, I love it. This looks pretty, man.</v>

00:36:47.478 --> 00:36:53.478
<v Andres Urrego>Yeah, but it's not reading the contacts in the pipeline. Interesting. Okay. Appointments.</v>

00:46:50.918 --> 00:46:53.558
<v Andres Urrego>Steve, how did you go with the PowerPoint and PDF stuff?</v>

00:47:12.998 --> 00:47:33.398
<v Adeleke Tolulope>So, I'm just testing the the PDF and the PPTC, so though I run into a lot of I run I run into some conflicts, some bugs which I already fixed, so I just made my first test of the PDF document, though it still required it required a lot of.</v>

00:47:33.798 --> 00:47:38.598
<v Adeleke Tolulope>It still requires some work, so the formatting, but at least it's a good start.</v>

00:48:06.118 --> 00:48:18.918
<v Andres Urrego>I, yeah, initially that's how it was built, right? That's kind of what I want to test first to make sure that, can we do it, right? So, but if we can, then we'll strip it without it.</v>

00:56:20.558 --> 00:56:29.878
<v Andres Urrego>Okay. All right, Steve, so you work on those. Let me know what you find. Abla, Jacob, where are we on the content for this week?</v>

00:56:34.478 --> 00:56:51.318
<v Andres Urrego>But I know you got everything pushed out early on last week, so I was hoping, I was hoping we would have had, hopefully by Sunday, something to review or, you know, at the latest, right, something to review for this week so that we wouldn't come into Monday kind of empty-handed.</v>

00:57:13.958 --> 00:57:33.758
<v Andres Urrego>Hey, like I said, let's just, again, let's just make sure, try, I mean, this should be your goal going forward, right? Every week, okay, how do I make sure I get to Friday and already have next week so I don't have to worry about it on Monday, you know, so that on Mondays you can strategize for the week after and then start your work that week for the week.</v>

00:58:32.878 --> 00:58:54.358
<v Andres Urrego>You said you'd be okay, but remember what I said Friday, Adeleke? I don't want you guys testing anything without writing notes. So like, if you're, I want you to, because it's so hard to remember everything that we run into, like the only way you can add your expertise directly into the tool is if you actually write these notes down.</v>

01:02:04.558 --> 01:02:25.798
<v Andres Urrego>Yeah, yeah, see, so if you have the reference image, try that too. You know, try that too. See if you can create a new image with your reference image. And Jacob, I want you to start testing the alloy ones because I'm meeting with them tomorrow. So I want us to start testing the alloy ones. I mean, right now we know Gemini can do it, but I want us to start testing it directly inside of Moil because...</v>

01:02:26.118 --> 01:02:32.438
<v Andres Urrego>If we can do that, we would literally be able to charge them without having to add extra work.</v>

01:03:29.153 --> 01:03:50.273
<v Andres Urrego>Big week, guys, so stay connected. Please don't disappear this week. Big week. I mean, we got a lot to do, a lot, like so many projects, so many projects. So I just added another project to the table, which I told Jacob about on Friday. It's for a massage play, so that one is basically done, honestly, with the website that we have.</v>

01:03:50.593 --> 01:04:09.873
<v Andres Urrego>just need to add images and things for her, but that website's going to be completed soon. I asked Taiwo to kind of create a document, and Taiwo, please get this done to me as soon as possible. A document of things that we will need to have and create for the clients, so the clients create themselves before we hand the projects over.</v>

01:04:10.113 --> 01:04:31.953
<v Andres Urrego>We need to be very organized there to make sure that the handoffs are going to be clean, that the handoffs are very, very structured. You know, that they're Vercel accounts, they're super based, they're resend, you know, what are the instructions to log into these accounts? I mean, all of those things we got to think about because we're basically giving people access to their own software.</v>

01:04:40.353 --> 01:04:46.033
<v Taiwo Ola Balogun>Andres, we have not set up the web URL.</v>

01:04:47.953 --> 01:04:49.873
<v Taiwo Ola Balogun>The webhook URL for this stripe.</v>

01:04:52.993 --> 01:04:59.153
<v Taiwo Ola Balogun>But that is the reason why it's not, that is the reason why it's not sending the ticket emails, the ticket mail emails.</v>

01:05:09.633 --> 01:05:15.233
<v Taiwo Ola Balogun>So, you can you can set it up now, because I will send you the the um endpoints.</v>

01:11:14.353 --> 01:11:33.633
<v Andres Urrego>Just let me where I need, let me know where I need to do it. Just research it, let me know where I need to do it. That way I can get it done as soon as I have a minute, because we can't wait. I need us moving. And if we're done with Meridian and this is the last thing that we need to do, I don't want you waiting until I get back. Let's start on something else, okay?</v>

01:11:33.873 --> 01:11:48.593
<v Andres Urrego>Let's start on the other ones. We definitely need to move fast. So thank you, thank you, thank you guys. I gotta go. I was, I needed to leave 5, 10 minutes ago. All right, talk to you in a bit. Catch you guys later. I'll jump back on the call as soon as I'm done with everything though, but thank you guys. Talk to you in a bit. Bye bye.</v>
