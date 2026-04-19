from app.core.security import verify_api_key
from fastapi import Depends

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(
    request: AnalyzeRequest,
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_key) 
):
    return make_decision(request, db)