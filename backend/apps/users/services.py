from apps.common.services import model_update, get_fields_to_update
from .models import User
from .types import UserObject, UserNewPassObject


def update_user(username: str, data: UserObject) -> User:
    user = User.objects.get(username=username)
    fields = get_fields_to_update(data)

    user, _ = model_update(instance=user, fields=fields,
                           data=data.dict())

    return user


def new_password(username: str, data: UserNewPassObject) -> bool:
    user = User.objects.get(username=username)

    user.set_password(data.new_password1)
    user.save()

    return user
