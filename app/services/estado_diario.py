from sqlalchemy.orm import Session

from app.models.estado_diario import EstadoDiario
from app.schemas.estado_diario import EstadoDiarioCreate


def get(db: Session, id_estado: int) -> EstadoDiario | None:
    return db.get(EstadoDiario, id_estado)


def get_all(db: Session) -> list[EstadoDiario]:
    return db.query(EstadoDiario).all()


def get_by_paciente(db: Session, id_paciente: int) -> list[EstadoDiario]:
    return db.query(EstadoDiario).filter(EstadoDiario.id_paciente == id_paciente).all()


def create(db: Session, data: EstadoDiarioCreate) -> EstadoDiario:
    obj = EstadoDiario(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_estado: int, data: EstadoDiarioCreate) -> EstadoDiario | None:
    obj = get(db, id_estado)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_estado: int) -> bool:
    obj = get(db, id_estado)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
