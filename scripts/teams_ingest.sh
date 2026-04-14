#!/bin/bash
# teams_ingest.sh — Pull Teams messages + auto-ingest into Brain
# Run this weekly (or add to cron). It pulls, saves, and processes.

set -e

BRAIN_DIR="$HOME/My Brain/knowledge-base"
TODAY=$(date +%Y-%m-%d)

echo "🔄 Pulling Teams messages..."
cd "$BRAIN_DIR"
python3 scripts/teams_pull.py --days 7

echo ""
echo "🧠 Ingesting into Brain..."
claude -p "I just added raw/teams-$TODAY.md to the Brain.
Read it carefully and:
1. Extract all decisions made (who decided what, when)
2. Extract all action items (who owns what, any deadlines mentioned)
3. Extract key context, announcements, or strategy shifts
4. Update Action-Tracker.md with any new action items
5. Update Decision-Log.md with any decisions
6. Update Memory.md if there's context Claude should remember
7. Update index.md to include the new teams file
Show me a summary of what you found and what you updated." \
--allowedTools Bash,Write,Read

echo ""
echo "🔁 Syncing wiki/ → quartz/content/ before commit..."
cd "$BRAIN_DIR"
bash scripts/sync_wiki.sh

echo ""
echo "📦 Committing to GitHub..."
git add .
git commit -m "Teams pull — $(date +%Y-%m-%d)" || echo "Nothing new to commit."
git push felipeu28 main

echo ""
echo "✅ Done! Teams digest is in raw/teams-$TODAY.md"
echo "   Brain files updated: Action-Tracker.md, Decision-Log.md, Memory.md"
echo "   Changes pushed to GitHub (origin) → Vercel redeploy triggered"
