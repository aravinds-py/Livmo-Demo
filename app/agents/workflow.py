import time

from app.retrieval.retriever import hybrid_retrieve
from app.core.llm import generate_answer
from app.evaluation.tracking import log_run


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
        latency_ms = round((time.time() - start) * 1000, 2)

        answer = "This may be urgent. Please contact emergency services or seek immediate medical help."

        log_run(
            question=question,
            answer=answer,
            route="urgent_safety_route",
            latency_ms=latency_ms,
            sources=[]
        )

        return {
            "answer": answer,
            "route": "urgent_safety_route",
            "sources": [],
            "latency_ms": latency_ms
        }

    retrieved = hybrid_retrieve(question)

    context = "\n\n".join([
        f"Source: {item['record']['source']}\n{item['record']['text']}"
        for item in retrieved
    ])

    sources = sorted(list({
        item["record"]["source"]
        for item in retrieved
    }))

    answer = generate_answer(question, context)

    latency_ms = round((time.time() - start) * 1000, 2)

    log_run(
        question=question,
        answer=answer,
        route="healthcare_rag",
        latency_ms=latency_ms,
        sources=sources
    )

    return {
        "answer": answer,
        "route": "healthcare_rag",
        "sources": sources,
        "latency_ms": latency_ms
    }