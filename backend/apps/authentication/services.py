from apps.users.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from django.core.mail import send_mail
from django.template.loader import render_to_string


from .types import (
    RegisterObject,
    LoginObject,
    VerifyEmailObject,
    SendVerificationEmailObject
)


def register(data: RegisterObject):
    user = User.objects.create_user(email=data.email,
                                    password=data.password1,
                                    username=data.username,
                                    public_username=data.public_username)

    return user


def login(data: LoginObject):
    user = authenticate(email=data.email, password=data.password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)

        return token


def send_verification_email(data: SendVerificationEmailObject):
    ...


def verify_email(data: VerifyEmailObject):
    ...
