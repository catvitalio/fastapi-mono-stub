from pydantic.alias_generators import to_snake
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)  # noqa: A003
    __name__: str  # noqa: A003

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return to_snake(cls.__name__)
