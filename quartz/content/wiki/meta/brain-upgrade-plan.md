---
tags:
  - graph/leaf
type: meta
---
# Brain Upgrade Plan — 2026-04-21

**Type:** meta
**Last updated:** 2026-04-21
**Status:** Implemented

Three additions to the Moil Brain: Hot Cache, Brain Save, Vault Lint.
Goal: every session starts warm; important content is capturable on demand; quality regressions surface weekly.

---

## Summary of Changes

| File | Action | Risk |
|------|--------|------|
| `wiki/hot/hot.md` | CREATE — rolling 7-day activity window | Zero (new file) |
| `wiki/meta/vault-health.md` | CREATE — lint report, overwritten weekly | Zero (new file) |
| `pi-workspace/bin/update-hot-cache.py` | CREATE — shared hot cache updater | Zero (new file) |
| `pi-workspace/bin/brain-lint.sh` | REPLACE — expand from 2 to 8 checks, new output path | Low (same interface) |
| `pi-workspace/bin/brain-save.sh` | CREATE — on-demand wiki note capture | Zero (new file) |
| `pi-workspace/bin/brain-query.sh` | MODIFY — add hot cache read at start, update at end | Low (additive only) |
| `pi-workspace/bin/brain-ingest.sh` | MODIFY — add hot cache update at end | Low (additive only) |
| `pi-workspace/bin/weekly-pulse.sh` | MODIFY — add lint call before Claude, non-fatal | Low (wrapped in set+e) |

---

## Feature 1 — Hot Cache

### Files
- `wiki/hot/hot.md` — the cache file (Quartz page, graph/leaf)
- `pi-workspace/bin/update-hot-cache.py` — Python updater called by both scripts

### Hot cache format
```
<!-- ENTRIES:ingest -->
- 2026-04-21 09:15 — 3 files queued, Claude exit 0
<!-- /ENTRIES:ingest -->

<!-- ENTRIES:query -->
- 2026-04-21 14:32 — Q: "What are the 3 most important focus areas?" → Buda HIVE, 2 stale deals, draft due
<!-- /ENTRIES:query -->

<!-- ENTRIES:save -->
- 2026-04-21 15:00 — Saved "Important Insight" → wiki/concepts/important-insight.md
<!-- /ENTRIES:save -->
```

### brain-query.sh changes (additive only)
- **At start (Step 0):** Read `wiki/hot/hot.md` into `$HOT_CACHE_CONTEXT`
- **In Claude prompt:** Add `RECENT BRAIN ACTIVITY:` section with `$HOT_CACHE_CONTEXT`
- **At end (Step 4):** Call `update-hot-cache.py hot.md query "<entry>"`

### brain-ingest.sh changes (additive only)
- **At end:** After ChromaDB re-index, call `update-hot-cache.py hot.md ingest "<entry>"`

### Rollback
- Delete `wiki/hot/hot.md` and `update-hot-cache.py`
- Revert `brain-query.sh` and `brain-ingest.sh` with `git checkout`

---

## Feature 2 — Brain Save

### File
- `pi-workspace/bin/brain-save.sh`

### Signature
```
brain-save.sh --title "Note title" --content "content text"
echo "content" | brain-save.sh --title "Note title"
```

### Behaviour
1. Parse `--title` and `--content` (or read stdin)
2. Validate: title required, content required
3. Call `claude -p` to classify and create wiki page (allowed tools: Read, Write, Edit, Glob, Grep)
4. Parse `SAVED_TO: wiki/path.md` from Claude output
5. Update hot cache (save section)
6. Run `bash scripts/sync_wiki.sh` (non-fatal)

### Classification → directory mapping (done by Claude)
- decision → `wiki/moil/` or `wiki/concepts/`
- insight → `wiki/concepts/`
- meeting-note → `wiki/meetings/`
- conversation-summary → `wiki/summaries/`
- reference → `wiki/concepts/`, `wiki/orgs/`, or `wiki/people/`

### Rollback
- Delete `pi-workspace/bin/brain-save.sh`

---

## Feature 3 — Vault Lint

### File
- `pi-workspace/bin/brain-lint.sh` (replaces existing 2-check version)
- Output: `wiki/meta/vault-health.md` (overwritten) + `quartz/content/raw/outputs/brain-lint-DATE.md` (archive)

### 8 checks (all in try/except — non-fatal)
1. **Orphans** — wiki pages with zero inbound wikilinks
2. **Dead wikilinks** — `[[links]]` that resolve to no wiki page
3. **Stale pages** — `Last updated:` > 60 days ago
4. **Missing frontmatter** — wiki pages missing the `---` YAML block
5. **Empty pages** — wiki pages with < 30 words of body content
6. **Duplicate titles** — two pages with the same `# Title` heading
7. **Broken external links** — HTTP non-2xx with 5s timeout (capped at 20 URLs)
8. **TODO/FIXME markers** — pages containing literal TODO or FIXME text

### weekly-pulse.sh change
Add before the Claude call (wrapped in `set +e / set -e`):
```
LINT_SCRIPT="$WORKSPACE/bin/brain-lint.sh"
set +e
if -x "$LINT_SCRIPT"; then timeout 120 bash "$LINT_SCRIPT"; fi
set -e
```

### Rollback
- `git checkout pi-workspace/bin/brain-lint.sh` (restores old 2-check version)
- `git checkout pi-workspace/bin/weekly-pulse.sh`
- Delete `wiki/meta/vault-health.md`

---

## Testing Plan

```bash
# 1. Verify hot.md is valid markdown
head -10 wiki/hot/hot.md

# 2. Test brain-lint.sh runs without crashing
timeout 120 bash pi-workspace/bin/brain-lint.sh

# 3. Verify vault-health.md was created
cat wiki/meta/vault-health.md | head -20

# 4. Test brain-save.sh with minimal input
echo "Test insight content" | bash pi-workspace/bin/brain-save.sh --title "Test Brain Save 2026-04-21"

# 5. Test hot cache update directly
pi-workspace/.venv/bin/python3 pi-workspace/bin/update-hot-cache.py \
  wiki/hot/hot.md query "- 2026-04-21 12:00 — Test entry"
cat wiki/hot/hot.md

# 6. Verify brain-ingest.sh and brain-query.sh have no syntax errors
bash -n pi-workspace/bin/brain-ingest.sh
bash -n pi-workspace/bin/brain-query.sh
```
