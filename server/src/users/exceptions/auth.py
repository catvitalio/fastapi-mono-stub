from starlette import status

from src.common.exceptions import DeclarativeHTTPException


class AuthException(DeclarativeHTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Authentication error'


class InvalidCredentialsException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Invalid credentials'


class UserWithThisEmailAlreadyExistsException(AuthException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'User with this email already exists'


class UserAlreadyActiveException(AuthException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'User already active'
