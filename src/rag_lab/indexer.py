from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import yaml


def build_index(spec_directory: str | Path) -> List[Dict[str, str]]:
    directory = Path(spec_directory)
    chunks: List[Dict[str, str]] = []

    for path in sorted(directory.glob("*.ya*ml")):
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))
        title = spec.get("info", {}).get("title", path.stem)
        for endpoint, methods in spec.get("paths", {}).items():
            for method, operation in methods.items():
                operation_id = operation.get("operationId", f"{method}_{endpoint}")
                summary = operation.get("summary") or operation.get("description", "")
                text = " ".join(
                    [
                        title,
                        endpoint,
                        method.upper(),
                        operation_id,
                        summary,
                        json.dumps(operation.get("requestBody", {}), sort_keys=True),
                        json.dumps(operation.get("responses", {}), sort_keys=True),
                    ]
                )
                chunks.append(
                    {
                        "document": path.name,
                        "title": title,
                        "operation_id": operation_id,
                        "endpoint": endpoint,
                        "method": method.upper(),
                        "text": text,
                    }
                )

    return chunks


def write_index(spec_directory: str | Path, output_path: str | Path) -> None:
    chunks = build_index(spec_directory)
    Path(output_path).write_text(json.dumps(chunks, indent=2), encoding="utf-8")
