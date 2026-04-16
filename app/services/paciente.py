from sqlalchemy.orm import Session

from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate


def get(db: Session, id_paciente: int) -> Paciente | None:
    return db.get(Paciente, id_paciente)


def get_all(db: Session) -> list[Paciente]:
    return db.query(Paciente).all()


def create(db: Session, data: PacienteCreate) -> Paciente:
    obj = Paciente(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id_paciente: int, data: PacienteCreate) -> Paciente | None:
    obj = get(db, id_paciente)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, id_paciente: int) -> bool:
    obj = get(db, id_paciente)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
