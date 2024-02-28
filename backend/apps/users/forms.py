from django.contrib.auth.forms import (
    UserCreationForm as UserCForm,
    UserChangeForm as UserChForm
)

from .models import User


class UserChangeForm(UserChForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserCreationForm(UserCForm):
    class Meta:
        model = User
        fields = ('username', 'email')
