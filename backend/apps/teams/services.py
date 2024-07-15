from .models import Team
from .types import TeamObject
from apps.common.services import model_update
from apps.common.services import get_fields_to_update
from django.db import transaction

import logging


logger = logging.getLogger(__name__)


@transaction.atomic
def create_team(data: TeamObject):
    team = Team(name=data.name)
    team.save()

    team.users.set(data.users)
    if data.novels is not None:
        team.novels.set(data.novels)

    logger.info(f"Translator \"{team.name}\" was created")

    return team


def update_team(team_id: int, data: TeamObject) -> dict:
    team = Team.objects.get(pk=team_id)

    fields = get_fields_to_update(data)

    team, _ = model_update(instance=team,
                           fields=fields,
                           data=data.dict())

    logger.info(f"Translator team {team.name} data: {data.dict()} was updated")

    return team


# maybe in future i just delete this services >
def add_novel_to_team(team_id: int, novel_id: int)\
        -> Team:
    team = Team.objects.get(pk=team_id)
    team.novels.add(novel_id)

    return team


def delete_novel_from_team(team_id: int, novel_id: int)\
        -> Team:
    team = Team.objects.get(pk=team_id)
    team.novels.remove(novel_id)

    return team


def add_user_to_team(team_id: int, user_id: int)\
        -> Team:
    team = Team.objects.get(pk=team_id)
    team.users.remove(user_id)

    return team


def delete_user_from_team(team_id: int, user_id: int)\
        -> Team:
    team = Team.objects.get(pk=team_id)
    team.users.remove(user_id)

    return team
