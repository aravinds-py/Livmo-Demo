from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Healthcare RAG Agent",
    description="Healthcare-focused RAG assistant using hybrid retrieval and FastAPI.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Healthcare RAG Agent is running"
    }