from fastapi import FastAPI
from app.routers import analyze

app = FastAPI(title="AI Decision Engine")

app.include_router(analyze.router)


@app.get("/")
def root():
    return {"message": "AI Decision Engine running"}