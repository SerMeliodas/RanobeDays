from .models import Team
from django.db.models import QuerySet


def get_teams() -> QuerySet:
    return Team.objects.all()


def get_team(pk: int) -> Team:
    return Team.objects.get(pk=pk)
