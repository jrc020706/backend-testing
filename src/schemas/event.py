from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    event_name: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    finish_date: Optional[datetime] = None
    created_by: Optional[int] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    event_id: int

    class Config:
        from_attributes = True