from datetime import datetime

from pydantic import BaseModel


class PreferenciasBase(BaseModel):
    tipo_preferencia: str
    valor: str | None = None
    fecha_actualizacion: datetime | None = None
    id_paciente: int | None = None


class PreferenciasCreate(PreferenciasBase):
    pass


class PreferenciasRead(PreferenciasBase):
    id_preferencia: int

    model_config = {"from_attributes": True}
