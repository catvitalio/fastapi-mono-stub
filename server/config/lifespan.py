from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin, BaseView

from db.session import engine
from .routes import admin_views


def startup_admin(app: FastAPI, views: list[type[BaseView]]) -> None:
    admin = Admin(app, engine=engine)
    for view in views:
        admin.add_view(view)


@asynccontextmanager
async def lifespan(app: FastAPI):
    startup_admin(app, admin_views)
    yield
