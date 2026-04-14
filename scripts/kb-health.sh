#!/usr/bin/env bash
# kb-health.sh — Run weekly brain health audit.
# Writes report to outputs/health/kb-health-YYYY-MM-DD.md + latest.
#
# Usage:
#   bash scripts/kb-health.sh            # print report, write to disk
#   bash scripts/kb-health.sh --strict   # also exit 1 if errors found (for CI)

set -e
cd "$(dirname "$0")/.."

if [[ "$1" == "--strict" ]]; then
  python3 scripts/kb-health.py --write --fail-on-errors
else
  python3 scripts/kb-health.py --write
fi
