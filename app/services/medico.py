from sqlalchemy.orm import Session

from app.models.medico import Medico
from app.schemas.medico import MedicoCreate


def get(db: Session, id_medico: int) -> Medico | None:
    return db.get(Medico, id_medico)


def get_all(db: Session) -> list[Medico]:
    return db.query(Medico).all()


def create(db: Session, data: MedicoCreate) -> Medico:
    obj = Medico(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_medico: int, data: MedicoCreate) -> Medico | None:
    obj = get(db, id_medico)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_medico: int) -> bool:
    obj = get(db, id_medico)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
