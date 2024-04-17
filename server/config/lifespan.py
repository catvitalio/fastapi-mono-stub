from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.asyncio import ConnectionPool
from starlette.staticfiles import StaticFiles

from .admin import admin
from .routes import api_router
from .settings import settings
from .taskiq import broker


def include_api_router(app: FastAPI) -> None:
    app.include_router(api_router, prefix='/api')


def mount_media(app: FastAPI) -> None:
    app.mount('/media', StaticFiles(directory='media'), name='media')


def mount_admin(app: FastAPI) -> None:
    admin.mount_to(app)


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
    include_api_router(app)
    mount_media(app)
    mount_admin(app)
    await startup_redis(app)
    await startup_taskiq_broker()

    yield

    await shutdown_taskiq_broker()
    await shutdown_redis(app)
