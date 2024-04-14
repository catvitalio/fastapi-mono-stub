from fastapi import HTTPException
from fastapi_jwt import (
    JwtAccessBearerCookie,
    JwtAuthorizationCredentials,
    JwtRefreshBearerCookie,
)
from jose import JWTError, jwt
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from config.security import access_security, refresh_security
from ...common.deps.db import get_db
from ..deps import get_current_user
from ..dtos.auth import LoginDto
from ..models.user import User
from ..utils import create_jwt_tokens
from .login import LoginService


class AdminAuthService(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form['username'], form['password']
        db = await anext(get_db())
        login_service = LoginService(db)
        try:
            user = await login_service.login(LoginDto(email=email, password=password))
        except HTTPException:
            return False

        if not user.is_admin:
            return False

        access_token, refresh_token = create_jwt_tokens(user.id)
        request.session.update({'access_token': access_token, 'refresh_token': refresh_token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        access_token = request.session.get('access_token')
        refresh_token = request.cookies.get('refresh_token')

        user = await self._authenticate_by_token(access_token, access_security)
        if not user:
            user = await self._authenticate_by_token(refresh_token, refresh_security)

        if user:
            access_token, refresh_token = create_jwt_tokens(user.id)
            request.session.update({'access_token': access_token, 'refresh_token': refresh_token})

        return bool(user)

    async def _authenticate_by_token(
        self,
        token: str | None,
        security: JwtAccessBearerCookie | JwtRefreshBearerCookie,
    ) -> User | None:
        if not token:
            return None

        try:
            decoded_jwt = jwt.decode(
                token,
                security.secret_key,
                algorithms=[security.algorithm],
            )
        except JWTError:
            return None

        db = await anext(get_db())

        user = await get_current_user(
            JwtAuthorizationCredentials(decoded_jwt['subject'], decoded_jwt['jti']),
            db,
        )

        return user if user.is_admin else None
