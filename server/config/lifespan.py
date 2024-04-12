from contextlib import asynccontextmanager
from typing import Iterable

from fastapi import FastAPI
from redis.asyncio import ConnectionPool
from sqladmin import Admin, BaseView

from src.users.services.admin_auth import AdminAuthService
from .db import engine
from .routes import ADMIN_VIEWS
from .settings import settings
from .taskiq import broker


def startup_admin(app: FastAPI, views: Iterable[type[BaseView]]) -> None:
    admin = Admin(app, engine=engine, authentication_backend=AdminAuthService(settings.SECRET_KEY))
    for view in views:
        admin.add_view(view)


async def startup_taskiq_broker() -> None:
    if not broker.is_worker_process:
        await broker.startup()


async def shutdown_taskiq_broker() -> None:
    if not broker.is_worker_process:
        await broker.shutdown()


async def startup_redis(app: FastAPI) -> None:
    app.state.redis_pool = ConnectionPool.from_url(settings.REDIS_URI.unicode_string())


async def shutdown_redis(app: FastAPI) -> None:
    app.state.redis_pool.disconnect()


@asynccontextmanager
async def lifespan(app: FastAPI):
    startup_admin(app, ADMIN_VIEWS)
    await startup_redis(app)
    await startup_taskiq_broker()
    yield
    await shutdown_taskiq_broker()
    await shutdown_redis(app)
