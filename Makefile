UV = uv run

check: lint format-check typecheck test

lint:
	$(UV) ruff check .

format-check:
	$(UV) ruff format --check .

typecheck:
	$(UV) mypy --strict src tests

test:
	$(UV) pytest -q

fix:
	$(UV) ruff check . --fix
	$(UV) ruff format .
	$(UV) pytest

.PHONY: check lint format-check typecheck test fix
