from typing import AsyncGenerator

import pytest_asyncio
from fastapi.testclient import TestClient

from main import app
from src.common.deps import get_db
from .db import create_tables, test_get_db


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    await create_tables()
    app.dependency_overrides[get_db] = test_get_db
    with TestClient(app) as client:
        yield client
