from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from app.database.connection import Base


class DecisionLog(Base):
    __tablename__ = "decision_logs"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(Text, nullable=False)
    decision = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    source = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)