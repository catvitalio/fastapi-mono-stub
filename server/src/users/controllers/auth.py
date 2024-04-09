from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import jwt_security
from src.common.deps.db import get_db
from ..dtos import AuthDto, JwtDto
from ..services import AuthService

router = APIRouter()


@router.post('/auth')
async def auth(dto: AuthDto, response: Response, db: AsyncSession = Depends(get_db)) -> JwtDto:
    service = AuthService(db)
    jwt = await service.auth(dto)
    jwt_security.set_access_cookie(response, jwt.access_token)
    jwt_security.set_refresh_cookie(response, jwt.refresh_token)
    return jwt
