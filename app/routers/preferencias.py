from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.preferencias import PreferenciasCreate, PreferenciasRead
from app.services import preferencias as service

router = APIRouter(prefix="/preferencias", tags=["Preferencias"])


@router.get("/paciente/{id_paciente}", response_model=list[PreferenciasRead])
def listar_por_paciente(id_paciente: int, db: Session = Depends(get_db)):
    return service.get_by_paciente(db, id_paciente)


@router.get("/{id_preferencia}", response_model=PreferenciasRead)
def obtener(id_preferencia: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_preferencia)
    if not obj:
        raise HTTPException(status_code=404, detail="Preferencia no encontrada")
    return obj


@router.post("/", response_model=PreferenciasRead, status_code=201)
def crear(data: PreferenciasCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_preferencia}", response_model=PreferenciasRead)
def actualizar(id_preferencia: int, data: PreferenciasCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_preferencia, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Preferencia no encontrada")
    return obj


@router.delete("/{id_preferencia}", status_code=204)
def eliminar(id_preferencia: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_preferencia):
        raise HTTPException(status_code=404, detail="Preferencia no encontrada")
