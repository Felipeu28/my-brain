# Brain Commands

Quick reference for running and managing the Brain system.

---

## GitHub

Auto-commit runs automatically after Teams pull and X bookmark ingest. For manual use:

**Manual commit:**
```bash
cd ~/My\ Brain/knowledge-base && git add . && git commit -m "Manual sync — $(date +%Y-%m-%d)" && git push
```

**View repo on GitHub:**
```bash
gh repo view felipeu28/my-brain --web
```

**Note:** Auto-commit happens automatically at the end of `teams_ingest.sh` (after Teams pull + Claude ingest) and when you run `x_bookmark_commit.sh` after a new bookmarks digest lands.

---

## Teams

**Pull latest Teams messages + ingest into Brain:**
```bash
cd ~/My\ Brain/knowledge-base && bash scripts/teams_ingest.sh
```
This pulls 7 days of Teams messages, saves to `raw/teams-YYYY-MM-DD.md`, runs Claude ingest to update Brain files, then auto-commits and pushes to GitHub.

**Pull Teams messages only (no ingest):**
```bash
cd ~/My\ Brain/knowledge-base && python3 scripts/teams_pull.py --days 7
```

---

## Health

**Generate a Brain heartbeat report:**
```bash
bash ~/My\ Brain/pi-workspace/bin/brain-heartbeat.sh
```
Writes a freshness snapshot to `knowledge-base/outputs/health/heartbeat-YYYY-MM-DD.md` and updates `heartbeat-latest.md`.

---

## X Bookmarks

**Commit latest X bookmarks digest to GitHub:**
```bash
cd ~/My\ Brain/knowledge-base && bash scripts/x_bookmark_commit.sh
```
Finds the most recent `raw/x-bookmarks-*.md` file and commits + pushes it.

---

## Brain Queries

Run these via Claude Cowork or paste into any Claude session with your Brain files attached.

**Weekly digest query:**
```
Read raw/x-bookmarks-[latest].md and give me:
1. Top 5 most actionable items for my work
2. Any patterns or themes worth tracking
3. Connections to things I've been working on
```

**Monthly synthesis:**
```
You are building a personal knowledge graph for my Brain.
Given these 4 weeks of bookmark digests, synthesize:
- Recurring themes across weeks
- Emerging signals worth watching
- Connections between topics
- My apparent priorities based on what I've been saving
```
