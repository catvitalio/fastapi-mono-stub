from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any  # noqa: A003
    __name__: str  # noqa: A003

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
