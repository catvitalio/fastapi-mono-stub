from typing import AsyncGenerator

import pytest_asyncio
from fastapi.testclient import TestClient

from config. import fastapi
from src.common.deps import get_db
from .db import create_tables, test_get_db


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    await create_tables()
    fastapi.dependency_overrides[get_db] = test_get_db
    with TestClient(fastapi) as client:
        yield client
