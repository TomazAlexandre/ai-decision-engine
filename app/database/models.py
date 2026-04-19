from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.database import Base

class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    value = Column(Float)
    decision = Column(String)
    confidence = Column(Float)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)