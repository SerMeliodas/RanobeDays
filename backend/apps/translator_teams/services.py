from .models import TranslatorTeam
from .types import TranslatorTeamObject
from apps.common.services import model_update


def create_translator_team(dto: TranslatorTeamObject):
    team = TranslatorTeam(name=dto.name)
    team.save()

    team.users.set(dto.users)
    team.novels.set(dto.novels)

    return team


def update_translator_team(team_id: int, dto: TranslatorTeamObject) -> dict:
    team = TranslatorTeam.objects.get(pk=team_id)
    fields = ['name', 'user', 'teams']

    team, _ = model_update(instance=team,
                           fields=fields,
                           data=dto.dict())

    return team


def add_novel_to_translator_team(team_id: int, novel_id: int)\
        -> TranslatorTeam:
    team = TranslatorTeam.objects.get(pk=team_id)
    team.novels.add(novel_id)

    return team


def delete_novel_from_translator_team(team_id: int, novel_id: int)\
        -> TranslatorTeam:
    team = TranslatorTeam.objects.get(pk=team_id)
    team.novels.remove(novel_id)

    return team


def add_user_to_translator_team(team_id: int, user_id: int)\
        -> TranslatorTeam:
    team = TranslatorTeam.objects.get(pk=team_id)
    team.users.remove(user_id)

    return team


def delete_user_from_translator_team(team_id: int, user_id: int)\
        -> TranslatorTeam:
    team = TranslatorTeam.objects.get(pk=team_id)
    team.users.remove(user_id)

    return team
