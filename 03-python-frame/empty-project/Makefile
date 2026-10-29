.PHONY: dev debug db-migrate db-upgrade db-downgrade

# 启动服务
dev:
	uv run --package web-service fastapi dev apps/web-service/app/main.py --port 8080

debug:
	uv run --package web-service fastapi run apps/web-service/app/main.py --port 8000

# 生成迁移脚本
db-migrate:
	uv run --package web-service alembic -c apps/web-service/alembic.ini revision --autogenerate -m "$(message)"

# 执行迁移
db-upgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini upgrade head

# 执行回滚
db-downgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini downgrade $(version)