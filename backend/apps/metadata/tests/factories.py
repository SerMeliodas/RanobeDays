import factory


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'metadata.Language'

    name = factory.Faker('language_name')
    abbreviation = factory.Faker('language_code')


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'metadata.Country'

    name = factory.Faker('country')


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'metadata.Genre'

    name = factory.Sequence(lambda n: f'{n}')


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'metadata.Tag'

    name = factory.Sequence(lambda n: f'{n}')
