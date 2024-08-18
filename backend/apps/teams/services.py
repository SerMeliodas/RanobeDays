from .models import Team
from .types import TeamObject
from .exceptions import TeamIsCreator

from apps.common.services import model_update
from apps.common.services import get_fields_to_update
from apps.novels.selectors import get_novel
from django.db import transaction

import logging


logger = logging.getLogger(__name__)


@transaction.atomic
def create_team(data: TeamObject):
    team = Team(name=data.name, team_type=data.team_type,
                description=data.description)
    team.save()

    team.users.set(data.users)

    if data.novels is not None:
        team.novels.set(data.novels)

    logger.info(f'Translator \"{team.name}\" was created')

    return team


def update_team(team: Team, data: TeamObject) -> dict:
    fields = get_fields_to_update(data)

    team, _ = model_update(instance=team,
                           fields=fields,
                           data=data.dict())

    logger.info(f'Translator team {team.name} data: {data.dict()} was updated')

    return team


def add_novel_to_team(novel_slug, team):
    team.novels.add(get_novel(novel_slug))

    return team


def remove_novel_from_team(novel_slug, team):
    novel = get_novel(novel_slug)

    if novel.creator == team:
        raise TeamIsCreator('You can not remove creator of this novel')

    team.novels.remove(novel)

    return team
