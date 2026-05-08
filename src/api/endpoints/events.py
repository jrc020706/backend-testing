from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from typing import List
from src.db.session import get_db
from src.schemas import event as event_schemas
from src.schemas import event_staff as es_schemas
from src.services.event_service import create_new_event
from src.crud import crud_event_staff
from src.api.deps import get_current_user
from src.models.user import User

router = APIRouter()

@router.post("/", response_model=event_schemas.Event)
async def create_event(
    event_in: event_schemas.EventCreate, 
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user)
):
    # Asignamos el ID del usuario logueado al campo created_by
    event_in.created_by = current_user.user_id
    return await create_new_event(event_in, db)

# Nueva funcionalidad: Asignar Staff a un Evento
@router.post("/assign-staff", response_model=es_schemas.EventStaff)
def assign_staff_to_event(
    assignment: es_schemas.EventStaffCreate, 
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user)
):
    return crud_event_staff.create(db, obj_in=assignment)

# Nueva funcionalidad: Listar Staff de un Evento
@router.get("/{event_id}/staff", response_model=List[es_schemas.EventStaff])
def read_event_staff(
    event_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user)
):
    return crud_event_staff.get_by_event(db, event_id=event_id)