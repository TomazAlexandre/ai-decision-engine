import json
from app.services.ai_service import analyze_with_ai


def make_decision(data: dict) -> dict:
    """
    Calls the AI service, parses the response, and returns
    a normalized decision payload.
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
        except (TypeError, ValueError):
            raise ValueError(f"Invalid confidence value returned by AI: {confidence}")

        if confidence < 0 or confidence > 1:
            raise ValueError(f"Confidence out of range: {confidence}")

        return {
            "decision": decision,
            "confidence": confidence,
            "source": "ai"
        }

    except Exception as e:
        return {
            "decision": "ERROR",
            "confidence": 0,
            "source": "fallback",
            "error": str(e)
        }