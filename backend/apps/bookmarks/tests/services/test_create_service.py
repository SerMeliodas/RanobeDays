from ...types import BookmarkObject
from ...services import create_bookmark

from apps.users.tests.factories import UserFactory
from apps.chapters.tests.factories import ChapterFactory

from unittest import TestCase


class BookmarkCreateServiceTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.chapter = ChapterFactory()

    def test_create(self):
        bookmark = create_bookmark(BookmarkObject(user=self.user,
                                                  chapter=self.chapter.pk))

        self.assertIsNotNone(bookmark)

        self.assertEqual(bookmark.user, self.user)
        self.assertEqual(bookmark.chapter, self.chapter)
