from .models import TranslatorTeam
from .types import TranslatorTeamObject
from apps.common.services import model_update


def create_translator_team(data: TranslatorTeamObject):
    team = TranslatorTeam(name=data.name)
    team.save()

    team.users.set(data.users)
    if data.novels is not None:
        team.novels.set(data.novels)

    return team


def update_translator_team(team_id: int, data: TranslatorTeamObject) -> dict:
    team = TranslatorTeam.objects.get(pk=team_id)
    fields = []

    for field, value in data.dict().items():
        if value is not None:
            fields.append(field)

    team, _ = model_update(instance=team,
                           fields=fields,
                           data=data.dict())

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
