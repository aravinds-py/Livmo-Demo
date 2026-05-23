import mlflow

from app.core.config import MLFLOW_TRACKING_URI

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("healthcare-rag-agent")


def log_run(question: str, answer: str, route: str, latency_ms: float, sources: list[str]):
    with mlflow.start_run():
        mlflow.log_param("route", route)
        mlflow.log_metric("latency_ms", latency_ms)
        mlflow.log_metric("num_sources", len(sources))

        mlflow.log_text(question, "question.txt")
        mlflow.log_text(answer, "answer.txt")
        mlflow.log_text("\n".join(sources), "sources.txt")