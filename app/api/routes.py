from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.workflow import run_healthcare_agent

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    route: str
    sources: list[str]
    latency_ms: float


@router.post("/query", response_model=QueryResponse)
def query(payload: QueryRequest):
    return run_healthcare_agent(payload.question)