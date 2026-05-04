---
tags:
  - graph/spoke
---
# Brain Ingestion + Synthesis Audit — 2026-05-03

**Type:** summary
**Last updated:** 2026-05-03
**Source:** [[raw/audits/2026-05-03-ingestion-and-synthesis-audit]], [[raw/audits/2026-05-03-implementation-plan]]
**Related:** [[wiki/concepts/brain-architecture]], [[wiki/projects/moil]], [[wiki/projects/clio]], [[wiki/projects/fitlogic]], [[wiki/projects/connectex]], [[wiki/projects/buda-edc-hive]], [[wiki/projects/meridian-buda]]

---

## Why this page exists

On 2026-05-03 the Brain was self-audited end-to-end: every launchd job, every synthesis script, every freshness check. The audit + companion 4-week implementation plan are the canonical record of what was broken, what shipped same-day to fix it, and what's queued for Weeks 2–4. This summary is the routing layer; the two raw audit files are the long-form record.

## Headline finding

**The Brain is input-rich and reflection-poor.** Capture is mostly working (morning briefing, Teams pull, email digest, X bookmarks, Claude sessions, GitHub activity, ChromaDB index). But the layer that **reads the captured data back into the graph was silently dead**:

1. **`com.moil.brain.entity-graph.plist`** was on disk but never loaded into launchd. `wiki/hot/relationship-radar.md` had been frozen at 2026-04-22 for 11+ days. The morning briefing's "going cold" list was built from stale data.
2. **`weekly-operating-brief.sh`** had run exactly once in 30 days. The Apr 26 file was the only Sunday-night decision doc that existed.
3. **`weekly-sessions-*.md`** rollup was mechanical — `count + truncated first prompt` — polluted by automation-self-runs (the correlator + editor + plan-radar were showing up as if they were Andres's sessions). Zero "what changed in your thinking this week" output across 78 sessions/week.
4. **ChromaDB** indexed 3,156 chunks daily but **zero scripts queried it.** Episodic memory was write-only.
5. **`scrape-x-bookmarks.sh`** had shipped three silent zero-item runs on 2026-05-02 before a manual retry; the Apr 25 file was a committed 234-byte placeholder. Cascaded into operating-brief skipping.
6. **Two "broken for 10+ days" failures in one day** (CI deploy, entity-graph) — same root pattern: a job stops running, no destination changes, no human checks.

## Seven resolved decisions (locked 2026-05-03)

1. **All four client projects get dedicated `wiki/projects/*` pages** — [[wiki/projects/fitlogic]], [[wiki/projects/connectex]], [[wiki/projects/buda-edc-hive]], [[wiki/projects/meridian-buda]] alongside [[wiki/projects/moil]] and [[wiki/projects/clio]]. The "default no" rule for client-as-project was overridden — these four are big enough to earn first-class status.
2. **Sentinel ships with email-on-red.** Briefing line *and* `--email-on-critical` page when any critical row goes stale.
3. **K&T#1 (Karpathy CLAUDE.md ingest/query/lint loop) treated as already shipped.** The existing `knowledge-base/CLAUDE.md` + `/brain-ingest`/`/brain-query`/`/brain-lint` slash commands + `kb-health.py` lint pass cover it. Adding only a `## Related`-block lint pass at Week-3 to assert every `wiki/people/*` and `wiki/projects/*` page carries explicit backlinks.
4. **Orphan sessions diagnosed.** All 11 `project: "-"` Claude sessions are the daily-correlator's *own* automated invocations (launchd job runs `claude` with no working directory, so Claude Code derives the `-` project label). Fix routed to the session-learnings filter — drop them from the rollup rather than re-attribute.
5. **Forks decided** — `~/agent-canvas-ui` (92 KB, no recent commits) → delete; `~/wiki-os-brain` (235 MB, last touched 2026-04-12) → archive to `~/archive/`. Andres to execute at his leisure.
6. **Item 8 split.** Quick automation-prompt filter ships in Week 2 (8a, ≤30 min); full session-learnings extractor stays Week 3 (8b, half-day).
7. **K&T#2 (gstack/clio-stack for Clio) — parallel track.** Spinning up as a separate code session in `~/luna-brain`. Out of Brain plan scope.

## Shipped same-day 2026-05-03

By end of day, **15 of 18 plan items shipped** (Weeks 1, 2, 3, and 4 all collapsed into a single execution day). The Week-by-Week framing in the original plan was wrong about the calendar but right about the dependency order.

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | Load `com.moil.brain.entity-graph` plist | ✅ | `launchctl list \| grep entity-graph` returns loaded |
| 2 | Freshness sentinel + email-on-critical | ✅ | `pi-workspace/bin/sentinel.sh` + `sentinel-config.tsv` + `com.moil.brain.sentinel.plist` all loaded; first run wrote `outputs/health/sentinel-latest.md`; briefing wired to inject |
| 3 | Repair `weekly-operating-brief.sh` | ✅ | Schedule moved Sunday 20:00 → Monday 08:00 (laptop reliably awake then); plist reloaded |
| 4 | Zero-item guard on X bookmarks | ✅ | `scrape-x-bookmarks.sh` quarantines 0-item runs to `*.zero-YYYY-MM-DD.md` and exits 2 — caught the 2026-05-03 cookie-expiry failure cleanly |
| 5 | Stand up `wiki/projects/` for all 6 projects | ✅ | Moil, Clio, FitLogic, Connectex, Buda EDC/HIVE, Meridian Buda — all live |
| 6 | `bin/project-activity.sh` daily rollup | ✅ | Ran once today (moil=58 / clio=23 / fitlogic=4 / connectex/* events); `com.moil.brain.project-activity.plist` loaded; fed by `project-config.tsv` |
| 7 | CI notify-on-failure sidecar + briefing Site CI line | ✅ | `.github/workflows/notify-on-failure.yml` + `feat(briefing): inject Site CI status line below H1` |
| 8a | Filter automation self-runs from weekly rollup | ✅ | `weekly-sessions-2026-05-03.md` shows *"7 automation self-runs filtered out"* |
| 8b | Session-learnings extractor | ✅ | `bin/session-learnings.sh` + `com.moil.brain.session-learnings.plist`; first run committed + pushed |
| 9 | Wire ChromaDB historical context into correlator | ✅ | `daily-correlator.py` + `pattern-surfacer.sh` both query Chroma now |
| 10 | Pattern-surfacer 28-day Wed/Sun cadence | 🟡 partial | Chroma wired ✅; cadence still Sun-only 7-day window — Wed slot pending |
| 11 | Persist `compute-last-contact.py` to `wiki/people` frontmatter | ✅ | First run persisted 6 last_contact updates; `com.moil.brain.last-contact.plist` loaded |
| 12 | Concept-of-the-day surfacer + 12 seeded concepts | ✅ | `concept-of-the-day.sh` + LRU rotation state file; first pick was `buda-hive` |
| 13 | Last-contact computed → wiki/people frontmatter | ✅ | (same artifact as item 11) |
| 14 | Append-and-review inbox + Sunday rescue | 🟡 partial | `append.sh` + Sunday review prompt shipped; OS-level hotkey still manual |
| 15 | Concept-of-the-day rotation | ✅ | (same as item 12) |
| 16 | Karpathy `## Related` linter + Chroma suggester | ✅ | `lint-related.sh` (250 pages scanned, 249 missing — triage workflow ships next) + `related-suggester.sh` (queues 25 pages/day to Chroma) |
| 17 | Append-inbox + Sunday review prompt | ✅ | (same as item 14) |
| 18 | Monday two-sentence pitch + this-week's-mistake | ✅ | `weekly-pitch-mistake.sh` + Monday template; first run wrote `wiki/weekly/...` |

Git commits (pi-workspace): `b90619a feat(brain/briefing): wire Week 4 forcing functions` · `edbdf6b feat(brain/related): Karpathy ## Related linter` · `ee693b9 feat(brain/weekly-pitch-mistake)` · `6d60a1d feat(brain/append-inbox)` · `c50c571 feat(brain/concept-of-the-day)` · `4b99230 feat(brain/learnings)` · `06b2a16 feat(brain/last-contact)` · `472cce1 feat(brain/chroma)` · `e92fed9 feat(brain/ingest): filter correlator self-runs` · `890c237 feat(brain/projects): per-project tracking` · `ec58bf5 feat(brain/sentinel)` · `1c9e9f6 fix(brain/sentinel): bump email-digest threshold` · `188e2bb fix(brain/operating-brief): move schedule` · `6b6f718 fix(brain/bookmarks): zero-item guard` · `897fd9c feat(briefing): inject Site CI status line`.

Git commits (knowledge-base): `7115308 docs(brain/audits)` · `e246967 feat(brain/projects)` · `e340786 feat(brain/week4)` · `fee4175 ci(brain): notify-on-failure sidecar`.

## Still open after 2026-05-03

- **Item 10 cadence** — pattern-surfacer needs the Wed 07:00 slot added and the window widened from 7 → 28 days (Chroma backbone is in place; this is a plist + arg flip)
- **Item 14 hotkey** — `append.sh` is callable from CLI and Sunday review prompt is wired; OS-level keyboard shortcut not yet bound
- **Related-block backfill** — Item 16's linter found 249/250 wiki pages missing `## Related` blocks. Triage workflow is the next layer (queued)
- **Brain-lint consolidation** — old `brain-lint` (stub-finder, orphan-finder) last ran 2026-04-24; needs to merge with the new Related linter into one weekly health pass

## Discovered during the audit (not in the original plan)

- **X cookies expire silently every ~5–7 days.** Apr 27 → May 3 logged 7 daily ERROR entries. Today's audit added the zero-item guard which caught the failure cleanly, but the *root* fix (sentinel threshold tightened to 24h + actionable email body) is queued.
- **`com.moil.brain.weekly-pulse.plist` is a phantom.** Plist loaded in launchd, but `bin/weekly-pulse.sh` was retired in commit `c111d2e`. Functionality is now covered by heartbeat + weekly-compile + operating-brief + sentinel. To be unloaded.
- **`index.md` raw-count drifts every run.** Auto-incrementing logic missing — manual count update needed periodically. Fixed in the next pass.
- **KB `CLAUDE.md` slash-command docs (/brain-ingest etc.) write to `quartz/content/wiki/` — wrong.** The architectural rule at the top of the same file says write to `wiki/`, then `sync_wiki.sh` mirrors. Drift fixed in the next pass.
- **Mem0 should be struck from `CURRENT_STATE.md`.** The v3 plan (line 121) already says "Mem0 + ChromaDB should no longer be described as a mature memory system" — Chroma stays as the only episodic layer; Mem0 referenced only as a memory-types taxonomy.

## Why this page is the right shape

The audit + plan are 1,000+ lines combined. They're meta-content about the Brain itself, not external knowledge to graph. Following the precedent of [[raw/brain-knowledge-layer-analysis|brain-knowledge-layer-analysis]] (Run 10 — logged only), the right move was a single summary page, not a decomposition into per-job pages. This page lets future Claude sessions answer "what's the state of the Brain self-upgrade work?" in two hops from `index.md`.

## Connections

- The 6 `wiki/projects/*` pages are the durable artifacts of this run — they're where item 6's daily rollup will write
- [[wiki/concepts/brain-architecture]] is the upstream concept page (5-layer pipeline); this audit is the operational state of that pipeline as of 2026-05-03
- [[MEMORY]] does not get new items from this audit — the brain self-upgrade work is internal infrastructure, not external commitment to clients/people

## Moil Relevance

The audit is the difference between "Andres has automation" and "Andres has automation he can trust." The sentinel + entity-graph reload mean the morning briefing's signals are no longer silently stale, which is what made the May 1–2 deploy outage and the entity-graph 11-day silence invisible until today.
