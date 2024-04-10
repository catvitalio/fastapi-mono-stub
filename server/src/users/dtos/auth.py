from pydantic import BaseModel, EmailStr


class LoginDto(BaseModel):
    email: EmailStr
    password: str


class RegisterDto(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class RegisterCompleteDto(BaseModel):
    token: str
