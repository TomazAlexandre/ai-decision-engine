from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.decision_engine import make_decision
from app.database.database import SessionLocal
from app.core.security import verify_api_key

router = APIRouter()  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(
    request: AnalyzeRequest,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_key)
):
    return make_decision(request, db)