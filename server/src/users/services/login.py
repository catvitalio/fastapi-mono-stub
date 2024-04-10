from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import hasher
from ..dtos import LoginDto
from ..models import User


class LoginService:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def login(self, dto: LoginDto) -> User:
        user = await self._get_user(dto.email)
        if not user or not hasher.verify(dto.password, user.hashed_password):
            raise HTTPException(status_code=401, detail='Invalid credentials')

        return user

    async def _get_user(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email, User.is_active == True)
        users = await self._db.execute(stmt)
        return users.scalar_one_or_none()
