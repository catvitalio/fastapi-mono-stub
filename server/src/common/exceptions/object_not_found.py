from starlette import status

from .declarative import DeclarativeHTTPException


class ObjectNotFoundException(DeclarativeHTTPException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, object_name: str = 'Object') -> None:
        super().__init__()
        self.detail = f'{object_name} not found'
