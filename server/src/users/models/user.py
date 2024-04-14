from sqlalchemy import Boolean, String
from sqlalchemy.orm import mapped_column

from src.common.models import Base


class User(Base):
    email = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password = mapped_column(String, nullable=False)
    first_name = mapped_column(String, index=True)
    last_name = mapped_column(String, index=True)
    is_active = mapped_column(Boolean, default=True, nullable=False)
    is_admin = mapped_column(Boolean, default=False, nullable=False)
