# Banking RAG Lab

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

Minimal public-safe retrieval project for indexing OpenAPI specs and querying them with local keyword-based search.

## Features

- Reads OpenAPI YAML files from a directory
- Builds lightweight operation-level chunks
- Writes a portable JSON index
- Retrieves matching operations for natural-language queries

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m rag_lab.index examples --output rag_index.json
PYTHONPATH=src python -m rag_lab.query rag_index.json "How do I create a payment?"
```

## Run Tests

```bash
PYTHONPATH=src python3 -m pytest -q
```

## Demo

This repo is designed as a lightweight retrieval demo. Build a JSON index from the sample specs, run a query such as `"How do I create a payment?"`, and review the ranked operation matches.

## Project Layout

- `src/rag_lab`: indexing and query modules
- `examples/`: neutral sample OpenAPI documents
- `tests/`: unit tests for indexing and retrieval

## Safety

- Uses only dummy sample specs
- Does not call external APIs
- Does not require a vector database or credentials

## March 2026 Refresh

- Public-safe packaging reviewed
- Retrieval flow re-validated
- Repository metadata and documentation polished
