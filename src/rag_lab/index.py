from __future__ import annotations

import argparse

from rag_lab.indexer import write_index


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a local JSON index from OpenAPI specs.")
    parser.add_argument("spec_directory")
    parser.add_argument("--output", default="rag_index.json")
    args = parser.parse_args()
    write_index(args.spec_directory, args.output)
    print(f"Wrote index to {args.output}")


if __name__ == "__main__":
    main()
