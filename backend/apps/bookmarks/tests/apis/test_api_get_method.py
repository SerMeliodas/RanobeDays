from rest_framework.test import APITestCase, APIClient
from dj_rest_auth.models import TokenModel
from django.urls import reverse

from apps.core.utils import get_response_data
from apps.users.tests.factories import UserFactory

from ..factories import BookmarkFactory

from ...serializers import BookmarkBaseSerializer


class BookmarkAPIGetTest(APITestCase):
    def setUp(self):
        self.bookmark = BookmarkFactory()
        self.bookmarks = [self.bookmark]

        self.user = self.bookmark.user

        for _ in range(5):
            self.bookmarks.append(BookmarkFactory(user=self.user))

        self.client = APIClient()
        self.token, _ = TokenModel.objects.get_or_create(user=self.user)

    def __performe_request(self):
        return self.client.get(reverse('bookmarks:bookmark'))

    def test_get_response(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.__performe_request()

        self.assertTrue(response.status_code == 200,
                        f'{response.status_code} -- {response.json()['data']}')

        self.assertTrue(
            dict(**response.json()) == get_response_data(response.status_code,
                                                         BookmarkBaseSerializer(self.bookmarks, many=True).data),
            'The expected response do not equal to recived response'
        )

    def test_get_authentication(self):
        response = self.__performe_request()

        self.assertTrue(response.status_code == 401,
                        f'{response.status_code} -- {response.json()['data']}')


class BookmarkDetailAPIGetTest(APITestCase):
    def setUp(self):
        self.bookmark = BookmarkFactory()

        self.user = self.bookmark.user

        self.client = APIClient()
        self.token, _ = TokenModel.objects.get_or_create(user=self.user)

    def __performe_request(self):
        return self.client.get(
            reverse('bookmarks:bookmark-detail',
                    kwargs={'pk': self.bookmark.pk})
        )

    def test_get_response(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.__performe_request()

        self.assertTrue(response.status_code == 200,
                        f'{response.status_code} -- {response.json()['data']}')

        self.assertTrue(
            dict(**response.json()) == get_response_data(response.status_code,
                                                         BookmarkBaseSerializer(self.bookmark).data),
            'The expected response do not equal to recived response'
        )

    def test_get_authentication(self):
        response = self.__performe_request()

        self.assertTrue(response.status_code == 401,
                        f'{response.status_code} -- {response.json()['data']}')

    def test_get_authorization(self):
        test_user = UserFactory()
        token, _ = TokenModel.objects.get_or_create(user=test_user)

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.__performe_request()

        self.assertTrue(response.status_code == 200,
                        f'{response.status_code} -- {response.json()['data']}')
