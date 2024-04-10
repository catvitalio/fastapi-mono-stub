from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import jwt_security
from src.common.deps.db import get_db
from ..dtos import JwtDto, LoginDto
from ..services import LoginService

router = APIRouter()


@router.post('/login')
async def login(dto: LoginDto, response: Response, db: AsyncSession = Depends(get_db)) -> JwtDto:
    service = LoginService(db)
    jwt = await service.login(dto)
    jwt_security.set_access_cookie(response, jwt.access_token)
    jwt_security.set_refresh_cookie(response, jwt.refresh_token)
    return jwt
