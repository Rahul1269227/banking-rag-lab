# Dummy Banking RAG Lab

Safe sample retrieval project for indexing OpenAPI specs and answering simple questions over them with local keyword search.

## What It Does

- Parses dummy OpenAPI specs
- Builds lightweight text chunks
- Stores a local JSON index
- Retrieves top matching chunks for a query

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m rag_lab.index examples --output rag_index.json
PYTHONPATH=src python -m rag_lab.query rag_index.json \"How do I create a payment?\"
```

## Notes

- No vector database is required
- No external APIs are called
- Only dummy example specs are included
