from pathlib import Path

from rag_lab.indexer import build_index
from rag_lab.query import search


BASE_DIR = Path(__file__).resolve().parents[1]


def test_indexer_builds_chunks_for_example_specs() -> None:
    chunks = build_index(BASE_DIR / "examples")

    assert len(chunks) >= 4
    assert any(chunk["operation_id"] == "initiatePayment" for chunk in chunks)
    assert any(chunk["operation_id"] == "retrieveBalances" for chunk in chunks)


def test_query_returns_payment_result() -> None:
    index_path = BASE_DIR / "tmp_test_index.json"
    from rag_lab.indexer import write_index

    write_index(BASE_DIR / "examples", index_path)
    results = search(index_path, "create a payment", limit=3)

    assert results
    assert results[0]["operation_id"] == "initiatePayment"
    index_path.unlink()
