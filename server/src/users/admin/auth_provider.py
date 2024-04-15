from sqlalchemy import select
from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminUser, AuthProvider
from starlette_admin.exceptions import LoginFailed

from src.common.deps.db import get_db
from ..dtos.auth import LoginDto
from ..exceptions.auth import AuthException, InvalidCredentialsException
from ..models.user import User
from ..services import LoginService


class EmailAndPasswordProvider(AuthProvider):
    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        db = await anext(get_db())
        login_service = LoginService(db)

        try:
            user = await login_service.login(LoginDto(email=username, password=password))
            if not user.is_admin:
                raise InvalidCredentialsException
        except AuthException:
            raise LoginFailed('Invalid username or password')

        request.session.update({'username': user.email})
        return response

    async def is_authenticated(self, request) -> bool:
        db = await anext(get_db())
        result = await db.execute(
            select(User).where(
                User.email == request.session.get('username', None),
                User.is_admin == True,
                User.is_active == True,
            ),
        )
        user = result.scalar_one_or_none()

        if request.session.get('username', None) == getattr(user, 'email', ''):
            request.state.user = user
            return True

        return False

    def get_admin_user(self, request: Request) -> AdminUser:
        user = request.state.user
        return AdminUser(username=user.email, photo_url=None)

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response
