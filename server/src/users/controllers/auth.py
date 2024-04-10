from fastapi import APIRouter, Depends, Response
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config.security import refresh_security
from src.common.deps.db import get_db
from ..dtos import LoginDto, RegisterCompleteDto, RegisterDto
from ..services import LoginService, RegisterService
from ..utils import get_jwt_response

router = APIRouter()


@router.post('/login')
async def login(dto: LoginDto, db: AsyncSession = Depends(get_db)) -> Response:
    service = LoginService(db)
    user = await service.login(dto)
    return get_jwt_response(user.id)


@router.post('/register')
async def register(dto: RegisterDto, db: AsyncSession = Depends(get_db)) -> Response:
    service = RegisterService(db)
    await service.register(dto)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/register/complete')
async def register_complete(
    dto: RegisterCompleteDto,
    db: AsyncSession = Depends(get_db),
) -> Response:
    service = RegisterService(db)
    user = await service.complete(dto)
    return get_jwt_response(user.id)


@router.post('/refresh')
async def refresh(refresh: JwtAuthorizationCredentials = Depends(refresh_security)) -> Response:
    return get_jwt_response(refresh.subject['id'])


@router.post('/logout')
async def logout() -> Response:
    return get_jwt_response(None)
