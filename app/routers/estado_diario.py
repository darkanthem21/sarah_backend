from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.estado_diario import EstadoDiarioCreate, EstadoDiarioRead
from app.services import estado_diario as service

router = APIRouter(prefix="/estados-diarios", tags=["Estados Diarios"])


@router.get("/", response_model=list[EstadoDiarioRead])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/paciente/{id_paciente}", response_model=list[EstadoDiarioRead])
def listar_por_paciente(id_paciente: int, db: Session = Depends(get_db)):
    return service.get_by_paciente(db, id_paciente)


@router.get("/{id_estado}", response_model=EstadoDiarioRead)
def obtener(id_estado: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_estado)
    if not obj:
        raise HTTPException(status_code=404, detail="Estado diario no encontrado")
    return obj


@router.post("/", response_model=EstadoDiarioRead, status_code=201)
def crear(data: EstadoDiarioCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_estado}", response_model=EstadoDiarioRead)
def actualizar(id_estado: int, data: EstadoDiarioCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_estado, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Estado diario no encontrado")
    return obj


@router.delete("/{id_estado}", status_code=204)
def eliminar(id_estado: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_estado):
        raise HTTPException(status_code=404, detail="Estado diario no encontrado")
