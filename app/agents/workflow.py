import time

from app.retrieval.retriever import hybrid_retrieve
from app.core.llm import generate_answer


URGENT_KEYWORDS = [
    "chest pain",
    "difficulty breathing",
    "stroke",
    "severe bleeding",
    "unconscious",
    "emergency"
]


def is_urgent(question: str) -> bool:
    question = question.lower()
    return any(keyword in question for keyword in URGENT_KEYWORDS)


def run_healthcare_agent(question: str) -> dict:
    start = time.time()

    if is_urgent(question):
        return {
            "answer": "This may be urgent. Please contact emergency services or seek immediate medical help.",
            "route": "urgent_safety_route",
            "sources": [],
            "latency_ms": round((time.time() - start) * 1000, 2)
        }

    retrieved = hybrid_retrieve(question)

    context = "\n\n".join([
        f"Source: {item['record']['source']}\n{item['record']['text']}"
        for item in retrieved
    ])

    answer = generate_answer(question, context)

    sources = sorted(list({
        item["record"]["source"]
        for item in retrieved
    }))

    return {
        "answer": answer,
        "route": "healthcare_rag",
        "sources": sources,
        "latency_ms": round((time.time() - start) * 1000, 2)
    }