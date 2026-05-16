#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="${PY:-$ROOT/.venv/bin/python}"
TS="$(date +%Y%m%d-%H%M%S)"
WIKI_DIR="$ROOT/.codex_tmp/momtest-self-improve-$TS/wiki"
MEMORY_DIR="$ROOT/.codex_tmp/momtest-self-improve-$TS/memory"
SESSION_ID="momtest-self-improve-$TS"

echo "Demo wiki: $WIKI_DIR"
echo "Session:   $SESSION_ID"
echo

echo "1. Ingest The Mom Test into a fresh BookWiki"
"$PY" "$ROOT/tools/cognee_bookwiki.py" \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  ingest \
  --books "The Mom Test" \
  --max-chapters 6 \
  --max-note-packets 80 \
  --max-concepts 80
echo

echo "2. Baseline query: broad product question with weak grounding"
BASELINE_JSON="$("$PY" "$ROOT/tools/cognee_bookwiki.py" \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  query "How do I validate my AI audit idea without getting fooled by praise?" \
  --books "The Mom Test" \
  --limit 8)"
echo "$BASELINE_JSON"
BASELINE_PAGE="$(printf '%s' "$BASELINE_JSON" | "$PY" -c 'import json, sys; print(json.load(sys.stdin)["query_page"])')"
echo "Baseline page: $BASELINE_PAGE"
echo

echo "3. Lint after baseline: weak pages are visible"
"$PY" "$ROOT/tools/cognee_bookwiki.py" \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  lint
echo

echo "4. Improved query: use The Mom Test concepts, then promote it"
IMPROVED_JSON="$("$PY" "$ROOT/tools/cognee_bookwiki.py" \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  query "compliments facts commitment" \
  --books "The Mom Test" \
  --limit 8 \
  --save-playbook)"
echo "$IMPROVED_JSON"
PLAYBOOK_PATH="$(printf '%s' "$IMPROVED_JSON" | "$PY" -c 'import json, sys; print(json.load(sys.stdin)["playbook_path"])')"
echo "Promoted playbook: $PLAYBOOK_PATH"
echo

echo "5. Lint after improvement"
"$PY" "$ROOT/tools/cognee_bookwiki.py" \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  lint
echo

echo "6. Promoted durable memory"
sed -n '1,180p' "$PLAYBOOK_PATH"
echo

echo "7. Session memory events"
if [[ -f "$MEMORY_DIR/bookwiki_session.jsonl" ]]; then
  tail -n 10 "$MEMORY_DIR/bookwiki_session.jsonl"
else
  echo "Session was written to Redis. Use redis-cli or the status command to inspect the live backend."
fi
