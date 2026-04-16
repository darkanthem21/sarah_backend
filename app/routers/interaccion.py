from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.interaccion import InteraccionCreate, InteraccionRead
from app.services import interaccion as service

router = APIRouter(prefix="/interacciones", tags=["Interacciones"])


@router.get("/paciente/{id_paciente}", response_model=list[InteraccionRead])
def listar_por_paciente(id_paciente: int, db: Session = Depends(get_db)):
    return service.get_by_paciente(db, id_paciente)


@router.get("/{id_interaccion}", response_model=InteraccionRead)
def obtener(id_interaccion: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_interaccion)
    if not obj:
        raise HTTPException(status_code=404, detail="Interacción no encontrada")
    return obj


@router.post("/", response_model=InteraccionRead, status_code=201)
def crear(data: InteraccionCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.delete("/{id_interaccion}", status_code=204)
def eliminar(id_interaccion: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_interaccion):
        raise HTTPException(status_code=404, detail="Interacción no encontrada")
