from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .lifespan import lifespan
from .settings import settings

fastapi = FastAPI(lifespan=lifespan)

fastapi.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)
