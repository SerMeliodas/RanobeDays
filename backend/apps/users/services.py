from apps.common.services import model_update, get_fields_to_update
import datetime

from rest_framework.exceptions import ValidationError
from .models import User, PasswordReset
from .types import (
    UserObject, UserNewPassObject,
    ResetPasswordObject, RequestPasswordResetObject
)

from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .exceptions import TokenError


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
        raise ValidationError('User with this email do not exist')

    genarator = PasswordResetTokenGenerator()
    token = genarator.make_token(user)

    reset_obj = PasswordReset(email=user.email, token=token)
    reset_obj.save()

    reset_url = settings.BASE_URL + \
        reverse('users:password:reset-password', args=[token])

    _send_pass_reset_email(reset_url, data.email)

    return f'Request to reset password was sent to {data.email}'


def reset_password(data: ResetPasswordObject):
    reset_obj = PasswordReset.objects.filter(token=data.token).first()

    if not reset_obj:
        raise TokenError('Invalid token')

    if datetime.datetime.now().timestamp() - reset_obj.created_at.timestamp() >= 5*60:
        reset_obj.delete()
        raise TokenError('Token has been expired')

    user = User.objects.get(email=reset_obj.email)
    user.set_password(data.new_password1)
    user.save()

    reset_obj.delete()

    return 'Password was reset successfully'
