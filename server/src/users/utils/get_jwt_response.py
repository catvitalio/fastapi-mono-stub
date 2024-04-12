from fastapi import Response
from starlette import status

from config.security import access_security, refresh_security
from .create_jwt_tokens import create_jwt_tokens


def get_jwt_response(user_id: int | None) -> Response:
    response = Response(status_code=status.HTTP_204_NO_CONTENT)
    access_token, refresh_token = create_jwt_tokens(user_id)
    access_security.set_access_cookie(response, access_token if user_id else '')
    refresh_security.set_refresh_cookie(response, refresh_token if user_id else '')
    return response
