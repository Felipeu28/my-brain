#!/bin/bash
# Fix Brain graph clustering — copies hub README files to Quartz content folder
# Run from anywhere: bash ~/Desktop/fix-brain-graph.sh

set -e

BRAIN="$HOME/My Brain/knowledge-base"
QUARTZ="$BRAIN/quartz/content/wiki"

echo "→ Checking source files..."
for section in concepts moil people summaries; do
  src="$BRAIN/wiki/$section/README.md"
  if [ ! -f "$src" ]; then
    echo "  ⚠️  Missing: $src"
  else
    echo "  ✓ Found: wiki/$section/README.md"
  fi
done

echo ""
echo "→ Copying hub READMEs to Quartz..."
for section in concepts moil people summaries; do
  src="$BRAIN/wiki/$section/README.md"
  dst="$QUARTZ/$section/README.md"
  if [ -f "$src" ]; then
    mkdir -p "$(dirname "$dst")"
    cp "$src" "$dst"
    echo "  ✓ Copied $section/README.md"
  fi
done

echo ""
echo "→ Committing and pushing..."
cd "$BRAIN"
git config user.email "andres@moilapp.com"
git add quartz/content/wiki/concepts/README.md \
        quartz/content/wiki/moil/README.md \
        quartz/content/wiki/people/README.md \
        quartz/content/wiki/summaries/README.md 2>/dev/null || true
git commit -m "Add hub README files — fix graph clustering"
git push felipeu28 main

echo ""
echo "✅ Done! Vercel will redeploy in ~60 seconds."
echo "   Check: https://my-brain-two.vercel.app"
