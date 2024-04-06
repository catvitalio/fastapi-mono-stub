from sqlalchemy import Boolean, Column, Integer, String

from src.common.models import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
