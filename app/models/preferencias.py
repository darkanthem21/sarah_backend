from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Preferencias(Base):
    __tablename__ = "preferencias"

    id_preferencia: Mapped[int] = mapped_column(primary_key=True)
    tipo_preferencia: Mapped[str] = mapped_column(String(50))
    valor: Mapped[str | None] = mapped_column(String(200))
    fecha_actualizacion: Mapped[datetime | None]
    id_paciente: Mapped[int | None] = mapped_column(ForeignKey("paciente.id_paciente"))

    paciente: Mapped["Paciente | None"] = relationship(back_populates="preferencias")
