from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    decision: str
    confidence: float
    source: str