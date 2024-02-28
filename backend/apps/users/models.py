from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    first_name, last_name = None, None
    username = models.CharField("user name",
                                max_length=150,
                                unique=False)
    email = models.EmailField("email", unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
