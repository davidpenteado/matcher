# Reproducibility Notes

This document records the computational workflow used with MATCHER. It is intended to make the code release understandable and reproducible without bundling local corpora, indexes, virtual environments, or generated reports.

## Software Environment

Install dependencies from `requirements.txt` in a fresh virtual environment. The research run used LaBSE embeddings through `sentence-transformers` and FAISS for vector search. GPU acceleration was used when available, but the code can run on CPU for modest collections.

The repository does not include `.venv`, `venv_gpu`, or any installed libraries. These should be recreated from `requirements.txt`.

## Indexed Corpora Used in the Research Workflow

The language indexes were built from local page-level JSONL corpora. The following corpus counts describe the indexed files used in the working copy at the time of release:

| Language | Volumes | Pages | Volume share | Page share |
|---|---:|---:|---:|---:|
| Portuguese | 66 | 30,394 | 2.92% | 2.45% |
| English | 645 | 384,415 | 28.55% | 31.01% |
| French | 1,287 | 663,510 | 56.97% | 53.53% |
| Spanish | 26 | 10,573 | 1.15% | 0.85% |
| German | 110 | 79,460 | 4.87% | 6.41% |
| Italian | 125 | 71,160 | 5.53% | 5.74% |
| Total | 2,259 | 1,239,512 | 100.00% | 100.00% |

These counts are provided to document the scale and balance of the indexed corpora. They are not included in this code release.

## Index-Building Commands

The indexes were built with commands of this form:

```powershell
python -m src.textreuse.cli index --corpus corpus\French.jsonl --index_dir index_data\index_french --prefix French
```

For the multilingual corpus:

```powershell
python -m src.textreuse.cli index --corpus corpus\English.jsonl --index_dir index_data\index_english --prefix English
python -m src.textreuse.cli index --corpus corpus\French.jsonl --index_dir index_data\index_french --prefix French
python -m src.textreuse.cli index --corpus corpus\Spanish.jsonl --index_dir index_data\index_spanish --prefix Spanish
python -m src.textreuse.cli index --corpus corpus\German.jsonl --index_dir index_data\index_german --prefix German
python -m src.textreuse.cli index --corpus corpus\Italian.jsonl --index_dir index_data\index_italian --prefix Italian
python -m src.textreuse.cli index --corpus corpus\Portuguese.jsonl --index_dir index_data\index_portuguese --prefix Portuguese
```

## Matching Commands

Typical full multilingual run:

```powershell
python -m src.textreuse.cli run --pt_dir input --out_dir output_results --index_dir index_data --include_corpora French,English,Spanish,German,Italian
```

Visualization run:

```powershell
python -m src.textreuse.cli run --pt_dir input --out_dir output_results --index_dir index_data --include_corpora French,English,Spanish,German,Italian --viz
```

## Methodological Role of the Script

The script is not a fully automatic provenance classifier. It is a candidate-generation and inspection system. The computational stages are:

1. ingest query articles and reference pages;
2. clean text, including simple HTML-tag removal;
3. split text into overlapping character windows;
4. encode chunks with LaBSE;
5. search indexed chunks with FAISS;
6. aggregate hits by source volume;
7. identify dense source page windows;
8. align query and source sentences;
9. generate reports for manual verification.

Final provenance claims require manual review of textual alignment, titles, attributions, dates, issue metadata, editorial notes, and named source venues.

## Materials Deliberately Excluded

The following were excluded from the release folder:

- research corpora (`corpus/`);
- generated indexes (`index_data/`);
- query articles (`input/`);
- generated reports (`output_results/`);
- local Python environments (`.venv/`, `venv/`, `venv_gpu/`);
- model caches;
- build logs and scratch/debug scripts.

This keeps the code release small while documenting what external data are needed to reproduce the study.


