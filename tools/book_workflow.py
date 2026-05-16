from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import book_pipeline as pipeline


NOTE_FIELDS = tuple(pipeline.NOTE_SEMANTIC_FIELDS)


def _repo_root() -> Path:
    return REPO_ROOT


def _slugify(value: str, fallback: str = "book") -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or fallback


def _title_case(value: str) -> str:
    return " ".join(part.capitalize() for part in value.split("-") if part)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_text(path: Path, text: str, *, force: bool = False) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists. Use --force to overwrite.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _resolve_book_dir(source: Path, book_dir: Path | None) -> Path:
    if book_dir is not None:
        return book_dir.resolve()
    if source.is_dir():
        if source.name == "chapters":
            return source.parent.resolve()
        return source.resolve()
    return source.parent.resolve()


def _book_manifest(book_dir: Path) -> dict[str, Any]:
    manifest_path = book_dir / "manifests" / "book.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing book manifest: {manifest_path}")
    return _read_json(manifest_path)


def _chapter_rows(book_dir: Path) -> list[dict[str, Any]]:
    manifest = _book_manifest(book_dir)
    rows = manifest.get("chapters", [])
    return [row for row in rows if isinstance(row, dict)]


def _summary_source_for_chapter(book_dir: Path, chapter_id: str) -> str:
    summary_path = book_dir / "summaries" / f"{chapter_id}.md"
    if summary_path.exists():
        return str(summary_path)
    legacy_path = book_dir / "summary" / f"{chapter_id}.md"
    if legacy_path.exists():
        return str(legacy_path)
    return str(summary_path)


def _build_local_book_map(book_dir: Path) -> str:
    manifest = _book_manifest(book_dir)
    chapters = [row for row in manifest.get("chapters", []) if isinstance(row, dict)]
    book_root = book_dir.resolve()
    chunk_manifest = book_dir / "manifests" / "chunks.json"
    chunk_count = None
    if chunk_manifest.exists():
        try:
            chunk_count = int(_read_json(chunk_manifest).get("chunk_count", 0))
        except Exception:
            chunk_count = None

    lines: list[str] = []
    lines.append("# Local Book Map")
    lines.append("")
    lines.append("Use this file to ground the generated skill in the user's local preserved book artifacts.")
    lines.append("")
    lines.append("## Root Paths")
    lines.append("")
    lines.append(f"- Book root: `{book_root}/`")
    lines.append(f"- Book manifest: `{book_root / 'manifests' / 'book.json'}`")
    lines.append(f"- Chunk manifest: `{book_root / 'manifests' / 'chunks.json'}`")
    lines.append(f"- Source chunks: `{book_root / 'chunks'}/`")
    lines.append(f"- Chunk-note skeletons or filled notes: `{book_root / 'notes'}/`")
    lines.append(f"- Chunk extraction prompts: `{book_root / 'prompts'}/`")
    lines.append(f"- Chapter summary prompts: `{book_root / 'prompts' / 'summaries'}/`")
    lines.append(f"- Search index: `{book_root / 'indexes' / 'search.sqlite'}`")
    lines.append(f"- Full chapter text fallback: `{book_root / 'chapters'}/`")
    lines.append(f"- Legacy summaries fallback: `{book_root / 'summary'}/`")
    lines.append(f"- Canonical summaries: `{book_root / 'summaries'}/`")
    lines.append("")
    lines.append("## Retrieval Rule")
    lines.append("")
    lines.append("Search the preservation index first:")
    lines.append("")
    lines.append("```bash")
    lines.append(f'python3 tools/book_pipeline.py search "{book_root}" "query terms" --limit 8')
    lines.append("```")
    lines.append("")
    lines.append("Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.")
    lines.append("")
    if chunk_count is not None:
        lines.append("## Preservation Status")
        lines.append("")
        lines.append(f"- Current chapter count: {len(chapters)}")
        lines.append(f"- Current chunk count: {chunk_count}")
        lines.append("- Notes may be skeletons unless explicitly filled after chunk extraction.")
        lines.append("- Search indexes raw chunks and any non-empty filled notes.")
        lines.append("")
    lines.append("## Chapter Map")
    lines.append("")
    for index, chapter in enumerate(chapters, start=1):
        chapter_id = str(chapter.get("chapter_id") or "")
        title = str(chapter.get("title") or chapter_id)
        source_path = str(chapter.get("path") or "")
        lines.append(f"{index}. `{title}`")
        lines.append(f"   - Chapter ID: `{chapter_id}`")
        lines.append(f"   - Chunks: `{book_root / 'chunks' / f'{chapter_id}.jsonl'}`")
        lines.append(f"   - Notes: `{book_root / 'notes' / f'{chapter_id}.jsonl'}`")
        lines.append(f"   - Summary: `{_summary_source_for_chapter(book_dir, chapter_id)}`")
        lines.append(f"   - Full: `{source_path}`")
    return "\n".join(lines).rstrip() + "\n"


BOOK_SKILL_METADATA: dict[str, dict[str, str]] = {
    "price-to-scale": {
        "description": (
            "Coach SaaS pricing transformation from segmentation through packaging, pricing metrics, "
            "rate-setting, and rollout. Use for packaging redesigns, usage-based pricing decisions, "
            "GenAI monetization, churn response, and pricing operationalization."
        ),
        "short_description": (
            "Transform SaaS pricing with stronger packaging, metrics, rate-setting, and rollout."
        ),
        "default_prompt": (
            "Use ${skill_name} to improve SaaS packaging, pricing metrics, rate-setting, "
            "usage-based pricing choices, and pricing rollout using {book_title}."
        ),
    },
    "monetizing-innovation": {
        "description": (
            "Coach product and pricing decisions around willingness to pay, segmented packaging, "
            "bundling, and price integrity. Use for early pricing research, business cases, "
            "feature prioritization, and avoiding feature shock, minivations, hidden gems, and undead products."
        ),
        "short_description": (
            "Design products around willingness to pay, segmented packaging, and price integrity."
        ),
        "default_prompt": (
            "Use ${skill_name} to shape product design, willingness-to-pay research, packaging, "
            "and price integrity decisions using {book_title}."
        ),
    },
    "the-strategy-and-tactics-of-pricing": {
        "description": (
            "Coach value-based pricing strategy for durable profitability through economic value, "
            "price structure, value communication, pricing policy, and competitive response. "
            "Use for margin defense, segmented pricing, discount policy, and strategic pricing decisions."
        ),
        "short_description": (
            "Build value-based pricing strategy with economic value, price structure, and policy."
        ),
        "default_prompt": (
            "Use ${skill_name} to strengthen value-based pricing strategy, price structure, "
            "value communication, pricing policy, and competitive response using {book_title}."
        ),
    },
    "crossing-the-chasm": {
        "description": (
            "Coach go-to-market strategy for moving from early adopters to mainstream customers using "
            "beachhead targeting, whole-product design, positioning, distribution, pricing, and technology "
            "adoption lifecycle thinking. Use for category creation, niche selection, market-entry strategy, "
            "and chasm-crossing diagnosis."
        ),
        "short_description": (
            "Cross from early adopters to mainstream customers with beachhead strategy and whole-product focus."
        ),
        "default_prompt": (
            "Use ${skill_name} to diagnose chasm risk, choose a beachhead, shape whole-product strategy, "
            "and plan mainstream go-to-market moves using {book_title}."
        ),
    },
}


def _book_skill_metadata(book_title: str, skill_name: str) -> dict[str, str]:
    metadata = BOOK_SKILL_METADATA.get(_slugify(book_title))
    if metadata is None:
        return {
            "description": (
                f"Apply {book_title} to real situations with role-play, debriefs, rewrites, and chapter-grounded coaching. "
                "Use when the user wants sharper decisions, stronger lines, concept drills, or fast book lookup without re-reading the source."
            ),
            "short_description": (
                "Apply the book to real situations with role-play, rewrites, debriefs, and grounded lookup."
            ),
            "default_prompt": (
                f"Use ${skill_name} to apply {book_title} through role-play, rewrites, debriefs, "
                "and chapter-grounded coaching."
            ),
        }
    return {
        "description": metadata["description"],
        "short_description": metadata["short_description"],
        "default_prompt": metadata["default_prompt"].format(skill_name=skill_name, book_title=book_title),
    }


def _skill_name_from_book(book_title: str) -> str:
    return f"book-{_slugify(book_title)}-coach"


def _skill_display_name(skill_name: str) -> str:
    if skill_name.endswith("-coach"):
        base = skill_name[: -len("-coach")]
        return f"{_title_case(base)} Coach"
    return _title_case(skill_name)


def _build_skill_md(book_dir: Path, skill_name: str, book_title: str) -> str:
    metadata = _book_skill_metadata(book_title, skill_name)
    return f"""---
name: {skill_name}
description: "{metadata['description']}"
---

# {book_title} Coach

## Purpose

Act as the user's AI coach for {book_title}. Focus on practical next steps, realistic role-play, and concise debriefs.

## Grounding

Use `references/local-book-map.md` as the source of truth.
Search the local index first when chapter-specific guidance matters.
Use retrieved chunks, filled notes, and source-linked summaries before making book-specific claims.
Do not invent book details.
Prefer `chapter_id` and `chunk_id` references when possible.

## Default Workflow

1. Classify the request as `Live Coach`, `Role-Play`, `Debrief`, `Concept Drill`, `Rewrite My Line`, or `Book Lookup`.
2. Identify the most relevant chapter or concept.
3. Search the local index when chapter grounding matters.
4. Give one useful next step or one book-grounded response.
5. Keep the response sized to the user's stage in the conversation.

## Modes

### Live Coach

Use when the user is preparing for or handling a real situation.

Ask only for context that changes the next line:

- counterpart
- what they want
- what the user wants
- what relationship or outcome must not be damaged
- whether this is live, upcoming, or hypothetical

Then give one or two usable lines.

### Role-Play

Use when the user wants practice.

- Play the counterpart realistically.
- Stay in character until the user asks for feedback, says `pause`, or makes an out-of-role request.
- Apply pressure gradually.
- Keep each turn short enough for the user to practice actual replies.

### Debrief

Use when the user asks how they did, asks for feedback, or pauses a role-play.

Use this structure:

1. What worked
2. What missed
3. Better next line
4. Tactic from the book
5. One improvement for the next attempt

### Concept Drill

Use when the user wants retention or chapter practice.

- Ask one application question at a time.
- Prefer scenario questions over definitions.
- Correct the answer briefly.
- Ask a slightly harder follow-up.

### Rewrite My Line

Use when the user gives a sentence they want to say.

Return:

- `Too blunt`, `Too soft`, or `Good direction`
- a stronger version
- why it works
- the chapter or tactic behind it
"""


def _build_openai_yaml(skill_name: str, book_title: str) -> str:
    metadata = _book_skill_metadata(book_title, skill_name)
    return "\n".join(
        [
            "interface:",
            f'  display_name: "{_skill_display_name(skill_name)}"',
            f'  short_description: "{metadata["short_description"]}"',
            f'  default_prompt: "{metadata["default_prompt"]}"',
            "",
        ]
    )


def _resolve_runner_cmd(runner_cmd: str | None) -> str | None:
    value = (runner_cmd or os.environ.get("BOOK_WORKFLOW_RUNNER_CMD", "")).strip()
    return value or None


def _strip_code_fence(text: str) -> str:
    stripped = text.strip()
    match = re.match(r"^```(?:json|markdown|md)?\s*(.*?)\s*```$", stripped, flags=re.DOTALL)
    return match.group(1).strip() if match else stripped


def _run_runner(prompt: str, runner_cmd: str) -> str:
    completed = subprocess.run(
        runner_cmd,
        shell=True,
        cwd=str(_repo_root()),
        input=prompt,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.strip() or "runner exited non-zero"
        raise RuntimeError(stderr)
    output = _strip_code_fence(completed.stdout)
    if not output.strip():
        raise RuntimeError("runner returned empty output")
    return output


def _note_paths(book_dir: Path) -> list[Path]:
    return sorted((book_dir / "notes").glob("*.jsonl"))


def _summary_prompt_paths(book_dir: Path) -> list[Path]:
    return sorted((book_dir / "prompts" / "summaries").glob("*.md"))


def _semantic_payload_from_response(payload: dict[str, Any], *, chapter_id: str, chunk_id: str) -> dict[str, Any]:
    response_chunk_id = str(payload.get("chunk_id") or chunk_id)
    response_chapter_id = str(payload.get("chapter_id") or chapter_id)
    if response_chunk_id != chunk_id:
        raise ValueError(f"runner returned wrong chunk_id: expected {chunk_id}, got {response_chunk_id}")
    if response_chapter_id != chapter_id:
        raise ValueError(f"runner returned wrong chapter_id: expected {chapter_id}, got {response_chapter_id}")

    merged: dict[str, Any] = {}
    for field in NOTE_FIELDS:
        value = payload.get(field)
        if value is None:
            value = "" if field == "summary" else []
        if field == "summary":
            if not isinstance(value, str):
                raise ValueError(f"field {field} must be a string for {chunk_id}")
            merged[field] = value.strip()
            continue
        if not isinstance(value, list):
            raise ValueError(f"field {field} must be a list for {chunk_id}")
        merged[field] = value
    return merged


def extract_notes(
    book_dir: Path,
    *,
    runner_cmd: str | None,
    force: bool = False,
) -> int:
    resolved_runner = _resolve_runner_cmd(runner_cmd)
    if resolved_runner is None:
        raise RuntimeError("missing runner command; set BOOK_WORKFLOW_RUNNER_CMD or pass --runner-cmd")

    updated = 0
    for note_path in _note_paths(book_dir):
        rows = list(pipeline._read_jsonl(note_path))
        changed = False
        for row in rows:
            if pipeline.note_has_semantic_content(row) and not force:
                continue
            chapter_id = str(row.get("chapter_id") or note_path.stem)
            chunk_id = str(row.get("chunk_id") or "")
            if not chunk_id:
                raise ValueError(f"missing chunk_id in {note_path}")
            prompt_path = book_dir / "prompts" / chapter_id / f"{chunk_id}.md"
            if not prompt_path.exists():
                raise FileNotFoundError(f"missing note prompt: {prompt_path}")
            response = _run_runner(prompt_path.read_text(encoding="utf-8"), resolved_runner)
            payload = json.loads(response)
            semantic = _semantic_payload_from_response(payload, chapter_id=chapter_id, chunk_id=chunk_id)
            for field, value in semantic.items():
                row[field] = value
            changed = True
            updated += 1
        if changed:
            pipeline._write_jsonl(note_path, rows)
    return updated


def generate_summaries(
    book_dir: Path,
    *,
    runner_cmd: str | None,
    force: bool = False,
) -> int:
    resolved_runner = _resolve_runner_cmd(runner_cmd)
    if resolved_runner is None:
        raise RuntimeError("missing runner command; set BOOK_WORKFLOW_RUNNER_CMD or pass --runner-cmd")

    written = 0
    for prompt_path in _summary_prompt_paths(book_dir):
        chapter_id = prompt_path.stem
        note_path = book_dir / "notes" / f"{chapter_id}.jsonl"
        if not note_path.exists():
            raise FileNotFoundError(f"missing note file for summary generation: {note_path}")
        notes = list(pipeline._read_jsonl(note_path))
        untouched = [str(row.get("chunk_id") or "") for row in notes if not pipeline.note_has_semantic_content(row)]
        if untouched:
            raise RuntimeError(f"cannot summarize {chapter_id}; untouched notes remain: {', '.join(untouched[:5])}")
        summary_path = book_dir / "summaries" / f"{chapter_id}.md"
        if summary_path.exists() and not force:
            continue
        summary_text = _run_runner(prompt_path.read_text(encoding="utf-8"), resolved_runner).strip()
        if not summary_text:
            raise RuntimeError(f"runner returned empty summary for {chapter_id}")
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(summary_text + "\n", encoding="utf-8")
        written += 1
    return written


def audit_book(book_dir: Path) -> dict[str, Any]:
    manifest = _book_manifest(book_dir)
    chunk_manifest_path = book_dir / "manifests" / "chunks.json"
    chunk_manifest = _read_json(chunk_manifest_path) if chunk_manifest_path.exists() else {}
    chunk_files = sorted((book_dir / "chunks").glob("*.jsonl"))
    note_files = _note_paths(book_dir)
    summary_files = sorted((book_dir / "summaries").glob("*.md"))

    chunk_count = sum(1 for path in chunk_files for _ in pipeline._read_jsonl(path))
    note_rows = [row for path in note_files for row in pipeline._read_jsonl(path)]
    filled_count = sum(1 for row in note_rows if pipeline.note_has_semantic_content(row))
    untouched_count = len(note_rows) - filled_count
    validation_status = pipeline.cmd_validate(argparse.Namespace(book_dir=book_dir, max_chars=12000))

    return {
        "book_dir": str(book_dir.resolve()),
        "book_id": manifest.get("book_id"),
        "title": manifest.get("title"),
        "chapter_count": len(_chapter_rows(book_dir)),
        "chunk_manifest_count": chunk_manifest.get("chunk_count"),
        "chunk_count": chunk_count,
        "note_file_count": len(note_files),
        "note_count": len(note_rows),
        "filled_note_count": filled_count,
        "untouched_note_count": untouched_count,
        "summary_count": len(summary_files),
        "index_exists": (book_dir / "indexes" / "search.sqlite").exists(),
        "validate_ok": validation_status == 0,
    }


def ingest_source(
    source: Path,
    *,
    book_dir: Path | None = None,
    title: str | None = None,
    book_id: str | None = None,
    force: bool = False,
    pdf_level: int = 1,
    fallback_regex: bool = True,
) -> Path:
    source = source.resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source path not found: {source}")

    target_book_dir = _resolve_book_dir(source, book_dir)
    target_book_dir.mkdir(parents=True, exist_ok=True)

    if source.is_file() and source.suffix.lower() == ".pdf":
        chapters_dir = target_book_dir / "chapters"
        chapters_dir.mkdir(parents=True, exist_ok=True)
        pdf_script = _repo_root() / "tools" / "pdf_split_chapters.py"
        args = [
            sys.executable,
            str(pdf_script),
            str(source),
            "-o",
            str(chapters_dir),
            "--level",
            str(pdf_level),
        ]
        if force:
            args.append("--force")
        if fallback_regex:
            args.append("--fallback-regex")
        subprocess.run(args, check=True, cwd=str(_repo_root()))

    inferred_title = title or target_book_dir.name
    inferred_book_id = book_id or _slugify(inferred_title)
    pipeline.cmd_init_book(
        argparse.Namespace(
            book_dir=target_book_dir,
            title=inferred_title,
            book_id=inferred_book_id,
        )
    )
    return target_book_dir


def preserve_book(
    book_dir: Path,
    *,
    title: str | None = None,
    book_id: str | None = None,
    target_chars: int = pipeline.DEFAULT_TARGET_CHARS,
    overlap_chars: int = pipeline.DEFAULT_OVERLAP_CHARS,
    force_notes: bool = False,
    force_summaries: bool = False,
    skip_validate: bool = False,
    max_chars: int = 12000,
    runner_cmd: str | None = None,
) -> int:
    book_dir = book_dir.resolve()
    pipeline.cmd_init_book(argparse.Namespace(book_dir=book_dir, title=title, book_id=book_id))
    pipeline.cmd_chunk(
        argparse.Namespace(
            book_dir=book_dir,
            title=title,
            book_id=book_id,
            target_chars=target_chars,
            overlap_chars=overlap_chars,
        )
    )
    pipeline.cmd_prepare_notes(argparse.Namespace(book_dir=book_dir, force=force_notes))
    pipeline.cmd_import_summaries(argparse.Namespace(book_dir=book_dir, force=force_summaries))

    resolved_runner = _resolve_runner_cmd(runner_cmd)
    if resolved_runner is not None:
        extract_notes(book_dir, runner_cmd=resolved_runner, force=force_notes)
        pipeline.cmd_prepare_summaries(argparse.Namespace(book_dir=book_dir))
        generate_summaries(book_dir, runner_cmd=resolved_runner, force=force_summaries)
    else:
        pipeline.cmd_prepare_summaries(argparse.Namespace(book_dir=book_dir))

    pipeline.cmd_build_index(argparse.Namespace(book_dir=book_dir))
    if skip_validate:
        return 0
    return int(pipeline.cmd_validate(argparse.Namespace(book_dir=book_dir, max_chars=max_chars)))


def generate_book_skill(
    book_dir: Path,
    *,
    skill_name: str | None = None,
    skill_root: Path | None = None,
    force: bool = False,
) -> Path:
    book_dir = book_dir.resolve()
    manifest = _book_manifest(book_dir)
    book_title = str(manifest.get("title") or book_dir.name)
    chosen_skill_name = _slugify(skill_name or _skill_name_from_book(book_title))
    if not chosen_skill_name:
        raise ValueError("Skill name must include at least one letter or digit.")

    root = (skill_root or (_repo_root() / ".agents" / "skills")).resolve()
    skill_dir = root / chosen_skill_name
    if skill_dir.exists() and not force:
        raise FileExistsError(f"Skill directory already exists: {skill_dir}")

    (skill_dir / "agents").mkdir(parents=True, exist_ok=True)
    (skill_dir / "references").mkdir(parents=True, exist_ok=True)

    _write_text(skill_dir / "SKILL.md", _build_skill_md(book_dir, chosen_skill_name, book_title), force=True)
    _write_text(skill_dir / "agents" / "openai.yaml", _build_openai_yaml(chosen_skill_name, book_title), force=True)
    _write_text(skill_dir / "references" / "local-book-map.md", _build_local_book_map(book_dir), force=True)

    return skill_dir


def full_workflow(
    source: Path,
    *,
    book_dir: Path | None = None,
    title: str | None = None,
    book_id: str | None = None,
    force: bool = False,
    pdf_level: int = 1,
    fallback_regex: bool = True,
    target_chars: int = pipeline.DEFAULT_TARGET_CHARS,
    overlap_chars: int = pipeline.DEFAULT_OVERLAP_CHARS,
    force_notes: bool = False,
    force_summaries: bool = False,
    skip_validate: bool = False,
    max_chars: int = 12000,
    generate_skill: bool = False,
    skill_name: str | None = None,
    skill_root: Path | None = None,
    force_skill: bool = False,
    runner_cmd: str | None = None,
) -> tuple[Path, Path | None]:
    target_book_dir = ingest_source(
        source,
        book_dir=book_dir,
        title=title,
        book_id=book_id,
        force=force,
        pdf_level=pdf_level,
        fallback_regex=fallback_regex,
    )
    preserve_book(
        target_book_dir,
        title=title,
        book_id=book_id,
        target_chars=target_chars,
        overlap_chars=overlap_chars,
        force_notes=force_notes,
        force_summaries=force_summaries,
        skip_validate=skip_validate,
        max_chars=max_chars,
        runner_cmd=runner_cmd,
    )
    skill_dir = None
    if generate_skill:
        skill_dir = generate_book_skill(
            target_book_dir,
            skill_name=skill_name,
            skill_root=skill_root,
            force=force_skill,
        )
    return target_book_dir, skill_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the local book preservation workflow and generate book skills.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest", help="Normalize a source book into the local chapter workspace.")
    ingest.add_argument("source", type=Path, help="PDF file or book directory")
    ingest.add_argument("--book-dir", type=Path, default=None)
    ingest.add_argument("--title", default=None)
    ingest.add_argument("--book-id", default=None)
    ingest.add_argument("--force", action="store_true")
    ingest.add_argument("--pdf-level", type=int, default=1)
    ingest.add_argument("--no-fallback-regex", action="store_true")
    ingest.set_defaults(
        func=lambda args: ingest_source(
            args.source,
            book_dir=args.book_dir,
            title=args.title,
            book_id=args.book_id,
            force=args.force,
            pdf_level=args.pdf_level,
            fallback_regex=not args.no_fallback_regex,
        )
    )

    preserve = subparsers.add_parser("preserve", help="Prepare or complete a preserved book end to end.")
    preserve.add_argument("book_dir", type=Path)
    preserve.add_argument("--title", default=None)
    preserve.add_argument("--book-id", default=None)
    preserve.add_argument("--target-chars", type=int, default=pipeline.DEFAULT_TARGET_CHARS)
    preserve.add_argument("--overlap-chars", type=int, default=pipeline.DEFAULT_OVERLAP_CHARS)
    preserve.add_argument("--force-notes", action="store_true")
    preserve.add_argument("--force-summaries", action="store_true")
    preserve.add_argument("--skip-validate", action="store_true")
    preserve.add_argument("--max-chars", type=int, default=12000)
    preserve.add_argument("--runner-cmd", default=None)
    preserve.set_defaults(
        func=lambda args: preserve_book(
            args.book_dir,
            title=args.title,
            book_id=args.book_id,
            target_chars=args.target_chars,
            overlap_chars=args.overlap_chars,
            force_notes=args.force_notes,
            force_summaries=args.force_summaries,
            skip_validate=args.skip_validate,
            max_chars=args.max_chars,
            runner_cmd=args.runner_cmd,
        )
    )

    extract = subparsers.add_parser("extract-notes", help="Fill chunk-note JSONL files from prepared prompts.")
    extract.add_argument("book_dir", type=Path)
    extract.add_argument("--runner-cmd", default=None)
    extract.add_argument("--force", action="store_true")
    extract.set_defaults(func=lambda args: extract_notes(args.book_dir.resolve(), runner_cmd=args.runner_cmd, force=args.force))

    summaries = subparsers.add_parser("generate-summaries", help="Write canonical summaries from filled note prompts.")
    summaries.add_argument("book_dir", type=Path)
    summaries.add_argument("--runner-cmd", default=None)
    summaries.add_argument("--force", action="store_true")
    summaries.set_defaults(
        func=lambda args: generate_summaries(args.book_dir.resolve(), runner_cmd=args.runner_cmd, force=args.force)
    )

    audit = subparsers.add_parser("audit", help="Report whether a preserved book is query-ready.")
    audit.add_argument("book_dir", type=Path)
    audit.set_defaults(func=lambda args: print(json.dumps(audit_book(args.book_dir.resolve()), ensure_ascii=False, indent=2)) or 0)

    skill = subparsers.add_parser("generate-skill", help="Generate a standalone book skill from preserved artifacts.")
    skill.add_argument("book_dir", type=Path)
    skill.add_argument("--skill-name", default=None)
    skill.add_argument("--skill-root", type=Path, default=None)
    skill.add_argument("--force", action="store_true")
    skill.set_defaults(
        func=lambda args: generate_book_skill(
            args.book_dir,
            skill_name=args.skill_name,
            skill_root=args.skill_root,
            force=args.force,
        )
    )

    full = subparsers.add_parser("full", help="Ingest the source, preserve the book, and optionally generate a skill.")
    full.add_argument("source", type=Path)
    full.add_argument("--book-dir", type=Path, default=None)
    full.add_argument("--title", default=None)
    full.add_argument("--book-id", default=None)
    full.add_argument("--force", action="store_true")
    full.add_argument("--pdf-level", type=int, default=1)
    full.add_argument("--no-fallback-regex", action="store_true")
    full.add_argument("--target-chars", type=int, default=pipeline.DEFAULT_TARGET_CHARS)
    full.add_argument("--overlap-chars", type=int, default=pipeline.DEFAULT_OVERLAP_CHARS)
    full.add_argument("--force-notes", action="store_true")
    full.add_argument("--force-summaries", action="store_true")
    full.add_argument("--skip-validate", action="store_true")
    full.add_argument("--max-chars", type=int, default=12000)
    full.add_argument("--generate-skill", action="store_true")
    full.add_argument("--skill-name", default=None)
    full.add_argument("--skill-root", type=Path, default=None)
    full.add_argument("--force-skill", action="store_true")
    full.add_argument("--runner-cmd", default=None)
    full.set_defaults(
        func=lambda args: full_workflow(
            args.source,
            book_dir=args.book_dir,
            title=args.title,
            book_id=args.book_id,
            force=args.force,
            pdf_level=args.pdf_level,
            fallback_regex=not args.no_fallback_regex,
            target_chars=args.target_chars,
            overlap_chars=args.overlap_chars,
            force_notes=args.force_notes,
            force_summaries=args.force_summaries,
            skip_validate=args.skip_validate,
            max_chars=args.max_chars,
            generate_skill=args.generate_skill,
            skill_name=args.skill_name,
            skill_root=args.skill_root,
            force_skill=args.force_skill,
            runner_cmd=args.runner_cmd,
        )
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = args.func(args)
    if isinstance(result, Path):
        print(result)
        return 0
    if isinstance(result, tuple):
        book_dir, skill_dir = result
        print(book_dir)
        if skill_dir is not None:
            print(skill_dir)
        return 0
    if result is None:
        return 0
    return int(result)


if __name__ == "__main__":
    raise SystemExit(main())
