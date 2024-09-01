import factory
from apps.users.tests.factories import UserFactory
from apps.novels.tests.factories import NovelFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'comments.Comment'

    comment_type = 'novel'
    message = factory.Faker('text')

    user = factory.SubFactory(UserFactory)
    novel = factory.SubFactory(NovelFactory)
