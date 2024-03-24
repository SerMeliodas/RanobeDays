from .models import TranslatorTeam
from apps.novels.models import Novel
from django.db.models import QuerySet


def get_translator_teams_list() -> QuerySet:
    return TranslatorTeam.objects.all()


def get_translator_team_by_id(id: int) -> TranslatorTeam:
    return TranslatorTeam.objects.get(pk=id)


def get_translator_teams_by_novel_id(id: int) -> TranslatorTeam:
    return TranslatorTeam.objects.filter(novels=Novel.objects.get(pk=id))
