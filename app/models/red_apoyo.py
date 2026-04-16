from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class RedApoyo(Base):
    __tablename__ = "red_apoyo"

    id_apoyo: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    rut: Mapped[str | None] = mapped_column(String(12), unique=True)
    relacion: Mapped[str] = mapped_column(String(50))
    email: Mapped[str | None] = mapped_column(String(150))
    telefono: Mapped[str | None] = mapped_column(String(20))

    pacientes: Mapped[list["Paciente"]] = relationship(back_populates="red_apoyo")
