from pydantic import BaseModel


class RefreshDto(BaseModel):
    refresh_token: str
