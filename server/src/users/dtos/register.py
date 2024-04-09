from pydantic import BaseModel, EmailStr


class RegisterDto(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class RegisterCompleteDto(BaseModel):
    token: str
