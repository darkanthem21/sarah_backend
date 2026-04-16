from fastapi import FastAPI

from app.routers import (
    estado_diario,
    evento_medical,
    interaccion,
    medico,
    paciente,
    preferencias,
    red_apoyo,
    sintoma,
)

app = FastAPI(title="Sarah Backend")

app.include_router(red_apoyo.router)
app.include_router(medico.router)
app.include_router(sintoma.router)
app.include_router(paciente.router)
app.include_router(evento_medical.router)
app.include_router(estado_diario.router)
app.include_router(interaccion.router)
app.include_router(preferencias.router)


@app.get("/health")
def health():
    return {"status": "ok"}
