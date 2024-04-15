from datetime import datetime, timedelta
from typing import TypeAlias
from uuid import UUID

from jose import JWTError, jwt
from jose.constants import ALGORITHMS

from config.settings import settings
from ..exceptions.confirmation_token import InvalidTokenException

ID: TypeAlias = str | int | UUID


class ConfirmationTokenService:
    def __init__(self, ttl: timedelta) -> None:
        self._ttl = ttl

    def generate(self, id: ID) -> str:  # noqa: A002
        return jwt.encode({'sub': str(id), 'exp': datetime.now() + self._ttl}, *self.jwt_args)

    def decode(self, token: str) -> ID:
        try:
            return jwt.decode(token, *self.jwt_args)['sub']
        except (JWTError, KeyError):
            raise InvalidTokenException

    @property
    def jwt_args(self) -> tuple:
        return (
            settings.SECRET_KEY.get_secret_value(),
            ALGORITHMS.HS256,
        )
