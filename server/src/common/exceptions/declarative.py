from abc import ABC

from fastapi import HTTPException


class DeclarativeHTTPException(HTTPException, ABC):
    status_code: int
    detail: str

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)
