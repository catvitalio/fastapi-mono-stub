from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_async_engine(settings.POSTGRES_URI.unicode_string())
async_sessionmaker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)  # type: ignore
