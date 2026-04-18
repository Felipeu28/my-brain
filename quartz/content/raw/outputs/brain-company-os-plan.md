---
tags:
  - graph/leaf
type: plan
generated: 2026-04-18
status: active
---

# Brain Company OS — Full Implementation Plan
**Generated:** 2026-04-18  
**Author:** Claude Code audit session  
**Purpose:** Turn the Moil Brain from a passive archive into an active company operating system

---

## Part 1 — Current State Audit (as of 2026-04-18)

### What's running

| Automation | Status | Notes |
|---|---|---|
| `morning-briefing.sh` | ✅ Generating | Email delivery was broken (m365 `--` flag) — fixed inline in script |
| `weekly-compile.sh` | ✅ Running Fri 2pm | Creates wiki pages from weekly signals |
| `weekly-pulse.sh` | ✅ Running Fri 3pm | Produces real CEO-readable weekly intelligence |
| `chroma-index` / `wiki-to-chromadb.py` | ✅ Healthy | 231 pages, 828 chunks indexed as of Apr 17 |
| `content-calendar.sh` | ✅ Running Mon 9am | W16 calendar created + synced |
| `daily-email-digest.sh` | ✅ Running daily 6:30pm | Committed daily |
| `teams-pull.sh` | ⚠️ Intermittent | Apr 16 pull completely lost to 504; no error recovery |
| `x-bookmarks` | ⚠️ Requires Keychain | May silently hang if unattended |
| GitHub Pages deploy | ❌ Every push fails | `deploy-pages` 404 — Pages not enabled in repo settings |

### Raw files ingested this week (Apr 14–18)

Files committed since `briefing-2026-04-13.md`:
- `compile-2026-04-17.md` (weekly compile — 23 files, +368 lines)
- `pulse/pulse-2026-W16.md` (weekly pulse — 8 deals tracked)
- `briefings/briefing-2026-04-14.md` through `briefing-2026-04-17.md` (4 daily briefings)
- `content-calendar/calendar-2026-W16.md` (W16–W19 content plan)

Files in `quartz/content/raw/` that exist but have **no `ingested: true` frontmatter** (not yet processed into wiki):

| File | Type |
|---|---|
| `facebook-pages-2026-04-09.md` | Social profile data |
| `buda-hive-edc-2026-04-11.md` | EDC event intel |
| `buda-hive-edс-2026-04-09.md` | EDC event intel (duplicate filename?) |
| `outlook-emails-2026-04-09.md` | 9-month email history |
| `x-bookmarks-2026-04-11.md` | X bookmarks digest |
| `moilapp-website-2026-04-09.md` | Website content |
| `imessages-people-2026-04-09.md` | iMessage contacts |
| `know-me-extraction-prompts.md` | Personal context source |
| `moil-documents-2026-04-09.md` | Moil business documents |
| `github-project-tracker.md` | GitHub project data |
| `brain-guide.md` | Brain usage doc |
| `quartz-setup-guide.md` | Setup doc |

**14 raw files sitting unprocessed.** Some of these contain high-value intel (9-month email history, EDC events, iMessage contacts) that could meaningfully update `pipeline.md`, `people/`, and `orgs/`.

### Wiki state

- **241 wiki pages** total (brain-lint scanned 201 as of Apr 15 — delta is new pages from Runs 4–10)
- **68 people pages**
- **13 moil/ pages** (pipeline.md is live and current as of Apr 14)
- **15 stubs** (<150 words) — key ones: `lunabella`, `concepts/aedo`, `jacquie-martinez`, `roxana-esquivel`
- **19 orphans** (no inbound wikilinks) — mostly meeting transcripts and projects
- **Brain lint:** ran Apr 15; next Sunday Apr 19

### Scripts that exist vs. what actually runs

**In `pi-workspace/bin/`:**
```
morning-briefing.sh     ✅ scheduled
weekly-compile.sh       ✅ scheduled
weekly-pulse.sh         ✅ scheduled
content-calendar.sh     ✅ scheduled
daily-email-digest.sh   ✅ scheduled
teams-pull.sh           ✅ scheduled
brain-heartbeat.sh      ✅ runs inside morning-briefing
wiki-to-chromadb.py     ✅ scheduled (chroma-index launchd)
github-activity.sh      ✅ called by morning-briefing
ingest-claude-sessions.sh ✅ exists (manual trigger)
brain-lint.sh           ✅ exists (manual trigger)
```

**Defined as slash commands in CLAUDE.md but NOT implemented as scripts:**
```
/brain-ingest   → NO bin/brain-ingest.sh exists
/brain-query    → NO bin/brain-query.sh exists
/brain-explore  → NO bin/brain-explore.sh exists
```

**The core gap:** `morning-briefing.sh` already detects unprocessed clippings and writes to `ingest-queue.md`. But that detection stops there — it queues a notification and then exits. No script actually runs `/brain-ingest` automatically. The pipeline has a sensor but no actuator.

### What the Brain already does well

- **Daily intelligence:** morning-briefing reads `pipeline.md`, `AGENTS.md`, cross-references sent emails, flags going-cold relationships, and emails the result
- **Weekly synthesis:** `weekly-pulse.sh` produces real CEO 1-pagers (W16 had Alloy ATX closed, Helotes EDC locked, Jacob Centeno referral channel, 3 Q2 priority checks)
- **Chroma indexing:** daily — 828 chunks, semantic search available immediately
- **Structural knowledge:** `pipeline.md` is accurate and current (confirmed Apr 14); 13 moil/ pages cover ICP, GTM, competitors, metrics, customers

---

## Part 2 — The Vision

The Brain should run Moil. Not just store knowledge — execute.

Every morning Andres wakes up knowing exactly **who to call, what to post, what decisions need to be made** — sourced from his own knowledge graph, not reconstructed from zero.

Right now the Brain has the information. The gap is the last mile: raw data arrives daily but isn't automatically converted into wiki intelligence. And the wiki intelligence that exists isn't automatically fed into every action (meetings, content, sales outreach). Those two gaps — auto-ingestion and auto-injection — are the entire implementation.

**Before state:** Andres manually triggers `/brain-ingest` when he remembers to. Raw files accumulate. The morning briefing reads pipeline.md but not the 14 raw files sitting unprocessed. Cowork sessions start from zero.

**After state:** Every morning, unprocessed raw files are automatically ingested into wiki pages. Every meeting brief, content calendar, and sales action is pre-loaded with relevant Brain context. Andres makes decisions from intelligence, not memory.

---

## Phase 1 — Close the Ingestion Loop (Week 1, ~4 hours)

This is the unlock for everything else. Nothing in Phases 2–4 matters until raw → wiki is automatic.

### 1A. Implement `bin/brain-ingest.sh` (~2 hours)

**What to build:** `pi-workspace/bin/brain-ingest.sh` — a real script that the morning-briefing can call.

```bash
#!/usr/bin/env bash
# Brain ingest — processes unprocessed raw/ files into wiki pages.
# Run by morning-briefing.sh after clipping detection.
# Also safe to run manually: bash bin/brain-ingest.sh

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
KB_DIR="/Users/jarvisurrego/My Brain/knowledge-base"
RAW_DIR="$KB_DIR/quartz/content/raw"
LOG_FILE="/Users/jarvisurrego/My Brain/pi-workspace/.ingest-log"

DATE=$(date '+%Y-%m-%d')
echo "[$(date '+%Y-%m-%d %H:%M')] brain-ingest started" >> "$LOG_FILE"

# Find all raw/ files without ingested: true
UNPROCESSED=$(grep -rL "ingested: true" "$RAW_DIR" 2>/dev/null \
  | grep "\.md$" \
  | grep -v "README.md" \
  | grep -v "index.md" \
  | grep -v "/briefings/" \
  | grep -v "/outputs/" \
  | grep -v "/content-calendar/" \
  | grep -v "/pulse/" \
  | grep -v "PROCESSING.md" \
  | grep -v "brain-guide.md" \
  | grep -v "quartz-setup-guide.md")

COUNT=$(echo "$UNPROCESSED" | grep -c "\.md$" 2>/dev/null || echo 0)
echo "[$(date '+%Y-%m-%d %H:%M')] Found $COUNT files to ingest" >> "$LOG_FILE"

if [[ "$COUNT" -eq 0 ]]; then
  echo "[$(date '+%Y-%m-%d %H:%M')] Nothing to ingest" >> "$LOG_FILE"
  exit 0
fi

cd "$KB_DIR"

# Feed files to Claude for batch ingestion
FILE_LIST=$(echo "$UNPROCESSED" | tr '\n' '|')

/opt/homebrew/bin/claude -p "Run /brain-ingest for these unprocessed raw files: $FILE_LIST

Follow the ingestion protocol exactly:
1. Read index.md first to know what exists
2. For each file: classify type, extract concepts/people/orgs, create/update wiki pages with [[wikilinks]]
3. Mark each processed file with ingested: true and ingested_at: $DATE in frontmatter
4. Update index.md Source Inventory and stats
5. Append entries to log.md
6. At the end, run: bash scripts/sync_wiki.sh && python3 scripts/kb-health.py

Process all files before committing." \
  --allowedTools "Bash,Read,Write,Edit,Glob,Grep" \
  2>&1 | tee -a "$LOG_FILE"

echo "[$(date '+%Y-%m-%d %H:%M')] brain-ingest finished" >> "$LOG_FILE"
```

**Wire it into `morning-briefing.sh`:** Replace the existing clipping-detection block with a real call:

```bash
# After briefing generation, before sync/push:
INGEST_SCRIPT="$WORKSPACE/bin/brain-ingest.sh"
if [[ -x "$INGEST_SCRIPT" ]]; then
  UNPROCESSED=$(grep -rL "ingested: true" "$KB_DIR/quartz/content/raw/" 2>/dev/null \
    | grep "\.md$" | grep -v "README\|index\|briefings\|outputs\|content-calendar\|pulse\|PROCESSING\|brain-guide\|quartz-setup" \
    | wc -l | tr -d ' ')
  if [[ "${UNPROCESSED:-0}" -gt 0 ]]; then
    echo "[brain-ingest] $UNPROCESSED files to process — running ingest..." >> "$LOG_FILE"
    bash "$INGEST_SCRIPT" 2>>"$LOG_FILE" || echo "[brain-ingest] WARNING: ingest failed" >> "$LOG_FILE"
  fi
fi
```

This turns the existing sensor into an actuator. **Every morning, raw files that arrived overnight are automatically converted into wiki intelligence before the briefing is emailed.**

### 1B. Fix `add-raw-type-frontmatter.py` as a daily pass (~30 min)

The script ran once. New raw files (Teams pulls, email digests) arrive daily without type frontmatter, which breaks ingestion classification. Add to `morning-briefing.sh` before the ingest block:

```bash
cd "$KB_DIR"
python3 scripts/add-raw-type-frontmatter.py 2>>"$LOG_FILE" || true
```

### 1C. Wire Chroma re-index after ingest (~15 min)

After `brain-ingest.sh` completes, new wiki pages exist but aren't in Chroma. The daily Chroma job runs at 9:15am — if ingest runs at 8:47am, new pages ARE caught. But for the manual-run case, add to `brain-ingest.sh`:

```bash
# After ingestion completes:
python3 "$WORKSPACE/bin/wiki-to-chromadb.py" --quiet 2>>"$LOG_FILE" || true
```

This makes new wiki pages immediately queryable via `/brain-query` without waiting for the daily Chroma job.

---

## Phase 2 — Make the Brain Talk Back (Week 2, ~6 hours)

Phase 1 closes the write loop. Phase 2 closes the read loop. Once you can reliably query the Brain from a script, every downstream automation becomes straightforward.

### 2A. Implement `bin/brain-query.sh` (~3 hours)

This is the most high-leverage script in the entire plan. It's the API layer between every automation and the Brain's knowledge graph.

```bash
#!/usr/bin/env bash
# brain-query.sh [question] [--context-pages N] [--output-file path]
# Semantic search → context injection → Claude answer → saved output

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
KB_DIR="/Users/jarvisurrego/My Brain/knowledge-base"
WORKSPACE="/Users/jarvisurrego/My Brain/pi-workspace"

QUESTION="${1:-}"
OUTPUT_FILE="${3:-}"
DATE=$(date '+%Y-%m-%d')
SLUG=$(echo "$QUESTION" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | cut -c1-40)

if [[ -z "$QUESTION" ]]; then
  echo "Usage: brain-query.sh 'your question here'" >&2
  exit 1
fi

# Step 1: Semantic search via Chroma to find relevant wiki pages
RELEVANT_PAGES=$(python3 "$WORKSPACE/bin/wiki-to-chromadb.py" \
  --query "$QUESTION" --results 8 --format paths 2>/dev/null || echo "")

# Step 2: Feed pages + question to Claude
ANSWER=$(/opt/homebrew/bin/claude -p "You are the Moil Brain query engine. 
Question: $QUESTION

Use the wiki pages listed below as your primary context. Answer concisely with [[wikilink]] citations.
If you identify a gap (something the question implies that isn't in the wiki), flag it as: GAP: [topic]

Relevant pages: $RELEVANT_PAGES

Also check: wiki/moil/pipeline.md, wiki/moil/icp.md, wiki/andres/ANDRES.md" \
  --allowedTools "Read,Glob,Grep" 2>/dev/null)

# Step 3: Save to outputs
if [[ -n "$OUTPUT_FILE" ]]; then
  echo "$ANSWER" > "$OUTPUT_FILE"
else
  OUTPUT_PATH="$KB_DIR/quartz/content/raw/outputs/${DATE}-query-${SLUG}.md"
  cat > "$OUTPUT_PATH" <<EOF
---
tags:
  - graph/leaf
type: brain-query
question: "$QUESTION"
date: $DATE
---

# Brain Query: $QUESTION

$ANSWER
EOF
  echo "$OUTPUT_PATH"
fi

echo "$ANSWER"
```

**Key design decision:** The script returns the answer to stdout AND saves it. This means any automation can call it and capture the output inline, while also getting a persistent record.

### 2B. Brain → Morning Briefing auto-injection (~2 hours)

Extend the morning-briefing Claude prompt to include a Brain query step. Add to the briefing prompt after step 10 (PIPELINE CHECK):

```
11. BRAIN CONTEXT — run these queries before generating the briefing:
    - What are the 3 highest-priority open deals and their current blockers?
    - Who are the 2 relationships most at risk of going cold right now?
    - What is the one strategic decision Andres most needs to make this week?
    Source the answers from wiki/moil/pipeline.md, wiki/moil/customers.md, MEMORY.md, and recent briefings.
    Include a "Brain Says" section in the briefing with 3-5 bullets of specific, actionable intelligence.
```

This stops the briefing from being a data dump and makes it opinionated — the Brain tells Andres what to do, not just what happened.

### 2C. Cowork session auto-injection (CLAUDE.md hook, ~1 hour)

The CLAUDE.md `session-start` hook (or Pi agent init) should auto-query the Brain for context relevant to the session topic.

In `pi-workspace/AGENTS.md`, add a section:

```markdown
## On Session Start
When a new Claude Code or Pi session begins, run:
  bash ~/My\ Brain/pi-workspace/bin/brain-query.sh "[infer session topic from first message]"
Inject the result as system context before responding to the first user message.
```

The effect: every Cowork session starts with Brain context for the topic, not from zero.

---

## Phase 3 — Company Automations (Weeks 3–4, ~10 hours)

These are all `brain-query.sh` consumers. None of them work until Phase 2 is done.

### Automation 1: Daily Sales Intelligence Brief (add to morning-briefing)

After the existing pipeline check, add:

```bash
# In morning-briefing.sh, before the Claude briefing prompt:
SALES_INTEL=$(bash "$WORKSPACE/bin/brain-query.sh" \
  "Who are the 3 specific people I should call or email today to move revenue? Include their last contact date, what was discussed, and one sentence on what to say." 2>/dev/null || echo "")
```

Inject `$SALES_INTEL` into the briefing prompt as a dedicated section. This is the "3 names with context" section that transforms the briefing from a status report into a daily sales playbook.

**Expected output format:**
```
## Today's 3 Revenue Moves
1. Kate Silvas (Helotes EDC) — call Wed Apr 22 already booked. Send one-pager TODAY before call. Last discussed: partnership replication of Buda EDC model.
2. Jesutomilola Omoniyi — overdue 3 days. Text or call. Risk: Google xWF relationship. Say: "Hey Jesi, any good times this week?"
3. Merrie Santana — silent 18 days. Confirm HIVE service delivery. Simple check-in.
```

**Build time:** 30 min (just a brain-query call + prompt injection). Value: immediate.

### Automation 2: Meeting Intelligence Brief (trigger-based, ~3 hours)

**Trigger:** Calendar event starting in <2 hours with a known contact.

Create `bin/meeting-intel.sh [person-name] [meeting-topic]`:
1. Query Brain: everything about the person (`wiki/people/[person].md`, related orgs, pipeline stage)
2. Query Brain: last 3 touchpoints, open items, relationship context
3. Generate: 1-page pre-call brief (relationship history, talking points, open items, what you want from this meeting)
4. Email to Andres 30 min before

Wire into `morning-briefing.sh`: scan today's calendar, for each event with a person that has a `wiki/people/` page, schedule a `meeting-intel.sh` call for 30 min before.

```bash
# morning-briefing — meeting intel scheduling block
TODAY_MEETINGS=$(bash .pi/skills/morning-briefing/scripts/fetch-calendar.sh 0 2>/dev/null | \
  grep -oE '"subject":"[^"]*"' | head -5)
# For each meeting with a known person, at=$(meeting_time - 30min):
# at $TIME bash $WORKSPACE/bin/meeting-intel.sh "$PERSON" "$TOPIC"
```

**Why this matters:** The Helotes EDC call on Apr 22 is already in the calendar. Without this automation, Andres prepares cold. With it, he gets a brief at 9:30am — Kate Silvas relationship context, Buda EDC one-pager talking points, what to ask for on the call.

### Automation 3: Content Generation Engine (add to content-calendar Monday run)

Extend `content-calendar.sh` — before generating the week's calendar, run:

```bash
CONTENT_BRAIN=$(bash "$WORKSPACE/bin/brain-query.sh" \
  "What are the 5 best content angles for this week? Base it on: Moil ICP, recent wins (Alloy ATX, Buda HIVE Cohort 4), current product positioning, and what content has already been published in the last 30 days. For the strongest angle, write a 150-word first draft." 2>/dev/null)
```

Inject this into the content-calendar Claude prompt. The result: every Monday's content plan starts from the Brain's knowledge of what's working, what the ICP cares about, and what hasn't been said yet.

**Expected improvement:** Instead of generic "here are 5 content ideas," you get "here's a LinkedIn post about the Buda EDC cohort that positions Moil as the go-to tool for EDC programs statewide, written in Andres's voice, citing the specific Alloy ATX win as proof."

### Automation 4: Weekly Company Pulse — make it smart (~1 hour)

The weekly pulse is running ✅. But it synthesizes from signals, not from Brain queries. Extend `weekly-pulse.sh` to include a Brain query section:

```bash
CEO_QUESTIONS=$(bash "$WORKSPACE/bin/brain-query.sh" \
  "Based on this week's activity: what is the single biggest decision Andres needs to make next week? What is the one relationship most at risk? What is the strongest revenue signal in the pipeline?" 2>/dev/null)
```

Add this to the pulse output as "**Brain's 3 Questions for the CEO**" — a weekly forcing function that makes the pulse actionable, not just informational.

### Automation 5: Brain Health Monitor (improve brain-lint monthly)

The `brain-lint.sh` script exists and runs. Extend it to prioritize by impact:

```bash
# After running brain-lint.py, sort stubs by inbound wikilink count:
python3 scripts/kb-health.py --stub-priority-by-links --output outputs/health/kb-health-latest.md
```

Add a "fix this first" section to the health report:
- Stubs most linked to (highest priority to expand)
- Orphans that belong in ANDRES.md (quick wins)
- Raw files > 30 days old with no `ingested: true` (data rotting in queue)

---

## Phase 4 — Brain as Competitive Advantage (Month 2+)

These unlock the Brain's external leverage. Don't start until Phases 1–3 are solid.

### 4A. wiki-os REST API

A FastAPI wrapper over `brain-query.sh` makes the Brain queryable from any tool — Zapier, Make, mobile app, OpenClaw, external webhooks.

```
GET /query?q=what+deals+are+stale
GET /context?topic=meeting+with+kate+silvas
POST /ingest   # trigger ingest from external source
```

Wire from OpenClaw: OpenClaw already has `brain_gateway.sh` calling into the Brain (seen in `morning-briefing.sh`'s `OPENCLAW_EVENTS` block). This API formalizes that interface.

### 4B. Apollo CRM → Brain sync

Apollo is connected (MCP available in Claude sessions). Build a weekly Apollo pull:
- New contacts added to Apollo → auto-create `wiki/people/[contact].md` pages
- Apollo company data → update `wiki/orgs/` pages with deal size, title, industry
- This closes the gap where the Brain knows about deals but not the people behind them

### 4C. Bi-directional Teams sync

Today: Teams messages pulled → wiki. Tomorrow: Brain intel pushed back into Teams conversations.
When a Teams message mentions a deal, person, or org that has a wiki page, the brain-agent replies inline with a Brain context card: "FYI: FitLogic is at risk — delivery deadline was Apr 18, last contact 6 days ago."

### 4D. Mobile Brain query

A Shortcuts widget on Andres's iPhone that calls `brain-query.sh` via the REST API. Mid-meeting access to "everything I know about this person" without opening a laptop.

### 4E. Auto-relationship mapping

When a new name appears in Teams/email/calendar that doesn't have a `wiki/people/` page, auto-create a stub with: name, first seen date, context of first mention, org affiliation. This stops the pattern where high-value contacts get mentioned 3x before anyone creates their page.

---

## Architecture (current → target)

```
CURRENT STATE
─────────────────────────────────────────────────────────────────
INPUTS                    PROCESSING               OUTPUTS
------                    ----------               -------
Daily briefing     ──→    morning-briefing.sh  ──→ briefing-YYYY-MM-DD.md (not emailed)
Teams messages     ──→    teams-pull.sh        ──→ raw/teams-*.md (unprocessed)
Email digests      ──→    daily-email-digest   ──→ raw/email-digest-*.md (unprocessed)
X bookmarks        ──→    x_bookmark_commit    ──→ raw/x-bookmarks-*.md (unprocessed)
Compile/pulse      ──→    weekly-compile.sh    ──→ wiki pages (batch, manual trigger)
                          weekly-pulse.sh      ──→ pulse-W16.md (generated, not actioned)
[14 raw files sit unprocessed; wiki is not queried by any downstream action]


TARGET STATE
─────────────────────────────────────────────────────────────────
INPUTS                    PROCESSING               OUTPUTS
------                    ----------               -------
Daily briefing            brain-ingest.sh      ──→ wiki/ pages (daily, automatic)
Teams messages     ──→    (new: 8:47am daily)  ──→ Chroma index (immediate)
Email digests             brain-query.sh             │
X bookmarks               (new: on-demand)     ◀────┘
Web clippings             
GitHub activity    ──→    morning-briefing.sh  ──→ briefing + "Brain Says" + 3 revenue moves
                          (extended)               (emailed daily)
                                │
                                ├──→ meeting-intel.sh ──→ pre-call brief (30 min before meeting)
                                ├──→ content-calendar ──→ Brain-sourced content angles + drafts
                                ├──→ weekly-pulse.sh  ──→ CEO 1-pager + "3 questions" section
                                └──→ [future] API     ──→ Mobile, OpenClaw, Zapier
```

---

## Prioritized Action List

| # | Action | Est. Time | Unlocks |
|---|--------|-----------|---------|
| 🔴 1 | Create `bin/brain-ingest.sh` | 2h | Auto-processing of 14 stale raw files + all future files |
| 🔴 2 | Wire `brain-ingest.sh` into `morning-briefing.sh` | 30m | Daily auto-ingestion loop |
| 🔴 3 | Fix `add-raw-type-frontmatter.py` as daily step | 30m | Clean type metadata for ingest |
| 🔴 4 | Create `bin/brain-query.sh` | 3h | All query-based automations (Phases 3–4) |
| 🟡 5 | Inject Brain query into morning-briefing prompt | 1h | "Brain Says" section + 3 revenue moves |
| 🟡 6 | Implement `bin/meeting-intel.sh` | 3h | Pre-call briefs (Helotes EDC call Apr 22 is the first test) |
| 🟡 7 | Extend `content-calendar.sh` with Brain query | 30m | Brain-sourced content angles |
| 🟡 8 | Extend `weekly-pulse.sh` with "3 CEO questions" | 30m | Actionable weekly pulse |
| 🟠 9 | Fix GitHub Pages (1-click) | 5m | Live site updates |
| 🟠 10 | Fix Teams 504 error handling | 1h | Stop data loss on paginated pulls |
| 🟠 11 | Apollo → wiki sync | 3h | CRM intelligence in Brain |
| 🟠 12 | wiki-os REST API | 4h | Mobile + external tool access |

**Critical path:** Items 1 → 2 → 4 → 5. Everything else builds on this chain.

---

## The One Metric That Matters

**Brain Utilization Rate:** What percentage of Andres's daily decisions are informed by a Brain query versus reconstructed from memory?

| State | Rate | Indicator |
|---|---|---|
| Today (passive) | ~0% | Brain stores knowledge; nothing reads it automatically |
| After Phase 1 | ~10% | Briefing reads pipeline.md; raw files get processed daily |
| After Phase 2 | ~40% | Briefing includes Brain queries; meetings get pre-briefs |
| After Phase 3 | ~70% | Every content piece, every sales action, every weekly review starts from Brain |
| After Phase 4 | ~90% | Every tool (mobile, OpenClaw, Zapier) queries Brain first |

**30-day target: ≥50%.**

---

## Immediate Next Steps (This Weekend)

1. **Fix GitHub Pages** — go to `https://github.com/Felipeu28/my-brain/settings/pages` → Source = GitHub Actions. 5 minutes.
2. **Ingest the 14 stale raw files** — run `/brain-ingest` in this Claude session. Clears the queue, gives data for `brain-query.sh` testing.
3. **Build `brain-ingest.sh`** — use the scaffold above; test against the 14 files; wire into morning-briefing.
4. **Build `brain-query.sh`** — use the scaffold above; test with "what deals are stale?"; verify it returns pipeline context.
5. **Before Apr 22 Helotes EDC call** — manually run `meeting-intel.sh` or a `/brain-query` for Kate Silvas context. This is the first real test of whether the Brain is adding value to sales.

---

_Source: git log since 2026-04-14, automation-audit-2026-04-17.md, brain-lint-2026-04-15.md, pulse-2026-W16.md, wiki/moil/pipeline.md, morning-briefing.sh inspection, pi-workspace/bin/ inventory_
