from datetime import timedelta

from fastapi_jwt import JwtAccessBearerCookie, JwtRefreshBearerCookie
from passlib.context import CryptContext

from .settings import settings

access_security = JwtAccessBearerCookie(
    secret_key=settings.SECRET_KEY.get_secret_value(),
    access_expires_delta=timedelta(minutes=30),
    refresh_expires_delta=timedelta(days=30),
)
refresh_security: JwtRefreshBearerCookie = JwtRefreshBearerCookie.from_other(  # type: ignore
    access_security,
)

hasher = CryptContext(schemes=['bcrypt'], deprecated='auto')
