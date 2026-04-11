import json
from app.services.ai_service import analyze_with_ai

def make_decision(data: dict):
    try:
        ai_raw = analyze_with_ai(data)

        # regra simples mock
        value = data.get("value", 0)

        if value >= 70:
            return {
                "decision": "APPROVE",
                "confidence": 0.9,
                "source": "mock"
            }
        else:
            return {
                "decision": "REJECT",
                "confidence": 0.6,
                "source": "mock"
            }

    except Exception as e:
        return {
            "decision": "ERROR",
            "confidence": 0,
            "error": str(e)
        }

# -def make_decision(data: dict):
#    ai_raw = analyze_with_ai(data)
#
#    try:
#        ai_response = json.loads(ai_raw)
#    except:
#        ai_response = {
#            "decision": "ERROR",
#            "confidence": 0,
#            "raw": ai_raw
#        }
#
#    return ai_response -###
