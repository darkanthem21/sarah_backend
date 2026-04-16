from datetime import datetime

from pydantic import BaseModel


class InteraccionBase(BaseModel):
    fecha_hora: datetime
    emisor: str
    tipo_mensaje: str
    contenido: str | None = None
    feedback_paciente: str | None = None
    id_paciente: int | None = None


class InteraccionCreate(InteraccionBase):
    pass


class InteraccionRead(InteraccionBase):
    id_interaccion: int

    model_config = {"from_attributes": True}
