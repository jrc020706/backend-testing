from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.db.session import get_db
from src.schemas import role as schemas
from src.crud import crud_role

router = APIRouter()

@router.post("/", response_model=schemas.Role)
def create_role(role_in: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud_role.create(db, obj_in=role_in)

@router.get("/", response_model=List[schemas.Role])
def read_roles(db: Session = Depends(get_db)):
    return crud_role.get_multi(db)
