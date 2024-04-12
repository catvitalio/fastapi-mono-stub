from config.security import access_security, refresh_security


def create_jwt_tokens(user_id: int) -> tuple[str, str]:
    access_token = access_security.create_access_token({'id': user_id})
    refresh_token = refresh_security.create_refresh_token({'id': user_id})
    return access_token, refresh_token
