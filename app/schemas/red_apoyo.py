from pydantic import BaseModel, EmailStr


class RedApoyoBase(BaseModel):
    nombre: str
    apellido: str
    rut: str | None = None
    relacion: str
    email: EmailStr | None = None
    telefono: str | None = None


class RedApoyoCreate(RedApoyoBase):
    pass


class RedApoyoRead(RedApoyoBase):
    id_apoyo: int

    model_config = {"from_attributes": True}
