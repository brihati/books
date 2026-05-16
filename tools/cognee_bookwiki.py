#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.book_pipeline import _build_match_query, _snippet


DEFAULT_BOOKS_ROOT = REPO_ROOT / "files"
DEFAULT_WIKI_DIR = REPO_ROOT / "wiki"
DEFAULT_MEMORY_DIR = REPO_ROOT / "memory"
DEFAULT_DATASET = "bookwiki"
DEFAULT_SESSION_ID = "bookwiki-demo"


@dataclass(frozen=True)
class BookSource:
    book_dir: Path
    book_id: str
    title: str
    chapters: list[dict[str, Any]]


@dataclass(frozen=True)
class MemoryPacket:
    packet_id: str
    kind: str
    title: str
    body: str
    metadata: dict[str, Any]


@dataclass(frozen=True)
class SearchHit:
    book_id: str
    book_title: str
    chapter_id: str
    chunk_id: str
    kind: str
    title: str
    location: str
    snippet: str
    source_path: str


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _slugify(value: str, fallback: str = "item") -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or fallback


def _title_case_slug(value: str) -> str:
    return " ".join(part.capitalize() for part in value.split("-") if part)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_local_env(path: Path = REPO_ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


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


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _append_log(wiki_dir: Path, action: str, title: str, detail: str) -> None:
    wiki_dir.mkdir(parents=True, exist_ok=True)
    log_path = wiki_dir / "log.md"
    entry = f"## [{_now_iso()}] {action} | {title}\n\n{detail.strip()}\n\n"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def discover_books(books_root: Path, requested: list[str] | None = None) -> list[BookSource]:
    requested_slugs = {_slugify(item) for item in requested or []}
    books: list[BookSource] = []
    for manifest_path in sorted(books_root.glob("*/manifests/book.json")):
        manifest = _read_json(manifest_path)
        title = str(manifest.get("title") or manifest_path.parents[1].name)
        book_id = str(manifest.get("book_id") or _slugify(title))
        aliases = {_slugify(title), _slugify(book_id), _slugify(manifest_path.parents[1].name)}
        if requested_slugs and not aliases.intersection(requested_slugs):
            continue
        chapters = [row for row in manifest.get("chapters", []) if isinstance(row, dict)]
        books.append(BookSource(manifest_path.parents[1], book_id, title, chapters))
    if requested_slugs and not books:
        raise SystemExit(f"No matching books found under {books_root}: {', '.join(requested or [])}")
    return books


def _chapter_by_id(book: BookSource) -> dict[str, dict[str, Any]]:
    lookup: dict[str, dict[str, Any]] = {}
    for chapter in book.chapters:
        chapter_id = str(chapter.get("chapter_id") or "")
        if chapter_id:
            lookup[chapter_id] = chapter
    return lookup


def _summary_packets(book: BookSource, *, max_chapters: int | None = None) -> list[MemoryPacket]:
    chapter_lookup = _chapter_by_id(book)
    packets: list[MemoryPacket] = []
    summary_paths = sorted((book.book_dir / "summaries").glob("*.md"))
    if max_chapters is not None:
        summary_paths = summary_paths[:max_chapters]
    for summary_path in summary_paths:
        chapter_id = summary_path.stem
        chapter = chapter_lookup.get(chapter_id, {})
        chapter_title = str(chapter.get("title") or chapter_id)
        text = summary_path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        source_pages = None
        if chapter.get("start_page") is not None and chapter.get("end_page") is not None:
            source_pages = f"{chapter.get('start_page')}-{chapter.get('end_page')}"
        body = "\n".join(
            [
                f"# {book.title}: {chapter_title}",
                "",
                f"Book ID: {book.book_id}",
                f"Chapter ID: {chapter_id}",
                f"Source summary: {summary_path}",
                f"Source pages: {source_pages or 'unknown'}",
                "",
                text,
            ]
        )
        packets.append(
            MemoryPacket(
                packet_id=f"{book.book_id}:{chapter_id}:summary",
                kind="summary",
                title=f"{book.title} / {chapter_title}",
                body=body,
                metadata={
                    "book_id": book.book_id,
                    "book_title": book.title,
                    "chapter_id": chapter_id,
                    "chapter_title": chapter_title,
                    "source_path": str(summary_path),
                    "source_pages": source_pages,
                },
            )
        )
    return packets


def _note_packets_and_concepts(
    book: BookSource,
    *,
    max_note_packets: int | None = 80,
) -> tuple[list[MemoryPacket], dict[str, list[dict[str, Any]]]]:
    packets: list[MemoryPacket] = []
    concepts: dict[str, list[dict[str, Any]]] = defaultdict(list)
    rows_seen = 0
    for note_path in sorted((book.book_dir / "notes").glob("*.jsonl")):
        for note in _read_jsonl(note_path):
            rows_seen += 1
            chapter_id = str(note.get("chapter_id") or note_path.stem)
            chunk_id = str(note.get("chunk_id") or chapter_id)
            source = note.get("source") if isinstance(note.get("source"), dict) else {}
            chapter_title = str(source.get("chapter_title") or chapter_id)
            terms = _as_list(note.get("terms"))
            definitions = _as_list(note.get("definitions"))
            key_points = _as_list(note.get("key_points"))
            actionable = _as_list(note.get("actionable_lessons"))
            examples = _as_list(note.get("examples"))
            for raw_term in terms + _definition_terms(definitions):
                concept_slug = _slugify(raw_term)
                if len(concept_slug) < 3:
                    continue
                concepts[concept_slug].append(
                    {
                        "term": raw_term,
                        "book_id": book.book_id,
                        "book_title": book.title,
                        "chapter_id": chapter_id,
                        "chapter_title": chapter_title,
                        "chunk_id": chunk_id,
                        "source_pages": source.get("source_pages"),
                        "source_path": source.get("source_path"),
                        "summary": str(note.get("summary") or ""),
                        "key_points": key_points[:3],
                    }
                )
            if max_note_packets is not None and len(packets) >= max_note_packets:
                continue
            if not any([note.get("summary"), key_points, actionable, examples, terms, definitions]):
                continue
            body = "\n".join(
                [
                    f"# {book.title}: {chapter_title} note",
                    "",
                    f"Book ID: {book.book_id}",
                    f"Chapter ID: {chapter_id}",
                    f"Chunk ID: {chunk_id}",
                    f"Source pages: {source.get('source_pages') or 'unknown'}",
                    "",
                    f"Summary: {note.get('summary') or ''}",
                    "",
                    "Key points:",
                    *[f"- {item}" for item in key_points[:8]],
                    "",
                    "Actionable lessons:",
                    *[f"- {item}" for item in actionable[:6]],
                    "",
                    "Examples:",
                    *[f"- {item}" for item in examples[:6]],
                    "",
                    "Terms:",
                    *[f"- {item}" for item in terms[:12]],
                ]
            )
            packets.append(
                MemoryPacket(
                    packet_id=f"{book.book_id}:{chunk_id}:note",
                    kind="note",
                    title=f"{book.title} / {chapter_title} / {chunk_id}",
                    body=body,
                    metadata={
                        "book_id": book.book_id,
                        "book_title": book.title,
                        "chapter_id": chapter_id,
                        "chapter_title": chapter_title,
                        "chunk_id": chunk_id,
                        "source_path": source.get("source_path"),
                        "source_pages": source.get("source_pages"),
                    },
                )
            )
    if rows_seen == 0:
        return packets, concepts
    return packets, concepts


def _as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _definition_terms(definitions: list[str]) -> list[str]:
    terms: list[str] = []
    for definition in definitions:
        term = definition.split(":", 1)[0].strip()
        if term:
            terms.append(term)
    return terms


def collect_memory(
    books: list[BookSource],
    *,
    include_notes: bool = True,
    max_chapters: int | None = None,
    max_note_packets: int | None = 80,
) -> tuple[list[MemoryPacket], dict[str, list[dict[str, Any]]]]:
    packets: list[MemoryPacket] = []
    concepts: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for book in books:
        packets.extend(_summary_packets(book, max_chapters=max_chapters))
        if include_notes:
            note_packets, note_concepts = _note_packets_and_concepts(book, max_note_packets=max_note_packets)
            packets.extend(note_packets)
            for slug, entries in note_concepts.items():
                concepts[slug].extend(entries)
    return packets, concepts


class SessionStore:
    def __init__(self, *, memory_dir: Path, redis_url: str | None, enabled: bool = True) -> None:
        self.memory_dir = memory_dir
        self.redis_url = redis_url or os.environ.get("REDIS_URL") or "redis://localhost:6379/0"
        self.enabled = enabled
        self.redis_client: Any | None = None
        if enabled:
            self.redis_client = self._connect()

    def _connect(self) -> Any | None:
        try:
            import redis

            client = redis.Redis.from_url(self.redis_url, decode_responses=True)
            client.ping()
            return client
        except Exception:
            return None

    @property
    def backend(self) -> str:
        return "redis" if self.redis_client is not None else "jsonl"

    def append(self, session_id: str, event_type: str, payload: dict[str, Any]) -> None:
        row = {"ts": _now_iso(), "session_id": session_id, "type": event_type, "payload": payload}
        _append_jsonl(self.memory_dir / "bookwiki_session.jsonl", row)
        if self.redis_client is not None:
            key = f"bookwiki:{session_id}:events"
            self.redis_client.rpush(key, json.dumps(row, ensure_ascii=False, sort_keys=True))
            self.redis_client.ltrim(key, -200, -1)

    def recent(self, session_id: str, limit: int = 8) -> list[dict[str, Any]]:
        if self.redis_client is not None:
            key = f"bookwiki:{session_id}:events"
            rows = self.redis_client.lrange(key, -limit, -1)
            return [json.loads(row) for row in rows]
        path = self.memory_dir / "bookwiki_session.jsonl"
        if not path.exists():
            return []
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        return [row for row in rows if row.get("session_id") == session_id][-limit:]


def _write_schema(wiki_dir: Path) -> None:
    _write_text(
        wiki_dir / "AGENTS.md",
        """# BookWiki Maintenance Rules

This wiki is the generated, inspectable memory layer for the Cognee BookWiki hackathon project.

Rules for agents:
- Treat `files/<Book>/` artifacts as source truth. Do not edit raw book artifacts from this wiki workflow.
- Cite book, chapter, chunk, and source paths for claims that come from books.
- Keep concept pages short and cross-linked with Obsidian wiki links such as `books/book-slug`, `concepts/concept-slug`, and `playbooks/playbook-slug`.
- Use `index.md` for navigation and `log.md` as an append-only operation log.
- Promote useful query answers into `playbooks/` during self-improvement instead of leaving them only in chat history.
- During lint, flag duplicate concepts, broken links, orphan pages, and weakly sourced pages.
""",
    )


def write_wiki(
    *,
    wiki_dir: Path,
    books: list[BookSource],
    concepts: dict[str, list[dict[str, Any]]],
    packet_count: int,
    max_concepts: int = 80,
) -> dict[str, Any]:
    _write_schema(wiki_dir)
    book_links: list[str] = []
    for book in books:
        slug = _slugify(book.title)
        summary_paths = sorted((book.book_dir / "summaries").glob("*.md"))
        note_paths = sorted((book.book_dir / "notes").glob("*.jsonl"))
        lines = [
            f"# {book.title}",
            "",
            f"- Book ID: `{book.book_id}`",
            f"- Source root: `{book.book_dir}`",
            f"- Chapters: {len(book.chapters)}",
            f"- Summary files: {len(summary_paths)}",
            f"- Note files: {len(note_paths)}",
            "",
            "## Chapter Map",
            "",
        ]
        for chapter in book.chapters:
            chapter_id = str(chapter.get("chapter_id") or "")
            title = str(chapter.get("title") or chapter_id)
            if not chapter_id:
                continue
            lines.append(f"- `{chapter_id}`: {title}")
        _write_text(wiki_dir / "books" / f"{slug}.md", "\n".join(lines))
        book_links.append(f"- [[books/{slug}|{book.title}]]")

    concept_links = _write_concept_pages(wiki_dir, concepts, max_concepts=max_concepts)
    index_lines = [
        "# BookWiki Index",
        "",
        f"Generated: {_now_iso()}",
        f"Memory packets prepared: {packet_count}",
        "",
        "## Books",
        "",
        *(book_links or ["- No books ingested yet."]),
        "",
        "## Concepts",
        "",
        *(concept_links or ["- No concepts extracted yet."]),
        "",
        "## Operations",
        "",
        "- `log.md` records ingest/query/improve/lint events.",
        "- `queries/` stores query briefs.",
        "- `playbooks/` stores promoted answers from the self-improvement loop.",
    ]
    _write_text(wiki_dir / "index.md", "\n".join(index_lines))
    return {"book_count": len(books), "concept_count": len(concept_links), "packet_count": packet_count}


def _write_concept_pages(
    wiki_dir: Path,
    concepts: dict[str, list[dict[str, Any]]],
    *,
    max_concepts: int,
) -> list[str]:
    ranked = sorted(concepts.items(), key=lambda item: (-len(item[1]), item[0]))[:max_concepts]
    links: list[str] = []
    for slug, entries in ranked:
        canonical = Counter(str(entry.get("term") or _title_case_slug(slug)) for entry in entries).most_common(1)[0][0]
        by_book = Counter(str(entry.get("book_title") or "") for entry in entries)
        lines = [
            f"# {canonical}",
            "",
            f"- Evidence count: {len(entries)}",
            "- Books: " + ", ".join(book for book, _count in by_book.most_common() if book),
            "",
            "## Source Evidence",
            "",
        ]
        for entry in entries[:12]:
            book_slug = _slugify(str(entry.get("book_title") or entry.get("book_id") or "book"))
            lines.append(
                "- "
                f"[[books/{book_slug}|{entry.get('book_title')}]] / "
                f"`{entry.get('chapter_id')}` / `{entry.get('chunk_id')}`"
            )
            summary = str(entry.get("summary") or "").strip()
            if summary:
                lines.append(f"  - {summary[:400]}")
            for key_point in entry.get("key_points") or []:
                lines.append(f"  - {key_point}")
        _write_text(wiki_dir / "concepts" / f"{slug}.md", "\n".join(lines))
        links.append(f"- [[concepts/{slug}|{canonical}]] ({len(entries)} sources)")
    return links


async def _cognee_remember(
    packets: list[MemoryPacket],
    *,
    dataset: str,
    session_id: str | None,
    permanent: bool,
) -> dict[str, Any]:
    _prepare_cognee_env()
    import cognee

    texts = [packet.body for packet in packets]
    if not texts:
        return {"status": "skipped", "reason": "no packets"}
    if permanent:
        result = await cognee.remember(
            texts,
            dataset_name=dataset,
            run_in_background=False,
            self_improvement=False,
        )
    else:
        result = await cognee.remember(
            "\n\n".join(texts),
            dataset_name=dataset,
            session_id=session_id,
            run_in_background=False,
            self_improvement=False,
        )
    return {"status": "ok", "result_type": type(result).__name__}


async def _cognee_recall(query: str, *, dataset: str, session_id: str | None, top_k: int) -> dict[str, Any]:
    _prepare_cognee_env()
    import cognee

    results = await cognee.recall(
        query_text=query,
        datasets=[dataset],
        session_id=session_id,
        top_k=top_k,
    )
    return {
        "status": "ok",
        "results": [getattr(result, "text", str(result)) for result in results],
    }


def _prepare_cognee_env() -> None:
    openai_key = os.environ.get("OPENAI_API_KEY")
    if openai_key and not os.environ.get("LLM_API_KEY"):
        os.environ["LLM_API_KEY"] = openai_key
    if openai_key and not os.environ.get("EMBEDDING_API_KEY"):
        os.environ["EMBEDDING_API_KEY"] = openai_key


def maybe_cognee_remember(
    packets: list[MemoryPacket],
    *,
    dataset: str,
    session_id: str | None,
    permanent: bool,
    enabled: bool,
) -> dict[str, Any]:
    if not enabled:
        return {"status": "disabled"}
    try:
        return asyncio.run(_cognee_remember(packets, dataset=dataset, session_id=session_id, permanent=permanent))
    except Exception as exc:
        return {"status": "error", "error": f"{type(exc).__name__}: {exc}"}


def maybe_cognee_recall(
    query: str,
    *,
    dataset: str,
    session_id: str | None,
    top_k: int,
    enabled: bool,
) -> dict[str, Any]:
    if not enabled:
        return {"status": "disabled", "results": []}
    try:
        return asyncio.run(_cognee_recall(query, dataset=dataset, session_id=session_id, top_k=top_k))
    except Exception as exc:
        return {"status": "error", "error": f"{type(exc).__name__}: {exc}", "results": []}


def ingest_books(
    *,
    books_root: Path,
    requested_books: list[str] | None,
    wiki_dir: Path,
    memory_dir: Path,
    session_id: str,
    redis_url: str | None,
    use_redis: bool,
    use_cognee: bool,
    dataset: str,
    include_notes: bool,
    max_chapters: int | None,
    max_note_packets: int | None,
    max_concepts: int,
) -> dict[str, Any]:
    books = discover_books(books_root, requested_books)
    packets, concepts = collect_memory(
        books,
        include_notes=include_notes,
        max_chapters=max_chapters,
        max_note_packets=max_note_packets,
    )
    stats = write_wiki(wiki_dir=wiki_dir, books=books, concepts=concepts, packet_count=len(packets), max_concepts=max_concepts)
    store = SessionStore(memory_dir=memory_dir, redis_url=redis_url, enabled=use_redis)
    store.append(
        session_id,
        "ingest",
        {
            "books": [book.title for book in books],
            "packet_count": len(packets),
            "concept_count": stats["concept_count"],
            "session_backend": store.backend,
        },
    )
    _append_log(
        wiki_dir,
        "ingest",
        ", ".join(book.title for book in books),
        f"Prepared {len(packets)} memory packets and {stats['concept_count']} concept pages. Session backend: {store.backend}.",
    )
    cognee_result = maybe_cognee_remember(
        packets,
        dataset=dataset,
        session_id=session_id,
        permanent=True,
        enabled=use_cognee,
    )
    return {**stats, "session_backend": store.backend, "cognee": cognee_result}


def search_books(books: list[BookSource], query: str, *, limit: int) -> list[SearchHit]:
    hits: list[SearchHit] = []
    match_query = _build_match_query(query)
    for book in books:
        index_path = book.book_dir / "indexes" / "search.sqlite"
        if not index_path.exists():
            continue
        conn = sqlite3.connect(index_path)
        try:
            rows = conn.execute(
                """
                SELECT book_id, chapter_id, chunk_id, kind, title, body, metadata,
                       bm25(docs, 1.0, 8.0, 8.0, 0.5, 12.0, 1.0, 0.0) AS rank
                FROM docs
                WHERE docs MATCH ?
                ORDER BY CASE kind WHEN 'summary' THEN 0 WHEN 'note' THEN 1 ELSE 2 END, rank
                LIMIT ?
                """,
                (match_query, limit),
            ).fetchall()
        finally:
            conn.close()
        for row in rows:
            book_id, chapter_id, chunk_id, kind, title, body, metadata, _rank = row
            meta = json.loads(metadata or "{}")
            location = str(meta.get("source_pages") or f"{meta.get('char_start', '?')}-{meta.get('char_end', '?')}")
            hits.append(
                SearchHit(
                    book_id=str(book_id),
                    book_title=book.title,
                    chapter_id=str(chapter_id),
                    chunk_id=str(chunk_id),
                    kind=str(kind),
                    title=str(title),
                    location=location,
                    snippet=_snippet(str(body), query),
                    source_path=str(meta.get("source_path") or meta.get("chapter_source_path") or ""),
                )
            )
    return hits[:limit]


def _query_page_name(query: str) -> str:
    return f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{_slugify(query, fallback='query')[:64]}.md"


def write_query_page(
    *,
    wiki_dir: Path,
    query: str,
    hits: list[SearchHit],
    cognee_result: dict[str, Any],
    session_events: list[dict[str, Any]],
) -> Path:
    lines = [
        f"# Query Brief: {query}",
        "",
        f"- Created: {_now_iso()}",
        f"- Cognee recall: `{cognee_result.get('status')}`",
        f"- Session events considered: {len(session_events)}",
        "",
        "## Working Answer",
        "",
        "Use the source hits below as the grounding layer, then promote durable conclusions into a playbook if the answer is useful.",
        "",
    ]
    cognee_results = cognee_result.get("results") or []
    if cognee_results:
        lines.extend(["## Cognee Recall", ""])
        for result in cognee_results[:5]:
            lines.append(f"- {str(result).strip()[:800]}")
        lines.append("")
    lines.extend(["## Source Hits", ""])
    if not hits:
        lines.append("- No source hits found in the local book indexes.")
    for index, hit in enumerate(hits, start=1):
        book_slug = _slugify(hit.book_title)
        lines.extend(
            [
                f"{index}. [[books/{book_slug}|{hit.book_title}]] / `{hit.chapter_id}` / `{hit.chunk_id}`",
                f"   - Kind: `{hit.kind}`",
                f"   - Location: {hit.location}",
                f"   - Source path: `{hit.source_path}`",
                f"   - Snippet: {hit.snippet}",
            ]
        )
    path = wiki_dir / "queries" / _query_page_name(query)
    _write_text(path, "\n".join(lines))
    return path


def query_books(
    *,
    books_root: Path,
    requested_books: list[str] | None,
    wiki_dir: Path,
    memory_dir: Path,
    query: str,
    session_id: str,
    redis_url: str | None,
    use_redis: bool,
    use_cognee: bool,
    dataset: str,
    limit: int,
    save_playbook: bool,
) -> dict[str, Any]:
    books = discover_books(books_root, requested_books)
    store = SessionStore(memory_dir=memory_dir, redis_url=redis_url, enabled=use_redis)
    store.append(session_id, "query", {"query": query, "books": [book.title for book in books]})
    session_events = store.recent(session_id)
    cognee_result = maybe_cognee_recall(query, dataset=dataset, session_id=session_id, top_k=limit, enabled=use_cognee)
    hits = search_books(books, query, limit=limit)
    query_page = write_query_page(
        wiki_dir=wiki_dir,
        query=query,
        hits=hits,
        cognee_result=cognee_result,
        session_events=session_events,
    )
    _append_log(
        wiki_dir,
        "query",
        query,
        f"Wrote `{query_page}` with {len(hits)} source hits. Session backend: {store.backend}. Cognee: {cognee_result.get('status')}.",
    )
    playbook_path = None
    if save_playbook:
        playbook_path = promote_query_page(
            query_page=query_page,
            wiki_dir=wiki_dir,
            memory_dir=memory_dir,
            session_id=session_id,
            redis_url=redis_url,
            use_redis=use_redis,
            use_cognee=use_cognee,
            dataset=dataset,
            feedback="Auto-promoted from query because --save-playbook was used.",
        )
    return {
        "query_page": str(query_page),
        "playbook_path": str(playbook_path) if playbook_path else None,
        "hit_count": len(hits),
        "session_backend": store.backend,
        "cognee": cognee_result,
    }


def latest_query_page(wiki_dir: Path) -> Path:
    query_pages = sorted((wiki_dir / "queries").glob("*.md"), key=lambda path: path.stat().st_mtime)
    if not query_pages:
        raise SystemExit(f"No query pages found under {wiki_dir / 'queries'}. Run `query` first.")
    return query_pages[-1]


def promote_query_page(
    *,
    query_page: Path,
    wiki_dir: Path,
    memory_dir: Path,
    session_id: str,
    redis_url: str | None,
    use_redis: bool,
    use_cognee: bool,
    dataset: str,
    feedback: str,
) -> Path:
    text = query_page.read_text(encoding="utf-8").strip()
    heading_match = re.search(r"^#\s+Query Brief:\s*(.+)$", text, flags=re.MULTILINE)
    title = heading_match.group(1).strip() if heading_match else query_page.stem
    playbook_slug = _slugify(title, fallback="promoted-answer")
    playbook_path = wiki_dir / "playbooks" / f"{playbook_slug}.md"
    playbook_text = "\n".join(
        [
            f"# Playbook: {title}",
            "",
            f"- Promoted: {_now_iso()}",
            f"- Source query page: `{query_page}`",
            f"- Session ID: `{session_id}`",
            "",
            "## Feedback",
            "",
            feedback.strip() or "No explicit feedback provided.",
            "",
            "## Promoted Answer",
            "",
            text,
        ]
    )
    _write_text(playbook_path, playbook_text)
    store = SessionStore(memory_dir=memory_dir, redis_url=redis_url, enabled=use_redis)
    store.append(session_id, "improve", {"query_page": str(query_page), "playbook_path": str(playbook_path), "feedback": feedback})
    _append_log(wiki_dir, "improve", title, f"Promoted `{query_page}` to `{playbook_path}`.")
    packet = MemoryPacket(
        packet_id=f"playbook:{playbook_slug}",
        kind="playbook",
        title=f"Playbook: {title}",
        body=playbook_text,
        metadata={"playbook_path": str(playbook_path), "query_page": str(query_page), "session_id": session_id},
    )
    maybe_cognee_remember([packet], dataset=dataset, session_id=session_id, permanent=True, enabled=use_cognee)
    return playbook_path


def lint_wiki(*, wiki_dir: Path, memory_dir: Path, session_id: str, redis_url: str | None, use_redis: bool) -> dict[str, Any]:
    pages = sorted(path for path in wiki_dir.rglob("*.md") if path.name not in {"log.md"})
    page_keys = {path.relative_to(wiki_dir).with_suffix("").as_posix() for path in pages}
    inbound: Counter[str] = Counter()
    broken_links: list[str] = []
    weak_sources: list[str] = []
    duplicate_titles: dict[str, list[str]] = defaultdict(list)
    for path in pages:
        rel = path.relative_to(wiki_dir).as_posix()
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        if title_match:
            duplicate_titles[_slugify(title_match.group(1))].append(rel)
        for link in re.findall(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", text):
            target = link.strip().strip("/")
            inbound[target] += 1
            if target not in page_keys:
                broken_links.append(f"{rel} -> {target}")
        if rel.startswith(("concepts/", "playbooks/", "queries/")) and "chapter-" not in text and "chunk-" not in text:
            weak_sources.append(rel)
    orphans = [
        path.relative_to(wiki_dir).as_posix()
        for path in pages
        if path.relative_to(wiki_dir).with_suffix("").as_posix() not in inbound
        and not path.relative_to(wiki_dir).as_posix() in {"index.md", "AGENTS.md", "lint.md"}
    ]
    duplicates = {title: rels for title, rels in duplicate_titles.items() if len(rels) > 1}
    broken_link_lines = [f"- {item}" for item in broken_links[:100]] or ["- None found."]
    orphan_lines = [f"- {item}" for item in orphans[:100]] or ["- None found."]
    weak_source_lines = [f"- {item}" for item in weak_sources[:100]] or ["- None found."]
    lines = [
        "# BookWiki Lint Report",
        "",
        f"- Created: {_now_iso()}",
        f"- Pages scanned: {len(pages)}",
        f"- Broken links: {len(broken_links)}",
        f"- Orphan pages: {len(orphans)}",
        f"- Weakly sourced pages: {len(weak_sources)}",
        f"- Duplicate titles: {len(duplicates)}",
        "",
        "## Broken Links",
        "",
        *broken_link_lines,
        "",
        "## Orphan Pages",
        "",
        *orphan_lines,
        "",
        "## Weakly Sourced Pages",
        "",
        *weak_source_lines,
        "",
        "## Duplicate Titles",
        "",
    ]
    if duplicates:
        for title, rels in sorted(duplicates.items()):
            lines.append(f"- `{title}`: {', '.join(rels)}")
    else:
        lines.append("- None found.")
    _write_text(wiki_dir / "lint.md", "\n".join(lines))
    store = SessionStore(memory_dir=memory_dir, redis_url=redis_url, enabled=use_redis)
    store.append(
        session_id,
        "lint",
        {
            "pages": len(pages),
            "broken_links": broken_links,
            "orphans": orphans,
            "weak_sources": weak_sources,
            "duplicate_titles": duplicates,
        },
    )
    _append_log(wiki_dir, "lint", "wiki health check", f"Wrote `{wiki_dir / 'lint.md'}`.")
    return {
        "page_count": len(pages),
        "broken_link_count": len(broken_links),
        "orphan_count": len(orphans),
        "weak_source_count": len(weak_sources),
        "duplicate_title_count": len(duplicates),
        "session_backend": store.backend,
    }


def cmd_status(args: argparse.Namespace) -> int:
    status: dict[str, Any] = {}
    try:
        import cognee

        status["cognee"] = getattr(cognee, "__version__", "installed")
    except Exception as exc:
        status["cognee"] = f"missing: {exc}"
    store = SessionStore(memory_dir=args.memory_dir, redis_url=args.redis_url, enabled=not args.no_redis)
    status["session_backend"] = store.backend
    status["redis_url"] = store.redis_url
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    result = ingest_books(
        books_root=args.books_root,
        requested_books=args.books,
        wiki_dir=args.wiki_dir,
        memory_dir=args.memory_dir,
        session_id=args.session_id,
        redis_url=args.redis_url,
        use_redis=not args.no_redis,
        use_cognee=args.use_cognee,
        dataset=args.dataset,
        include_notes=not args.no_notes,
        max_chapters=args.max_chapters,
        max_note_packets=args.max_note_packets,
        max_concepts=args.max_concepts,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    result = query_books(
        books_root=args.books_root,
        requested_books=args.books,
        wiki_dir=args.wiki_dir,
        memory_dir=args.memory_dir,
        query=args.query,
        session_id=args.session_id,
        redis_url=args.redis_url,
        use_redis=not args.no_redis,
        use_cognee=args.use_cognee,
        dataset=args.dataset,
        limit=args.limit,
        save_playbook=args.save_playbook,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def cmd_improve(args: argparse.Namespace) -> int:
    query_page = args.query_page or latest_query_page(args.wiki_dir)
    playbook_path = promote_query_page(
        query_page=query_page,
        wiki_dir=args.wiki_dir,
        memory_dir=args.memory_dir,
        session_id=args.session_id,
        redis_url=args.redis_url,
        use_redis=not args.no_redis,
        use_cognee=args.use_cognee,
        dataset=args.dataset,
        feedback=args.feedback,
    )
    print(str(playbook_path))
    return 0


def cmd_lint(args: argparse.Namespace) -> int:
    result = lint_wiki(
        wiki_dir=args.wiki_dir,
        memory_dir=args.memory_dir,
        session_id=args.session_id,
        redis_url=args.redis_url,
        use_redis=not args.no_redis,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build a Cognee + Redis BookWiki over preserved book artifacts.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    parser.add_argument("--memory-dir", type=Path, default=DEFAULT_MEMORY_DIR)
    parser.add_argument("--books-root", type=Path, default=DEFAULT_BOOKS_ROOT)
    parser.add_argument("--session-id", default=DEFAULT_SESSION_ID)
    parser.add_argument("--redis-url", default=None)
    parser.add_argument("--dataset", default=DEFAULT_DATASET)
    parser.add_argument("--no-redis", action="store_true", help="Do not try Redis; write session memory to JSONL only.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="Check Cognee import and Redis session memory availability.")
    status.set_defaults(func=cmd_status)

    ingest = subparsers.add_parser("ingest", help="Ingest preserved book artifacts into the generated wiki and optional Cognee memory.")
    ingest.add_argument("--books", nargs="*", default=None, help="Book titles, directory names, or book IDs to ingest.")
    ingest.add_argument("--use-cognee", action="store_true", help="Also call cognee.remember for permanent memory.")
    ingest.add_argument("--no-notes", action="store_true", help="Only ingest chapter summaries.")
    ingest.add_argument("--max-chapters", type=int, default=None)
    ingest.add_argument("--max-note-packets", type=int, default=80)
    ingest.add_argument("--max-concepts", type=int, default=80)
    ingest.set_defaults(func=cmd_ingest)

    query = subparsers.add_parser("query", help="Query local book indexes, session memory, and optional Cognee recall.")
    query.add_argument("query")
    query.add_argument("--books", nargs="*", default=None)
    query.add_argument("--use-cognee", action="store_true", help="Also call cognee.recall.")
    query.add_argument("--limit", type=int, default=8)
    query.add_argument("--save-playbook", action="store_true", help="Immediately promote the query brief into playbooks/.")
    query.set_defaults(func=cmd_query)

    improve = subparsers.add_parser("improve", help="Promote a useful query brief into a durable playbook page.")
    improve.add_argument("--query-page", type=Path, default=None)
    improve.add_argument("--feedback", default="User marked this answer as useful.")
    improve.add_argument("--use-cognee", action="store_true", help="Also call cognee.remember for the promoted playbook.")
    improve.set_defaults(func=cmd_improve)

    lint_cmd = subparsers.add_parser("lint", help="Health-check wiki coherence.")
    lint_cmd.set_defaults(func=cmd_lint)
    return parser


def main(argv: list[str] | None = None) -> int:
    _load_local_env()
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
