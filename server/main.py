from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import MIDDLEWARE, api_router, lifespan

app = FastAPI(
    middleware=MIDDLEWARE,
    lifespan=lifespan,
)
app.include_router(api_router, prefix='/api')
app.mount('/media', StaticFiles(directory='media'), name='media')
