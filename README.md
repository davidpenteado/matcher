# MATCHER

MATCHER is a Python tool for identifying cross-lingual text reuse between query documents and indexed reference corpora. It encodes texts with LaBSE, searches multilingual vector indexes with FAISS, aggregates candidate matches by source volume, localizes dense page windows, and produces sentence-level alignments for manual verification.

## Structure

```text
src/textreuse/        source code
docs/                data schema and reproducibility notes
examples/            minimal input and corpus examples
requirements.txt     Python dependencies
match.ps1            Windows convenience wrapper
```

## Installation

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Data

Place query documents in `input/`. Reference corpora should be page-level JSONL files in `corpus/`, with records such as:

```json
{"id":"French/Journal/Volume/p42","series":"Journal","title":"Volume","page":42,"text":"Page text..."}
```

See `docs/DATA_SCHEMA.md` for details.

## Build an Index

```powershell
python -m src.textreuse.cli index --corpus corpus\French.jsonl --index_dir index_data\index_french --prefix French
```

## Run Matching

```powershell
python -m src.textreuse.cli run --pt_dir input --out_dir output_results --index_dir index_data --include_corpora French,English,Spanish,German,Italian
```

With visual reports:

```powershell
python -m src.textreuse.cli run --pt_dir input --out_dir output_results --index_dir index_data --include_corpora French,English,Spanish,German,Italian --viz
```

Windows wrapper:

```powershell
.\match.ps1 French
```

## Outputs

MATCHER writes tabular, JSONL, and HTML reports to `output_results/`. The reports are intended for inspection and manual provenance assessment.

## Reproducibility

See `docs/REPRODUCIBILITY.md`.

## Citation

See `CITATION.cff`.

## License

MIT License.
