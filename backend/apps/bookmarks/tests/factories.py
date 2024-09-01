import factory
from apps.users.tests.factories import UserFactory
from apps.chapters.tests.factories import ChapterFactory


class BookmarkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'bookmarks.Bookmark'

    user = factory.SubFactory(UserFactory)
    chapter = factory.SubFactory(ChapterFactory)
