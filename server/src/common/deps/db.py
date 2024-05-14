from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from config.db import Session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session
