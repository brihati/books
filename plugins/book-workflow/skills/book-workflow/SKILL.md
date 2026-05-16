---
name: book-workflow
description: Run the local book preservation workflow, prepare hierarchical summaries, and generate per-book skills from preserved artifacts. Use when the user wants to ingest a book, chunk chapters, prepare notes or summary prompts, rebuild the search index, validate the artifacts, or scaffold a new book-specific coaching skill.
---

# Book Workflow

## Purpose

Use this skill as the UI-first entrypoint for the local book pipeline. The user should be able to say things like:

- `$book-workflow let's create end to end pipeline for "files/Never Split the Difference" book`
- `$book-workflow prepare this book for querying`
- `$book-workflow refresh the coach skill for "files/The Mom Test"`

The skill should interpret the plain-English intent and run the appropriate local workflow without requiring the user to know the CLI.

## Grounding

Use the local book artifacts as the source of truth:

- `manifests/book.json`
- `manifests/chunks.json`
- `chapters/`
- `chunks/`
- `notes/`
- `prompts/`
- `prompts/summaries/`
- `summaries/`
- `indexes/search.sqlite`

Read `references/workflow.md` for the end-to-end flow and runner contract.

## Intent Mapping

Translate natural-language requests into one of these actions:

1. `full`
   - end-to-end setup for a new or incomplete book
   - ingest if needed, extract notes, generate summaries, rebuild the index, validate, and generate or refresh the coach skill
2. `preserve`
   - complete or repair the preserved artifacts for an existing book directory
3. `generate-skill`
   - refresh the standalone coach skill from the current book artifacts
4. `audit`
   - report whether the book is query-ready and which stage is incomplete

Default to `full` when the user asks to set up a book for querying, coaching, or end-to-end use.

## Default Workflow

1. Resolve the source path from the user's request.
2. Detect whether it is:
   - a PDF
   - a normalized book directory
   - a `chapters/` directory
3. Run the full workflow when the user wants a ready-to-query book:
   - ingest source if needed
   - chunk chapters
   - prepare note prompts
   - materialize filled notes using a configured generic runner or by filling local artifacts directly as the current Codex agent
   - generate canonical chapter summaries using a configured generic runner or by writing them directly as the current Codex agent
   - rebuild the search index
   - validate completeness
   - generate or refresh the coach skill
4. Report exactly what happened and whether the book is now query-ready.

## Runner Requirement

The extraction and summary stages require either a configured generic runner or direct Codex-assisted completion of the generated local prompt artifacts. The skill should rely on local workflow configuration and repo artifacts rather than asking the user to type raw CLI flags in the UI.

If the runner is missing and direct Codex-assisted completion is not being performed, explain that the workflow cannot finish the extraction and summary stages yet, and do not claim success.
