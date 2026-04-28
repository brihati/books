# PDF → per-chapter plain text

This folder includes a small script to split a PDF into per-chapter `.txt` files using the PDF outline / Table of Contents (ToC).

## Setup

```bash
cd /Users/sachin/books
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pymupdf
```

## List chapters from the PDF ToC

```bash
. .venv/bin/activate
python tools/pdf_split_chapters.py "files/Never Split the Difference/Never Split the Difference.pdf" --list --level 1
```

## Write chapter `.txt` files (ToC-based)

Only keep real chapters (example: titles starting with `CHAPTER <number>`):

```bash
. .venv/bin/activate
python tools/pdf_split_chapters.py "files/Never Split the Difference/Never Split the Difference.pdf" \
  --level 1 \
  --include-title-regex '(?i)^\s*chapter\s+[0-9]+'
```

Outputs to `<out_dir>/` (default is `files/<pdf_stem>_chapters/`) and also writes a `chapters.json` manifest.

## If the PDF has no outline/ToC

Try regex-based detection (best-effort / may need tweaking):

```bash
. .venv/bin/activate
python tools/pdf_split_chapters.py files/E001005.pdf \
  --fallback-regex \
  --list
```
