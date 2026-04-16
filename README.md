# Sarah — Backend 

Backend para almacenamiento de datos del asistente clínico conversacional **Sarah**, diseñado para mejorar la adherencia a tratamientos farmacológicos para la obesidad.

## Contexto

La baja adherencia a tratamientos es un problema crítico entre consultas médicas. Los pacientes suelen abandonar debido a efectos secundarios, dudas, falta de seguimiento y pérdida de motivación.

**Sarah** acompaña al paciente diariamente, detecta señales tempranas de riesgo de abandono y entrega información estructurada al equipo médico para facilitar intervenciones oportunas.

## Stack

| Capa | Tecnología |
|---|---|
| Lenguaje | Python 3.12+ |
| Framework | FastAPI |
| Base de datos | PostgreSQL 16 |
| ORM / Migraciones | SQLAlchemy + Alembic |
| Gestión de entorno | UV |
| Linting / Formato | Ruff |
| Contenedores | Docker + Docker Compose |

## Estructura del proyecto

```
app/
├── main.py          # Instancia FastAPI y registro de routers
├── core/
│   ├── config.py    # Settings cargados desde .env via pydantic-settings
│   └── database.py  # Engine, SessionLocal, Base y dependencia get_db
├── models/          # Modelos ORM de SQLAlchemy (un archivo por dominio)
├── schemas/         # Schemas Pydantic para request/response
├── routers/         # Handlers agrupados por dominio
└── services/        # Lógica de negocio, llamada desde los routers
tests/               # Tests con pytest
```

### Requisitos previos

- [UV](https://docs.astral.sh/uv/)
- Docker y Docker Compose

### Variables de entorno

```bash
cp .env.example .env
# Editar .env con los valores correspondientes
```

### Desarrollo local

```bash
# Instalar dependencias
uv sync

# Levantar la base de datos
docker compose up db -d

# Correr el servidor en modo desarrollo (hot-reload)
uv run fastapi dev app/main.py
```

La API queda disponible en `http://localhost:8000`.  
Documentación interactiva: `http://localhost:8000/docs`.

### Stack completo con Docker

```bash
docker compose up --build
```

Para detener y eliminar el volumen de PostgreSQL:

```bash
docker compose down -v
```

## Comandos útiles

```bash
# Linting
uv run ruff check .

# Formateo
uv run ruff format .

# Tests
uv run pytest

# Test específico
uv run pytest tests/path/test_file.py::test_name
```

## Migraciones de base de datos

Las migraciones se gestionan con Alembic. Los modelos heredan de `Base` definida en `app/core/database.py`.

```bash
# Crear una nueva migración
uv run alembic revision --autogenerate -m "descripción"

# Aplicar migraciones
uv run alembic upgrade head
```

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/health` | Health check de la API |

> La documentación completa de la API está disponible en `/docs` (Swagger UI) y `/redoc`.
