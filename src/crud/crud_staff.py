from sqlalchemy.orm import Session
from src.models.staff import Staff
from src.schemas.staff import StaffCreate

def get(db: Session, staff_id: int):
    return db.query(Staff).filter(Staff.staff_id == staff_id).first()

def get_multi(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Staff).offset(skip).limit(limit).all()

def create(db: Session, *, obj_in: StaffCreate) -> Staff:
    db_obj = Staff(
        name=obj_in.name,
        category=obj_in.category,
        email=obj_in.email,
        telephone=obj_in.telephone,
        description=obj_in.description
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
