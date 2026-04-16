from datetime import date
from decimal import Decimal

from sqlalchemy import CheckConstraint, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class EstadoDiario(Base):
    __tablename__ = "estado_diario"
    __table_args__ = (
        CheckConstraint("adherencia BETWEEN 0 AND 1", name="ck_estado_adherencia"),
        CheckConstraint("animo BETWEEN 1 AND 5", name="ck_estado_animo"),
        CheckConstraint("motivacion BETWEEN 1 AND 5", name="ck_estado_motivacion"),
        CheckConstraint(
            "alerta_riesgo_tratamiento BETWEEN 1 AND 5",
            name="ck_estado_alerta_tratamiento",
        ),
        CheckConstraint(
            "alerta_riesgo_abandono BETWEEN 1 AND 5",
            name="ck_estado_alerta_abandono",
        ),
    )

    id_estado: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[date]
    adherencia: Mapped[Decimal | None] = mapped_column(Numeric(3, 2))
    peso: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    tamano: Mapped[str | None]
    animo: Mapped[int | None]
    motivacion: Mapped[int | None]
    alerta_riesgo_tratamiento: Mapped[int | None]
    alerta_riesgo_abandono: Mapped[int | None]
    imc: Mapped[Decimal | None] = mapped_column(Numeric(4, 2))
    id_paciente: Mapped[int | None] = mapped_column(ForeignKey("paciente.id_paciente"))

    paciente: Mapped["Paciente | None"] = relationship(back_populates="estados_diarios")
    sintomas: Mapped[list["Sintoma"]] = relationship(
        secondary="estado_sintoma", back_populates="estados_diarios"
    )
