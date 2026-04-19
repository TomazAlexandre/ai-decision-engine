from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.decision_engine import make_decision
from app.database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest, db: Session = Depends(get_db)):
    return make_decision(request, db)