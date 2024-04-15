from typing import Any, Coroutine

from fastapi import Request
from starlette_admin.contrib.sqla import ModelView
from starlette_admin.fields import StringField

from config.security import hasher
from ..models import User


class UserView(ModelView):
    fields = (
        'id',
        StringField('email', 'Электронная почта'),
        StringField('hashed_password', 'Пароль'),
        StringField('first_name', 'Имя'),
        StringField('last_name', 'Фамилия'),
    )
    exclude_fields_from_detail = ('hashed_password',)
    exclude_fields_from_list = ('hashed_password',)
    model = User

    def before_create(
        self,
        request: Request,
        data: dict[str, Any],
        obj: User,
    ) -> Coroutine[Any, Any, None]:
        obj.hashed_password = self._hash_password(obj.hashed_password)
        return super().before_create(request, data, obj)

    def before_edit(
        self,
        request: Request,
        data: dict[str, Any],
        obj: User,
    ) -> Coroutine[Any, Any, None]:
        obj.hashed_password = self._hash_password(obj.hashed_password)
        return super().before_edit(request, data, obj)

    def _hash_password(self, password: str) -> str:
        if not hasher.identify(password):
            return hasher.hash(password)
        return password
