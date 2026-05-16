# Book Workflow

Use this plugin to turn a local book into a query-ready preserved artifact set plus a generated coach skill.

## UI Contract

The preferred entrypoint is a natural-language skill request, for example:

```text
$book-workflow let's create end to end pipeline for "files/Never Split the Difference" book
```

The skill should map that request to the internal workflow automatically.

## Internal Commands

```bash
python3 plugins/book-workflow/scripts/book_workflow.py full "files/Book Name" --generate-skill
python3 plugins/book-workflow/scripts/book_workflow.py preserve "files/Book Name"
python3 plugins/book-workflow/scripts/book_workflow.py extract-notes "files/Book Name"
python3 plugins/book-workflow/scripts/book_workflow.py generate-summaries "files/Book Name"
python3 plugins/book-workflow/scripts/book_workflow.py audit "files/Book Name"
```

## Full Workflow

1. Ingest
   - If the source is a PDF, split it into chapter text files.
   - Initialize the book manifest from the chapter directory.
2. Preserve
   - Chunk the chapters.
   - Prepare chunk-note skeletons and prompt packets.
   - Materialize filled note JSONL files from the prompts with either a configured runner or the current Codex agent.
   - Generate canonical `summaries/*.md` from the filled notes with either a configured runner or the current Codex agent.
   - Rebuild the search index.
   - Validate the artifacts.
3. Generate Skill
   - Create or refresh a standalone skill under `.agents/skills/<skill-name>/`.
   - Write `SKILL.md`, `agents/openai.yaml`, and `references/local-book-map.md`.
   - Default generated names should start with `book-` so they are easy to search in the skill picker.

## Runner Contract

Note extraction and summary generation can use a configured runner command, but the workflow must remain provider-neutral.

- The runner is supplied via `--runner-cmd` or `BOOK_WORKFLOW_RUNNER_CMD`.
- The workflow sends the prompt content on stdin.
- For chunk extraction, the runner must return one JSON object matching the note schema.
- For chapter summaries, the runner must return markdown only.
- Invalid output or non-zero exit status must fail the workflow.
- Do not add a bundled provider-specific runner. If a provider runner is needed, keep it outside the generic workflow or make it explicitly optional.

## Codex-Assisted Mode

When no runner is configured, the current Codex agent can complete the model-dependent stages directly from local artifacts:

```bash
python3 plugins/book-workflow/scripts/book_workflow.py ingest "/path/to/book.pdf" --book-dir "files/Book Name" --title "Book Name" --book-id book-name --force
python3 plugins/book-workflow/scripts/book_workflow.py preserve "files/Book Name" --title "Book Name" --book-id book-name --skip-validate
```

Then fill `notes/*.jsonl` from `prompts/<chapter>/<chunk>.md`, prepare summaries, write `summaries/*.md`, rebuild the index, validate, audit, and generate the skill.

## Success Contract

The workflow is successful only when:

- note rows are filled rather than untouched skeletons
- canonical `summaries/*.md` exist for the expected chapters
- `indexes/search.sqlite` exists
- `python3 tools/book_pipeline.py validate "<book_dir>"` passes
- the generated coach skill points at the current local book artifacts
