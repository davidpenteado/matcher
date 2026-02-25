# MATCHER - Text Reuse Detection Tool

**MATCHER** detects, rates, and visualizes text reuse between documents in any pair of supported languages using semantic deep learning.

Developed as a heuristic digital tool to aid researchers in documenting and discovering textual connections across languages. It uses state-of-the-art cross-lingual embeddings (`sentence-transformers/LaBSE`), fast vector similarity search (`FAISS`), and precise lexical matching (`Rapidfuzz`) to align texts seamlessly.

This tool aims to provide rigorous methodological support for academic research, ensuring source tracking and detailed visualizations of text overlaps. It processes large corpora rapidly while providing qualitative, granular sentence-level alignment.

---

## Installation

### Python
This tool is written in **Python 3** (recommended 3.11+). Python allows for fast execution and efficient integration of the deep learning models used by the tool. If you don't have Python installed, you can download it from [python.org](https://www.python.org/).

### Download the Tool
To download the tool to your computer, you can clone this repository using Git:

```bash
git clone https://github.com/your-username/matcher.git
cd matcher
```

Alternatively, you can download the project as a `.zip` file using the GitHub interface (Code > Download ZIP) and extract it.

### Installing Requirements
It is highly recommended to create a Virtual Environment (`venv`) to keep the dependencies isolated from your system Python.

**On Linux / MacOS:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### Core Libraries and Modules
The tool relies on mathematical and deep learning libraries, including:
- `sentence-transformers`: For cross-lingual LaBSE embeddings.
- `faiss-cpu`: For extremely fast semantic vector search.
- `rapidfuzz`: For precise string and token similarity scoring.
- `pypdf`, `tqdm`, `click`, `pyyaml`.
- Built-in `sqlite3` for local metadata database management.

*Note: The first time you run the tool, it will automatically download the LaBSE embedding model (around 1.8GB).*

---

## Usage

The tool is operated via a Command Line Interface (CLI) using the `src/textreuse/cli.py` module. It features two main operational commands: `index` (to build your textual database) and `run` (to scan for text reuse).

### 1. Building the Vector Index
Before analyzing documents, you need to build a Semantic FAISS index from your reference corpus.

```bash
python -m src.textreuse.cli index --corpus <path_to_corpus> --index_dir <output_dir>
```

**Arguments:**
- `--corpus`: Path to the directory containing your reference texts or a `.jsonl` file. *(Required)*
- `--index_dir`: Directory where the resulting FAISS index and SQLite metadata will be saved. *(Default: `index_data`)*
- `--append`: Include this flag to append new documents to an existing index without overwriting.
- `--prefix`: Assigns a custom prefix for `doc_ids` to better organize multiple corpora.

### 2. Running Cross-Lingual Alignment
Once your index is built, you can use the `run` command to compare your source documents (e.g., in Portuguese) against the indexed multilingual corpus.

```bash
python -m src.textreuse.cli run --pt_dir <path_to_input_files> --out_dir <output_dir> --index_dir <index_dir> --viz
```

**Arguments:**
- `--pt_dir`: Path to the input directory or individual file you want to analyze. Supports `.txt`, `.md`, and `.pdf`. *(Required)*
- `--out_dir`: Output directory where the analysis results and reports will be saved. *(Required)*
- `--index_dir`: Directory pointing to your built FAISS index. *(Default: `index_data`)*
- `--min_score`: Filter results by a minimum match score (0-100). *(Default: 50)*
- `--include_corpora`: A comma-separated list to limit the search to specific languages (e.g., `French,Spanish`).
- `--viz`: A flag that enables the processing and generation of extended interactive alignment visualizations (`HTML` and `SVG`).

---

## Results and Outputs

When the execution completes, MATCHER organizes the text reuse data into several comprehensive formats inside the directory specified by `--out_dir`.

### Data Formats
1. **`results.csv`**
   - A spreadsheet-ready file tracking essential metadata across all scanned files.
   - Columns include: `Source File`, `Match Score`, `Overall Article Score`, `Corpus Document Title`, `Corpus ID`, and chunk offsets.

2. **`results.jsonl` (JSON Lines)**
   - A line-delimited JSON file storing detailed records piece by piece.
   - Ideal for structured data ingestion into databases like ElasticSearch or BigQuery.
   - Contains exact substrings of the `query_chunk` alongside the `source_chunk`.

### Visual Analytics (if `--viz` is used)
3. **Interactive HTML Report (`<filename>_viz_report.html`)**
   - A highly legible side-by-side color-coded report mapping the original text to the top 4 candidate volumes.
   - Hover and review highlights depicting exact text reuse overlaps, scored by confidence tier.
   - Provides summary metrics including **Overall Article Coverage** and **Average Match Similarity**.
   
4. **Alignment SVG (`<filename>_alignment.svg`)**
   - High-fidelity visual vector graphics drawing direct connecting lines between aligned sentences in the queried document and target corpora. Color and opacity define match confidence.

### Supported Multilingual Architecture
When deployed using the default configuration, the `MultiLanguageIndexer` inherently supports partitioned searches spanning diverse languages including:
- French (and French Newspapers)
- English
- Portuguese
- Italian
- Spanish
- German

---

## Reporting Bugs and Suggestions
As a heuristic data mining framework, bugs or unexpected tokenization behavior may occasionally emerge depending on the strictness and encoding format of your input data. 
To ensure continuous improvement, please open an **Issue** on the repository page detailing:
- Your Operating System.
- The command that triggered the error.
- The stack trace or output message.

## How to Cite
If you utilize this tool in your academic research, please cite the repository securely and reference the authors. *(Citation `.cff` and `BibTeX` pending repository publication).*

## Acknowledgments
MATCHER heavily leverages standard state-of-the-art architectures provided by `HuggingFace` and `Meta FAISS`. 

## License
[MIT License](./LICENSE)
Copyright (c) 2024
