from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class EventoMedical(Base):
    __tablename__ = "evento_medical"

    id_evento: Mapped[int] = mapped_column(primary_key=True)
    tipo_evento: Mapped[str] = mapped_column(String(50))
    fecha_hora: Mapped[datetime]
    estado_evento: Mapped[str] = mapped_column(String(30))
    notas: Mapped[str | None] = mapped_column(Text)
    id_medico: Mapped[int | None] = mapped_column(ForeignKey("medico.id_medico"))

    medico: Mapped["Medico | None"] = relationship(back_populates="eventos")
    pacientes: Mapped[list["Paciente"]] = relationship(
        secondary="paciente_evento", back_populates="eventos"
    )
