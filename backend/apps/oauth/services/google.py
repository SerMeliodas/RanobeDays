from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.conf import settings
from urllib.parse import urlencode

from apps.core.exceptions import ApplicationError

from apps.authentication.types import RegisterObject, LoginObject
from apps.authentication.services import register, login

from ..selectors import get_google_client_credentials
from ..types import GoogleAccessTokensObject
import requests
import hashlib
import os

User = get_user_model()


class GoogleLoginRegisterService:
    API_URI = reverse_lazy('oauth:google:callback')

    GOOGLE_AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
    GOOGLE_ACCESS_TOKEN_OBATAIN_URL = 'https://oauth2.googleapis.com/token'
    # GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

    SCOPES = [
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'openid',
    ]

    def __init__(self):
        self._credentials = get_google_client_credentials()
        self._user_info = ...

    @staticmethod
    def _generate_state_session_token() -> str:
        return hashlib.sha256(os.urandom(1024)).hexdigest()

    def _get_redirect_uri(self) -> str:
        return f'{settings.BASE_URL}{self.API_URI}'

    def get_auth_url(self) -> tuple[str]:
        redirect_uri = self._get_redirect_uri()
        state = self._generate_state_session_token()

        params = {
            'response_type': 'code',
            'client_id': self._credentials.client_id,
            'redirect_uri': redirect_uri,
            'scope': ' '.join(self.SCOPES),
            'state': state,
            'access_type': 'offline',
            'include_granted_scopes': 'true',
            'prompt': 'select_account'
        }

        query_params = urlencode(params)

        auth_url = f'{self.GOOGLE_AUTH_URL}?{query_params}'

        return auth_url, state

    def get_tokens(self, code: str):
        data = {
            'code': code,
            'client_id': self._credentials.client_id,
            'client_secret': self._credentials.secret,
            'redirect_uri': self._get_redirect_uri(),
            'grant_type': 'authorization_code',
        }

        response = requests.post(
            self.GOOGLE_ACCESS_TOKEN_OBATAIN_URL, data=data)

        if not response.ok:
            raise ApplicationError(
                'Failed to obtain access token from Google.')

        tokens = response.json()

        return GoogleAccessTokensObject(
            id_token=tokens['id_token'],
            access_token=tokens['access_token']
        )

    # TODO: think about genereating pass for users which are registering via oauth2
    def _generate_password(self) -> str:
        string_to_hash = self._user_info['sub']+self._user_info['email']
        return hashlib.sha256(string_to_hash.encode('utf-8')).hexdigest()

    def _register(self) -> User:
        password = self._generate_password()

        register_object = RegisterObject(
            email=self._user_info['email'],
            username=slugify(self._user_info['name']),
            password1=password,
            password2=password,
            public_username=self._user_info['name']
        )

        user = register(register_object)
        user.is_verified = True
        user.save()

        return user

    def _login(self, user: User) -> str:
        password = self._user_info['sub']+self._user_info['email']
        login_object = LoginObject(
            email=user.email,
            password=hashlib.sha256(password.encode('utf-8')).hexdigest()
        )

        return login(login_object)

    def _isUserExists(self):
        return User.objects.filter(email=self._user_info['email']).exists()

    def proced_user(self, code: str):
        self._user_info = self.get_tokens(code).decode_id_token()

        if not self._isUserExists():
            user = self._register()

        user = User.objects.get(email=self._user_info['email'])

        return self._login(user)
