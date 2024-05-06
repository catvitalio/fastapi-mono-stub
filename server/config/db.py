from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_async_engine(settings.DATABASE_URI.unicode_string())
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)  # type: ignore

test_engine = create_async_engine(
    settings.TEST_DATABASE_URI.unicode_string(),
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
TestSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
    class_=AsyncSession,
)  # type: ignore
