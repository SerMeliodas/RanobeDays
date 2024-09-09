from apps.users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.urls import reverse

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


def _send_confirm_email(url: str, email: str):
    msg_html = render_to_string(
        'authentication/email/confirm_email.html', context={'url': url}
    )

    msg_plain = render_to_string(
        'authentication/email/confirm_email.txt', context={'url': url}
    )

    send_mail(
        subject='Confirm email',
        message=msg_plain,
        html_message=msg_html,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=True
    )


def send_verification_email(data: SendVerificationEmailObject):
    user = User.objects.filter(email=data.email).first()

    token = default_token_generator.make_token(user)

    url = settings.BASE_URL + \
        reverse('auth:confirm-email', args=[token])

    _send_confirm_email(url, data.email)

    return f'Confirmation email was sent to {data.email}'


def verify_email(data: VerifyEmailObject):
    ...
