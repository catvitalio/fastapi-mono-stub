from starlette import status

from .declarative import DeclarativeHTTPException


class ConfirmationTokenException(DeclarativeHTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Confirmation token error'


class InvalidTokenException(ConfirmationTokenException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Invalid confirmation token'
