.PHONY: dev debug db-migrate db-upgrade db-downgrade

dev:
	uv run --package web-service fastapi dev apps/web-service/app/main.py --port 8080

debug:
	uv run --package web-service fastapi run apps/web-service/app/main.py --port 8000

db-migrate:
	uv run --package web-service alembic -c apps/web-service/alembic.ini revision --autogenerate -m "$(message)"

db-upgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini upgrade head

db-downgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini downgrade $(version)