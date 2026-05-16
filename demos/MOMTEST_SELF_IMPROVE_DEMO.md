# The Mom Test Self-Improvement Demo

This demo shows BookWiki improving through a feedback/promotion loop:

1. Ingest `The Mom Test`.
2. Ask a broad startup-validation question that has weak grounding.
3. Run lint to make weak wiki state visible.
4. Ask a better concept-level query.
5. Promote the useful result into a durable playbook.
6. Inspect session memory and the promoted playbook.

## One-Command Demo

```bash
bash demos/momtest_self_improve.sh
```

If Redis is running and reachable, the command output should show `session_backend: redis`. If not, the tool falls back to JSONL session memory so the demo still runs locally.

## Manual Commands

Use a fresh wiki directory so the demo is repeatable:

```bash
WIKI_DIR=.codex_tmp/momtest-demo-wiki
MEMORY_DIR=.codex_tmp/momtest-demo-memory
SESSION_ID=momtest-demo
```

Ingest the book:

```bash
.venv/bin/python tools/cognee_bookwiki.py \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  ingest \
  --books "The Mom Test" \
  --max-chapters 6 \
  --max-note-packets 80 \
  --max-concepts 80
```

Baseline query:

```bash
.venv/bin/python tools/cognee_bookwiki.py \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  query "How do I validate my AI audit idea without getting fooled by praise?" \
  --books "The Mom Test" \
  --limit 8
```

Expected signal:

```text
hit_count: 0
```

Lint the weak state:

```bash
.venv/bin/python tools/cognee_bookwiki.py \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  lint
```

Improved query:

```bash
.venv/bin/python tools/cognee_bookwiki.py \
  --wiki-dir "$WIKI_DIR" \
  --memory-dir "$MEMORY_DIR" \
  --session-id "$SESSION_ID" \
  query "compliments facts commitment" \
  --books "The Mom Test" \
  --limit 8 \
  --save-playbook
```

Expected signal:

```text
hit_count: 8
playbook_path: wiki/playbooks/compliments-facts-commitment.md
```

## Demo Narrative

```text
Before:
- The agent receives a real founder-style question.
- The wiki records it as a query brief.
- The answer is weak because the query does not match the book's concept vocabulary.

Feedback:
- Lint exposes the weak query page.
- We retry through the book's concepts: compliments, facts, commitment.

After:
- The query returns source-backed hits.
- The useful result is promoted into a playbook.
- Future runs can reuse the playbook instead of repeating the weak path.
```

## Best Query Set

Use these for a short live demo:

```text
Weak baseline:
How do I validate my AI audit idea without getting fooled by praise?

Improved grounded query:
compliments facts commitment

Alternative grounded queries:
commitment advancement
premature zoom
past specifics
learning bottleneck
```

## Honest Claim

This is not yet a fully autonomous self-improving agent. It is a working self-improvement loop:

```text
query -> saved brief -> lint/feedback -> better grounded query -> promoted playbook -> reusable memory
```
