from apps.users.tests.factories import UserFactory
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class AuthTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory(password='testpass')

    def test_login(self):
        response = self.client.post(reverse('auth:login'), format='json',
                                    data={
                                    'email': self.user.email,
                                    'password': 'testpass'
                                    })

        self.assertEqual(response.status_code, 200,
                         f'{response.status_code} -- {response.json()}')

    # def test_verify_email(self):
    #     ...
    #

    def test_logout(self):
        response = self.client.post(reverse('auth:login'), format='json',
                                    data={
                                    'email': self.user.email,
                                    'password': 'testpass'
                                    })

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {
                                response.json()['data']['token']}')

        response = self.client.post(reverse('auth:logout'))

        self.assertEqual(response.status_code, 200,
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
