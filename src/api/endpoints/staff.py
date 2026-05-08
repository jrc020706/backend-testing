from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from typing import List
from src.db.session import get_db
from src.schemas import staff as schemas
from src.crud import crud_staff
from src.api.deps import get_current_user
from src.models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Staff)
def create_staff(
    staff_in: schemas.StaffCreate, 
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user)
):
    return crud_staff.create(db, obj_in=staff_in)

@router.get("/", response_model=List[schemas.Staff])
def read_staff(
    db: Session = Depends(get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: User = Security(get_current_user)
):
    return crud_staff.get_multi(db, skip=skip, limit=limit)

@router.get("/{staff_id}", response_model=schemas.Staff)
def read_staff_member(staff_id: int, db: Session = Depends(get_db)):
    staff = crud_staff.get(db, staff_id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return staff
