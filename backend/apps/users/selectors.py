from .models import User


def get_user(username: str):
    return User.objects.get(username=username)
