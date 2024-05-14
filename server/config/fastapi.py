from fastapi import FastAPI

from .lifespan import lifespan
from .middleware import MIDDLEWARE

fastapi = FastAPI(lifespan=lifespan)

for middleware_class, kwargs in MIDDLEWARE:
    fastapi.add_middleware(middleware_class, **kwargs)
