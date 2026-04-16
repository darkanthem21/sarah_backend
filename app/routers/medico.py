from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.medico import MedicoCreate, MedicoRead
from app.services import medico as service

router = APIRouter(prefix="/medicos", tags=["Médicos"])


@router.get("/", response_model=list[MedicoRead])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id_medico}", response_model=MedicoRead)
def obtener(id_medico: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_medico)
    if not obj:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return obj


@router.post("/", response_model=MedicoRead, status_code=201)
def crear(data: MedicoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_medico}", response_model=MedicoRead)
def actualizar(id_medico: int, data: MedicoCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_medico, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return obj


@router.delete("/{id_medico}", status_code=204)
def eliminar(id_medico: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_medico):
        raise HTTPException(status_code=404, detail="Médico no encontrado")
