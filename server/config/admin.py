from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin import I18nConfig
from starlette_admin.contrib.sqla import Admin

from config.db import engine
from config.settings import settings
from src.users.admin import EmailAndPasswordProvider, UserView

admin = Admin(
    engine,
    title='FastAPI Admin',
    i18n_config=I18nConfig(default_locale='ru'),
    auth_provider=EmailAndPasswordProvider(),
    middlewares=[
        Middleware(
            SessionMiddleware,
            secret_key=settings.SECRET_KEY.get_secret_value(),
        ),
    ],
)
admin.add_view(UserView(UserView.model, icon='fa fa-user'))
