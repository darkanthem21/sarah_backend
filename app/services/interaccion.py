from sqlalchemy.orm import Session

from app.models.interaccion import Interaccion
from app.schemas.interaccion import InteraccionCreate


def get(db: Session, id_interaccion: int) -> Interaccion | None:
    return db.get(Interaccion, id_interaccion)


def get_all(db: Session) -> list[Interaccion]:
    return db.query(Interaccion).all()


def get_by_paciente(db: Session, id_paciente: int) -> list[Interaccion]:
    return db.query(Interaccion).filter(Interaccion.id_paciente == id_paciente).all()


def create(db: Session, data: InteraccionCreate) -> Interaccion:
    obj = Interaccion(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_interaccion: int) -> bool:
    obj = get(db, id_interaccion)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
