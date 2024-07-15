from django.db import models
from django.contrib.auth import get_user_model


class Team(models.Model):

    TEAM_TYPES = {
        ("A", "Autor"),
        ("T", "Translator")
    }

    name = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model())
    novels = models.ManyToManyField("novels.Novel")
    team_type = models.CharField(max_length=1, choices=TEAM_TYPES, default="A")
    description = models.TextField(null=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return f"Team '{self.name}' with id: {self.pk}"
