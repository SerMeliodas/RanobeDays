from django.db import models
from apps.common.models import BaseModel
from apps.core.exceptions import AlreadyExistError


class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    volume = models.IntegerField(default=1)
    number = models.IntegerField(default=1)
    novel = models.ForeignKey('novels.Novel', on_delete=models.CASCADE)
    team = models.ForeignKey(
        'teams.Team', on_delete=models.CASCADE, default=None)
    text = models.TextField()

    class Meta:
        db_table = 'chapters'
        default_related_name = 'chapters'
        ordering = ['novel', '-created_at', 'team']

    def clean(self):
        instance = Chapter.objects.filter(title=self.title, novel=self.novel)

        if instance.exists():
            raise AlreadyExistError(self)
