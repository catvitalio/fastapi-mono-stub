from typing import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from config.db import TestSession, test_engine
from src.common.models import Base


async def test_get_db():
    async with TestSession() as session:  # type: ignore
        yield session


async def create_tables() -> None:
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def db() -> AsyncGenerator[AsyncSession, None]:
    await create_tables()
    db: AsyncSession = TestSession()  # type: ignore
    try:
        yield db
    finally:
        await db.close()
