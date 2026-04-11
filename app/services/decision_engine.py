from app.services.ai_service import analyze_with_ai

def make_decision(data: dict):
    print(f"[DECISION] Input: {data}")

    value = data.get("value", 0)

    try:
        # IA
        ai_raw = analyze_with_ai(data)

        # MOCK 
        if value >= 70:
            return {
                "decision": "APPROVE",
                "confidence": 0.9,
                "source": "rule_based"
            }
        else:
            return {
                "decision": "REJECT",
                "confidence": 0.6,
                "source": "rule_based"
            }

    except Exception as e:
        print(f"[ERROR] AI failed: {e}")

        return {
            "decision": "ERROR",
            "confidence": 0.0,
            "source": "fallback"
        }