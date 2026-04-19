from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    user: str
    value: float

class AnalyzeResponse(BaseModel):
    decision: str
    confidence: float
    source: str