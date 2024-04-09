from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import hasher, jwt_security
from ..dtos import AuthDto, JwtDto
from ..models import User


class AuthService:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def auth(self, dto: AuthDto) -> JwtDto:
        user = await self._get_user(dto.email)
        if not user or not hasher.verify(dto.password, user.hashed_password):
            raise HTTPException(status_code=401, detail='Invalid credentials')

        return JwtDto(
            access_token=jwt_security.create_access_token({'id': user.id}),
            refresh_token=jwt_security.create_refresh_token({'id': user.id}),
        )

    async def _get_user(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email, User.is_active == True)
        users = await self._db.execute(stmt)
        return users.scalar_one_or_none()
