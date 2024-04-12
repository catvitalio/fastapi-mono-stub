from fastapi import APIRouter

from src.users.admin import UserAdmin
from src.users.routes import router as users_router

ADMIN_VIEWS = [UserAdmin]
api_router = APIRouter()
api_router.include_router(users_router, prefix='/users', tags=['users'])
