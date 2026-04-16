from datetime import date
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Paciente(Base):
    __tablename__ = "paciente"

    id_paciente: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    rut: Mapped[str] = mapped_column(String(12), unique=True)
    fecha_nacimiento: Mapped[date]
    sexo: Mapped[str] = mapped_column(String(10))
    tamano_actual: Mapped[str | None] = mapped_column(String(10))
    ficha_clinica: Mapped[str | None]
    email: Mapped[str | None] = mapped_column(String(150))
    telefono: Mapped[str | None] = mapped_column(String(20))
    peso_actual: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    id_apoyo: Mapped[int | None] = mapped_column(ForeignKey("red_apoyo.id_apoyo"))

    red_apoyo: Mapped["RedApoyo | None"] = relationship(back_populates="pacientes")
    medicos: Mapped[list["Medico"]] = relationship(
        secondary="paciente_medico", back_populates="pacientes"
    )
    eventos: Mapped[list["EventoMedical"]] = relationship(
        secondary="paciente_evento", back_populates="pacientes"
    )
    estados_diarios: Mapped[list["EstadoDiario"]] = relationship(back_populates="paciente")
    interacciones: Mapped[list["Interaccion"]] = relationship(back_populates="paciente")
    preferencias: Mapped[list["Preferencias"]] = relationship(back_populates="paciente")
