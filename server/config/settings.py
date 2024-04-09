from pydantic import EmailStr, Field, PostgresDsn, RedisDsn, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URI: PostgresDsn
    REDIS_URI: RedisDsn

    SECRET_KEY: SecretStr
    ACCESS_EXPIRE_MINUTES: int = 15
    REFRESH_EXPIRE_MINUTES: int = 60 * 24 * 30
    SECURE_HASH_ALGORITHM: str = 'HS256'

    MAIL_USERNAME: EmailStr = 'example@mail.com'
    MAIL_PASSWORD: SecretStr = Field('')
    MAIL_SERVER: str = 'mail.com'
    MAIL_PORT: int = 587
    MAIL_FROM: EmailStr = 'example@mail.com'
    MAIL_FROM_NAME: str = 'example'
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = True
    MAIL_USE_CREDENTIALS: bool = True
    MAIL_VALIDATE_CERTS: bool = True

    FRONTEND_URL: str = 'http://localhost:3000'
    BACKEND_URL: str = 'http://localhost:8000'


settings = Settings()  # type: ignore
