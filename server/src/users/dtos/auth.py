from pydantic import BaseModel, EmailStr, field_validator

from ..validators import check_email_existance


class LoginDto:
    class Input(BaseModel):
        email: EmailStr
        password: str

    class Output(BaseModel):
        access_token: str
        refresh_token: str


class RegisterDto:
    class Input(BaseModel):
        email: EmailStr
        password: str
        first_name: str
        last_name: str

    check_email_existance = field_validator('email')(check_email_existance)

    class Output(BaseModel):
        id: int  # noqa: A003


class RegisterCompleteDto:
    class Input(BaseModel):
        token: str

    class Output(BaseModel):
        access_token: str
        refresh_token: str
