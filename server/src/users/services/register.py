from src.common.deps import get_db
from src.common.tasks import send_mail
from ..dtos.auth import RegisterCompleteDto, RegisterDto


class RegisterService:
    def __init__(self) -> None:
        self._db = get_db()

    async def register(self, dto: RegisterDto.Input) -> RegisterDto.Output:
        await send_mail.kiq(
            'Registration',
            'mail/register.html',
            {
                'link': 'link',
            },
            [dto.email],
        )
        return RegisterDto.Output(id=1)

    async def complete(self, dto: RegisterCompleteDto.Input) -> RegisterCompleteDto.Output:
        return RegisterCompleteDto.Output(id=1)
