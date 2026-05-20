# Data Schema

MATCHER can index either a directory of `.txt`, `.md`, or `.pdf` files, or a page-level JSONL corpus. For large historical corpora, JSONL is recommended because it preserves bibliographic and page metadata.

## Recommended JSONL Format

Each line is one page-level record:

```json
{"id":"French/Journal title/VolumeID/p42","series":"Journal title","title":"VolumeID","page":42,"text":"OCR text for the page..."}
```

Required fields:

- `id`: stable page identifier;
- `text`: page text.

Recommended fields:

- `series`: journal or series title;
- `title`: volume identifier;
- `page`: page number.

## Identifier Convention

The preferred identifier convention is:

```text
Language/Series title/VolumeID/pPageNumber
```

This allows the script to aggregate chunk-level matches by source volume and then inspect dense page windows.

## Query Articles

Query articles are placed in `input/` as `.txt`, `.md`, or `.pdf` files. If `.txt` files contain simple HTML markup, the ingestion layer removes tags before matching.

## Excluded Data

The research corpora and indexes are not included in this code release. To reproduce the full study, users must provide equivalent Corpus A query articles and Corpus B reference corpora, or obtain the archived data/indexes through the data repository associated with the publication.

