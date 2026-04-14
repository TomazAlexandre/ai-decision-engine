import json

from sqlalchemy.orm import Session

from app.database.models import DecisionLog
from app.services.ai_service import analyze_with_ai


def make_decision(data: dict, db: Session) -> dict:
    """
    Calls the AI service, validates the response, stores the decision,
    and returns a normalized payload.
    """
    try:
        ai_raw = analyze_with_ai(data)
        parsed = json.loads(ai_raw)

        decision = parsed.get("decision", "ERROR")
        confidence = parsed.get("confidence", 0)

        if decision not in ["APPROVE", "REJECT"]:
            raise ValueError(f"Invalid decision returned by AI: {decision}")

        try:
            confidence = float(confidence)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid confidence value returned by AI: {confidence}") from exc

        if confidence < 0 or confidence > 1:
            raise ValueError(f"Confidence out of range: {confidence}")

        result = {
            "decision": decision,
            "confidence": confidence,
            "source": "ai",
            "input": data,
        }

    except Exception as e:
        result = {
            "decision": "ERROR",
            "confidence": 0,
            "source": "fallback",
            "input": data,
            "error": str(e),
        }

    log = DecisionLog(
        input_data=json.dumps(data, ensure_ascii=False),
        decision=result["decision"],
        confidence=result["confidence"],
        source=result["source"],
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    result["id"] = log.id
    result["created_at"] = log.created_at.isoformat()

    return result