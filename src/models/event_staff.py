from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.db.base import Base

class EventStaff(Base):
    __tablename__ = "event_staff"

    event_staff_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.event_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
