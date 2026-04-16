from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.evento_medical import EventoMedicalCreate, EventoMedicalRead
from app.services import evento_medical as service

router = APIRouter(prefix="/eventos", tags=["Eventos Médicos"])


@router.get("/", response_model=list[EventoMedicalRead])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id_evento}", response_model=EventoMedicalRead)
def obtener(id_evento: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_evento)
    if not obj:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return obj


@router.post("/", response_model=EventoMedicalRead, status_code=201)
def crear(data: EventoMedicalCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_evento}", response_model=EventoMedicalRead)
def actualizar(id_evento: int, data: EventoMedicalCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_evento, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return obj


@router.delete("/{id_evento}", status_code=204)
def eliminar(id_evento: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_evento):
        raise HTTPException(status_code=404, detail="Evento no encontrado")
