from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    value: int = Field(..., ge=0, le=100)
    user: str