from sqlalchemy.orm import Session

from app.models.evento_medical import EventoMedical
from app.schemas.evento_medical import EventoMedicalCreate


def get(db: Session, id_evento: int) -> EventoMedical | None:
    return db.get(EventoMedical, id_evento)


def get_all(db: Session) -> list[EventoMedical]:
    return db.query(EventoMedical).all()


def create(db: Session, data: EventoMedicalCreate) -> EventoMedical:
    obj = EventoMedical(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_evento: int, data: EventoMedicalCreate) -> EventoMedical | None:
    obj = get(db, id_evento)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_evento: int) -> bool:
    obj = get(db, id_evento)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
