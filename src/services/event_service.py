from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemas.event import EventCreate
from src.crud import crud_event

async def create_new_event(event_data: EventCreate, db: Session):
    if event_data.finish_date <= event_data.start_date:
        raise HTTPException(status_code=400, detail="La fecha de fin debe ser posterior al inicio")
    
    # Si todo está bien, llamamos al CRUD para guardar
    return crud_event.create(db, obj_in=event_data)