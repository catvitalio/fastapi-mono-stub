from fastapi import FastAPI

from config import MIDDLEWARE, ROUTES, lifespan

app = FastAPI(
    routes=ROUTES,
    middleware=MIDDLEWARE,
    lifespan=lifespan,
)
