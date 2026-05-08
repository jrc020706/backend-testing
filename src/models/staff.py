from sqlalchemy import Column, Integer, String, Text
from src.db.base import Base

class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(45))
    email = Column(String(65), unique=True, index=True)
    telephone = Column(String(15))
    description = Column(Text) # Interpretado como TEXT a pesar del BIGINT en DER
