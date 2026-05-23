import json
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from app.core.config import INDEX_PATH, EMBEDDING_MODEL


_model = None


def get_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)

    return _model


def load_index() -> list[dict]:
    path = Path(INDEX_PATH)

    if not path.exists():
        raise FileNotFoundError("Index not found. Run python scripts/ingest.py first.")

    return json.loads(path.read_text(encoding="utf-8"))


def dense_search(query: str, records: list[dict], top_k: int = 5):
    model = get_model()

    query_embedding = model.encode([query], normalize_embeddings=True)[0]
    document_embeddings = np.array([record["embedding"] for record in records])

    scores = document_embeddings @ query_embedding
    ranked_indices = np.argsort(scores)[::-1][:top_k]

    return [(records[i], float(scores[i])) for i in ranked_indices]


def sparse_search(query: str, records: list[dict], top_k: int = 5):
    corpus = [record["text"].lower().split() for record in records]
    bm25 = BM25Okapi(corpus)

    scores = bm25.get_scores(query.lower().split())
    ranked_indices = np.argsort(scores)[::-1][:top_k]

    return [(records[i], float(scores[i])) for i in ranked_indices]


def hybrid_retrieve(query: str, top_k: int = 4):
    records = load_index()

    dense_results = dense_search(query, records, top_k)
    sparse_results = sparse_search(query, records, top_k)

    merged = {}

    for record, score in dense_results:
        merged[record["id"]] = {
            "record": record,
            "score": score,
            "type": "dense"
        }

    for record, score in sparse_results:
        if record["id"] in merged:
            merged[record["id"]]["score"] += score
            merged[record["id"]]["type"] = "dense+sparse"
        else:
            merged[record["id"]] = {
                "record": record,
                "score": score,
                "type": "sparse"
            }

    results = list(merged.values())
    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:top_k]