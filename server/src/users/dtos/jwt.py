from pydantic import BaseModel


class JwtDto(BaseModel):
    access_token: str
    refresh_token: str
