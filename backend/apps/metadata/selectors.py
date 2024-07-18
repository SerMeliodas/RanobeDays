from .models import Tag, Genre, Language, Country


def tag_list() -> list[Tag]:
    return Tag.objects.all()


def get_tag(pk: int) -> Tag:
    return Tag.objects.get(pk=pk)


def get_genre(pk: int) -> Genre:
    return Genre.objects.get(pk=pk)


def genre_list() -> list[Genre]:
    return Genre.objects.all()


def get_language(pk: int) -> Language:
    return Language.objects.get(pk=pk)


def language_list() -> list[Language]:
    return Language.objects.all()


def get_country(pk: int) -> Country:
    return Country.objects.get(pk=pk)


def country_list() -> list[Country]:
    return Country.objects.all()
