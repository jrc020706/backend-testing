from sqlalchemy import Column, Integer, String
from src.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
