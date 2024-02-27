from fastapi import FastAPI

from config import lifespan, routes

app = FastAPI(
    routes=routes,
    lifespan=lifespan,
)
