# BRAIN ACTIVATION — IMPLEMENTATION PLAN
## Moil Brain: From Sensor Array to Intelligence Engine

*April 22, 2026 — Ground-truth implementation plan built against actual codebase state*

---

## SYSTEM AUDIT SUMMARY

Before building, know what you have:

| Component | Status | Notes |
|---|---|---|
| ChromaDB | ✅ Live | 23 MB, last indexed 2026-04-21, nomic-embed-text via LM Studio |
| Hot cache (`wiki/hot/hot.md`) | ✅ Live | Rolling 7-day, written by every major pipeline step |
| 11 launchd jobs | ✅ Running | Teams, email, briefing, claude sessions, weekly compile, etc. |
| Morning briefing | ✅ Running | Weekdays 8:45am, writes `raw/briefings/briefing-YYYY-MM-DD.md` |
| `ingest-claude-sessions.py` | ✅ Full JSONL parser | Entity matching, weekly rollups — best model script in repo |
| `brain-lint.sh` | ✅ Production-quality | 8-check vault audit, no deps |
| MEMORY.md | ⚠️ At 200-line cap | Must prune before adding new action items |
| `brain` launcher model | ❌ Stale | Hardcodes `qwen2.5-coder-7b`, routing doc says `qwen3-8b`/`qwen3-14b` |
| `.mem0-data/` | ❌ Missing | Mem0 not initialized (only ChromaDB is live) |
| `github-repos.yaml` | ❌ Unconfirmed | `github-activity.sh` references it — may silently fail |
| `brain-setup-automations` | ❌ Incomplete | Only installs 3 of 11 plists; 8 were manually registered |
| Cross-source correlator | ❌ Does not exist | **The core gap** |
| People entity graph builder | ❌ Does not exist | People files exist; nightly enrichment does not |
| Pre-meeting briefer | ❌ Does not exist | No proactive pre-meeting context |
| Weekly intelligence digest | ❌ Partial | `weekly-pulse.sh` exists but is not a true correlation product |

**The architecture is correct. The intelligence layer is missing.**

---

## PHASED PLAN

### PHASE 0 — Prerequisite Fixes (Day 1, ~2 hours)
*These must be done before any new scripts will work correctly. Fixes only — no new features.*

#### 0A. Audit ChromaDB metadata for `source_type` field
**Why it matters:** The daily correlator needs to filter yesterday's data by source type (bookmark vs Teams vs email vs WhatsApp). If `wiki-to-chromadb.py` doesn't write `source_type` metadata into each chunk, cross-source correlation is impossible.

**Action:**
1. Run `python3 pi-workspace/bin/wiki-to-chromadb.py --stats` to inspect existing metadata
2. Open `pi-workspace/bin/wiki-to-chromadb.py` — confirm the `metadata={}` dict written per chunk includes at minimum: `source_type`, `date`, `file_path`, `title`
3. If missing: add these fields to the chunk metadata before the `collection.upsert()` call, then re-index (`--ingest`)

**Files to touch:** `pi-workspace/bin/wiki-to-chromadb.py`
**Estimated time:** 45 minutes

---

#### 0B. Fix `brain` launcher model name
**Why it matters:** The launcher hardcodes `qwen2.5-coder-7b-instruct-mlx` but routing doc says `qwen3-8b` / `qwen3-14b`. Every Pi session starts with the wrong model.

**Action:** Open `pi-workspace/bin/brain`. Change `PRIMARY_MODEL` to `qwen3-14b` (briefings/synthesis). Update the unload list to remove the old `qwen3.5-9b-mlx` and `qwen3.5-4b-mlx` names.

**Files to touch:** `pi-workspace/bin/brain`
**Estimated time:** 10 minutes

---

#### 0C. Prune MEMORY.md below 200-line cap
**Why it matters:** MEMORY.md is at its hard cap. Phases 1–4 will add new open actions. No room = items will get silently dropped or the health check will fail.

**Action:** Archive completed items from MEMORY.md to `knowledge-base/log.md`. Target: get to ≤150 lines so there's buffer.

**Files to touch:** `MEMORY.md`, `log.md`
**Estimated time:** 30 minutes

---

#### 0D. Verify `github-repos.yaml` exists
**Action:** Check `ls pi-workspace/github-repos.yaml`. If missing, create it with the repos that matter for the morning briefing (OpenClawAgent/workspace, vllm-mlx, my-brain). Fixes the morning briefing's silent empty GitHub section.

**Files to touch:** `pi-workspace/github-repos.yaml`
**Estimated time:** 15 minutes

---

### PHASE 1 — The Signal Brief (Days 2–5, ~6 hours)
*One new script. One injection point. Changes what you see every morning by Day 5.*

**Goal:** Inject a 3-bullet Signal Brief into the existing morning briefing that surfaces cross-source connections you wouldn't think to ask about.

---

#### 1A. Create `daily-correlator.py`

**File:** `pi-workspace/bin/daily-correlator.py`

**What it does:**
1. Opens ChromaDB at `pi-workspace/.chroma-data/`
2. Queries for all chunks where `date >= yesterday` — gets raw data across all source types
3. Groups results by `source_type` (Teams / email / WhatsApp / bookmark / claude-session / briefing)
4. If LM Studio is unavailable (embedding model not loaded), falls back to `grep -r yesterday's date wiki/` across raw files
5. Calls Claude API (`claude-opus-4-5`) with the correlation prompt (see below)
6. Returns a structured 3-section markdown block
7. Writes to `/tmp/signal-brief-YYYY-MM-DD.md`

**Correlation prompt (the core intelligence call):**

```
You are a cross-source intelligence analyst for Andres Urrego's personal brain system.

Below is all data ingested in the last 24 hours, tagged by source type.
Source types: [Teams meeting transcripts] [email digest] [WhatsApp messages]
              [X bookmarks] [GitHub commits] [Claude session captures]

Your job is to find connections that DO NOT EXIST within a single source.
You are looking for signal that only appears when you look across sources.

Rules:
- Do not surface connections that are obvious (same topic, same day = not interesting)
- Do not surface connections where both data points are from the same source type
- The value is in the non-obvious: something bookmarked + a meeting topic + a commit = signal

Output exactly 3 sections, nothing else:

## CROSS-SOURCE CONNECTION
One non-obvious link across two or more source types.
Format: "[Source A] [specific finding] → [Source B] [specific finding]
Why this matters: [1 sentence]"

## ACTIVE PERSON FLAG
One person who appeared across multiple source types in the last 24h.
Format: "[Name] — [sources where they appeared]
Signal: [what their multi-source presence means]"

## SILENCE ANOMALY
One project, topic, or person that is quiet when the pattern says it shouldn't be.
Look at last 7 days for context, flag anything silent for 5+ days that was recently active.
Format: "[Subject] — last active [date] via [source]
Why it matters: [1 sentence]"

DATA:
{data}
```

---

#### 1B. Inject Signal Brief into `morning-briefing.sh`

**File:** `pi-workspace/bin/morning-briefing.sh`

**Injection point:** Add a block **before** the main Claude Code `-p` call that:
1. Runs `python3 pi-workspace/bin/daily-correlator.py`
2. Reads the output from `/tmp/signal-brief-YYYY-MM-DD.md`
3. Prepends it to the briefing context as a `## SIGNAL BRIEF` section

This means you see the correlator output inside your morning briefing — no new interface to check, no new habit to build.

---

#### 1C. Create launchd plist

**File:** `pi-workspace/launchd/com.moil.brain.daily-correlator.plist`
**Schedule:** 6:00 AM daily (45 minutes before morning briefing at 8:45 AM — gives time for LM Studio to produce embeddings if needed)

---

#### 1D. Update `brain-setup-automations`

Add all 11 plists to the setup script so the automation is recoverable on OS reinstall.

---

**Phase 1 deliverable:** Every weekday morning you wake up to a briefing that includes, at the top: one cross-source connection, one active person flag, one silence anomaly. These are things the data found — not things you asked for.

**Success signal:** Within 3 days, the correlator surfaces something you didn't know you needed to think about.

---

### PHASE 2 — Entity Graph Builder (Days 6–14, ~8 hours)
*Your people files stop being static snapshots and start being live relationship intelligence.*

**Goal:** Every person file in `wiki/people/` is automatically enriched nightly with their activity across all sources. A relationship radar surfaces who needs attention.

---

#### 2A. Create `entity-graph-builder.py`

**File:** `pi-workspace/bin/entity-graph-builder.py`

**What it does — nightly at midnight:**

**Step 1 — Entity extraction:**
- Reads yesterday's raw data (from ChromaDB + hot cache)
- Calls Claude API with an extraction prompt:
  ```
  Extract all person mentions from this data.
  For each person: name (normalize variants), source type, context (what were they doing),
  any commitment made to or by them, associated project.
  Output as JSON array.
  ```

**Step 2 — People file enrichment:**
- For each extracted person, finds their `wiki/people/[name].md` file
  - If the file exists: appends a new `## Recent Activity` entry (date-stamped, 2-3 lines max)
  - If the file doesn't exist AND the person appeared in 3+ sources: creates a new stub page with proper frontmatter
- Keeps each person file lean: prunes `## Recent Activity` entries older than 30 days

**Step 3 — Relationship radar:**
- Flags any person who meets ALL of:
  - Last contact > 14 days (from `last_contact:` frontmatter)
  - AND appeared in 2+ active projects
  - AND appeared in any source in the last 30 days (not fully cold)
- Writes flagged people to `wiki/hot/relationship-radar.md` (replaces file each run)
- This file is injected into the morning briefing

**Step 4 — Commitment tracker:**
- Scans extracted entities for commitments: phrases like "I'll send", "will follow up", "will connect you with", "getting back to"
- Appends open commitments to a `wiki/hot/open-commitments.md` file
- Morning briefing injects this file

---

#### 2B. Inject relationship radar into morning briefing

**File:** `pi-workspace/bin/morning-briefing.sh`

Add injection of `wiki/hot/relationship-radar.md` and `wiki/hot/open-commitments.md` into the briefing context. These will appear in the briefing as "## RELATIONSHIP RADAR" and "## OPEN COMMITMENTS" sections.

---

#### 2C. Create launchd plist

**File:** `pi-workspace/launchd/com.moil.brain.entity-graph.plist`
**Schedule:** Daily midnight (processes the full day's data before the 6 AM correlator runs)

---

**Phase 2 deliverable:** The morning briefing now includes: who needs your attention (relationship radar), what you've promised people (commitment tracker), and your people files are living documents updated by data rather than manual effort.

**Success signal:** The briefing surfaces a relationship that's been going stale before you realized it.

---

### PHASE 3 — Weekly Brain Digest (Days 15–21, ~6 hours)
*Your week is synthesized for you before Monday starts.*

**Goal:** A "Brain Weekly" delivered Monday morning that shows what your attention actually focused on last week — not what your calendar said, what the data said.

---

#### 3A. Create `weekly-brain-digest.py`

**File:** `pi-workspace/bin/weekly-brain-digest.py`

**What it does — Sunday at 8:00 PM:**

**Step 1 — Full week data pull:**
- Queries ChromaDB for all chunks with `date >= 7 days ago`
- Groups by source type and by day of week
- Pulls the full week's hot cache history

**Step 2 — Weekly synthesis Claude call:**

```
You have access to a full week of data from Andres's personal intelligence system.
This data spans: Teams meetings, email, WhatsApp, bookmarks, GitHub, and Claude sessions.

Produce a Brain Weekly briefing with exactly these sections:

## THEME REPORT (top 3 recurring themes)
What kept surfacing across sources this week?
Not calendar items — patterns in where attention kept returning.
Evidence: cite specific sources for each theme.

## TOP PEOPLE THIS WEEK (top 3 by cross-source activity)
Who was most active across sources? Why does each person matter this week?
Include: name, which sources, why relevant.

## MOMENTUM vs SILENCE
Projects with clear forward momentum: [evidence: specific commits/meetings/messages]
Projects that have gone quiet: [last active date, expected activity, why this matters]

## WEEKLY ANOMALY
One thing that happened this week that the data pattern says is unusual.
Compare against the prior 3-week baseline.

## ONE RECOMMENDED ACTION FOR MONDAY
Based purely on data patterns — not calendar, not what feels important.
Be specific: who, about what, why now.
```

**Step 3 — Output:**
- Saves to `raw/pulse/brain-weekly-YYYY-WNN.md`
- Commits + pushes to felipeu28 main

---

#### 3B. Wire into existing `weekly-pulse.sh`

The existing `weekly-pulse.sh` runs Fridays at 3pm. The Brain Weekly runs Sundays at 8pm (a separate, more synthesis-focused product). Do not replace `weekly-pulse.sh` — add the Brain Weekly as a complementary output.

**Launchd:** `pi-workspace/launchd/com.moil.brain.weekly-digest.plist`
**Schedule:** Sunday 8:00 PM

---

**Phase 3 deliverable:** Monday morning you have a full picture of what last week actually was — themes, people, momentum, anomalies — before the day begins. The Brain is now telling you what happened, not waiting to be asked.

---

### PHASE 4 — Pre-Meeting Briefer (Days 22–30, ~8 hours)
*You stop walking into meetings cold.*

**Goal:** 30 minutes before every Teams meeting, a one-page contextual briefing exists in your Brain. No prep required.

---

#### 4A. Create `meeting-briefer.py`

**File:** `pi-workspace/bin/meeting-briefer.py`

**Trigger mechanism:** A cron job runs every 30 minutes. It:
1. Calls `m365 request -u "https://graph.microsoft.com/v1.0/me/calendarview?startdatetime={now}&enddatetime={now+90min}"` to get upcoming meetings
2. For each meeting starting in 25–45 minutes (the 30-min window):
   - Checks if a briefing already exists for that meeting at `raw/meeting-briefs/brief-YYYY-MM-DD-HH-slug.md`
   - If not, generates one

**Briefing generation:**

**Step 1 — Attendee context:**
- For each attendee, query ChromaDB: `query_texts=[attendee_name]`, filter `source_type: teams|email|whatsapp`, n=20
- Reads their `wiki/people/[name].md` if it exists
- Extracts: last interaction date, any open commitments, active project association

**Step 2 — Meeting history:**
- Queries ChromaDB: `query_texts=[meeting_title]`, filter `source_type: teams`, n=20
- Finds prior instances of this recurring meeting
- Extracts: what was decided, what was left unresolved

**Step 3 — Relevant data:**
- Queries ChromaDB: `query_texts=[meeting_title + keywords]`, `date >= 14 days ago`, all source types
- Finds: bookmarks, messages, notes related to the likely agenda

**Step 4 — Claude synthesis:**

```
Andres has a meeting in 30 minutes: {meeting_title}
Attendees: {attendees}
Duration: {duration}

Generate a pre-meeting briefing using the Brain data below.
Be brief — this is a one-page briefing, not a report.

## PEOPLE CONTEXT
For each attendee: last interaction + any open commitments + current project role.
Flag: anyone you have an overdue commitment to.

## LAST SESSION
If recurring: what was decided last time? What was left unresolved?
The delta between last meeting and this one — what changed?

## RELEVANT INTEL
Top 3 data points from the last 2 weeks that are directly relevant to this meeting.
Cite source type for each.

## SUGGESTED FOCUS
Based on the data, what is the most important thing to resolve in this meeting?
Be specific. One sentence.

CONTEXT DATA:
{context}
```

**Step 5 — Output:**
- Saves to `raw/meeting-briefs/brief-YYYY-MM-DD-HH-slug.md`
- Adds entry to hot cache under "upcoming-meetings" section
- Optional: sends macOS notification via `osascript -e 'display notification ...'`

---

#### 4B. Create launchd plist

**File:** `pi-workspace/launchd/com.moil.brain.meeting-briefer.plist`
**Schedule:** Every 30 minutes during business hours (`StartCalendarInterval` entries for :00 and :30 of each hour, 7am–7pm)

---

**Phase 4 deliverable:** You walk into every meeting with a one-page brief already sitting in your Brain. People context, history, relevant intel, and a suggested focus — all from your own data.

**Success signal:** You catch something in a meeting brief that you would have forgotten to bring up.

---

### PHASE 5 — Hardening + Closed Loop (Days 31–45, ~10 hours)
*Turn the individual pieces into a self-maintaining system.*

---

#### 5A. Fix `brain-setup-automations` (complete all 11 plists)

**File:** `pi-workspace/bin/brain-setup-automations`

Rewrite to install all 11 existing plists + the 4 new Phase 1–4 plists. This makes the automation recoverable on any OS reinstall. Also add `launchctl list | grep moil` verification at the end.

---

#### 5B. Daily coherence check in `brain-heartbeat.sh`

Extend the existing heartbeat to also check:
- Is Signal Brief file present for today? (`/tmp/signal-brief-YYYY-MM-DD.md`)
- Is `wiki/hot/relationship-radar.md` less than 24h old?
- Is ChromaDB last_indexed timestamp less than 25h ago?
- Is LM Studio embedding model reachable? (can skip if ChromaDB was already indexed today)

Heartbeat already writes to `outputs/health/` — add a "BRAIN ACTIVATION STATUS" block to its output.

---

#### 5C. ANDRES.md daily regeneration

**File:** `pi-workspace/bin/andres-dashboard-update.py`

Currently `wiki/andres/ANDRES.md` is the graph's gravitational center but is manually maintained. Add a nightly step that:
- Reads all hub/spoke pages and extracts their "Last updated" date
- Updates the "STATUS" section of ANDRES.md to show which hubs are stale (>14 days)
- Updates the "ACTIVE THIS WEEK" section from hot cache
- Updates the "OPEN COMMITMENTS" count from `wiki/hot/open-commitments.md`
- Runs `sync_wiki.sh` after

**Wire into:** `com.moil.brain.entity-graph` plist (runs after entity graph builder at midnight)

---

#### 5D. Signal quality feedback loop

**File:** `pi-workspace/bin/signal-feedback.sh`

After one month of running, add a lightweight feedback loop:
- Reads the last 30 days of signal briefs from `/tmp/signal-brief-*.md` (or archive them to `raw/signal-briefs/`)
- Asks Claude: "Which of these 30 cross-source connections turned out to be accurate or useful, based on what Andres worked on in the following 48 hours?"
- Updates a `wiki/hot/signal-quality.md` calibration log
- This file gets injected into the correlator prompt: "Prior signals that proved accurate: [examples]. Signals that proved low-value: [examples]. Calibrate toward this."

This is the feedback loop that makes the correlator smarter over time — the system learns what "signal" means for Andres specifically.

---

#### 5E. Claude Managed Agents integration (when ready)

Anthropic launched Managed Agents on April 8, 2026. The current architecture uses launchd + shell scripts to simulate an agentic loop. As Managed Agents matures:

1. **Replace the correlator cron** with a persistent agent that maintains state across runs — it knows which signals it already surfaced, can track whether they proved accurate
2. **Move pre-meeting briefer** into a managed agent that maintains a calendar subscription and runs continuously rather than on a 30-min poll
3. **Implement Karpathy's dream cycle**: a nightly managed agent that enriches wiki pages while you sleep by querying external sources (Brave Search API) for new information about tracked entities (competitors, contacts, topics)

**This is Phase 5E, not Phase 1, because:** managed agents require architectural changes, and the cron-based approach delivers 90% of the value with 10% of the complexity. Build the intelligence first, then move to persistent agents.

---

## IMPLEMENTATION SEQUENCE (CRITICAL PATH)

```
Day 1     Phase 0: ChromaDB metadata audit + brain launcher fix + MEMORY.md prune
Day 2     Phase 1A: Write daily-correlator.py
Day 3     Phase 1B: Inject into morning-briefing.sh + test run manually
Day 4     Phase 1C+D: Wire launchd + update brain-setup-automations
Day 5     LIVE: First Signal Brief in morning briefing ← milestone
Days 6-8  Phase 2A: Write entity-graph-builder.py
Days 9-11 Phase 2B+C: Inject into briefing + wire launchd
Day 12    LIVE: Relationship radar + open commitments in briefing ← milestone
Days 13-17 Phase 3: Weekly Brain Digest (simpler — builds on correlator)
Day 18    LIVE: First Brain Weekly delivered Sunday night ← milestone
Days 19-26 Phase 4: Pre-meeting briefer (most complex — Graph API + timing)
Day 27    LIVE: Pre-meeting briefs auto-generated ← milestone
Days 28-35 Phase 5: Hardening, ANDRES.md automation, feedback loop
Day 42    Phase 5E planning: evaluate Claude Managed Agents maturity
```

---

## FILE MANIFEST — NEW FILES CREATED

```
pi-workspace/bin/
  daily-correlator.py          Phase 1 — core intelligence script
  entity-graph-builder.py      Phase 2 — nightly people enrichment
  weekly-brain-digest.py       Phase 3 — Sunday synthesis
  meeting-briefer.py           Phase 4 — pre-meeting context
  andres-dashboard-update.py   Phase 5C — ANDRES.md automation
  signal-feedback.sh           Phase 5D — calibration loop

pi-workspace/launchd/
  com.moil.brain.daily-correlator.plist   6:00 AM daily
  com.moil.brain.entity-graph.plist       midnight daily
  com.moil.brain.weekly-digest.plist      Sunday 8:00 PM
  com.moil.brain.meeting-briefer.plist    every 30 min, 7am–7pm

wiki/hot/
  relationship-radar.md        generated nightly by entity-graph-builder
  open-commitments.md          generated nightly by entity-graph-builder
  signal-quality.md            generated monthly by signal-feedback

raw/signal-briefs/
  signal-brief-YYYY-MM-DD.md   daily archives (moved from /tmp)

raw/meeting-briefs/
  brief-YYYY-MM-DD-HH-slug.md  pre-meeting briefings
```

---

## FILES MODIFIED

```
pi-workspace/bin/morning-briefing.sh   — inject signal brief + relationship radar
pi-workspace/bin/brain-heartbeat.sh   — add activation status checks
pi-workspace/bin/brain-setup-automations — complete all 11+4 plists
pi-workspace/bin/brain                 — fix model name (qwen3-14b)
pi-workspace/bin/wiki-to-chromadb.py  — add source_type/date to metadata (if missing)
wiki/andres/ANDRES.md                  — add sections for automation to target
```

---

## RISK LOG

| Risk | Mitigation |
|---|---|
| LM Studio not running when correlator fires at 6 AM | Fallback: `grep -r` across raw files by date — lower quality but functional |
| ChromaDB metadata missing `source_type` | Phase 0A catches this before building Phase 1 |
| MSAL token expires mid-week | `meeting-briefer.py` wraps m365 calls in try/except; logs token expiry to heartbeat |
| Signal Brief is low quality for first 2 weeks | Expected — calibration via Phase 5D fixes it; low-quality signal is still better than no signal |
| Morning briefing already long; signal brief adds more | Cap signal brief at 150 words; inject at top so it's seen before rest |
| Phase 4 timing: meeting window might be wrong | Use conservative 25–45 minute window; add `already_briefed` check to avoid duplicates |
| Claude Managed Agents not mature enough for Phase 5E | The entire plan is cloud-Claude-independent; Managed Agents is additive, not required |

---

## THE MOIL BUSINESS CASE (EXPLICIT)

Every script you build here is a module in what Moil sells.

| Brain Module | Moil Product Equivalent |
|---|---|
| `daily-correlator.py` | Cross-source intelligence layer for enterprise KB |
| `entity-graph-builder.py` | Relationship intelligence product for sales/CS teams |
| Pre-meeting briefer | Deal intelligence feature (who's meeting with who, what was said) |
| Weekly Brain Digest | Executive intelligence digest product |
| Feedback loop | AI that calibrates to user preference — the moat |

When you have 30 days of the correlator running on your own data, you have:
- A live demo of the product
- Real output examples for the pitch deck
- A calibration log showing accuracy improving over time
- Personal testimony: "I built this for myself and it caught X, Y, Z"

The most credible enterprise AI pitch is not "we have a great idea." It is "here is 30 days of output from a system running on my own data, and here is what it found."

---

## HOW TO START THIS WEEK

**Today (45 min):**
1. Run `python3 pi-workspace/bin/wiki-to-chromadb.py --stats` — check if metadata has `source_type` and `date` fields
2. Fix `brain` launcher model name
3. Check MEMORY.md line count; archive enough to get under 150 lines

**Tomorrow (3 hours):**
1. Write `daily-correlator.py` using `wiki-to-chromadb.py` and `ingest-claude-sessions.py` as the reference models
2. Run it manually: `python3 pi-workspace/bin/daily-correlator.py`
3. Read the output. See what it finds.

**End of Week 1:**
The Signal Brief is in your morning briefing. You have seen at least 5 outputs. You know whether it's surfacing real signal or noise. That feedback directly shapes Phases 2–5.

---

*Plan prepared April 22, 2026. Built against actual codebase state — not theoretical.*
*Scripts reference existing infrastructure: ChromaDB at `pi-workspace/.chroma-data/`, hot cache at `wiki/hot/hot.md`, launchd at `pi-workspace/launchd/`, cloud Claude via `/opt/homebrew/bin/claude`.*
