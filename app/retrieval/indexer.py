import json
from pathlib import Path
from sentence_transformers import SentenceTransformer

from app.core.config import DOCS_PATH, INDEX_PATH, EMBEDDING_MODEL
from app.retrieval.chunking import load_documents, chunk_text


def build_index() -> dict:
    model = SentenceTransformer(EMBEDDING_MODEL)

    documents = load_documents(DOCS_PATH)
    records = []

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for i, chunk in enumerate(chunks):
            records.append({
                "id": f"{doc['source']}_{i}",
                "source": doc["source"],
                "text": chunk
            })

    if not records:
        raise ValueError("No documents found in data/healthcare_docs")

    embeddings = model.encode(
        [record["text"] for record in records],
        normalize_embeddings=True
    )

    for record, embedding in zip(records, embeddings):
        record["embedding"] = embedding.tolist()

    Path(INDEX_PATH).parent.mkdir(parents=True, exist_ok=True)
    Path(INDEX_PATH).write_text(json.dumps(records, indent=2), encoding="utf-8")

    return {
        "documents_loaded": len(documents),
        "chunks_indexed": len(records),
        "index_path": INDEX_PATH
    }