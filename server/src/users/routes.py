from fastapi import APIRouter

from .controllers.register import router as register_router

router = APIRouter()
router.include_router(register_router)
