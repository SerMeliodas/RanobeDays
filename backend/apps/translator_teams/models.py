from django.db import models
from django.contrib.auth import get_user_model
from apps.novels.models import Novel


class TranslatorTeam(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model())
    novels = models.ManyToManyField(Novel)

    class Meta:
        db_table = 'translators-teams'

    def __str__(self):
        return f"Group {self.name}"
