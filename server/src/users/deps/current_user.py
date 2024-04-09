from fastapi import Depends, Security
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import jwt_security
from src.common.deps.db import get_db
from ..models.user import User


async def get_current_user(
    credentials: JwtAuthorizationCredentials = Security(jwt_security),
    db: AsyncSession = Depends(get_db),
) -> User:
    return await db.get(User, credentials.subject['id'])  # type: ignore
