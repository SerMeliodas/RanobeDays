from apps.common.services import model_update, get_fields_to_update

from rest_framework.exceptions import ValidationError
from .models import User
from .types import (
    UserObject, UserNewPassObject,
    ResetPasswordObject, RequestPasswordResetObject
)

from apps.core.exceptions import TokenError

from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

genarator = PasswordResetTokenGenerator()


def update_user(user: User, data: UserObject) -> User:
    fields = get_fields_to_update(data)

    user, _ = model_update(instance=user, fields=fields,
                           data=data.dict())

    return user


def new_password(user: User, data: UserNewPassObject) -> bool:
    user.set_password(data.new_password1)
    user.save()

    return user


def _send_pass_reset_email(reset_url: str, email: str):
    msg_plain = render_to_string(
        'users/email/reset_pass.txt', context={'reset_url': reset_url}
    )
    msg_html = render_to_string(
        'users/email/reset_pass.html', context={'reset_url': reset_url}
    )

    send_mail(
        subject='Resset password RanobeDays',
        message=msg_plain,
        html_message=msg_html,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=True
    )


def request_reset_password(data: RequestPasswordResetObject):
    user = User.objects.filter(email__iexact=data.email).first()

    if not user:
        raise ValidationError('User with this email does not exist')

    if not user.is_verified:
        raise ValidationError('User email is not verified')

    token = genarator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    reset_url = settings.BASE_URL + \
        reverse('users:password:reset-password', kwargs={
            'token': token,
            'uid': uid
        })

    _send_pass_reset_email(reset_url, data.email)

    return f'Request to reset password was sent to {data.email}'


def reset_password(data: ResetPasswordObject):
    user = User.objects.get(pk=urlsafe_base64_decode(data.uid))

    if not genarator.check_token(user, data.token):
        raise TokenError('Invalid token')

    user.set_password(data.new_password1)
    user.save()

    return 'Password was reset successfully'
