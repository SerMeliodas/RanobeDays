from .models import TranslatorTeam
from django.db.models import QuerySet


def get_translator_teams() -> QuerySet:
    return TranslatorTeam.objects.all()


def get_translator_team(pk: int) -> TranslatorTeam:
    return TranslatorTeam.objects.get(pk=pk)
