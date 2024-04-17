from typing import Sequence

from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import _MiddlewareClass

from config.settings import settings

type TMiddlewareClass = type[_MiddlewareClass]
type TMiddlewareDeclaration = tuple[TMiddlewareClass, dict]

MIDDLEWARE: Sequence[TMiddlewareDeclaration] = (
    (
        CORSMiddleware,
        {
            'allow_origins': settings.CORS_ALLOW_ORIGINS,
            'allow_credentials': settings.CORS_ALLOW_CREDENTIALS,
            'allow_methods': settings.CORS_ALLOW_METHODS,
            'allow_headers': settings.CORS_ALLOW_HEADERS,
        },
    ),
)
