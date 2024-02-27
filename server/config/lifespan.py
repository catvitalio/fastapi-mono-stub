from contextlib import asynccontextmanager
from typing import Iterable

from fastapi import FastAPI
from sqladmin import Admin, BaseView

from .routes import ADMIN_VIEWS


def startup_admin(app: FastAPI, views: Iterable[type[BaseView]]) -> None:
    from db.session import engine

    admin = Admin(app, engine=engine)
    for view in views:
        admin.add_view(view)


@asynccontextmanager
async def lifespan(app: FastAPI):
    startup_admin(app, ADMIN_VIEWS)
    yield
