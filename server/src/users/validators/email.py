from fastapi import Depends
from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.deps import get_db
from ..models.user import User


async def check_email_existance(email: str, db: AsyncSession = Depends(get_db)) -> str:
    stmt = select(exists(User).where(User.email == email))
    is_exists = await db.execute(stmt)
    assert not is_exists, 'Email already exists'

    return email
