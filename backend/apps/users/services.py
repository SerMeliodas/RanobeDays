from apps.common.services import model_update, get_fields_to_update
from .models import User
from .types import UserObject, UserNewPassObject


def update_user(user: User, data: UserObject) -> User:
    fields = get_fields_to_update(data)

    user, _ = model_update(instance=user, fields=fields,
                           data=data.dict())

    return user


def new_password(user: User, data: UserNewPassObject) -> bool:
    user.set_password(data.new_password1)
    user.save()

    return user
