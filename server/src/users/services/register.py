from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.settings import settings
from src.common.services import ConfirmationTokenService
from src.common.tasks import send_mail
from ..dtos import RegisterCompleteDto, RegisterDto
from ..models import User


class RegisterService:
    TOKEN_TTL = timedelta(days=365)

    def __init__(self, db: AsyncSession) -> None:
        self._db = db
        self._token_service = ConfirmationTokenService(ttl=self.TOKEN_TTL)

    async def register(self, dto: RegisterDto) -> None:
        await self._validate_user(dto)
        user = await self._create_user(dto)
        await self._send_mail(user)

    async def _validate_user(self, dto: RegisterDto) -> None:
        user = await self._get_user(dto.email, is_active=True)
        if user:
            raise HTTPException(status_code=400, detail='User with this email already exists')

    async def _create_user(self, dto: RegisterDto) -> User:
        user = await self._get_user(dto.email, is_active=False)
        if not user:
            user = User(
                email=dto.email,
                hashed_password=hasher.hash(dto.password),
                first_name=dto.first_name,
                last_name=dto.last_name,
                is_active=False,
            )
            self._db.add(user)
            await self._db.commit()
            await self._db.refresh(user)

        return user

    async def _get_user(self, email: str, *, is_active: bool) -> User | None:
        stmt = select(User).where(User.email == email, User.is_active == is_active)
        users = await self._db.execute(stmt)
        return users.scalar_one_or_none()

    async def _send_mail(self, user: User) -> None:
        token = self._token_service.generate(user.id)
        await send_mail.kiq(
            'Registration',
            'mail/register.html',
            {'link': f'{settings.FRONTEND_URL}/confirm?token={token}'},
            [user.email],
        )

    async def complete(self, dto: RegisterCompleteDto) -> User:
        id = self._token_service.decode(dto.token)  # noqa: A001
        user = await self._db.get(User, int(id))

        if not user:
            raise HTTPException(status_code=401, detail='Invalid token')
        elif user.is_active:
            raise HTTPException(status_code=400, detail='User already active')

        user.is_active = True
        await self._db.commit()

        return user
