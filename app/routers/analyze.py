from fastapi import APIRouter
from app.services.decision_engine import make_decision

router = APIRouter()


@router.post("/analyze")
def analyze(data: dict):
    result = make_decision(data)
    return result

