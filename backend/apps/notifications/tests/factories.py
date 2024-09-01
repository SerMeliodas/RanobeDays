import factory
from apps.novels.tests.factories import NovelFactory
from apps.users.tests.factories import UserFactory


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'notifications.Notification'

    notification_type = 'update'
    novel = factory.SubFactory(NovelFactory)
    user = factory.SubFactory(UserFactory)

    message = factory.Faker('text')
