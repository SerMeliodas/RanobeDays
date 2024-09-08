from django.db import models
from django.contrib.auth import get_user_model


class Email(models.Model):
    email = models.EmailField()
    user = models.OneToOneField(
        get_user_model(), models.CASCADE, related_name='email_verified')
    verified = models.BooleanField()
