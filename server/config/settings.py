from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URI: PostgresDsn

    SECRET_KEY: SecretStr
    ACCESS_EXPIRE_MINUTES: int = 15
    REFRESH_EXPIRE_MINUTES: int = 60 * 24 * 30
    SECURE_HASH_ALGORITHM: str = 'HS256'


settings = Settings()  # type: ignore
