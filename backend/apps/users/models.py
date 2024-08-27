from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

from .managers import UserManager


def _get_save_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"users_avatars/{instance.username}.{extension}"


class User(AbstractUser):
    first_name, last_name = None, None

    username = models.CharField("username", max_length=150, unique=True)
    public_username = models.CharField(
        "public username", max_length=150, default="user")

    email = models.EmailField("email", unique=True)
    avatar = models.ImageField(
        default="default_avatar.png", upload_to=_get_save_path)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username + " " + str(self.pk)

    def _change_avatar_size(self):
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self._change_avatar_size()


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
