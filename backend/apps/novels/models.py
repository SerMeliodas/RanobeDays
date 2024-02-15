from django.db import models


class Novel(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')
    genres = models.ManyToManyField('Genre')

    class Meta:
        db_table = 'novels'


class Chapter(models.Model):
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
