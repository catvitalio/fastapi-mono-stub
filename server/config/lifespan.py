from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.asyncio import ConnectionPool

from .settings import settings
from .taskiq import broker


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
    await startup_redis(app)
    await startup_taskiq_broker()
    yield
    await shutdown_taskiq_broker()
    await shutdown_redis(app)
