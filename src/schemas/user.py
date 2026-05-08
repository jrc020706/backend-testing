from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    telephone: Optional[str] = None
    role_id: int

class UserCreate(UserBase):
    password: str # En una app real, esto se hashea antes de guardar

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    role_id: Optional[int] = None
    is_active: Optional[bool] = None

class User(UserBase):
    user_id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
