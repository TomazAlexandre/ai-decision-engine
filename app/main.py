from fastapi import FastAPI

from app.database.connection import Base, engine
from app.routers import analyze

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Decision Engine")

app.include_router(analyze.router)


@app.get("/")
def root():
    return {"message": "AI Decision Engine running"}