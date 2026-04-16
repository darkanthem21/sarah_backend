from pydantic import BaseModel, EmailStr


class MedicoBase(BaseModel):
    nombre: str
    apellido: str
    especialidad: str | None = None
    email: EmailStr | None = None
    telefono: str | None = None


class MedicoCreate(MedicoBase):
    pass


class MedicoRead(MedicoBase):
    id_medico: int

    model_config = {"from_attributes": True}
