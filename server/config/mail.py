from pathlib import Path

from fastapi_mail import ConnectionConfig, FastMail

from .settings import settings

mail = FastMail(
    ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD.get_secret_value(),
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
        MAIL_STARTTLS=settings.MAIL_STARTTLS,
        MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
        USE_CREDENTIALS=settings.MAIL_USE_CREDENTIALS,
        VALIDATE_CERTS=settings.MAIL_VALIDATE_CERTS,
        TEMPLATE_FOLDER=Path('templates/'),
    ),
)
