from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.sintoma import SintomaCreate, SintomaRead
from app.services import sintoma as service

router = APIRouter(prefix="/sintomas", tags=["Síntomas"])


@router.get("/", response_model=list[SintomaRead])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id_sintoma}", response_model=SintomaRead)
def obtener(id_sintoma: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_sintoma)
    if not obj:
        raise HTTPException(status_code=404, detail="Síntoma no encontrado")
    return obj


@router.post("/", response_model=SintomaRead, status_code=201)
def crear(data: SintomaCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_sintoma}", response_model=SintomaRead)
def actualizar(id_sintoma: int, data: SintomaCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_sintoma, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Síntoma no encontrado")
    return obj


@router.delete("/{id_sintoma}", status_code=204)
def eliminar(id_sintoma: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_sintoma):
        raise HTTPException(status_code=404, detail="Síntoma no encontrado")
