from django.db import models
from apps.common.models import BaseModel
from apps.common.exceptions import AlreadyExistError


class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    novel = models.ForeignKey("novels.Novel", on_delete=models.CASCADE)
    translator_team = models.ForeignKey(
        "translator_teams.TranslatorTeam", on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = "chapters"
        default_related_name = "chapters"
        ordering = ["novel", "-created_at", "translator_team"]

    def clean(self):
        instance = Chapter.objects.filter(title=self.title, novel=self.novel)

        if instance.exists():
            raise AlreadyExistError(self)
