import factory
from apps.novels.tests.factories import NovelFactory
from apps.teams.tests.factories import TeamFactory


class ChapterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'chapters.Chapter'

    title = factory.Sequence(lambda n: f'Chapter {n}')
    volume = 1
    number = factory.Faker('random_digit_not_null')

    novel = factory.SubFactory(NovelFactory)
    team = factory.SubFactory(TeamFactory)

    text = factory.Faker('text')
