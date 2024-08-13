from django.core.management.base import BaseCommand
from apps.novels.models import Novel
from apps.metadata.models import Tag, Genre, Country, Language

from random import randint


class Command(BaseCommand):
    BASE_NOVEL_NAME = 'novel'
    BASE_TAG_NAME = 'tag'
    BASE_GENRE_NAME = 'genre'
    BASE_COUNTRY_NAME = 'country'
    BASE_LANGUAGE_NAME = 'language'

    TAGS_COUNT = 10
    LANGUAGES_COUNT = 10
    COUNTRIES_COUNT = 10
    GENRES_COUNT = 10
    NOVELS_COUNT = 100

    def handle(self, *args, **options):
        self.create_tags()
        self.create_genres()
        countries = self.create_countries()
        languages = self.create_languages()

        self.create_novels(countries, languages)

    def create_novels(self, countries, languages):
        for i in range(self.NOVELS_COUNT):
            title = f'{self.BASE_NOVEL_NAME}_{i}'
            novel = Novel(title=title, original_title=title,
                          language=languages[randint(
                              0, self.LANGUAGES_COUNT - 1)],
                          translated_language=languages[randint(
                              0, self.LANGUAGES_COUNT - 1)],
                          country=countries[randint(
                              0, self.COUNTRIES_COUNT - 1)],
                          status=1,
                          )
            novel.clean()
            novel.save()

            novel.tags.set([randint(1, self.TAGS_COUNT - 1)])
            novel.genres.set([randint(1, self.GENRES_COUNT - 1)])

            self.stdout.write(self.style.SUCCESS(f'Created novel {i}'))

    def create_tags(self):
        result = []

        for i in range(self.TAGS_COUNT):
            tag = Tag.objects.create(name=f'{self.BASE_TAG_NAME}_{i}')
            result.append(tag)
            self.stdout.write(self.style.SUCCESS(f'Created tag {i}'))

        return result

    def create_genres(self):
        result = []

        for i in range(self.GENRES_COUNT):
            genre = Genre.objects.create(name=f'{self.BASE_GENRE_NAME}_{i}')
            result.append(genre)
            self.stdout.write(self.style.SUCCESS(f'Created genre {i}'))

        return result

    def create_countries(self):
        result = []

        for i in range(self.COUNTRIES_COUNT):
            contry = Country.objects.create(
                name=f'{self.BASE_COUNTRY_NAME}_{i}')
            result.append(contry)
            self.stdout.write(self.style.SUCCESS(f'Created country {i}'))

        return result

    def create_languages(self):
        result = []
        for i in range(self.LANGUAGES_COUNT):
            lang = Language.objects.create(
                name=f'{self.BASE_LANGUAGE_NAME}_{i}')
            result.append(lang)
            self.stdout.write(self.style.SUCCESS(f'Created language {i}'))

        return result
