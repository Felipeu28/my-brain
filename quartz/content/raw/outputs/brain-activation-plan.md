# FROM SENSOR TO SIGNAL
## Activating Andres's Brain: From Passive Accumulation to Active Intelligence

*April 2026 — Research + Thesis + Concrete Plan*

---

## PART ONE: EXECUTIVE THESIS

### The Problem Is Not the Data. It's the Architecture.

You've built something rare. Most people who talk about "second brains" have a folder in Notion and a Readwise account. You have bookmarks flowing in, Teams transcripts ingested, WhatsApp classified, project commits tracked, and a Quartz wiki backed by ChromaDB — all running on automations, every day. That is not a second brain. That is a nervous system without a brain attached to it.

Here's the uncomfortable truth: **storing more data will not help you work better.** The accumulation trap is the most seductive failure mode in personal knowledge management. The system feels productive because it's collecting. But collection is not intelligence.

Andrej Karpathy, who coined the LLM Wiki pattern in 2025, framed this precisely. His insight was that knowledge becomes useful not when stored but when *compiled* — pre-synthesized into structure that doesn't require retrieval. He built AutoResearch in early 2026 on this principle: a single autonomous loop that ran 700 ML experiments in two days and discovered 20 optimizations that a year of passive reading never would have. The key word is *loop*. Not archive. Loop.

Garry Tan published GBrain on April 9, 2026 — an open-source personal AI memory system comprising 10,000+ Markdown files, 3,000+ people pages, 280+ meeting transcripts, and 13 years of calendar data, running 20+ autonomous cron jobs. His stated thesis: *"GBrain is my attempt to be in control of my own personal AI that could become my intentionally designed cognitive armor. It's more important to be above the API line now than ever."* The key feature GBrain introduced: "dream cycles" — autonomous overnight processing where agents enrich and consolidate knowledge while Garry sleeps. He wakes up to a brain that is smarter than when he went to sleep.

You are six weeks behind Garry Tan's personal stack and six months ahead of the rest of the world. The window to move from sensor to signal is now.

### Why Now

Three converging forces make the transition from passive to active intelligence achievable today — not theoretically, actually:

**1. The infrastructure exists.** Anthropic launched Claude Managed Agents on April 8, 2026 — a hosted API that handles the full agentic loop: sandboxing, long-running sessions, tool execution, multi-agent coordination. The plumbing you used to have to build yourself is now a managed service. This matters because it changes the question from *"can I run persistent agents?"* to *"what should my agents do?"*

**2. The data advantage is perishable.** In December 2025, Meta acquired Limitless (formerly Rewind AI) — the company that built continuous personal capture. That signals that capture itself is becoming a commodity, absorbed by Big Tech. The moat is no longer having the data. The moat is being the first to turn YOUR specific data into decisions. That advantage narrows every month.

**3. The white space is enormous.** Garry Tan's analysis of Anthropic's February 2026 study showed that software engineering accounts for 49.7% of all agentic tool calls. Healthcare: 1%. Legal: 0.9%. Personal business intelligence: effectively 0%. You are not competing in a crowded space. You are building in territory that barely exists yet.

### The Core Thesis

**A Brain becomes valuable not when it stores well, but when it correlates across sources and surfaces non-obvious connections before you think to ask.**

Your bookmarks are not just bookmarks. They are *interest signals* — a real-time feed of what problems your subconscious is trying to solve. Your Teams meetings are not just transcripts. They are *relationship and decision signals* — who was in the room, what was decided, what was left unresolved. Your WhatsApp is *priority signals* — what people need from you, what you've committed to, what's urgent. Your project commits are *momentum signals* — what's moving, what's stuck, what's been abandoned.

Right now, those signals exist in isolation. The booking about AI pricing models sits next to the Moil pricing call transcript which sits next to your competitor's pricing change — but nothing connects them. The intelligence layer — the correlator — is missing.

**You have sensors. You don't have actuators.** This document is the plan to build them.

---

## PART TWO: GAP ANALYSIS

### What You Have

| Layer | What Exists | Status |
|---|---|---|
| Capture | Bookmarks, Teams transcripts, WhatsApp, commits, morning news | ✅ Running |
| Storage | ChromaDB (vector), Quartz wiki (structured markdown) | ✅ Running |
| Classification | Daily ingestion pipeline, categories assigned | ✅ Running |
| Retrieval | Can query ChromaDB, can search wiki | ✅ Functional |
| Synthesis | Manual / ad hoc | ⚠️ Weak |
| Cross-source correlation | None | ❌ Missing |
| Proactive output | None — only responds when asked | ❌ Missing |
| Action triggers | None | ❌ Missing |
| People intelligence | Data exists, not surfaced | ❌ Missing |

### What's Missing (The 20% That Gets 80% of the Value)

The gap is not more data sources. The gap is exactly three things:

**1. A daily correlation job.** Something that takes all of yesterday's data across all sources and asks: *"What connections exist here that don't exist within a single source?"* This is the core missing piece. It's a prompt, a cron job, and an output format. It could exist by the end of this week.

**2. A people intelligence layer.** You're working with a large number of people across multiple projects. You have data on all of them. But nothing tells you: *"You haven't connected with [person] in three weeks and they're linked to two active deals."* Or: *"[Person] showed up in both a Teams meeting and a WhatsApp thread this week — there's a convergence there worth noticing."* Relationship graphs are the highest-ROI intelligence layer for anyone who sells, manages, or collaborates.

**3. Proactive outputs.** Right now your Brain is a library. Libraries are passive — they wait to be consulted. What you need is an editor — something that prepares a briefing you didn't know you needed, flags the anomaly you would have missed, and surfaces the opportunity hiding in the noise. The output format matters: it needs to be embedded in your existing daily workflow (morning briefing), not a new interface you have to learn to check.

### The Accumulation Trap

The seductive wrong answer is: *"Let's add more sources."* More Slack channels. Emails. LinkedIn. Browser history.

Resist this completely. More data without a correlation engine is just more noise. The value curve of additional data sources is sharply diminishing. The value curve of correlation quality on existing sources is sharply ascending. Every hour spent adding a new data source is an hour not spent building the intelligence layer. Freeze the inputs at their current state and activate what you already have.

---

## PART THREE: PHASED IMPLEMENTATION

### Phase 1 — Quick Wins (Weeks 1–2): The Signal Brief

**Goal:** Ship one proactive output that proves the concept and changes your daily experience.

**The Signal Brief** is a short daily section added to your existing morning briefing. It contains exactly three things:

1. **The Cross-Source Connection** — One non-obvious link that appeared across two or more data sources yesterday. Example: *"You bookmarked two articles about infrastructure pricing models (bookmarks), and your Moil-Pricing meeting transcript from Tuesday mentions an open question about tiered plans (Teams). These are the same problem."*

2. **The Active Person Flag** — One person who showed up in multiple sources yesterday and what it means. Example: *"[Name] appeared in a WhatsApp thread (priority: high), a Teams meeting (decision: deferred to them), and a bookmark you tagged under their project. They are a critical node this week."*

3. **The Silence Anomaly** — One topic, project, or person that has been quiet when it shouldn't be. Example: *"No activity on Project X for 8 days. Last mention: commit on April 14. Last meeting: April 11. This has stalled."*

**What this requires:**

- One Python script (the correlator) that pulls yesterday's data from ChromaDB across all source types
- One Claude API call per day with a structured prompt: "Given this multi-source data from the past 24 hours, identify: (1) one non-obvious cross-source connection, (2) one person who is a high-frequency node, (3) one silence anomaly"
- Output appended to the morning briefing markdown before you read it

**Estimated build time: 3–5 hours.** This is the highest-leverage move in the entire plan. Ship this before anything else.

---

### Phase 2 — Correlation Engine (Weeks 3–6): The Intelligence Layer

**Goal:** Build the infrastructure that makes correlation systematic, not ad hoc.

**2A. The Entity Graph**

Build a people-and-projects graph on top of your existing ChromaDB data. Every time a person's name appears in a data source, log:
- Source type (Teams / WhatsApp / bookmark / commit)
- Date
- Project context (if detectable)
- Sentiment signal (did they ask something of you? did you commit something to them?)

This doesn't require a separate database. It can live as a structured set of Markdown files in your Quartz wiki — exactly the GBrain pattern Garry Tan uses. One file per person. Updated nightly by an agent.

The agent's job: scan yesterday's data for entity mentions → update each person's file with new context → flag any person who has crossed a threshold (last contact > 14 days + active in 2+ projects = surface for follow-up).

**2B. The Weekly Trend Detector**

Every Sunday evening, a second agent runs a longer synthesis across the full week. Its job: identify which themes, topics, and problems appeared across multiple sources throughout the week. What kept surfacing? What you bookmarked on Monday and then talked about in a meeting on Thursday is not a coincidence — it's a signal of where your mind is actually focused, often ahead of where your calendar is focused.

Output: a "Brain Weekly" digest (one page) delivered Monday morning with:
- Top 3 recurring themes this week
- Top 3 people by activity
- Projects with momentum vs. projects with silence
- One recommended action based on the pattern

**2C. Project Intelligence Snapshots**

For each active project, run a weekly synthesis that pulls all related data (meetings, bookmarks, messages, commits tagged to that project) and produces a one-paragraph project brief: what's moving, what's stuck, what the data suggests should happen next.

This replaces the mental overhead of tracking project status across fragmented sources. The Brain maintains the state. You don't have to.

---

### Phase 3 — Proactive Intelligence at Scale (Weeks 7–12)

**Goal:** The Brain stops being a system you query and becomes a system that surfaces decisions.

**3A. The Agentic Loop (Claude Managed Agents)**

Implement a persistent agent — using Claude Managed Agents API (launched April 8, 2026) — that runs as a background process. Its behavior:

- At end of each day: correlate, produce Signal Brief, update entity graph
- On detection of a convergence (same person/topic/project across 3+ sources in 48 hours): surface an alert
- Weekly: produce Brain Weekly, update project snapshots
- On silence threshold crossed: flag the anomaly

This is Karpathy's AutoResearch pattern applied to personal intelligence instead of ML experiments. The loop runs continuously. You set the triggers and the output formats. The agent does the rest.

**3B. Pre-Meeting Briefing**

Before any Teams meeting (detectable from calendar), auto-generate a one-page briefing: who's in this meeting (pull their entity files), what was discussed last time (pull prior meeting transcripts), what bookmarks and messages are related to the meeting topic (ChromaDB query), what's unresolved (last meeting → this meeting delta).

This exists before you open the meeting. No preparation required.

**3C. The Recommendation Engine**

Train a simple classification layer on top of your correlation output: when does a cross-source signal warrant (a) just a note, (b) a flagged recommendation, or (c) an urgent alert? Start with rule-based thresholds (3+ sources, <48 hours, high-priority contact = urgent). Over time, your feedback on each output teaches the system what matters to you.

---

## PART FOUR: SPECIFIC SCRIPTS AND AUTOMATIONS (PRIORITY ORDER)

### Priority 1: The Daily Correlator (Build This First)

```python
# daily_correlator.py
# Runs at 6:00 AM every day via cron
# Queries ChromaDB for yesterday's data across all sources
# Calls Claude API with correlation prompt
# Appends output to morning briefing

import chromadb
from anthropic import Anthropic
from datetime import datetime, timedelta

CORRELATION_PROMPT = """
You are analyzing yesterday's data from a personal intelligence system.
Data sources: bookmarks, Teams meeting transcripts, WhatsApp messages, project commits.

Below is all data ingested in the last 24 hours, tagged by source type.

Your job:
1. CROSS-SOURCE CONNECTION: Identify ONE non-obvious connection that spans multiple sources.
   Do not surface connections within a single source. Find the link across sources.
   Format: "[Source A]: [finding] connects to [Source B]: [finding] because [reason]"

2. ACTIVE PERSON FLAG: Identify ONE person who appeared across multiple sources.
   Format: "[Name] — appeared in [sources], context: [brief], signal: [what this means]"

3. SILENCE ANOMALY: Identify ONE project or topic that has gone quiet unexpectedly.
   Compare against typical activity levels. Flag anything with 7+ days of silence.
   Format: "[Topic/Project] — last active [date], expected activity: [why it matters now]"

Be specific. Be non-obvious. Surface things Andres wouldn't think to ask about.

DATA:
{data}
"""

def run_daily_correlation():
    client = chromadb.Client()
    collection = client.get_collection("brain_data")
    
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    
    # Query all sources from yesterday
    results = collection.query(
        query_texts=[""],
        where={"date": {"$gte": yesterday_str}},
        n_results=200
    )
    
    # Format for Claude
    formatted_data = format_results_by_source(results)
    
    # Call Claude
    anthropic = Anthropic()
    response = anthropic.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": CORRELATION_PROMPT.format(data=formatted_data)
        }]
    )
    
    # Append to morning briefing
    signal_brief = response.content[0].text
    append_to_morning_briefing(signal_brief, yesterday_str)
    
if __name__ == "__main__":
    run_daily_correlation()
```

### Priority 2: Entity Graph Builder

```python
# entity_graph_builder.py
# Runs nightly at midnight
# Extracts entity mentions from yesterday's data
# Updates person files in Quartz wiki
# Flags follow-up candidates

ENTITY_EXTRACTION_PROMPT = """
Extract all person mentions from this data.
For each person, identify:
- Name (normalize variations)
- Source type where mentioned
- Context (what were they doing / asking / deciding)
- Any commitment made to them or by them
- Project association (if detectable)

Output as JSON array.

DATA: {data}
"""

PERSON_UPDATE_PROMPT = """
Given this new activity data for {name} and their existing profile,
update their person file.

Add new context, update last contact date, flag any open commitments.
Keep the file under 500 words. Prioritize recency.

EXISTING PROFILE: {existing_profile}
NEW ACTIVITY: {new_activity}
"""

def build_entity_graph():
    # Extract entities from yesterday's data
    # For each entity, update their Quartz wiki page
    # Flag anyone with: last_contact > 14 days AND active in 2+ projects
    pass
```

### Priority 3: Weekly Brain Digest

```python
# weekly_digest.py
# Runs Sunday at 8:00 PM
# Synthesizes the full week across all sources
# Produces "Brain Weekly" delivered Monday morning

WEEKLY_SYNTHESIS_PROMPT = """
You have access to a full week of data from Andres's personal intelligence system.

Produce a "Brain Weekly" briefing with exactly:

THEMES (3 max): What kept surfacing across sources this week?
These are NOT calendar items. These are patterns in what Andres's attention 
kept returning to — in bookmarks, in conversations, in meetings.

TOP PEOPLE (3 max): Who was most active this week across all sources?
Include why each person matters this week specifically.

MOMENTUM vs SILENCE:
- Projects with clear forward momentum (evidence: commits, meetings, messages)
- Projects that have gone quiet (evidence: absence of activity)

ONE RECOMMENDED ACTION: Based purely on the data patterns this week,
what is the single most important thing Andres should do on Monday?
Be specific and directional. Not "follow up with your team." Tell him who, about what.

DATA: {week_data}
"""
```

### Priority 4: Pre-Meeting Briefing

```python
# meeting_briefer.py
# Triggers 30 minutes before each Teams meeting (via calendar webhook)
# Generates a one-page contextual briefing

PRE_MEETING_PROMPT = """
Andres has a meeting in 30 minutes: {meeting_title} with {attendees}.

Using the Brain data, generate a pre-meeting briefing:

PEOPLE CONTEXT: For each attendee, summarize: last interaction, 
any open commitments, their current project involvement.

LAST SESSION: If this is a recurring meeting, what was discussed last time?
What was decided? What was left unresolved?

RELEVANT DATA: What bookmarks, messages, or notes from the past two weeks
are directly relevant to this meeting's likely agenda?

SUGGESTED FOCUS: Based on the data, what is the most important thing 
to resolve or advance in this meeting?

Be brief. This is a one-page briefing, not a report.
"""
```

### Priority 5: The Silence Detector (Standalone Cron)

```python
# silence_detector.py
# Runs every 48 hours
# Scans for projects/topics/people that have gone quiet
# Threshold: 7 days silence + currently active in 2+ other sources

def detect_silence_anomalies():
    """
    Surface the things that shouldn't be quiet.
    Active projects lose momentum silently — no one announces a stall.
    This catches it.
    """
    # Query entity graph for last activity dates
    # Compare against activity baseline (rolling 30-day average)
    # Flag: silence > 7 days AND entity was active in prior 30 days
    # Output: list of anomalies with last activity date and context
    pass
```

---

## PART FIVE: THE MOIL CONNECTION

This is where the meta-lesson lives, and it's worth being explicit about it.

**What you are building for yourself is the prototype for what Moil sells.**

Garry Tan's white space data is directional evidence: software engineering consumes half of all agentic AI usage. The other half — healthcare, legal, sales, operations, personal business intelligence — is essentially unbuilt. Under 5% utilization across all of it. The reason is not lack of interest. The reason is lack of a working prototype. Most founders pitch "AI that works on your business data" without having personally built a system that actually does it.

You are building that system. Every automation you create for your own Brain is a validated proof point. Every correlation that surfaces a non-obvious connection is evidence that the system works. Every pre-meeting briefing that changes how a conversation goes is a testimonial you can give yourself.

Karpathy's framing is useful here. He argues that AI applications in the next phase will succeed by supplying three things that general-purpose AI models lack: *private data, sensors, and feedback loops.* Your Brain has all three. The question for Moil is: can you externalize this architecture for other knowledge workers?

The Brain becomes the pitch:
- "We've built this for ourselves. It runs daily. Here's what it surfaces."
- "The gap between passive capture and active intelligence is exactly what we solve."
- "We're not selling a tool you have to maintain. We're selling intelligence that updates itself."

**The sequence:** Build it for yourself → prove it changes your daily work → show it to potential customers as a live demo → build Moil's product on the same architecture with a customer-facing interface.

The most credible founder pitch is not "I have an idea for this." It's "I built this for myself, it works, and I want to sell it."

---

## CLOSING: THE ONE THING TO DO THIS WEEK

Stop adding sensors. Build one actuator.

The daily correlator — Priority 1 above — takes 3–5 hours to build against your existing ChromaDB data and morning briefing pipeline. It will change how your day starts on Day 1. It does not require Phase 2 or Phase 3 to be useful. It is the minimum viable proof that your Brain can do something other than remember.

Everything else in this document flows from that first proof. Build the correlator. Run it for two weeks. See what it surfaces. Then decide what to build next based on what was missing from the output.

That is the YC approach applied to your own cognitive infrastructure: launch something real, get real signal, iterate fast.

You have the data. You have the pipeline. You have the infrastructure. The only thing missing is the loop.

Close the loop.

---

*Document prepared April 22, 2026. Research draws on: Karpathy's 2025 LLM Year in Review and AutoResearch (March 2026); Garry Tan's GBrain release (April 9, 2026) and white space analysis of Anthropic's agent usage data (February 2026); Anthropic's Claude Managed Agents launch (April 8, 2026); Limitless/Meta acquisition context (December 2025).*
