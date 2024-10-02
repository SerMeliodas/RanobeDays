from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.urls import reverse

from django.core.mail import send_mail
from django.template.loader import render_to_string

from .exceptions import AlreadyVerifiedError
from apps.core.exceptions import TokenError


from .types import (
    RegisterObject,
    LoginObject,
    SendVerificationEmailObject
)


User = get_user_model()


def register(data: RegisterObject) -> User:
    user = User.objects.create_user(email=data.email,
                                    password=data.password1,
                                    username=data.username,
                                    public_username=data.public_username)

    return user


def login(data: LoginObject) -> str:
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


def send_verification_email(data: SendVerificationEmailObject) -> (int, str):
    user = User.objects.filter(email=data.email).first()

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    url = settings.BASE_URL + \
        reverse('auth:confirm-email', kwargs={
            'token': token,
            'uid': uid
        })

    _send_confirm_email(url, data.email)

    return f'Confirmation email was sent to {data.email}'


def verify_email(uid: str, token: str) -> (int, str):
    user_pk = urlsafe_base64_decode(uid)
    user = User.objects.get(pk=user_pk)

    if user.is_verified:
        raise AlreadyVerifiedError('User email is already verified')

    if not default_token_generator.check_token(user, token):
        raise TokenError('Invalid token')

    user.is_verified = True
    user.save()

    return 'Email was successfully confirmed'
