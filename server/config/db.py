from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..src.common.utils import find_models
from .settings import settings

engine = create_async_engine(settings.DATABASE_URI.unicode_string())

Session: type[AsyncSession] = sessionmaker(
    engine,  # type: ignore
    expire_on_commit=False,
    class_=AsyncSession,
)

test_engine = create_async_engine(
    settings.TEST_DATABASE_URI.unicode_string(),
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)

TestSession: type[AsyncSession] = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,  # type: ignore
    class_=AsyncSession,
)

find_models()
