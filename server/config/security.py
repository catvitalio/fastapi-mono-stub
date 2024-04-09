from fastapi_jwt import JwtAccessBearer
from passlib.context import CryptContext

from .settings import settings

jwt_security = JwtAccessBearer(secret_key=settings.SECRET_KEY.get_secret_value())
hasher = CryptContext(schemes=['bcrypt'], deprecated='auto')
