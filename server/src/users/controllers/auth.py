from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import jwt_security
from src.common.deps.db import get_db
from ..dtos.auth import LoginDto, RegisterCompleteDto, RegisterDto
from ..services.register import RegisterService

router = APIRouter()


@router.post('/login')
async def login(dto: LoginDto.Input, response: Response) -> LoginDto.Output:
    access = jwt_security.create_access_token({})
    refresh = jwt_security.create_refresh_token({})
    jwt_security.set_access_cookie(response, access)
    jwt_security.set_refresh_cookie(response, refresh)
    return LoginDto.Output(access_token=access, refresh_token=refresh)
