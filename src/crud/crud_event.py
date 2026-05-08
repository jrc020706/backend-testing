from sqlalchemy.orm import Session
from src.models.event import Event
from src.schemas.event import EventCreate

def create(db: Session, *, obj_in: EventCreate) -> Event:
    db_obj = Event(
        event_name=obj_in.event_name,
        description=obj_in.description,
        location=obj_in.location,
        start_date=obj_in.start_date,
        finish_date=obj_in.finish_date,
        created_by=obj_in.created_by
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Puedes agregar más funciones como get, update, delete
