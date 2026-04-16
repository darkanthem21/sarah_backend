from datetime import date
from decimal import Decimal

from pydantic import BaseModel, EmailStr


class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    rut: str
    fecha_nacimiento: date
    sexo: str
    tamano_actual: str | None = None
    ficha_clinica: str | None = None
    email: EmailStr | None = None
    telefono: str | None = None
    peso_actual: Decimal | None = None
    id_apoyo: int | None = None


class PacienteCreate(PacienteBase):
    pass


class PacienteRead(PacienteBase):
    id_paciente: int

    model_config = {"from_attributes": True}
