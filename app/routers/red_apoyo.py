from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.red_apoyo import RedApoyoCreate, RedApoyoRead
from app.services import red_apoyo as service

router = APIRouter(prefix="/red-apoyo", tags=["Red de Apoyo"])


@router.get("/", response_model=list[RedApoyoRead])
def listar(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id_apoyo}", response_model=RedApoyoRead)
def obtener(id_apoyo: int, db: Session = Depends(get_db)):
    obj = service.get(db, id_apoyo)
    if not obj:
        raise HTTPException(status_code=404, detail="Red de apoyo no encontrada")
    return obj


@router.post("/", response_model=RedApoyoRead, status_code=201)
def crear(data: RedApoyoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.put("/{id_apoyo}", response_model=RedApoyoRead)
def actualizar(id_apoyo: int, data: RedApoyoCreate, db: Session = Depends(get_db)):
    obj = service.update(db, id_apoyo, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Red de apoyo no encontrada")
    return obj


@router.delete("/{id_apoyo}", status_code=204)
def eliminar(id_apoyo: int, db: Session = Depends(get_db)):
    if not service.delete(db, id_apoyo):
        raise HTTPException(status_code=404, detail="Red de apoyo no encontrada")
