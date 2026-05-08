from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from src.db.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.role_id"), nullable=False)
    name = Column(String(65), nullable=False)
    email = Column(String(55), unique=True, index=True, nullable=False)
    telephone = Column(String(15))
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
