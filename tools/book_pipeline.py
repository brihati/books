#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


DEFAULT_TARGET_CHARS = 7000
DEFAULT_OVERLAP_CHARS = 700
NOTE_SEMANTIC_FIELDS = (
    "summary",
    "key_points",
    "arguments",
    "examples",
    "stories",
    "definitions",
    "names",
    "dates",
    "numbers",
    "places",
    "terms",
    "quotes",
    "actionable_lessons",
    "open_questions",
)


@dataclass(frozen=True)
class ChapterSource:
    chapter_id: str
    index: int
    title: str
    path: str
    start_page: int | None
    end_page: int | None
    char_count: int


@dataclass(frozen=True)
class Chunk:
    book_id: str
    chapter_id: str
    chunk_id: str
    chunk_index: int
    chapter_title: str
    source_path: str
    source_pages: str | None
    char_start: int
    char_end: int
    text: str
    checksum: str


def _slugify(value: str, fallback: str = "book") -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or fallback


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSONL in {path}:{line_number}: {exc}") from exc


def _chapter_id(index: int, title: str) -> str:
    title_part = _slugify(re.sub(r"^chapter\s+\d+\s*", "", title, flags=re.I), fallback="chapter")
    return f"chapter-{index:02d}-{title_part[:48].strip('-')}"


def _load_chapter_manifest(book_dir: Path) -> list[ChapterSource]:
    manifest_path = book_dir / "chapters" / "chapters.json"
    if manifest_path.exists():
        manifest = _read_json(manifest_path)
        sources: list[ChapterSource] = []
        for row in manifest.get("chapters", []):
            index = int(row["index"])
            title = str(row["title"])
            out_file = Path(str(row["out_file"]))
            path = out_file if out_file.is_absolute() else (Path.cwd() / out_file)
            if not path.exists():
                path = book_dir / "chapters" / out_file.name
            text = path.read_text(encoding="utf-8")
            sources.append(
                ChapterSource(
                    chapter_id=_chapter_id(index, title),
                    index=index,
                    title=title,
                    path=str(path),
                    start_page=int(row["start_page_1based"]) if row.get("start_page_1based") else None,
                    end_page=int(row["end_page_1based"]) if row.get("end_page_1based") else None,
                    char_count=len(text),
                )
            )
        return sources

    chapter_paths = sorted((book_dir / "chapters").glob("*.txt"))
    sources = []
    for index, path in enumerate(chapter_paths, start=1):
        title = path.stem
        text = path.read_text(encoding="utf-8")
        sources.append(
            ChapterSource(
                chapter_id=_chapter_id(index, title),
                index=index,
                title=title,
                path=str(path),
                start_page=None,
                end_page=None,
                char_count=len(text),
            )
        )
    return sources


def _paragraph_spans(text: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    cursor = 0
    blocks = re.split(r"(\n\s*\n+)", text)
    for block in blocks:
        start = cursor
        end = cursor + len(block)
        cursor = end
        if not block.strip():
            continue
        stripped = block.strip()
        leading = len(block) - len(block.lstrip())
        trailing = len(block.rstrip())
        spans.append((start + leading, start + trailing, stripped))
    if not spans and text.strip():
        spans.append((0, len(text), text.strip()))
    return spans


def _split_large_span(start: int, paragraph: str, target_chars: int) -> list[tuple[int, int, str]]:
    if len(paragraph) <= target_chars:
        return [(start, start + len(paragraph), paragraph)]

    pieces: list[tuple[int, int, str]] = []
    current: list[str] = []
    current_start = start
    cursor = start
    units = re.split(r"(?<=[.!?])\s+|\n+", paragraph)
    for unit in units:
        unit = unit.strip()
        if not unit:
            continue
        unit_start = paragraph.find(unit, max(cursor - start, 0))
        if unit_start == -1:
            unit_start = cursor - start
        absolute_start = start + unit_start
        current_len = sum(len(part) + 1 for part in current)
        if current and current_len + len(unit) > target_chars:
            text = " ".join(current).strip()
            pieces.append((current_start, current_start + len(text), text))
            current = []
            current_start = absolute_start
        if len(unit) > target_chars:
            for offset in range(0, len(unit), target_chars):
                part = unit[offset : offset + target_chars].strip()
                if part:
                    part_start = absolute_start + offset
                    pieces.append((part_start, part_start + len(part), part))
            current_start = absolute_start + len(unit)
            cursor = absolute_start + len(unit)
            continue
        current.append(unit)
        cursor = absolute_start + len(unit)

    if current:
        text = " ".join(current).strip()
        pieces.append((current_start, current_start + len(text), text))
    return pieces


def _overlap_text(text: str, overlap_chars: int) -> str:
    if overlap_chars <= 0 or len(text) <= overlap_chars:
        return text if overlap_chars > 0 else ""
    cut = len(text) - overlap_chars
    boundary = text.find("\n\n", cut)
    if boundary == -1:
        boundary = cut
    return text[boundary:].strip()


def _chunk_chapter(
    *,
    book_id: str,
    source: ChapterSource,
    target_chars: int,
    overlap_chars: int,
) -> list[Chunk]:
    text = Path(source.path).read_text(encoding="utf-8")
    paragraphs = _paragraph_spans(text)
    chunks: list[Chunk] = []
    current_parts: list[str] = []
    current_start: int | None = None
    current_end = 0
    chunk_index = 1

    def flush() -> None:
        nonlocal current_parts, current_start, current_end, chunk_index
        if current_start is None or not current_parts:
            return
        chunk_text = "\n\n".join(part.strip() for part in current_parts if part.strip()).strip()
        if not chunk_text:
            return
        chunk_id = f"{source.chapter_id}-chunk-{chunk_index:03d}"
        digest = hashlib.sha256(chunk_text.encode("utf-8")).hexdigest()[:16]
        pages = None
        if source.start_page is not None and source.end_page is not None:
            pages = f"{source.start_page}-{source.end_page}"
        chunks.append(
            Chunk(
                book_id=book_id,
                chapter_id=source.chapter_id,
                chunk_id=chunk_id,
                chunk_index=chunk_index,
                chapter_title=source.title,
                source_path=source.path,
                source_pages=pages,
                char_start=current_start,
                char_end=current_end,
                text=chunk_text,
                checksum=digest,
            )
        )
        chunk_index += 1
        overlap = _overlap_text(chunk_text, overlap_chars)
        current_parts = [overlap] if overlap else []
        current_start = max(current_end - len(overlap), 0) if overlap else None

    split_spans: list[tuple[int, int, str]] = []
    for start, _end, paragraph in paragraphs:
        split_spans.extend(_split_large_span(start, paragraph, target_chars))

    for start, end, paragraph in split_spans:
        paragraph_len = len(paragraph)
        current_len = sum(len(part) + 2 for part in current_parts)
        if current_parts and current_len + paragraph_len > target_chars:
            flush()
        if current_start is None:
            current_start = start
        current_parts.append(paragraph)
        current_end = end
        if paragraph_len >= target_chars:
            flush()

    flush()
    return chunks


def cmd_init_book(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    title = args.title or book_dir.name
    book_id = args.book_id or _slugify(title)
    for name in ["chunks", "notes", "prompts", "summaries", "indexes", "manifests"]:
        (book_dir / name).mkdir(parents=True, exist_ok=True)

    chapters = _load_chapter_manifest(book_dir)
    data = {
        "book_id": book_id,
        "title": title,
        "book_dir": str(book_dir),
        "chapter_count": len(chapters),
        "chapters": [asdict(chapter) for chapter in chapters],
    }
    _write_json(book_dir / "manifests" / "book.json", data)
    print(f"Initialized book manifest: {book_dir / 'manifests' / 'book.json'}")
    return 0


def cmd_chunk(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    book_manifest = book_dir / "manifests" / "book.json"
    if not book_manifest.exists():
        cmd_init_book(argparse.Namespace(book_dir=book_dir, title=args.title, book_id=args.book_id))
    manifest = _read_json(book_manifest)
    book_id = str(manifest["book_id"])
    chapters = _load_chapter_manifest(book_dir)
    all_chunks: list[Chunk] = []
    for source in chapters:
        chunks = _chunk_chapter(
            book_id=book_id,
            source=source,
            target_chars=args.target_chars,
            overlap_chars=args.overlap_chars,
        )
        all_chunks.extend(chunks)
        out_path = book_dir / "chunks" / f"{source.chapter_id}.jsonl"
        _write_jsonl(out_path, (asdict(chunk) for chunk in chunks))
        print(f"Wrote {len(chunks):02d} chunks: {out_path}")

    _write_json(
        book_dir / "manifests" / "chunks.json",
        {
            "book_id": book_id,
            "target_chars": args.target_chars,
            "overlap_chars": args.overlap_chars,
            "chunk_count": len(all_chunks),
            "chapters": [
                {
                    "chapter_id": source.chapter_id,
                    "title": source.title,
                    "chunk_count": sum(1 for chunk in all_chunks if chunk.chapter_id == source.chapter_id),
                }
                for source in chapters
            ],
        },
    )
    print(f"Wrote chunk manifest: {book_dir / 'manifests' / 'chunks.json'}")
    return 0


def _empty_note(chunk: dict[str, Any]) -> dict[str, Any]:
    return {
        "book_id": chunk["book_id"],
        "chapter_id": chunk["chapter_id"],
        "chunk_id": chunk["chunk_id"],
        "source": {
            "chapter_title": chunk["chapter_title"],
            "source_path": chunk["source_path"],
            "source_pages": chunk.get("source_pages"),
            "char_start": chunk["char_start"],
            "char_end": chunk["char_end"],
            "checksum": chunk["checksum"],
        },
        "summary": "",
        "key_points": [],
        "arguments": [],
        "examples": [],
        "stories": [],
        "definitions": [],
        "names": [],
        "dates": [],
        "numbers": [],
        "places": [],
        "terms": [],
        "quotes": [],
        "actionable_lessons": [],
        "open_questions": [],
    }


def _value_has_content(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, dict):
        return any(_value_has_content(item) for item in value.values())
    if isinstance(value, list):
        return any(_value_has_content(item) for item in value)
    return True


def note_has_semantic_content(note: dict[str, Any]) -> bool:
    return any(_value_has_content(note.get(field)) for field in NOTE_SEMANTIC_FIELDS)


def _note_is_untouched(note: dict[str, Any]) -> bool:
    return not note_has_semantic_content(note)


def _note_prompt(chunk: dict[str, Any], note: dict[str, Any]) -> str:
    schema = json.dumps(note, ensure_ascii=False, indent=2)
    return f"""Extract preservation notes for this book chunk.

Rules:
- Preserve concrete content: claims, examples, stories, names, dates, numbers, definitions, terms, and useful quotes.
- Keep wording faithful to the source; do not add outside facts.
- Quotes must be short and must appear in the chunk.
- If a field has nothing meaningful, leave it as an empty list or empty string.
- Return only valid JSON matching the schema.

Schema:
{schema}

Chunk text:
<<<
{chunk["text"]}
>>>
"""


def _iter_chunk_files(book_dir: Path) -> list[Path]:
    return sorted((book_dir / "chunks").glob("*.jsonl"))


def _iter_summary_files(book_dir: Path) -> list[Path]:
    return sorted(_summary_sources_by_chapter(book_dir).values())


def _chapter_lookup(book_dir: Path) -> dict[str, dict[str, Any]]:
    manifest_path = book_dir / "manifests" / "book.json"
    if not manifest_path.exists():
        return {}
    manifest = _read_json(manifest_path)
    lookup: dict[str, dict[str, Any]] = {}
    for chapter in manifest.get("chapters", []):
        chapter_id = str(chapter.get("chapter_id") or "")
        if not chapter_id:
            continue
        start_page = chapter.get("start_page")
        end_page = chapter.get("end_page")
        source_pages = None
        if start_page is not None and end_page is not None:
            source_pages = f"{start_page}-{end_page}"
        lookup[chapter_id] = {
            "title": str(chapter.get("title") or chapter_id),
            "source_path": str(chapter.get("path") or ""),
            "source_pages": source_pages,
        }
    return lookup


def _chapter_rows(book_dir: Path) -> list[dict[str, Any]]:
    manifest_path = book_dir / "manifests" / "book.json"
    if not manifest_path.exists():
        return []
    manifest = _read_json(manifest_path)
    return [row for row in manifest.get("chapters", []) if isinstance(row, dict)]


def _markdown_title(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def _looks_like_summary_prompt(text: str) -> bool:
    stripped = text.lstrip()
    if stripped.startswith("Create a source-linked hierarchical chapter summary from these chunk notes."):
        return True
    return "Chunk notes:" in text and "```json" in text


def _summary_target_path(book_dir: Path, source_path: Path) -> Path | None:
    chapter_lookup = _chapter_lookup(book_dir)
    stem = source_path.stem
    if stem in chapter_lookup:
        return book_dir / "summaries" / f"{stem}.md"

    index_match = re.match(r"^(\d{1,3})\b", stem)
    if index_match:
        chapter_index = int(index_match.group(1))
        for chapter in _chapter_rows(book_dir):
            if int(chapter.get("index", 0)) == chapter_index:
                chapter_id = str(chapter.get("chapter_id") or "")
                if chapter_id:
                    return book_dir / "summaries" / f"{chapter_id}.md"
    return None


def _summary_chapter_id(book_dir: Path, source_path: Path) -> str | None:
    if source_path.parent.name == "summaries":
        return source_path.stem
    target_path = _summary_target_path(book_dir, source_path)
    return target_path.stem if target_path is not None else None


def _summary_sources_by_chapter(book_dir: Path) -> dict[str, Path]:
    sources: dict[str, Path] = {}
    for dirname in ["summaries", "summary"]:
        summary_dir = book_dir / dirname
        if not summary_dir.exists():
            continue
        for path in sorted(summary_dir.glob("*.md")):
            chapter_id = _summary_chapter_id(book_dir, path)
            if chapter_id is None:
                continue
            sources.setdefault(chapter_id, path)
    return sources


def _import_summaries(book_dir: Path, *, force: bool = False, quiet: bool = False) -> dict[str, int]:
    out_dir = book_dir / "summaries"
    out_dir.mkdir(parents=True, exist_ok=True)
    stats = {"imported": 0, "skipped_prompts": 0, "skipped_missing_map": 0, "skipped_existing": 0}

    for source_path in _summary_sources_by_chapter(book_dir).values():
        text = source_path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        chapter_id = _summary_chapter_id(book_dir, source_path)
        if chapter_id is None:
            stats["skipped_missing_map"] += 1
            continue
        target_path = out_dir / f"{chapter_id}.md"
        if source_path.resolve() == target_path.resolve():
            continue
        if _looks_like_summary_prompt(text):
            stats["skipped_prompts"] += 1
            continue
        if target_path.exists() and not force:
            stats["skipped_existing"] += 1
            continue
        target_path.write_text(text + "\n", encoding="utf-8")
        stats["imported"] += 1
        if not quiet:
            print(f"Imported summary: {source_path} -> {target_path}")

    if not quiet:
        print(
            "Summary import complete: "
            f"{stats['imported']} imported, "
            f"{stats['skipped_prompts']} prompt stubs skipped, "
            f"{stats['skipped_missing_map']} unmapped skipped, "
            f"{stats['skipped_existing']} existing skipped."
        )
    return stats


def cmd_prepare_notes(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    chunk_files = _iter_chunk_files(book_dir)
    if not chunk_files:
        raise SystemExit(f"No chunk files found under {book_dir / 'chunks'}. Run `chunk` first.")

    total = 0
    for chunk_file in chunk_files:
        notes: list[dict[str, Any]] = []
        prompt_dir = book_dir / "prompts" / chunk_file.stem
        prompt_dir.mkdir(parents=True, exist_ok=True)
        for chunk in _read_jsonl(chunk_file):
            note = _empty_note(chunk)
            notes.append(note)
            prompt_path = prompt_dir / f"{chunk['chunk_id']}.md"
            prompt_path.write_text(_note_prompt(chunk, note), encoding="utf-8")
            total += 1
        note_path = book_dir / "notes" / f"{chunk_file.stem}.jsonl"
        if args.force or not note_path.exists():
            _write_jsonl(note_path, notes)
        print(f"Prepared {len(notes):02d} note skeletons and prompts for {chunk_file.stem}")
    print(f"Prepared {total} chunk-note prompt packets.")
    return 0


def _note_search_text(note: dict[str, Any]) -> str:
    pieces: list[str] = []
    for key in [
        "summary",
        "key_points",
        "arguments",
        "examples",
        "stories",
        "definitions",
        "names",
        "dates",
        "numbers",
        "places",
        "terms",
        "quotes",
        "actionable_lessons",
        "open_questions",
    ]:
        value = note.get(key)
        if isinstance(value, str):
            pieces.append(value)
        elif isinstance(value, list):
            pieces.extend(json.dumps(item, ensure_ascii=False) if isinstance(item, dict) else str(item) for item in value)
    return "\n".join(piece for piece in pieces if piece)


def cmd_build_index(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    _import_summaries(book_dir, quiet=True)
    index_path = book_dir / "indexes" / "search.sqlite"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    if index_path.exists():
        index_path.unlink()
    book_manifest_path = book_dir / "manifests" / "book.json"
    book_id = book_dir.name
    if book_manifest_path.exists():
        book_id = str(_read_json(book_manifest_path).get("book_id", book_id))
    chapter_lookup = _chapter_lookup(book_dir)
    summary_sources = _summary_sources_by_chapter(book_dir)
    conn = sqlite3.connect(index_path)
    conn.execute(
        "CREATE VIRTUAL TABLE docs USING fts5(book_id, chapter_id, chunk_id, kind, title, body, metadata UNINDEXED)"
    )

    rows = 0
    for chunk_file in _iter_chunk_files(book_dir):
        for chunk in _read_jsonl(chunk_file):
            conn.execute(
                "INSERT INTO docs(book_id, chapter_id, chunk_id, kind, title, body, metadata) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    chunk["book_id"],
                    chunk["chapter_id"],
                    chunk["chunk_id"],
                    "chunk",
                    chunk["chapter_title"],
                    chunk["text"],
                    json.dumps(
                        {
                            "source_path": chunk["source_path"],
                            "source_pages": chunk.get("source_pages"),
                            "char_start": chunk["char_start"],
                            "char_end": chunk["char_end"],
                            "checksum": chunk["checksum"],
                        },
                        ensure_ascii=False,
                    ),
                ),
            )
            rows += 1

    for note_file in sorted((book_dir / "notes").glob("*.jsonl")):
        for note in _read_jsonl(note_file):
            body = _note_search_text(note)
            if not body.strip():
                continue
            conn.execute(
                "INSERT INTO docs(book_id, chapter_id, chunk_id, kind, title, body, metadata) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    note["book_id"],
                    note["chapter_id"],
                    note["chunk_id"],
                    "note",
                    note.get("source", {}).get("chapter_title", ""),
                    body,
                    json.dumps(note.get("source", {}), ensure_ascii=False),
                ),
            )
            rows += 1

    for chapter_id, summary_file in sorted(summary_sources.items()):
        body = summary_file.read_text(encoding="utf-8").strip()
        if not body:
            continue
        chapter_meta = chapter_lookup.get(chapter_id, {})
        conn.execute(
            "INSERT INTO docs(book_id, chapter_id, chunk_id, kind, title, body, metadata) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                book_id,
                chapter_id,
                chapter_id,
                "summary",
                chapter_meta.get("title") or _markdown_title(body) or chapter_id,
                body,
                json.dumps(
                    {
                        "source_path": str(summary_file),
                        "source_pages": chapter_meta.get("source_pages"),
                        "chapter_source_path": chapter_meta.get("source_path"),
                    },
                    ensure_ascii=False,
                ),
            ),
        )
        rows += 1

    conn.commit()
    conn.close()
    print(f"Indexed {rows} documents: {index_path}")
    return 0


def cmd_import_summaries(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    _import_summaries(book_dir, force=args.force)
    return 0


def _chapter_summary_prompt(chapter_id: str, notes: list[dict[str, Any]]) -> str:
    compact_notes = []
    for note in notes:
        compact_notes.append(
            {
                "chunk_id": note.get("chunk_id"),
                "source": note.get("source", {}),
                "summary": note.get("summary", ""),
                "key_points": note.get("key_points", []),
                "arguments": note.get("arguments", []),
                "examples": note.get("examples", []),
                "stories": note.get("stories", []),
                "definitions": note.get("definitions", []),
                "names": note.get("names", []),
                "dates": note.get("dates", []),
                "numbers": note.get("numbers", []),
                "places": note.get("places", []),
                "terms": note.get("terms", []),
                "quotes": note.get("quotes", []),
                "actionable_lessons": note.get("actionable_lessons", []),
                "open_questions": note.get("open_questions", []),
            }
        )

    payload = json.dumps(compact_notes, ensure_ascii=False, indent=2)
    return f"""Create a source-linked hierarchical chapter summary from these chunk notes.

Rules:
- Use only the notes below.
- Preserve the original sequence by chunk_id unless a thematic grouping is clearly better.
- Deduplicate repeated points.
- Keep concrete examples, stories, definitions, names, dates, numbers, places, terms, and short quotes.
- Keep examples attached to the idea they support.
- Do not invent missing details.
- If notes are incomplete, say which chunk_ids need extraction before a complete summary can be trusted.

Output:
1. Chapter title
2. Detailed chapter summary
3. Key points
4. Important examples and stories
5. Definitions and terms
6. Names, dates, numbers, and places
7. Short relevant quotes or standout statements
8. Actionable lessons
9. Source chunk IDs used

Chapter ID: {chapter_id}

Chunk notes:
```json
{payload}
```
"""


def cmd_prepare_summaries(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    note_files = sorted((book_dir / "notes").glob("*.jsonl"))
    if not note_files:
        raise SystemExit(f"No note files found under {book_dir / 'notes'}. Run `prepare-notes` first.")

    out_dir = book_dir / "prompts" / "summaries"
    out_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    for note_file in note_files:
        notes = list(_read_jsonl(note_file))
        if not notes:
            continue
        chapter_id = str(notes[0].get("chapter_id") or note_file.stem)
        prompt_path = out_dir / f"{chapter_id}.md"
        prompt_path.write_text(_chapter_summary_prompt(chapter_id, notes), encoding="utf-8")
        total += 1
        print(f"Wrote summary prompt: {prompt_path}")
    print(f"Prepared {total} chapter summary prompts.")
    return 0


def _snippet(text: str, query: str, limit: int = 420) -> str:
    lowered = text.lower()
    terms = [term.lower() for term in re.findall(r"[A-Za-z0-9']+", query)]
    positions = [lowered.find(term) for term in terms if lowered.find(term) >= 0]
    start = max(min(positions) - 120, 0) if positions else 0
    snippet = text[start : start + limit].replace("\n", " ")
    return re.sub(r"\s+", " ", snippet).strip()


def _fts5_quote(value: str) -> str:
    return f'"{value.replace("\"", "\"\"")}"'


def _search_terms(query: str) -> list[str]:
    normalized = query.replace("’", "'")
    terms = re.findall(r"[0-9A-Za-z]+(?:'[0-9A-Za-z]+)*", normalized)
    seen: set[str] = set()
    ordered: list[str] = []
    for term in terms:
        if term in seen:
            continue
        seen.add(term)
        ordered.append(term)
    return ordered


def _build_match_query(query: str) -> str:
    raw = re.sub(r"\s+", " ", query.replace("’", "'")).strip()
    if not raw:
        raise SystemExit("Search query cannot be empty.")

    clauses: list[str] = []
    seen: set[str] = set()

    def add_clause(clause: str) -> None:
        if clause and clause not in seen:
            seen.add(clause)
            clauses.append(f"({clause})")

    add_clause(_fts5_quote(raw))

    normalized_phrase = " ".join(_search_terms(raw))
    if normalized_phrase:
        add_clause(_fts5_quote(normalized_phrase))

    token_terms = _search_terms(raw)
    if token_terms:
        add_clause(" AND ".join(_fts5_quote(term) for term in token_terms))

    return " OR ".join(clauses)


def cmd_search(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    index_path = book_dir / "indexes" / "search.sqlite"
    if not index_path.exists():
        raise SystemExit(f"Missing index: {index_path}. Run `build-index` first.")
    conn = sqlite3.connect(index_path)
    query = args.query
    match_query = _build_match_query(query)
    rows = conn.execute(
        """
        SELECT book_id, chapter_id, chunk_id, kind, title, body, metadata,
               bm25(docs, 1.0, 8.0, 8.0, 0.5, 12.0, 1.0, 0.0) AS rank
        FROM docs
        WHERE docs MATCH ?
        ORDER BY CASE kind WHEN 'summary' THEN 0 WHEN 'note' THEN 1 ELSE 2 END, rank
        LIMIT ?
        """,
        (match_query, args.limit),
    ).fetchall()
    conn.close()

    for idx, row in enumerate(rows, start=1):
        book_id, chapter_id, chunk_id, kind, title, body, metadata, rank = row
        meta = json.loads(metadata or "{}")
        location = meta.get("source_pages") or f"{meta.get('char_start', '?')}-{meta.get('char_end', '?')}"
        print(f"{idx}. {kind} | {chapter_id} | {chunk_id} | {title} | {location}")
        print(f"   {_snippet(body, query)}")
    if not rows:
        print("No matches.")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    problems: list[str] = []
    book_manifest = book_dir / "manifests" / "book.json"
    chunk_manifest = book_dir / "manifests" / "chunks.json"
    if not book_manifest.exists():
        problems.append(f"missing book manifest: {book_manifest}")
    if not chunk_manifest.exists():
        problems.append(f"missing chunk manifest: {chunk_manifest}")

    chunk_files_by_chapter = {path.stem: path for path in _iter_chunk_files(book_dir)}
    note_files_by_chapter = {path.stem: path for path in sorted((book_dir / "notes").glob("*.jsonl"))}

    chapter_rows = _chapter_rows(book_dir)
    if chapter_rows:
        for chapter in chapter_rows:
            chapter_id = str(chapter.get("chapter_id") or "")
            if not chapter_id:
                continue
            chunk_file = chunk_files_by_chapter.get(chapter_id)
            if chunk_file is None:
                problems.append(
                    f"missing chunk file for chapter {chapter_id}: {book_dir / 'chunks' / f'{chapter_id}.jsonl'}"
                )

    for chunk_file in _iter_chunk_files(book_dir):
        notes_file = note_files_by_chapter.get(chunk_file.stem)
        if notes_file is None:
            problems.append(f"missing note file for chapter {chunk_file.stem}: {book_dir / 'notes' / f'{chunk_file.stem}.jsonl'}")
            continue

        chunk_rows = list(_read_jsonl(chunk_file))
        note_rows = list(_read_jsonl(notes_file))
        chunk_ids = [str(chunk.get("chunk_id") or "") for chunk in chunk_rows]
        note_rows_by_chunk_id: dict[str, dict[str, Any]] = {}
        for note in note_rows:
            note_chunk_id = str(note.get("chunk_id") or "")
            if note_chunk_id in note_rows_by_chunk_id:
                problems.append(f"duplicate note chunk_id {note_chunk_id} in {notes_file}")
            note_rows_by_chunk_id[note_chunk_id] = note

        seen_chunk_ids: set[str] = set()

        for chunk in chunk_rows:
            chunk_id = str(chunk.get("chunk_id") or "")
            text = str(chunk.get("text") or "")
            if not chunk_id:
                problems.append(f"missing chunk_id in chunk file {chunk_file}")
                continue
            if chunk_id in seen_chunk_ids:
                problems.append(f"duplicate chunk_id {chunk_id} in {chunk_file}")
                continue
            seen_chunk_ids.add(chunk_id)
            if not text.strip():
                problems.append(f"empty chunk text for chunk {chunk_id} in {chunk_file}")
            if len(text) > args.max_chars:
                problems.append(f"chunk exceeds {args.max_chars} chars for chunk {chunk_id} in {chunk_file}")

            note = note_rows_by_chunk_id.get(chunk_id)
            if note is None:
                problems.append(f"missing note for chunk {chunk_id} in {notes_file}")
                continue
            if _note_is_untouched(note):
                problems.append(f"untouched note skeleton for chunk {chunk_id} in {notes_file}")

        extra_notes = sorted(set(note_rows_by_chunk_id) - set(chunk_ids))
        for extra_chunk_id in extra_notes:
            if extra_chunk_id:
                problems.append(f"orphan note for unknown chunk {extra_chunk_id} in {notes_file}")
            else:
                problems.append(f"orphan note with missing chunk_id in {notes_file}")

    index_path = book_dir / "indexes" / "search.sqlite"
    if not index_path.exists():
        problems.append(f"missing search index: {index_path}")

    if problems:
        print("Validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    total_chunks = sum(1 for chunk_file in _iter_chunk_files(book_dir) for _ in _read_jsonl(chunk_file))
    print(f"Validation passed. Found {total_chunks} chunks.")
    return 0


def cmd_setup(args: argparse.Namespace) -> int:
    book_dir = args.book_dir.resolve()
    cmd_init_book(argparse.Namespace(book_dir=book_dir, title=args.title, book_id=args.book_id))
    cmd_chunk(
        argparse.Namespace(
            book_dir=book_dir,
            title=args.title,
            book_id=args.book_id,
            target_chars=args.target_chars,
            overlap_chars=args.overlap_chars,
        )
    )
    cmd_prepare_notes(argparse.Namespace(book_dir=book_dir, force=args.force_notes))
    cmd_prepare_summaries(argparse.Namespace(book_dir=book_dir))
    cmd_import_summaries(argparse.Namespace(book_dir=book_dir, force=args.force_summaries))
    cmd_build_index(argparse.Namespace(book_dir=book_dir))
    if not args.skip_validate:
        return cmd_validate(argparse.Namespace(book_dir=book_dir, max_chars=args.max_chars))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Preserve book content with chunking, notes, summaries, and retrieval.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_book = subparsers.add_parser("init-book", help="Create a book manifest and artifact directories.")
    init_book.add_argument("book_dir", type=Path)
    init_book.add_argument("--title", default=None)
    init_book.add_argument("--book-id", default=None)
    init_book.set_defaults(func=cmd_init_book)

    setup = subparsers.add_parser(
        "setup", help="Initialize a book, generate preservation artifacts, import summaries, and build the search index."
    )
    setup.add_argument("book_dir", type=Path)
    setup.add_argument("--title", default=None)
    setup.add_argument("--book-id", default=None)
    setup.add_argument("--target-chars", type=int, default=DEFAULT_TARGET_CHARS)
    setup.add_argument("--overlap-chars", type=int, default=DEFAULT_OVERLAP_CHARS)
    setup.add_argument("--force-notes", action="store_true")
    setup.add_argument("--force-summaries", action="store_true")
    setup.add_argument("--skip-validate", action="store_true")
    setup.add_argument("--max-chars", type=int, default=12000)
    setup.set_defaults(func=cmd_setup)

    chunk = subparsers.add_parser("chunk", help="Split chapter text files into stable semantic chunks.")
    chunk.add_argument("book_dir", type=Path)
    chunk.add_argument("--title", default=None)
    chunk.add_argument("--book-id", default=None)
    chunk.add_argument("--target-chars", type=int, default=DEFAULT_TARGET_CHARS)
    chunk.add_argument("--overlap-chars", type=int, default=DEFAULT_OVERLAP_CHARS)
    chunk.set_defaults(func=cmd_chunk)

    prepare_notes = subparsers.add_parser("prepare-notes", help="Create chunk note JSONL skeletons and prompt packets.")
    prepare_notes.add_argument("book_dir", type=Path)
    prepare_notes.add_argument("--force", action="store_true")
    prepare_notes.set_defaults(func=cmd_prepare_notes)

    build_index = subparsers.add_parser("build-index", help="Build a local SQLite FTS search index.")
    build_index.add_argument("book_dir", type=Path)
    build_index.set_defaults(func=cmd_build_index)

    import_summaries = subparsers.add_parser(
        "import-summaries", help="Import real chapter summary markdown files into the canonical summaries directory."
    )
    import_summaries.add_argument("book_dir", type=Path)
    import_summaries.add_argument("--force", action="store_true")
    import_summaries.set_defaults(func=cmd_import_summaries)

    prepare_summaries = subparsers.add_parser(
        "prepare-summaries", help="Create chapter summary prompts from chunk-note JSONL files."
    )
    prepare_summaries.add_argument("book_dir", type=Path)
    prepare_summaries.set_defaults(func=cmd_prepare_summaries)

    search = subparsers.add_parser("search", help="Search preserved chunks and notes.")
    search.add_argument("book_dir", type=Path)
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=8)
    search.set_defaults(func=cmd_search)

    validate = subparsers.add_parser("validate", help="Validate generated preservation artifacts.")
    validate.add_argument("book_dir", type=Path)
    validate.add_argument("--max-chars", type=int, default=12000)
    validate.set_defaults(func=cmd_validate)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
