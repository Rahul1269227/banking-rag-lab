from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Dict, List


def search(index_path: str | Path, query: str, limit: int = 5) -> List[Dict[str, object]]:
    chunks = json.loads(Path(index_path).read_text(encoding="utf-8"))
    query_terms = _tokenize(query)
    ranked = []

    for chunk in chunks:
        text_terms = _tokenize(chunk["text"])
        overlap = sum((query_terms & text_terms).values())
        if overlap:
            ranked.append(
                {
                    "score": overlap,
                    "document": chunk["document"],
                    "operation_id": chunk["operation_id"],
                    "endpoint": chunk["endpoint"],
                    "method": chunk["method"],
                    "title": chunk["title"],
                }
            )

    return sorted(ranked, key=lambda item: item["score"], reverse=True)[:limit]


def _tokenize(text: str) -> Counter:
    tokens = [token.strip(".,:/{}[]()").lower() for token in text.split()]
    return Counter(token for token in tokens if token)


def main() -> None:
    parser = argparse.ArgumentParser(description="Search a local JSON RAG index.")
    parser.add_argument("index_path")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    print(json.dumps(search(args.index_path, args.query, args.limit), indent=2))


if __name__ == "__main__":
    main()
