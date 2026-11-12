import inspect
from collections.abc import Callable
from typing import cast

from fastapi import FastAPI
from starlette.types import ASGIApp

from app.core.middleware import response, process_time, cors

MIDDLEWARES = [
    process_time.MIDDLEWARE,
    cors.MIDDLEWARE,
    response.MIDDLEWARE,
]

# 注册所有中间件
def register_middleware(app: FastAPI) -> None:
    for callable_obj, kwargs in MIDDLEWARES:
        if inspect.isclass(callable_obj):
            app.add_middleware(cast(Callable[..., ASGIApp], callable_obj), **kwargs)
        else:
            app.middleware("http")(callable_obj, **kwargs)
