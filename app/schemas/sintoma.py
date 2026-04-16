from pydantic import BaseModel, field_validator


class SintomaBase(BaseModel):
    nombre_sintoma: str
    severidad: int | None = None
    notas: str | None = None

    @field_validator("severidad")
    @classmethod
    def severidad_rango(cls, v: int | None) -> int | None:
        if v is not None and v not in (1, 2, 3):
            raise ValueError("severidad debe estar entre 1 y 3")
        return v


class SintomaCreate(SintomaBase):
    pass


class SintomaRead(SintomaBase):
    id_sintoma: int

    model_config = {"from_attributes": True}
