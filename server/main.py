from fastapi import FastAPI

from config import lifespan
from config.middleware import MIDDLEWARE

app = FastAPI(lifespan=lifespan)

for middleware_class, kwargs in MIDDLEWARE:
    app.add_middleware(middleware_class, **kwargs)
