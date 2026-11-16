.PHONY: dev debug test test-unit test-integration test-e2e test-smoke db-migrate db-upgrade db-downgrade

# 启动服务
dev:
	uv run --package web-service fastapi dev apps/web-service/app/main.py --port 8080

debug:
	uv run --package web-service fastapi run apps/web-service/app/main.py --port 8000

test:
	uv run pytest apps/web-service/test/unit/ apps/web-service/test/integration/ -q --cov=app --cov-report=term-missing --cov-fail-under=80

test-unit:
	uv run pytest apps/web-service/test/unit/ -q

test-integration:
	uv run pytest apps/web-service/test/integration/ -q

test-e2e:
	uv run pytest apps/web-service/test/e2e/ -v

test-smoke:
	uv run pytest apps/web-service/test/unit/ apps/web-service/test/integration/ apps/web-service/test/e2e/ -q -m smoke

# 生成迁移脚本
db-migrate:
	uv run --package web-service alembic -c apps/web-service/alembic.ini revision --autogenerate -m "$(message)"

# 执行迁移
db-upgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini upgrade head

# 执行回滚
db-downgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini downgrade $(version)