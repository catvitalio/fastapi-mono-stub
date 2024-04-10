from pydantic import BaseModel, EmailStr


class MeDto(BaseModel):
    id: int  # noqa: A003
    email: EmailStr
    first_name: str
    last_name: str
