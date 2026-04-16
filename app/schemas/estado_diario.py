from datetime import date
from decimal import Decimal

from pydantic import BaseModel, field_validator


class EstadoDiarioBase(BaseModel):
    fecha: date
    adherencia: Decimal | None = None
    peso: Decimal | None = None
    tamano: str | None = None
    animo: int | None = None
    motivacion: int | None = None
    alerta_riesgo_tratamiento: int | None = None
    alerta_riesgo_abandono: int | None = None
    imc: Decimal | None = None
    id_paciente: int | None = None

    @field_validator("animo", "motivacion", "alerta_riesgo_tratamiento", "alerta_riesgo_abandono")
    @classmethod
    def rango_1_5(cls, v: int | None) -> int | None:
        if v is not None and not (1 <= v <= 5):
            raise ValueError("el valor debe estar entre 1 y 5")
        return v

    @field_validator("adherencia")
    @classmethod
    def rango_adherencia(cls, v: Decimal | None) -> Decimal | None:
        if v is not None and not (0 <= v <= 1):
            raise ValueError("adherencia debe estar entre 0 y 1")
        return v


class EstadoDiarioCreate(EstadoDiarioBase):
    pass


class EstadoDiarioRead(EstadoDiarioBase):
    id_estado: int

    model_config = {"from_attributes": True}
