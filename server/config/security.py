from fastapi_jwt import JwtAccessBearer

from .settings import settings

jwt_security = JwtAccessBearer(secret_key=settings.SECRET_KEY.get_secret_value())
