from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.paciente import PacienteCreate, PacienteRead
from app.services import paciente as service

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])


@router.get("/", response_model=list[PacienteRead])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id_paciente}", response_model=PacienteRead)
def obtener(id_paciente: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_paciente)
    if not obj:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return obj


@router.post("/", response_model=PacienteRead, status_code=201)
def crear(data: PacienteCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_paciente}", response_model=PacienteRead)
def actualizar(id_paciente: int, data: PacienteCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_paciente, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return obj


@router.delete("/{id_paciente}", status_code=204)
def eliminar(id_paciente: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_paciente):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
