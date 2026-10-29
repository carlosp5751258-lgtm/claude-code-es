# CLAUDE.md — Proyecto Python

## Entorno
- Gestor: `uv` (alternativa: `pip install -e ".[dev]"`)
- Ejecutar: `uv run python -m paquete`
- Tests: `uv run pytest -q` (uno: `uv run pytest tests/test_x.py::test_y`)
- Formato y lint: `uv run ruff format . && uv run ruff check --fix .`
- Tipos: `uv run mypy src/`

## Convenciones
- Type hints en toda función pública.
- `pathlib` en vez de `os.path`.
- Logging con `logging.getLogger(__name__)`, nunca `print` en código de librería.
- Docstrings estilo Google, en español.

## Flujo
1. Escribe o ajusta el test primero.
2. Implementa.
3. `ruff` + `mypy` + `pytest` antes de dar la tarea por terminada.

## No hacer
- No usar `except:` sin tipo.
- No commitear `.env` ni datos de `data/raw/`.
