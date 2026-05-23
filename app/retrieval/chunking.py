from pathlib import Path


def load_documents(folder_path: str) -> list[dict]:
    documents = []

    for file_path in Path(folder_path).glob("*.txt"):
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        documents.append({
            "source": file_path.name,
            "text": text
        })

    return documents


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 80) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks