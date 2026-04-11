from fastapi import APIRouter
from app.schemas.request import AnalyzeRequest
from app.schemas.response import AnalyzeResponse
from app.services.decision_engine import make_decision

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: AnalyzeRequest):
    result = make_decision(data.model_dump())
    return result