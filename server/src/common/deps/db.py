from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from config.db import async_sessionmaker


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:  # type: ignore
        yield session
