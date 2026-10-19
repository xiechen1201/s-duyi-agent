# apps/web-service/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.core.config import web_settings, common_settings

app = FastAPI(
    title=web_settings.app_name,
    docs_url=None if common_settings.environment == "production" else "/docs",
    redoc_url=None if common_settings.environment == "production" else "/redoc",
    openapi_url=(
        None if common_settings.environment == "production" else "/openapi.json"
    ),
)


from app.api.webcome import router as webcome_router
from app.api.items import router as items_router

app.include_router(webcome_router)
app.include_router(items_router, prefix="/items")
