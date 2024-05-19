from dj_rest_auth.registration.serializers import RegisterSerializer as BaseRegisterSerializer
from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
import pdb


class RegisterSerializer(BaseRegisterSerializer):
    def validate_username(self, username):
        ...


class LoginSerializer(BaseLoginSerializer):
    def _validate_username(self, username, password):
        ...

    def _validate_username_email(self, username, email, password):
        ...
