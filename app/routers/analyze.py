import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import DecisionLog
from app.services.decision_engine import make_decision

router = APIRouter()


@router.post("/analyze")
def analyze(data: dict, db: Session = Depends(get_db)):
    return make_decision(data, db)


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    logs = db.query(DecisionLog).order_by(DecisionLog.id.desc()).all()

    history = []
    for log in logs:
        history.append({
            "id": log.id,
            "input_data": json.loads(log.input_data),
            "decision": log.decision,
            "confidence": log.confidence,
            "source": log.source,
            "created_at": log.created_at.isoformat(),
        })

    return history