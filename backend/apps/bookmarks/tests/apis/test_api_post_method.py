from rest_framework.test import APIClient, APITestCase
from django.urls import reverse

from dj_rest_auth.models import TokenModel

from ...serializers import BookmarkBaseSerializer
from ..factories import BookmarkFactory
from apps.chapters.tests.factories import ChapterFactory


class BookmarkAPIPostTest(APITestCase):
    def setUp(self):
        self.bookmark = BookmarkFactory()
        self.user = self.bookmark.user

        self.token, _ = TokenModel.objects.get_or_create(user=self.user)

        self.client = APIClient()

    def __perform_request(self, bookmark_object: dict):
        return self.client.post(reverse('bookmarks:bookmark'),
                                bookmark_object,
                                format='json')

    def test_post_method(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.__perform_request(
            BookmarkBaseSerializer(self.bookmark).data
        )

        self.assertTrue(response.status_code == 400,
                        f'{response.status_code} -- {response.json()['data']}')

        response = self.__perform_request({
            'chapter': ChapterFactory().pk
        })

        self.assertTrue(response.status_code == 201,
                        f'{response.status_code} -- {response.json()['data']}')

    def test_post_method_authentication(self):
        response = self.__perform_request({
            'chapter': ChapterFactory().pk
        })

        self.assertTrue(response.status_code == 401,
                        f'{response.status_code} -- {response.json()['data']}')
