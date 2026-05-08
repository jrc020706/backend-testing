from pydantic import BaseModel, EmailStr
from typing import Optional

class StaffBase(BaseModel):
    name: str
    category: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    description: Optional[str] = None

class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    staff_id: int

    class Config:
        from_attributes = True
