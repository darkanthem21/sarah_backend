from sqlalchemy.orm import Session

from app.models.red_apoyo import RedApoyo
from app.schemas.red_apoyo import RedApoyoCreate


def get(db: Session, id_apoyo: int) -> RedApoyo | None:
    return db.get(RedApoyo, id_apoyo)


def get_all(db: Session) -> list[RedApoyo]:
    return db.query(RedApoyo).all()


def create(db: Session, data: RedApoyoCreate) -> RedApoyo:
    obj = RedApoyo(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_apoyo: int, data: RedApoyoCreate) -> RedApoyo | None:
    obj = get(db, id_apoyo)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_apoyo: int) -> bool:
    obj = get(db, id_apoyo)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
