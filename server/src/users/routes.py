from fastapi import APIRouter

from .controllers.auth import router as auth_router
from .controllers.register import router as register_router

router = APIRouter()
router.include_router(register_router)
router.include_router(auth_router)
