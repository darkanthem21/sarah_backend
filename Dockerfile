FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install uv && uv sync --no-dev

COPY app/ app/

CMD ["uv", "run", "fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
