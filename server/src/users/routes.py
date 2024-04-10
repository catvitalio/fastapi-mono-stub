from fastapi import APIRouter

from .controllers.login import router as login_router
from .controllers.me import router as me_router
from .controllers.register import router as register_router

router = APIRouter()
router.include_router(register_router)
router.include_router(login_router)
router.include_router(me_router)
