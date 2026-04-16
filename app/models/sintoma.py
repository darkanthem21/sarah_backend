from sqlalchemy import CheckConstraint, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Sintoma(Base):
    __tablename__ = "sintoma"

    id_sintoma: Mapped[int] = mapped_column(primary_key=True)
    nombre_sintoma: Mapped[str] = mapped_column(String(100))
    severidad: Mapped[int | None] = mapped_column(
        CheckConstraint("severidad BETWEEN 1 AND 3", name="ck_sintoma_severidad")
    )
    notas: Mapped[str | None] = mapped_column(Text)

    estados_diarios: Mapped[list["EstadoDiario"]] = relationship(
        secondary="estado_sintoma", back_populates="sintomas"
    )
