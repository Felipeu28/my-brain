#!/bin/bash
# x_bookmark_commit.sh — Commit the latest X bookmarks digest to GitHub
# Run this after a new x-bookmarks-*.md file lands in raw/

set -e

BRAIN_DIR="$HOME/My Brain/knowledge-base"
TODAY=$(date +%Y-%m-%d)

echo "🔍 Looking for latest X bookmarks file..."
cd "$BRAIN_DIR"

LATEST=$(ls -t raw/x-bookmarks-*.md 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
  echo "❌ No x-bookmarks-*.md file found in raw/. Nothing to commit."
  exit 1
fi

echo "📄 Found: $LATEST"
echo ""
echo "📦 Committing to GitHub..."
git add .
git commit -m "X bookmarks — $TODAY" || echo "Nothing new to commit."
git push

echo ""
echo "✅ Done! $LATEST committed and pushed to felipeu28/my-brain"
