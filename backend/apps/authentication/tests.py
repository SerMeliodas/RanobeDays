from apps.users.tests.factories import UserFactory
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class AuthTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory(password='testpass')

    def test_login_without_verified_email(self):
        response = self.client.post(reverse('auth:login'), format='json',
                                    data={
                                    'email': self.user.email,
                                    'password': 'testpass'
                                    })

        self.assertEqual(
            {'non_field_errors': ['E-mail is not verified.']
             }, response.json()['data'],
            f'{response.status_code} -- {response.json()}')

    def test_verify_email(self):
        ...

    # def test_login_with_verified_email(self):
    #     ...
    #
    # def test_logout(self):
    #     ...
    #
    # def test_register(self):
    #     ...
