from sqlalchemy import Column, ForeignKey, Integer, Table

from app.core.database import Base

paciente_medico = Table(
    "paciente_medico",
    Base.metadata,
    Column("id_paciente", Integer, ForeignKey("paciente.id_paciente"), primary_key=True),
    Column("id_medico", Integer, ForeignKey("medico.id_medico"), primary_key=True),
)

paciente_evento = Table(
    "paciente_evento",
    Base.metadata,
    Column("id_paciente", Integer, ForeignKey("paciente.id_paciente"), primary_key=True),
    Column("id_evento", Integer, ForeignKey("evento_medical.id_evento"), primary_key=True),
)

estado_sintoma = Table(
    "estado_sintoma",
    Base.metadata,
    Column("id_estado", Integer, ForeignKey("estado_diario.id_estado"), primary_key=True),
    Column("id_sintoma", Integer, ForeignKey("sintoma.id_sintoma"), primary_key=True),
)
