from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Team(models.Model):

    TEAM_TYPES = (
        ('autor', _('Autor')),
        ('translator', _('Translator'))
    )

    name = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model())
    novels = models.ManyToManyField(
        'novels.Novel', related_name="teams", blank=True
    )
    team_type = models.CharField(choices=TEAM_TYPES, default=TEAM_TYPES[0][0])
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return f"{self.name} -- {self.team_type}"
