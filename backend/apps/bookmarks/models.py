from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel


class Bookmark(BaseModel):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    chapter = models.ForeignKey(
        'chapters.Chapter', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookmarks'
        unique_together = (('chapter', 'user'))

    def __str__(self):
        return f"{self.pk} - {self.user} - {self.chapter}"
