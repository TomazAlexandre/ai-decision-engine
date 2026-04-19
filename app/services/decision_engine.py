from sqlalchemy.orm import Session
from app.database.models import Decision

def make_decision(data, db: Session):
    try:
        if data.value > 100:
            decision = "APPROVED"
            confidence = 0.9
            source = "rule"
        else:
            decision = "REJECTED"
            confidence = 0.6
            source = "rule"

        db_decision = Decision(
            user=data.user,
            value=data.value,
            decision=decision,
            confidence=confidence,
            source=source
        )

        db.add(db_decision)
        db.commit()
        db.refresh(db_decision)

        return {
            "decision": decision,
            "confidence": confidence,
            "source": source
        }

    except Exception:
        return {
            "decision": "ERROR",
            "confidence": 0.0,
            "source": "fallback"
        }