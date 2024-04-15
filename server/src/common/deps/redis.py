from fastapi import Request
from redis.asyncio import ConnectionPool
from taskiq import TaskiqDepends


async def get_redis(request: Request = TaskiqDepends()) -> ConnectionPool:
    return request.app.state.redis_pool
