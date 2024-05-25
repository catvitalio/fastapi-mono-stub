from typing import NoReturn

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..exceptions import ObjectNotFoundException
from ..types import TModel


async def get_or_404(db: AsyncSession, model: type[TModel], **filters) -> TModel | NoReturn:
    result = await db.execute(select(model).filter_by(**filters))
    instance = result.scalars().first()
    if not instance:
        raise ObjectNotFoundException(model.__name__)
    return instance
