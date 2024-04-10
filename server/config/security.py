from fastapi_jwt import (
    JwtAccessBearerCookie,
    JwtRefreshBearerCookie,
)
from passlib.context import CryptContext

from .settings import settings

access_security = JwtAccessBearerCookie(secret_key=settings.SECRET_KEY.get_secret_value())
refresh_security = JwtRefreshBearerCookie(secret_key=settings.SECRET_KEY.get_secret_value())
hasher = CryptContext(schemes=['bcrypt'], deprecated='auto')
