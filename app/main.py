from fastapi import FastAPI
from app.routers import analyze


app = FastAPI(title="AI Decision Engine", description="API for analyzing text data", version="1.0.0" )

app.include_router(analyze.router)


@app.get("/")
def root():
    return {"message": "AI Decision Engine Running!"}

