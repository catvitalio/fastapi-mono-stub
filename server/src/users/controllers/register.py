from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import jwt_security
from src.common.deps.db import get_db
from ..dtos import JwtDto, RegisterCompleteDto, RegisterDto
from ..services.register import RegisterService

router = APIRouter()


@router.post('/register')
async def register(dto: RegisterDto, db: AsyncSession = Depends(get_db)) -> None:
    service = RegisterService(db)
    await service.register(dto)


@router.post('/register/complete')
async def register_complete(
    dto: RegisterCompleteDto,
    response: Response,
    db: AsyncSession = Depends(get_db),
) -> JwtDto:
    service = RegisterService(db)
    jwt = await service.complete(dto)
    jwt_security.set_access_cookie(response, jwt.access_token)
    jwt_security.set_refresh_cookie(response, jwt.refresh_token)
    return jwt
