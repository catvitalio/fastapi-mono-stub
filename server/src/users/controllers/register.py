from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.deps.db import get_db
from ..dtos import JwtDto, RegisterCompleteDto, RegisterDto
from ..services.register import RegisterService

router = APIRouter()


@router.post('/register')
async def register(dto: RegisterDto, db: AsyncSession = Depends(get_db)) -> None:
    service = RegisterService(db)
    await service.register(dto)


@router.post('/register/complete')
async def register_complete(dto: RegisterCompleteDto, db: AsyncSession = Depends(get_db)) -> JwtDto:
    service = RegisterService(db)
    return await service.complete(dto)
