from fastapi import FastAPI
from app.routers import analyze

from app.database.database import engine, Base
from app.database import models  # 👈 IMPORTANTE

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(analyze.router)