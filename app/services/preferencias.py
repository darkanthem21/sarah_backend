from sqlalchemy.orm import Session

from app.models.preferencias import Preferencias
from app.schemas.preferencias import PreferenciasCreate


def get(db: Session, id_preferencia: int) -> Preferencias | None:
    return db.get(Preferencias, id_preferencia)


def get_by_paciente(db: Session, id_paciente: int) -> list[Preferencias]:
    return db.query(Preferencias).filter(Preferencias.id_paciente == id_paciente).all()


def create(db: Session, data: PreferenciasCreate) -> Preferencias:
    obj = Preferencias(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_preferencia: int, data: PreferenciasCreate) -> Preferencias | None:
    obj = get(db, id_preferencia)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_preferencia: int) -> bool:
    obj = get(db, id_preferencia)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
