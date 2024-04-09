from fastapi import APIRouter, Depends

from ..deps import get_current_user
from ..dtos import MeDto
from ..models import User

router = APIRouter()


@router.get('/me')
async def get_me(user: User = Depends(get_current_user)) -> MeDto:
    return MeDto(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
    )
