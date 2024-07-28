from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Team(models.Model):

    TEAM_TYPES = (
        (1, _('Autor')),
        (2, _('Translator'))
    )

    name = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model())
    novels = models.ManyToManyField('novels.Novel', related_name="teams")
    team_type = models.IntegerField(choices=TEAM_TYPES, default=1)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return f"{self.name} -- {Team.TEAM_TYPES[self.team_type][1]}"
