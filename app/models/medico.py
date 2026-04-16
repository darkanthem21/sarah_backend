from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Medico(Base):
    __tablename__ = "medico"

    id_medico: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    especialidad: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str | None] = mapped_column(String(150))
    telefono: Mapped[str | None] = mapped_column(String(20))

    pacientes: Mapped[list["Paciente"]] = relationship(
        secondary="paciente_medico", back_populates="medicos"
    )
    eventos: Mapped[list["EventoMedical"]] = relationship(back_populates="medico")
