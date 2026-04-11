# The Brain System: A Practical Guide for Andres

Your Brain system is a multiplier for how you think, learn, and build. It's not a note-taking app—it's a personal research engine that compounds knowledge across sources, surfaces patterns you'd miss alone, and makes your thinking faster and sharper.

---

## Section 1: The Full Brain Architecture

Your system works in layers:

```
X Bookmarks → Obsidian raw/ → Processing → LLM Wiki → Queries
     ↓              ↓              ↓            ↓          ↓
  Weekly        Unfiltered     Themes &     Knowledge   Answers
  Collection     Content       Takeaways     Graph      w/ Context
```

**Layer 1 — Collection (X Bookmarks):** Weekly, Claude Cowork pulls your bookmarks and categorizes them into topics (Claude/AI Agents, Knowledge Management, Video AI, Marketing/Sales, Models/Research, Dev Tools, Business). This is your raw signal—unfiltered, timestamped, topical.

**Layer 2 — Storage (Obsidian raw/):** Files land in `raw/x-bookmarks-YYYY-MM-DD.md` with sections, bullet points, emoji tags, a stats table, and a "Themes & Takeaways" summary. Low-friction by design—speed over beauty.

**Layer 3 — Processing (You):** Over a few days, skim these files. Highlight what's genuinely useful. Some items get cross-linked to existing notes; some become seeds for deeper work. Most stay in raw/ as searchable reference.

**Layer 4 — LLM Wiki (The Brain):** Monthly, feed Claude batches of your processed notes + raw bookmark files. Claude builds a synthesis document—a personal knowledge graph showing connections, your patterns, and emergent themes across months. This is compression + insight on top of your notes.

**Layer 5 — Query (Answering Questions):** When you need to think through something, feed Claude your LLM Wiki + recent raw files + your question. Claude answers using *your* context—not generic web knowledge. 10x more useful than Google for decisions in your space.

The magic is the **Themes & Takeaways** section. Over time, these 2-3 bullet summaries per week become a compressed history of what you've been learning—searchable, indexable, and great for priming pattern recognition.

---

## Section 2: How to Use It Right Now

### Daily (10 min)
- Open the latest `x-bookmarks-YYYY-MM-DD.md` in Obsidian
- Skim Themes & Takeaways to prime your thinking
- If something connects to a live project, drop a reference: `"See raw/x-bookmarks-2026-04-11.md / Video AI section"`

### Weekly (30 min)
- When the new digest lands, review it
- Highlight top 5 items worth deeper work
- Create 1-2 new notes from insights; link 2-3 items to existing notes via `[[wiki links]]`
- Delete or archive low-signal items so raw/ stays useful

### Monthly (20 min synthesis)
Collect the 4 most recent `x-bookmarks-*.md` files and run this prompt:

```
You are building a personal knowledge graph for my Brain.
Given these 4 weeks of bookmark digests:

[paste 4 files here]

Create a synthesis that:
1. Lists emerging patterns across weeks
2. Identifies which topics are accelerating
3. Extracts my key assumptions as they appear in bookmarks
4. Suggests 3 areas worth deeper exploration
5. Flags any contradictions or belief shifts

Format: markdown, ~500 words.
```

---

## Section 3: How to Keep Improving It

### Automate the Collection
In Claude Cowork → Schedule a weekly task:
- **Frequency**: Every Monday, 9 AM
- **Task**: Run the X bookmark sweep (the workflow we built this session)
- **Output**: Auto-save to Obsidian `raw/x-bookmarks-YYYY-MM-DD.md`

Once this is scheduled, the collection is a utility—not a chore.

### Build a Processing Checklist
Create `PROCESSING_CHECKLIST.md` in Obsidian:
```markdown
## Weekly Processing (30 min)
- [ ] Skim Themes & Takeaways
- [ ] Mark 5 items worth deeper work
- [ ] Create 1-2 new notes from insights
- [ ] Cross-link to 2-3 existing notes
- [ ] Archive or delete low-signal items
```

Run this every Friday. Without it, raw/ becomes a graveyard.

### Add More Data Sources
Right now you're pulling X bookmarks only. Next sources to add:
- **Email digests**: Route key newsletters to a folder → Cowork summarizes weekly into `raw/digests-YYYY-MM-DD.md`
- **Slack**: Dedicated #brain-feed channel → weekly Cowork pull
- **GitHub activity**: What you shipped/starred that week
- **Reading list**: Pinboard, Readwise, or similar

Each source gets its own `raw/` file. Monthly, feed them all to Claude for combined synthesis.

### Create Topic-Specific Skills in Cowork
- **"Give me a marketing digest"**: Pull all bookmarks tagged #marketing, synthesize
- **"What am I thinking about AI agents?"**: Query all notes on that topic, show evolution
- **"Compare my stance on video AI 3 months ago vs now"**: Feed old + new files, highlight shifts

These become 10-second power queries — what would take 30 minutes of manual work.

### Build Your MOIL.md Context File
Create `MOIL.md` in your vault. This is your "Mission, Operating Principles, Identity, Legacy" file:

```markdown
# MOIL.md — Andres Context

## What I'm Building
[Describe MOIL and what it does]

## Operating Principles
- [Principle 1]
- [Principle 2]

## What Kinds of Insights Matter Most
- [e.g., distribution > product, AI leverage, async-first]

## 3-Year Vision
[Where this goes]
```

Feed this to Claude before any big query:
```
[MOIL.md as context]

Given my mission and principles, how should I think about [question]?
```

This ensures Claude sounds like *you*, not generic internet advice.

---

## Section 4: Best Practices for Querying the Brain

### Pattern 1 — The Synthesis Query
```
Files: MOIL.md + 3 months of x-bookmarks-*.md + LLM_Wiki_latest.md

"Show me the most important pattern in my thinking over the last 3 months.
What am I obsessed with? What's changing?"
```
Output: 300-word synthesis of your own intellectual evolution.

### Pattern 2 — The Decision Query
```
Files: Relevant brain files + decision at hand

"I'm deciding between [option A] and [option B].
What do my notes suggest about this? Where do I lean?"
```
Turns your Brain into a decision oracle grounded in your own history.

### Pattern 3 — The Deep Dive
```
Files: All files tagged with [topic]

"Teach me everything I know about [topic].
Structure it as if briefing a new team member.
What are my non-obvious insights?"
```
Use for onboarding, writing, or exposing blind spots.

### The Themes & Takeaways Secret
These short summaries are gold. Over a year you'll have 50+. Once a quarter, read *only* the Themes & Takeaways from all digests in sequence — skip the full files. You'll see patterns and belief shifts in 20 minutes that would take days of manual review.

---

## Section 5: Future Roadmap

| Timeline | Milestone |
|---|---|
| Month 1–2 | X bookmark automation running + process religiously + build MOIL.md |
| Month 2–3 | Add email digests + Slack channel → 3 data streams into raw/ |
| Month 3–4 | First monthly LLM Wiki synthesis — patterns you didn't consciously notice |
| Month 4–5 | Topic-specific Cowork skills — "marketing digest" becomes a power move |
| Month 6 | Feed Brain output into live projects; use queries to inform product decisions |
| Month 12 | Queryable decision engine grounded in 12 months of compressed personal knowledge |

---

## Section 6: Quick Reference Card

| Action | Frequency | Time | Output |
|---|---|---|---|
| Review weekly digest | Weekly | 10 min | Primed for the week |
| Process bookmarks | Weekly | 30 min | 5 new connections |
| Monthly LLM synthesis | Monthly | 20 min | Knowledge graph update |
| Query the Brain | As needed | 5–10 min | Answer in your voice |
| Update MOIL.md | Monthly | 30 min | Sharp context for Claude |

**Key Habits:**
- Every Thursday: Skim Themes & Takeaways ("What was the signal this week?")
- Every Friday: Create 1 new note from a bookmark
- Every month: Feed 4 digests to Claude for synthesis
- Every quarter: Full Brain query for a major decision

**Power Prompts:**
```
"What patterns am I not seeing in my bookmarks over the last 30 days?"
"Based on what I've been saving, where should I double down?"
"What did I believe about [topic] 3 months ago vs now?"
"What's the most actionable insight from this week's digest for [project]?"
```

---

## The One Thing to Remember

The system is only as good as your willingness to process. Automation collects—**you** create meaning. Spend 30 minutes a week turning raw signal into insight, and in 6 months you'll have a thinking partner that knows your mind better than any tool you've ever used.

Collection is automatic. Processing is the discipline. Synthesis is the payoff.
