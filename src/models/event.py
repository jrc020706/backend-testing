from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from src.db.base import Base
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True)
    created_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    event_name = Column(String(60), index=True, nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(45))
    start_date = Column(DateTime)
    finish_date = Column(DateTime)
