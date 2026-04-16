from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Interaccion(Base):
    __tablename__ = "interaccion"

    id_interaccion: Mapped[int] = mapped_column(primary_key=True)
    fecha_hora: Mapped[datetime]
    emisor: Mapped[str] = mapped_column(String(50))
    tipo_mensaje: Mapped[str] = mapped_column(String(50))
    contenido: Mapped[str | None] = mapped_column(Text)
    feedback_paciente: Mapped[str | None] = mapped_column(Text)
    id_paciente: Mapped[int | None] = mapped_column(ForeignKey("paciente.id_paciente"))

    paciente: Mapped["Paciente | None"] = relationship(back_populates="interacciones")
