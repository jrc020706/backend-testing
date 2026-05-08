from pydantic import BaseModel
from datetime import datetime

class EventStaffBase(BaseModel):
    event_id: int
    staff_id: int

class EventStaffCreate(EventStaffBase):
    pass

class EventStaff(EventStaffBase):
    event_staff_id: int
    created_at: datetime

    class Config:
        from_attributes = True
