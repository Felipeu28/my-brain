#!/usr/bin/env bash
# Pull 2 months of email history with pagination
set -e

KB_DIR="/Users/jarvisurrego/My Brain/knowledge-base"
DATE=$(date '+%Y-%m-%d')

if [[ "$(uname)" == "Darwin" ]]; then
  SINCE=$(date -u -v-2m '+%Y-%m-%dT00:00:00Z')
else
  SINCE=$(date -u -d "-2 months" '+%Y-%m-%dT00:00:00Z')
fi

echo "Importing email history since ${SINCE}..."

pull_all_pages() {
  local FOLDER="$1"
  local FILTER_FIELD="$2"
  local OUT_FILE="$3"
  local SKIP=0
  local BATCH=100
  local PAGE=0

  echo "[]" > "$OUT_FILE"

  while true; do
    PAGE=$((PAGE + 1))
    echo "  Fetching ${FOLDER} page ${PAGE} (skip=${SKIP})..."

    m365 request \
      --url "https://graph.microsoft.com/v1.0/me/mailFolders/${FOLDER}/messages?\$filter=${FILTER_FIELD} ge ${SINCE}&\$top=${BATCH}&\$skip=${SKIP}&\$orderby=${FILTER_FIELD} desc&\$select=subject,from,toRecipients,${FILTER_FIELD},bodyPreview,importance,isRead" \
      --output json \
      2>/dev/null > "/tmp/brain-page-${FOLDER}.json" || { echo "  API error on page ${PAGE}"; break; }

    COUNT=$(python3 -c "
import json
with open('/tmp/brain-page-${FOLDER}.json') as f:
    d = json.load(f)
items = d.get('value', d if isinstance(d, list) else [])
print(len(items))
" 2>/dev/null || echo "0")

    if [ "$COUNT" = "0" ]; then
      echo "  ${FOLDER}: done after ${SKIP} emails total."
      break
    fi

    python3 -c "
import json
with open('$OUT_FILE') as f: existing = json.load(f)
with open('/tmp/brain-page-${FOLDER}.json') as f: raw = json.load(f)
items = raw.get('value', raw if isinstance(raw, list) else [])
existing.extend(items)
with open('$OUT_FILE', 'w') as f: json.dump(existing, f)
print(f'  Accumulated {len(existing)} ${FOLDER} emails.')
"

    SKIP=$((SKIP + BATCH))

    if [ $SKIP -ge 1000 ]; then
      echo "  ${FOLDER}: hit 1000 email safety cap."
      break
    fi
  done
}

pull_all_pages "inbox" "receivedDateTime" "/tmp/brain-inbox-2m.json"
pull_all_pages "SentItems" "sentDateTime" "/tmp/brain-sent-2m.json"

INBOX_COUNT=$(python3 -c "import json; print(len(json.load(open('/tmp/brain-inbox-2m.json'))))")
SENT_COUNT=$(python3 -c "import json; print(len(json.load(open('/tmp/brain-sent-2m.json'))))")

echo ""
echo "✅ Pulled ${INBOX_COUNT} received + ${SENT_COUNT} sent emails (since ${SINCE})"
echo ""
