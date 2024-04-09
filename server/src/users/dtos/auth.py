from pydantic import BaseModel, EmailStr


class AuthDto(BaseModel):
    email: EmailStr
    password: str


class JwtDto(BaseModel):
    access_token: str
    refresh_token: str
