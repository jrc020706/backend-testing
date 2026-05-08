from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.core.security import get_password_hash

def get(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_multi(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create(db: Session, *, obj_in: UserCreate) -> User:
    db_obj = User(
        name=obj_in.name,
        email=obj_in.email,
        password_hash=get_password_hash(obj_in.password),
        telephone=obj_in.telephone,
        role_id=obj_in.role_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, *, db_obj: User, obj_in: UserUpdate) -> User:
    update_data = obj_in.model_dump(exclude_unset=True)
    for field in update_data:
        setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
