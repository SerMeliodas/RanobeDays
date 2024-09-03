from rest_framework.test import APIClient, APITestCase
from django.urls import reverse

from dj_rest_auth.models import TokenModel

from ..factories import BookmarkFactory
from apps.users.tests.factories import UserFactory


class BookmarkDetailAPIDeleteTest(APITestCase):
    def setUp(self):
        self.bookmark = BookmarkFactory()

        self.user = self.bookmark.user

        self.token, _ = TokenModel.objects.get_or_create(user=self.user)

        self.client = APIClient()

    def __perform_request(self):
        return self.client.delete(
            reverse('bookmarks:bookmark-detail', kwargs={'pk': self.bookmark.pk}))

    def test_delete_method(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.__perform_request()

        self.assertTrue(response.status_code == 200,
                        f'{response.status_code} -- {response.json()['data']}')

    def test_delete_authentication(self):
        response = self.__perform_request()

        self.assertTrue(response.status_code == 401,
                        f'{response.status_code} -- {response.json()['data']}')

    def test_delete_authorization(self):
        test_user = UserFactory()
        token, _ = TokenModel.objects.get_or_create(user=test_user)

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.__perform_request()

        self.assertTrue(response.status_code == 403,
                        f'{response.status_code} -- {response.json()['data']}')
