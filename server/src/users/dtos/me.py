from pydantic import BaseModel


class MeDto(BaseModel):
    id: int  # noqa: A003
    email: str
    first_name: str
    last_name: str
