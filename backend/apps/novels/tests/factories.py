import factory
from apps.teams.tests.factories import TeamFactory
from apps.metadata.tests import factories


class NovelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'novels.Novel'

    title = factory.Sequence(lambda n: f'Novel {n}')
    creator = factory.SubFactory(TeamFactory)

    language = factory.SubFactory(factories.LanguageFactory)
    translated_language = factory.SubFactory(factories.LanguageFactory)

    country = factory.SubFactory(factories.CountryFactory)
    status = 'frozen'

    synopsys = factory.Faker('text')

    @factory.post_generation
    def tags(self, creator, extracted, **kwargs):
        if not creator or not extracted:
            return

        self.tags.add(*extracted)

    @factory.post_generation
    def genres(self, creator, extracted, **kwargs):
        if not creator or not extracted:
            return

        self.genres.add(*extracted)
