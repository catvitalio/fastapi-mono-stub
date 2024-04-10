from fastapi import Response
from starlette.status import HTTP_204_NO_CONTENT

from config.security import access_security, refresh_security


def get_jwt_response(user_id: int) -> Response:
    response = Response(status_code=HTTP_204_NO_CONTENT)
    access_token = access_security.create_access_token({'id': user_id})
    refresh_token = refresh_security.create_refresh_token({'id': user_id})
    access_security.set_access_cookie(response, access_token)
    refresh_security.set_refresh_cookie(response, refresh_token)
    return response
