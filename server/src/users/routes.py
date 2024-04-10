from fastapi import APIRouter

from .controllers.auth import router as auth_router
from .controllers.me import router as me_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(me_router)
