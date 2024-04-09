from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.user import User


async def is_email_exists(email: str, db: AsyncSession) -> bool:
    stmt = select(exists(User).where(User.email == email))
    is_exists = (await db.execute(stmt)).scalar()
    return bool(is_exists)
