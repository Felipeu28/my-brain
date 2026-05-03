---
type: implementation-plan
date: 2026-05-03
tags:
  - graph/leaf
companion: raw/audits/2026-05-03-ingestion-and-synthesis-audit.md
---

# Moil Brain — 4-Week Implementation Plan (2026-05-03)

Companion to `raw/audits/2026-05-03-ingestion-and-synthesis-audit.md`. Where the audit asks "what's broken / what's missing", this asks "what do we ship, in what order, and how do we know it worked." Karpathy/Tan recommendations from `karpathy-tan-brain-recommendations.md` are folded in by number (K&T#N) where they earn their slot.

Two anchoring decisions before the table of contents:

1. **The Brain is input-rich and reflection-poor.** Section A of the audit shows capture is mostly working; Section C shows entity-graph is dead, ChromaDB is write-only, weekly-sessions is mechanical, and weekly-operating-brief ran once in 30 days. Almost every plan item below either fixes a silent failure or makes existing capture do more work. We are *not* adding new capture surfaces this month except where they unblock a synthesis upgrade we already own.
2. **K&T#1 (the Karpathy CLAUDE.md + ingest/query/lint loop) is mostly already shipped.** `knowledge-base/CLAUDE.md` is real, `/brain-ingest`, `/brain-query`, and `/brain-lint` slash commands are defined, `kb-health.py` is the lint pass. So we treat K&T#1 as **done** and route effort into the gaps the audit found instead of rebuilding what exists. This is the single biggest reconciliation between the two input docs.

---

## Section 0 — Project inventory

Counts as of 2026-05-03 09:30. `~/.claude/projects/` has 97 subdirectories — most are spent worktrees with 0–1 stale jsonl. The signal collapses cleanly into three parent repos.

### 0a + 0b. Claude Code session volume (30 days), aggregated

| Parent repo | 30d sessions (main + worktrees) | `project:` frontmatter labels (counts) |
|---|---|---|
| `~/My Brain/knowledge-base` (+ worktrees + raw) | ~125 | `Brain/KB` (53), `Brain/MyBrain` (2) |
| `~/My Brain/pi-workspace` (+ worktrees) | ~111 | `Brain/Automations` (96) |
| `~/luna-brain` (+ worktrees) | ~120 | `Clio` (39) |
| `~/My Brain` (vault root) | 41 | (mixed) |
| `~` (home-cwd) | 16 | `Home` (1) |
| `-` (orphan, no cwd) | 11 | `-` (11) |

**Three project labels carry all the signal: `Brain/Automations`, `Brain/KB`, `Clio`.** No client labels. No OpenClaw / vllm-mlx / agent-canvas-ui / wiki-os-brain labels — confirmed by 0c (those repos have no Claude project dir).

**Anomalies:** the 11 `project: "-"` orphan sessions are recent (newest 2026-05-03) — flagged in §5. Label-quote-style is inconsistent (`Brain/Automations` vs `"Brain/Automations"`); the weekly rollup double-counts unless normalized. 50+ stale worktree labels have 0 jsonl — cosmetic.

### 0c. Home-directory repos (top-level `~` only)

| Path | Last commit | Origin | Classification |
|---|---|---|---|
| `~/My Brain/knowledge-base` | 2026-05-03 (auto ingestion) | (felipeu28 only) | Internal — Brain (hot) |
| `~/My Brain/pi-workspace` | 2026-05-03 (briefing CI line) | `Felipeu28/moil-brain-workspace` | Internal — Brain (hot) |
| `~/luna-brain` | 2026-05-01 (graph edges fix #42) | `Felipeu28/Clio` | **Startup — Clio** |
| `~/agent-canvas-ui` | (no commits visible) | `openclaw/agent-canvas-ui` | Ambiguous — fork? |
| `~/vllm-mlx` | 2026-02-24 ("ss") | `waybarrios/vllm-mlx` | Internal — infra fork (dormant) |
| `~/wiki-os-brain` | 2026-04-12 | `Ansub/wiki-os` | Ambiguous — third-party fork |
| `~/OpenClawAgent/workspace` | 2026-03-30 | `JarvisUrregoTX/jarvis-workstation` | Internal — OpenClaw (dormant 30+d) |
| `~/OpenClawAgent/workspace/browser-agent` | 2026-02-18 | `kellyclaudeai/browser-agent` | Internal — OpenClaw (dormant 70+d) |

Non-git top-level dirs that look project-shaped but aren't tracked: `bot_workspace`, `clio-video`, `clio-video-assets`, `clio-voice-test`, `VoxTrends`, `workspaces`. Scratch surfaces.

### 0d. Grouped inventory

**Startups (2)** — get dedicated `wiki/projects/<slug>.md` + dedicated briefing block.

| Slug | Repo | 30d sessions | Status |
|---|---|---|---|
| `moil` | Felipeu28 org: `Moil-Code/*`, `Moil-Landingpages/*`, `Moil360` (none cloned at `~/`; signal via `github-activity.sh`) | indirect — covered by Brain repos' sessions | active, 13 paying clients per `wiki/moil/active-projects.md` |
| `clio` | `~/luna-brain` (= `Felipeu28/Clio`) | ~120 | active — Phase 1 |

**Client projects (13 paying, 10 warm)** — Tier 1 + 4 of `wiki/moil/active-projects.md`. None has a Claude session label. **Default policy: clients live in `wiki/orgs/` + the Tier-1 ledger; they do *not* get `wiki/projects/<slug>.md` unless promoted.** Section 5 question 1 asks Andres which (if any) of FitLogic, Connectex, Buda EDC/HIVE, Meridian Buda earn promotion.

**Internal / personal (8)** — only the two Brain repos are hot.

| Project | Activity |
|---|---|
| Brain — knowledge-base, pi-workspace | hot |
| OpenClaw dashboard, browser-agent | dormant (30+d, 70+d) |
| vllm-mlx, agent-canvas-ui, wiki-os-brain | dormant forks |
| Tier 5 personal (`fantelo`, `Lunabella`, `magical-reading-adventures`, `KyleBudaSpotlight`, `VoxTrends`, `CampaignControl`, `REFERREDLOCAL`) | mixed; 2 dormant 55+d |

**Ambiguous (3)** — see §5: `agent-canvas-ui`, `wiki-os-brain`, the orphan-session class.

---

## Section 1 — Phased rollout

Ordered by leverage × dependency. Week-1 Day-1 Item-1 is the entity-graph load: Andres asked for it sequenced into the plan rather than fixed ahead of approval.

### Week 1 — Restore broken ingestion + ship the freshness sentinel

1. **Load `com.moil.brain.entity-graph.plist` into launchd.** P0 — fixes audit §B's most critical drift.
2. **Build `bin/sentinel.sh` + `sentinel-config.yml` + wire into morning briefing.** Systemic answer to silent failures.
3. **Diagnose + repair `weekly-operating-brief.sh`.** Find the silent bail; fix or relax the precondition.
4. **Add fail-loud zero-item guard to `scrape-x-bookmarks.sh`.** Stops the cascade that broke operating-brief.

### Week 2 — Cross-project tracking + per-project rollups

5. **Stand up `wiki/projects/` for Moil + Clio (the two startups).** Create the schema; seed two pages.
6. **Build `bin/project-activity.sh` daily rollup.** Reads sessions + git + briefings, updates project pages.
7. **Restructure morning briefing's project sections** — dedicated Moil & Clio block; rolled-up Client Project Pulse from `wiki/moil/active-projects.md`.
8. **Replace `weekly-sessions-*.md` mechanical rollup with a real session-learnings extractor.** K&T#9 generator-verifier ethos applied to session intake.

### Week 3 — Make ChromaDB do work + tighten loops

9. **Wire ChromaDB historical context into `daily-correlator.py`.** First real automated query of the index.
10. **Run `pattern-surfacer.sh` on a rolling 28-day window, twice per week.** Audit recommendation #6.
11. **Fold `compute-last-contact.py` output into a persisted wiki page.** Audit recommendation #7.

### Week 4 — Forcing-function rituals (Karpathy/Tan-flavored)

12. **Concept-of-the-day surfacer + 12 seeded concepts.** K&T#3 — durable mental-model nodes wired into morning briefing.
13. **Monday "two-sentence pitch + this-week's-mistake" prompts in morning briefing.** K&T#8.
14. **Append-and-review inbox with hotkey + weekly rescue.** K&T#4.

Deferred to a v2 plan and not included this month: Slack pull (audit #8), voice-note autoflow (audit #9), gstack/clio-stack adoption (K&T#2 — Andres needs to decide whether Clio gets its own skill suite separately), evals harness (K&T#5 — Clio team decision), annual letter cron (K&T#6 — December), `vibe/` directory (K&T#7 — attitude shift, no infra needed), per-job verifier (K&T#9 — second layer of work after sentinel proves itself).

---

## Section 2 — Per-item spec

### 1. Load `com.moil.brain.entity-graph` into launchd

- **Gap:** Audit §B critical — plist on disk, not loaded; `wiki/hot/relationship-radar.md` frozen at Apr 22; 11–12 days silent. Audit §D #1.
- **Change:** Run the manual load step `~/CLAUDE.md` reserves to Andres. One-time.
- **Effort:** S — 30s execute, 2 min verify.
- **Composition:** Restores `wiki/hot/{relationship-radar, open-commitments, entity-queue}.md`. Item 9 then compounds against fresh data.
- **Acceptance:** `launchctl list | grep com.moil.brain.entity-graph` non-empty · 2026-05-04 `wiki/hot/relationship-radar.md` `last_updated:` reads today not 2026-04-22 · briefing's "going cold" section is non-stale.
- **First command:** `launchctl bootstrap gui/$(id -u) ~/My\ Brain/pi-workspace/launchd/com.moil.brain.entity-graph.plist` (Andres's preferred bootstrap variant; per `~/CLAUDE.md` he runs this himself).

### 2. Build `bin/sentinel.sh` + `sentinel-config.yml` + wire into morning briefing

- **Gap:** Audit §D #12, #13. Two "broken for 10+ days" failures in one day (CI deploy, entity-graph). The CI status line shipped 2026-05-03 fixes one specific surface; this is the general form. Schema and rules in §4b.
- **Change:**
  - New: `pi-workspace/bin/sentinel.sh` (~80 lines bash). Reads `sentinel-config.yml`, stats log + destination per row, emits markdown table.
  - New: `pi-workspace/sentinel-config.yml` — 10 entries, one per plist (schema in §4b).
  - New plist: `com.moil.brain.sentinel.plist`, daily 08:30. Writes `outputs/health/sentinel-latest.md`.
  - Edit `morning-briefing.sh`: after the CI-status block, inject `sentinel-latest.md` under `## Freshness Sentinel`.
- **Effort:** M — ~90 min. Honest M (no LLM, just stat() + arithmetic).
- **Composition:** Same surface as the CI line. After shipping, item 1's health is auto-verified daily — next silent failure surfaces within 36 hours.
- **Acceptance:** `bash pi-workspace/bin/sentinel.sh` standalone emits 10-row markdown table · 2026-05-04 briefing has `## Freshness Sentinel` block · backdate `.entity-graph-log` 4d → row goes red.
- **First command:** `code pi-workspace/sentinel-config.yml` (define schema first, script second).

### 3. Diagnose + repair `weekly-operating-brief.sh`

- **Gap:** Audit §B — 1 operating brief in 30d. Either not loaded, or silently bailing on the bookmark-count check (audit §D #2). Sunday-night decision doc that walks Andres into Monday.
- **Change:** Read `.operating-brief-log` + `launchctl list` to identify failure mode. If not loaded, bootstrap the plist. If silent-bailing, relax line 54's `BOOKMARK_FILES -eq 0` precondition to "0 bookmarks but ≥3 email or teams files = run with degraded grounding," and always log a one-line reason on bail.
- **Effort:** S — 20 min investigate + 15 min edit.
- **Composition:** Sentinel covers future skips. Output unchanged: `outputs/operating-brief/YYYY-WNN.md` + email.
- **Acceptance:** Sun 2026-05-04 evening, fresh `outputs/operating-brief/2026-W18.md` exists · log shows a reason on every non-run.
- **First command:** `tail -50 pi-workspace/.operating-brief-log; launchctl list | grep operating-brief`.

### 4. Fail-loud zero-item guard in `scrape-x-bookmarks.sh`

- **Gap:** Audit §B / §D #3 — three silent zero-item runs on 2026-05-02 before manual retry produced 214; the Apr 25 file is a committed 234-byte placeholder. Cascades into operating-brief skipping.
- **Change:** After scrape, count items. If `last_known_good > 50` and `today_count < 5`: write a warning-header file, exit non-zero, **skip the commit step**.
- **Effort:** S — 30 min including threshold test.
- **Composition:** Sentinel (item 2) treats the missing file as stale; the editorial job's last-known-good fallback keeps it running.
- **Acceptance:** Mock zero-item scrape → non-zero exit, no commit, no committed placeholder · real scrape with 50+ items behaves as today.
- **First command:** `grep -n 'item.*count\|wc -l' pi-workspace/bin/scrape-x-bookmarks.sh`.

### 5. Stand up `wiki/projects/` for Moil + Clio

- **Gap:** `wiki/projects/` already exists but holds only Tier 5 personal projects. The two startups have no aggregating page. Karpathy's compounding-wiki ethos says: every meaningful thing gets a page.
- **Change:** Create `wiki/projects/moil.md` and `wiki/projects/clio.md` (`graph/hub`, `type: startup`, `status: active`, `last_touched`). Schema in §3a. Update `wiki/projects/README.md` index. Link both from `wiki/andres/ANDRES.md`.
- **Effort:** S — 45 min.
- **Composition:** Item 6 writes to these pages; item 7 surfaces them; item 8 fills the `## Recent decisions` block.
- **Acceptance:** Both pages exist with §3a schema · `kb-health.py` passes · ANDRES.md lists both.
- **First command:** `cp wiki/projects/lunabella.md wiki/projects/clio.md` (use as layout reference).

### 6. Build `bin/project-activity.sh` daily rollup

- **Gap:** Item 5's pages are static without this. Andres asked for per-project activity surfaced daily.
- **Change:** New `pi-workspace/bin/project-activity.sh` (~120 lines). Reads `pi-workspace/project-config.yml` (curated tracked-projects list — see §3b for the anti-pattern guard). Inputs: last 7d `raw/sessions/*.md` (filtered by `project:` frontmatter), last 7d `outputs/github-activity-*.md` (filtered by repo), latest `outputs/operating-brief/*.md`. Rewrites each `wiki/projects/<slug>.md`'s `## Last 7 days` block (session count + top 3 asks + commits-by-day + operating-brief mentions) and updates `last_touched:`. New plist daily 08:00, before briefing at 08:45.
  - Initial `project-config.yml`: `startups: [moil, clio]` with `session_label_match: ["Brain/KB","Brain/Automations"]` for moil (closest proxy — no "Moil" session label exists) and `["Clio"]` for clio. Clients section populated only after Section 5 question 1 is answered.
- **Effort:** M — 90 min. Pure aggregation, no LLM.
- **Composition:** Builds on item 5; flows into item 7; sentinel covers it.
- **Acceptance:** Standalone run populates `## Last 7 days` on both startup pages with today's `last_touched` · `sync_wiki.sh && kb-health.py` clean.
- **First command:** `code pi-workspace/project-config.yml` (schema first).

### 7. Restructure morning briefing's project sections

- **Gap:** Andres's request: startups dedicated, clients rolled up, internal/personal hidden unless fresh.
- **Change:** Edit `morning-briefing.sh`. After the sentinel block, inject (a) `## This Week — Moil & Clio` (concat the two startup pages' `## Last 7 days` blocks), (b) `## Client Project Pulse` (one row per Tier 1 + Tier 4 client from `wiki/moil/active-projects.md`, sorted by staleness desc, capped at 15 rows). Tier 5 personal projects only if `last_touched < 7d`.
- **Effort:** S — 30 min.
- **Composition:** Reads items 5+6's outputs. No new data source.
- **Acceptance:** 2026-05-04 briefing has both headings, Client Pulse sorted by staleness desc.
- **First command:** `grep -n '## ' pi-workspace/bin/morning-briefing.sh | head -30`.

### 8. Replace `weekly-sessions-*.md` mechanical rollup with a session-learnings extractor

- **Gap:** Audit §C / §D #4. Rollup is `count + truncated first prompt`, polluted by automation-sessions (correlator, editor, plan-radar). 78 human sessions/week, zero "what changed in Andres's thinking this week" output. K&T#9 generator-verifier ethos: the LLM reads sessions back.
- **Change:** Edit `pi-workspace/bin/ingest-claude-sessions.py` rollup writer. (a) Filter sessions whose first prompt matches automation patterns (constant-list of known automation prompts). (b) Send remaining sessions' per-session summaries to one Claude call → extract Decisions / Tools used / Recurring frictions / Unresolved (asked-twice). (c) When `project:` matches `Clio`/`Brain/KB`/`Brain/Automations`, tag the decision. Item 6 reads this output for each project page's `## Recent decisions`.
- **Effort:** L — half-day. Prompt design + automation-filter tuning + per-project attribution + 3-week eval spot-check.
- **Composition:** Replaces (not augments) the mechanical "By project" table. Output flows into item 6.
- **Acceptance:** 2026-05-10 rollup has 4 sections each with ≥3 substantive items · zero automation-prompt sessions named · at least one decision project-tagged.
- **First command:** `code pi-workspace/bin/ingest-claude-sessions.py`.

### 9. Wire ChromaDB historical context into `daily-correlator.py`

- **Gap:** Audit §C / §D #5 — 3,156 chunks daily, zero queries. Correlator's silence-anomaly section sharpens dramatically with 90-day cadence vs. 7-day `hot.md`.
- **Change:** Edit `daily-correlator.py` `build_context()`. For top-3 active persons by yesterday's mention count, run `wiki-to-chromadb.py --query "<name>" --top 10`. Inject hits as a "Historical context (90d)" block in the prompt. Cap at 3 persons to keep latency <5s.
- **Effort:** M — 90 min (subprocess + prompt + spot-check).
- **Composition:** Strengthens the strongest existing script. Pairs with item 1.
- **Acceptance:** 2026-05-04 `signal-brief-*.md` has Historical-context block · silence-anomaly references "historical cadence every Nd" not just "silent X days".
- **First command:** `grep -n 'def build_context' pi-workspace/bin/daily-correlator.py`.

### 10. Pattern-surfacer 28-day window, twice/week

- **Gap:** Audit §D #6 — ran once in 30 days; 7d window misses 2-3 week arcs.
- **Change:** Edit `pattern-surfacer.sh` → add `MONTH_AGO=$(date -v -28d ...)` second pass; output `## Rolling 28-day patterns` in the same file. Edit plist to fire Wed + Sun 07:00.
- **Effort:** S — 45 min (prompt scaffolding exists).
- **Composition:** Sentinel entry: max 96h stale.
- **Acceptance:** Wed 2026-05-06 morning has fresh `outputs/patterns/*-patterns.md` with both `## This week` and `## Rolling 28-day` sections.
- **First command:** `grep -n 'WEEK_AGO\|date -v' pi-workspace/bin/pattern-surfacer.sh`.

### 11. Persist `compute-last-contact.py` output

- **Gap:** Audit §D #7 — JSON to stdout, consumed once, discarded. Historical cadence not persisted.
- **Change:** Add `--write` flag → writes `wiki/hot/relationship-signals.md` (graph/leaf, auto). Edit `morning-briefing.sh` to call with `--write`.
- **Effort:** S — 30 min.
- **Composition:** Cross-checks the entity-graph radar. Disagreement is diagnostic.
- **Acceptance:** File exists, regenerated daily · kb-health passes.
- **First command:** `grep -n 'argparse\|argv' pi-workspace/bin/compute-last-contact.py`.

### 12. Concept-of-the-day surfacer + 12 seeded concepts

- **Gap:** K&T#3. Karpathy/Tan return to ~8 mental models constantly. Brain captures sessions but no durable mental-model nodes that get re-touched on schedule.
- **Change:** Seed 12 concept pages (most exist; gap-fill: Software 3.0, Animals-vs-Ghosts, Vibe Coding, Append-and-Review, Generator-Verifier, Earnestness, Founder Mode, Idea Maze, Two-Sentence Pitch, Why Now, Evals-as-Moat, Power-to-the-People). Each gets frontmatter `mental-model: true` + `last_revisited`. New `bin/concept-of-the-day.sh`: picks oldest `last_revisited` from `mental-model: true` pages, emits paragraph + forcing question into `## Concept of the day` briefing block. `last_revisited` updates manually when item 13's Monday block records an answer.
- **Effort:** M — 90 min (~6 pages need real seeding + script + briefing edit).
- **Composition:** Pattern-surfacer (item 10) can later detect concept re-emergence in code.
- **Acceptance:** 12 concept pages with both frontmatter fields · 2026-05-04 briefing has the block.
- **First command:** `ls wiki/concepts/ | head -30`.

### 13. Monday two-sentence pitch + this-week's-mistake prompts

- **Gap:** K&T#8. Tan's pitch-as-mantra + mistake-as-most-viewed-YouTube. Zero-cost forcing functions.
- **Change:** Edit `morning-briefing.sh`: on Monday (`date +%u == 1`), inject `## Monday founder block` with the two prompts. Andres's written responses → existing `weekly-compile.sh` ingests into new `wiki/founder/{pitches,mistakes}.md`.
- **Effort:** S — 20 min.
- **Composition:** Layered on briefing + weekly-compile. No new automation.
- **Acceptance:** Mon 2026-05-04 briefing has the block; Tue–Sun don't.
- **First command:** `date +%u`.

### 14. Append-and-review inbox + hotkey + weekly rescue

- **Gap:** K&T#4. Many capture surfaces, no fast-fragmentary-thought slot.
- **Change:** `touch raw/inbox/notes.md` with `graph/leaf` frontmatter and the watch:/read:/listen: tag rule. Bind Raycast/Alfred hotkey to open at line 3. Edit `weekly-compile.sh` to read the file. Sunday rescue ritual stays manual (15 min).
- **Effort:** S — 15 min for file + hotkey; rescue is recurring time.
- **Composition:** Reuses weekly-compile.
- **Acceptance:** File exists, hotkey works · Fri 2026-05-08 compile excerpts the file.
- **First command:** `touch "/Users/jarvisurrego/My Brain/knowledge-base/raw/inbox/notes.md"`.

---

## Section 3 — Cross-project tracking design

Standalone treatment of items 5, 6, 7 plus the discipline that keeps them honest.

### 3a. Storage layout — `wiki/projects/`

Schema for every page in this folder:

```yaml
---
tags: [graph/hub]              # graph/hub for startups; graph/spoke for personal/client-promoted; graph/leaf when archived
status: active                 # active | warm | dormant | archived
type: startup                  # startup | client | personal | internal
last_touched: 2026-05-03       # auto-maintained
---
# <Name>
**Repo(s):** <list>  **Contacts:** [[wiki/people/...]]
## Status        ← manual prose, ≤3 sentences (stage, next decision-maker, blocker)
## Last 7 days   ← auto by bin/project-activity.sh
## Recent decisions  ← auto-extracted from weekly-sessions (item 8) + operating-brief
## Open questions    ← manual, 3–7 items
## Connections       ← [[wiki/...]] backlinks
```

**Per-tier policy:**

| Page kind | Folder | Tag | Auto-rollup |
|---|---|---|---|
| Startup (Moil, Clio) | `wiki/projects/<slug>.md` | `graph/hub` | daily |
| Personal active (Tier 5) | `wiki/projects/<slug>.md` (already present) | `graph/spoke` | daily — empty most days (dormant) |
| Client (Tier 1 + 4) | **NOT a separate page** — `wiki/orgs/<slug>.md` + row in `wiki/moil/active-projects.md` | `graph/spoke` | indirectly via item 7's Client Pulse |
| Internal infra | implicit | — | — |

**Why clients don't get their own `wiki/projects/<slug>.md`:** they already have `wiki/orgs/<slug>.md` + a row in the canonical ledger. Duplicating violates the source-of-truth hierarchy. **Promote a client to a project page only when the engagement is multi-quarter / multi-repo / custom-build** — §5 question 1 names the four candidates.

### 3b. Rollup script contract — `bin/project-activity.sh`

- **Schedule:** daily 08:00, before morning-briefing.
- **Reads:** `pi-workspace/project-config.yml`, last 7d `raw/sessions/*.md`, last 7d `outputs/github-activity-*.md`, latest `outputs/operating-brief/*.md`, latest `weekly-sessions-*.md`.
- **Writes:** `## Last 7 days` + `## Recent decisions` of each tracked `wiki/projects/<slug>.md`; updates `last_touched:`; runs `sync_wiki.sh`.

**Anti-pattern guard (load-bearing):** **Do not auto-derive the project list from `~/.claude/projects/`.** §0 shows 95% of those 97 labels are scratch / spent worktrees / one-off cwd. The list is **curated** in `project-config.yml`. The rule: every project page has a stable repo *and* named contacts *and* manual status prose; if those three are missing, it's not a project, it's a session.

### 3c. Briefing surfacing (item 7 specifics)

- `## This Week — Moil & Clio` — full `## Last 7 days` blocks from both startup pages, side by side. Top of the briefing.
- `## Client Project Pulse` — one row per Tier 1 + Tier 4 client from `wiki/moil/active-projects.md`. Columns: Client · Days since touch · Latest decision. Sorted by staleness desc within tier; cap 15 rows.
- **Internal/personal stays out** unless `last_touched < 7d`; rare. When present, a one-line `## Personal projects` block at the bottom.

### 3d. Composition with the sentinel

`sentinel-config.yml` gets a `project-activity` entry (daily, 36h, non-critical) plus destination checks on the startup pages. **A startup with 14+ days untouched is a yellow flag, not a red alarm** — the briefing's Moil & Clio block surfaces "Clio quiet for 14 days"; Andres decides if that's a focus week or drift.

---

## Section 4 — Defenses against silent failure

We've now hit two "broken for 10+ days" failures in one day:
- The GitHub Pages deploy was red for 10 days (CI status line shipped 2026-05-03 fixes the surface).
- The entity-graph plist was unloaded for 11+ days (item 1 fixes; this section ensures it's caught next time).

The pattern is the same: **a job stops running, no destination changes, no human checks.** The CI fix addressed one specific job (deploy.yml). The systematic answer is **one freshness sentinel that knows about every plist**.

### 4a. Why one centralized sentinel beats the alternatives

Considered alternatives:

| Approach | Why not |
|---|---|
| Grafana / Prometheus dashboard | Single-user laptop. No daemon to scrape. Overkill. |
| Slack webhook on each script's tail | Andres's Slack is for customer comms, not Brain self-talk. Will become noise; will be muted. |
| External uptime monitor (UptimeRobot, Healthchecks.io) per job | Requires every script to ping out. 10 jobs × outbound pings = config sprawl. Fails offline. |
| Per-job verifier (K&T#9) | Different problem — verifier checks *correctness* of output. Sentinel checks *existence*. Both are useful; sentinel is cheaper and addresses the failure class we keep hitting. |
| Email-on-error from each script | Each script needs the error path coded. Misses silent success-with-zero-output failures (the X bookmark Apr 25 case). |

The right fit for a single-user laptop-resident system: **stat() the log files and destinations, render to markdown, embed in the morning briefing**. Andres reads the briefing every weekday; that's already the place he sees Brain status. No new surface, no new noise, no daemon, no internet dep.

### 4b. `sentinel-config.yml` schema

One entry per scheduled job. Required keys: `name`, `log`, `destination`, `expected_max_hours`, `critical`. Optional: `skip_on` (weekday filter), `destination_glob` (filter when destination is a dir), `destination_min_size_bytes` (zero-item guard).

```yaml
jobs:
  - name: entity-graph
    log: pi-workspace/.entity-graph-log
    destination: knowledge-base/wiki/hot/relationship-radar.md
    expected_max_hours: 36                      # 2× the 24h interval
    critical: true

  - name: morning-briefing
    log: pi-workspace/.morning-briefing-log
    destination: knowledge-base/quartz/content/raw/briefings/
    expected_max_hours: 30
    skip_on: [Sat, Sun]
    critical: true

  - name: x-bookmarks
    log: pi-workspace/.x-bookmarks-log
    destination: knowledge-base/raw/
    destination_glob: "x-bookmarks-*.md"
    destination_min_size_bytes: 5000             # catches the Apr 25 zero-item case
    expected_max_hours: 30
    critical: false

  - name: weekly-operating-brief
    log: pi-workspace/.operating-brief-log
    destination: knowledge-base/outputs/operating-brief/
    expected_max_hours: 192                      # weekly, 8d margin
    critical: false

  # plus: chroma-index, pattern-surfacer, kb-health, project-activity, teams-daily, email-digest
```

**Stale rules (per row, OR-combined):** `now - mtime(log) > expected_max_hours` · `now - mtime(newest file matching destination_glob in destination) > expected_max_hours` · `destination_min_size_bytes` set and newest file smaller (zero-item guard). Skip if today's weekday is in `skip_on`.

### 4c. Output format (injected into morning briefing)

```markdown
## Freshness Sentinel
Last checked: 2026-05-04 08:30

| Job | Status | Last log | Last output | Expected max |
|---|---|---|---|---|
| entity-graph | 🟢 ok | 2026-05-04 00:15 | 2026-05-04 00:15 | 36h |
| morning-briefing | 🟢 ok | 2026-05-04 08:45 | 2026-05-04 08:45 | 30h |
| weekly-operating-brief | 🟡 stale 9d | 2026-04-25 20:00 | 2026-04-26 20:00 | 192h |
| x-bookmarks | 🔴 zero-item run | 2026-05-03 19:00 | 234 bytes | 30h + 5KB |
```

🔴 only when `critical: true` *and* stale. 🟡 for non-critical staleness. The CI line we shipped today uses 🔴; the sentinel's red prefix matches.

### 4d. Where it lands

`pi-workspace/bin/morning-briefing.sh` — insertion order in the briefing:

1. H1 + date (existing)
2. Site CI status line (shipped 2026-05-03)
3. **`## Freshness Sentinel` block (new — item 2)**
4. `## Concept of the day` (new — item 12)
5. `## This Week — Moil & Clio` (new — item 7)
6. `## Client Project Pulse` (new — item 7)
7. Existing briefing body (calendar / email / GitHub / signal-brief)
8. `## Monday founder block` on Mondays only (new — item 13)

The sentinel block lives near the top because it's the **trust signal**: "the rest of this document is fresh." If any critical row is red, Andres knows to discount the briefing's "going cold" / pattern claims.

### 4e. Defending the choice

A grandfathered observability system would be over-engineered. The sentinel is ~80 lines of bash, one config file, one plist, one block in the briefing. Cost of building: 90 minutes. Cost of running: ~2 seconds/day. Cost of a missed silent failure (we just experienced two): days to weeks of Brain dysfunction. The ROI is obvious. The fact that the briefing is the readout surface means **adding observability cannot fail to be observed** — there is no separate dashboard for Andres to forget to check.

---

## Section 5 — Resolved decisions (locked 2026-05-03)

All seven open questions answered by Andres on 2026-05-03 before execution. Captured here as the authoritative record:

1. **Client project pages — all four promoted.** [`wiki/projects/fitlogic.md`](../../wiki/projects/fitlogic.md), [`wiki/projects/connectex.md`](../../wiki/projects/connectex.md), [`wiki/projects/buda-edc-hive.md`](../../wiki/projects/buda-edc-hive.md), [`wiki/projects/meridian-buda.md`](../../wiki/projects/meridian-buda.md) get dedicated pages alongside `moil.md` and `clio.md`. Section 3a's "default no" is overridden — these four are big enough to earn first-class status. Item 6's `project-config.yml` gets all six slugs at week-2 implementation.

2. **Sentinel ships with email-on-red.** Briefing line *and* `--email-on-critical` page. Item 2 grew the flag. **Shipped 2026-05-03** — see resolution log below.

3. **K&T#1 — small extension layered on top.** Karpathy's `## Related` backlink block is genuinely additive — explicit beats hidden. Treat the existing `knowledge-base/CLAUDE.md` + `/brain-ingest`/`/brain-query`/`/brain-lint` as the foundation; add a Week-3 lint pass that asserts every `wiki/people/*` and `wiki/projects/*` page carries a `## Related` block with ≥1 backlink. New item slotted in as **item 12 → 12a (Related-block lint)**.

4. **Orphan sessions — diagnosed 2026-05-03.** All 11 `project: "-"` sessions are the daily-correlator's *own* automated invocations (`source_jsonl: ~/.claude/projects/-/...`). Cause: the launchd job invokes `claude` with no working directory, so Claude Code derives the `-` project label. Not a Spotlight launch, not a real user session. **Fix routed to item 8 (correlator-output filter)** — drop these sessions from `weekly-sessions-*.md` rather than re-attribute them. No backfill needed.

5. **Forks — decided 2026-05-03.**
   - **`~/agent-canvas-ui`** (92 KB, openclaw fork, no recent commits, no brain refs): **delete.** Tiny enough to re-clone if ever wanted. Recommendation surfaced; Andres to `rm -rf ~/agent-canvas-ui` at his leisure.
   - **`~/wiki-os-brain`** (235 MB, Ansub/wiki-os fork, last touched 2026-04-12 with a single image-add commit, no brain refs): **archive.** Was an evaluated Quartz alternative; 235 MB is large enough that we shouldn't keep it active in `~/`. Recommendation: `mv ~/wiki-os-brain ~/archive/` (or `~/.archive/`) — Andres to do at his leisure.

6. **Item 8 — split as recommended.** Quick filter (drop automation-prompt sessions from `weekly-sessions-*.md` rollup) ships as **item 8a in Week 2** (S, ≤30 min). Full session-learnings extractor stays as **item 8b in Week 3** (L), composing with the ChromaDB wake-up.

7. **K&T#2 (gstack/clio-stack for Clio) — parallel track confirmed.** Spinning up as a separate code session in `~/luna-brain`. Out of Brain plan scope.

### Week 1 — execution log (2026-05-03)

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | Load `com.moil.brain.entity-graph` plist | ✅ live | `launchctl list \| grep entity-graph` → loaded |
| 2 | Freshness sentinel + email-on-critical | ✅ live | [bin/sentinel.sh](../../../../pi-workspace/bin/sentinel.sh) · [sentinel-config.tsv](../../../../pi-workspace/sentinel-config.tsv) · [com.moil.brain.sentinel.plist](../../../../pi-workspace/launchd/com.moil.brain.sentinel.plist) all loaded; first run wrote [sentinel-latest.md](../../outputs/health/sentinel-latest.md); briefing wired to inject |
| 3 | Repair weekly-operating-brief | ✅ live | Schedule moved Sunday 20:00 → Monday 08:00 (laptop reliably awake); plist reloaded |
| 4 | Zero-item guard on X bookmarks | ✅ live | [scrape-x-bookmarks.sh](../../../../pi-workspace/bin/scrape-x-bookmarks.sh) quarantines 0-item runs to `*.zero-YYYY-MM-DD.md` and exits 2 |

Items 5–14 unchanged; remaining weeks proceed as written.

---

*End of plan. Total scope: 14 items across 4 weeks, of which 4 are sentinel/observability (items 1, 2, the policy-level discipline in §4, plus the new 12a Related-block lint), 4 are cross-project tracking (5, 6, 7, the design in §3), 4 are synthesis upgrades (8a filter, 8b extractor, 9, 10), 1 is relationship-layer persistence (11), and 3 are Karpathy/Tan-flavored ritual items (12, 13, 14). Effort budget: ~3.5 days of focused work distributed across 4 weeks. Week 1 shipped 2026-05-03.*
