from apps.users.tests.factories import UserFactory
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class AuthTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory(password='testpass')

    def _set_auth_token(self):
        response = self.client.post(reverse('auth:login'), format='json',
                                    data={
                                    'email': self.user.email,
                                    'password': 'testpass'
                                    })

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {
                                response.json()['data']['token']}')

    def test_login(self):
        response = self.client.post(reverse('auth:login'), format='json',
                                    data={
                                    'email': self.user.email,
                                    'password': 'testpass'
                                    })

        self.assertEqual(response.status_code, 200,
                         f'{response.status_code} -- {response.json()}')

    def test_send_confirmation_email(self):
        self._set_auth_token()

        response = self.client.post(reverse('auth:send-verification-email'),
                                    format='json',
                                    data={
                                    'email': self.user.email
                                    })

        self.assertEqual(response.status_code, 200,
                         f'{response.status_code} -- {response.json()}')

    def test_logout(self):
        self._set_auth_token()

        response = self.client.post(reverse('auth:logout'))

        self.assertEqual(response.status_code, 200,
                         f'{response.status_code} -- {response.json()}')

    def test_register_password_missmatch(self):
        response = self.client.post(reverse('auth:register'), format='json',
                                    data={
                                    'username': 'testuser',
                                    'public_username': 'user',
                                    'email': 'test@test.com',
                                    'password1': 'qwdqwdasdaad',
                                    'password2': 'qwdqwd!@#!@#'
                                    })

        self.assertEqual(response.status_code, 400,
                         f'{response.status_code} -- {response.json()}')

    def test_register(self):
        response = self.client.post(reverse('auth:register'), format='json',
                                    data={
                                    'username': 'testuser',
                                    'public_username': 'user',
                                    'email': 'test@test.com',
                                    'password1': 'qwdqwd!@#!@#',
                                    'password2': 'qwdqwd!@#!@#'
                                    })

        self.assertEqual(response.status_code, 201,
                         f'{response.status_code} -- {response.json()}')
