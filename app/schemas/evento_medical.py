from datetime import datetime

from pydantic import BaseModel


class EventoMedicalBase(BaseModel):
    tipo_evento: str
    fecha_hora: datetime
    estado_evento: str
    notas: str | None = None
    id_medico: int | None = None


class EventoMedicalCreate(EventoMedicalBase):
    pass


class EventoMedicalRead(EventoMedicalBase):
    id_evento: int

    model_config = {"from_attributes": True}
