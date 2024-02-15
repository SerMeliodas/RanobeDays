from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    class Meta:
        abstract = True


class Novel(BaseModel):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')
    genres = models.ManyToManyField('Genre')

    class Meta:
        db_table = 'novels'


class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    novel = models.ForeignKey('Novel', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = 'chapters'
        default_related_name = 'chapters'
        ordering = ['novel']


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tags'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'genres'
