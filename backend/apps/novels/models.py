from django.db import models
from django.utils.text import slugify

from apps.common.exceptions import AlreadyExistError
from apps.common.models import BaseModel


class Novel(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=title, db_index=True)
    tags = models.ManyToManyField("Tag", db_index=True)
    genres = models.ManyToManyField("Genre", db_index=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "novels"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Novel, self).save(*args, **kwargs)

    def clean(self):
        try:
            obj = Novel.objects.get(title=self.title)
            raise AlreadyExistError(obj)
        except self.DoesNotExist:
            pass


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def clean(self):
        try:
            obj = Tag.objects.get(name=self.name)
            raise AlreadyExistError(obj)
        except self.DoesNotExist:
            pass


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genres"

    def clean(self):
        try:
            obj = Genre.objects.get(name=self.name)
            raise AlreadyExistError(obj)
        except self.DoesNotExist:
            pass
