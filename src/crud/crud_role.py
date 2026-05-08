from sqlalchemy.orm import Session
from src.models.role import Role
from src.schemas.role import RoleCreate

def create(db: Session, *, obj_in: RoleCreate) -> Role:
    db_obj = Role(name=obj_in.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_multi(db: Session):
    return db.query(Role).all()
