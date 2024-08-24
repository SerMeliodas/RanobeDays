from django.db import models
from apps.common.models import BaseModel


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
        ordering = ['volume', 'number', 'team']

    def __str__(self):
        return f"{self.volume}:{self.number} - {self.title} - {self.novel}"
