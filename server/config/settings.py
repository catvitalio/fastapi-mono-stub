from pydantic import EmailStr, Field, PostgresDsn, RedisDsn, SecretStr
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: PostgresDsn
    TEST_DATABASE_URI: MultiHostUrl = 'sqlite+aiosqlite:///:memory:'  # type: ignore
    REDIS_URI: RedisDsn

    SECRET_KEY: SecretStr

    MAIL_USERNAME: EmailStr = 'example@mail.com'
    MAIL_PASSWORD: SecretStr = Field('')
    MAIL_SERVER: str = 'mail.com'
    MAIL_PORT: int = 587
    MAIL_FROM: EmailStr = 'example@mail.com'
    MAIL_FROM_NAME: str = 'example'
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    MAIL_USE_CREDENTIALS: bool = True
    MAIL_VALIDATE_CERTS: bool = True

    FRONTEND_URL: str = 'http://localhost:3000'
    BACKEND_URL: str = 'http://localhost:8000'

    CORS_ALLOW_ORIGINS: list[str] = ['http://localhost', FRONTEND_URL]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ['*']
    CORS_ALLOW_HEADERS: list[str] = ['*']


settings = Settings()  # type: ignore
