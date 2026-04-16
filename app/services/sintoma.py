from sqlalchemy.orm import Session

from app.models.sintoma import Sintoma
from app.schemas.sintoma import SintomaCreate


def get(db: Session, id_sintoma: int) -> Sintoma | None:
    return db.get(Sintoma, id_sintoma)


def get_all(db: Session) -> list[Sintoma]:
    return db.query(Sintoma).all()


def create(db: Session, data: SintomaCreate) -> Sintoma:
    obj = Sintoma(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_sintoma: int, data: SintomaCreate) -> Sintoma | None:
    obj = get(db, id_sintoma)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_sintoma: int) -> bool:
    obj = get(db, id_sintoma)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
