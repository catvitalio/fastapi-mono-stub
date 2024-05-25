from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from config.security import hasher
from config.settings import settings
from src.common.tasks import send_mail
from src.common.utils import get_or_404
from ....common.services.confirmation_token import ConfirmationTokenService
from ...dtos.auth import ResetPasswordCompleteDto, ResetPasswordDto
from ...models import User


class ResetPasswordService:
    TOKEN_TTL = timedelta(minutes=30)

    def __init__(self, db: AsyncSession) -> None:
        self._db = db
        self._token_service = ConfirmationTokenService(ttl=self.TOKEN_TTL)

    async def reset(self, dto: ResetPasswordDto) -> None:
        user = await get_or_404(self._db, User, email=dto.email)
        token = self._token_service.generate(user.id)

        await send_mail.kiq(
            'Reset password',
            'mail/reset_password.html',
            {'link': f'{settings.FRONTEND_URL}/reset-password?token={token}'},
            [user.email],
        )

    async def complete(self, dto: ResetPasswordCompleteDto) -> None:
        id = self._token_service.decode(dto.token)  # noqa: A001
        user = await get_or_404(self._db, User, id=int(id))
        user.is_active = True
        user.hashed_password = hasher.hash(dto.password)
        await self._db.commit()
