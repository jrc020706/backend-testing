from sqlalchemy.orm import Session
from src.models.event_staff import EventStaff
from src.schemas.event_staff import EventStaffCreate

def create(db: Session, *, obj_in: EventStaffCreate) -> EventStaff:
    db_obj = EventStaff(
        event_id=obj_in.event_id,
        staff_id=obj_in.staff_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_by_event(db: Session, event_id: int):
    return db.query(EventStaff).filter(EventStaff.event_id == event_id).all()
