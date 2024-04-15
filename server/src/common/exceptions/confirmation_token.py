from fastapi import HTTPException
from starlette import status


class ConfirmationTokenException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str = 'Confirmation token error',
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)


class InvalidTokenException(ConfirmationTokenException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
