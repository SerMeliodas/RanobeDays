from django.db import models
from apps.novels.models import Novel
from apps.common.models import BaseModel
from apps.common.exceptions import AlreadyExistError


class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = "chapters"
        default_related_name = "chapters"
        ordering = ["novel", "-created_at"]

    def clean(self):
        instance = Chapter.objects.get(title=self.title, novel=self.novel)

        if instance and instance.pk != self.pk:
            raise AlreadyExistError(Chapter)
