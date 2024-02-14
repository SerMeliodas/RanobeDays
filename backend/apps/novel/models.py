from django.db import models


class Novel(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField('Genre')
    tags = models.ManyToManyField('Tag')


class Chapter(models.Model):
    title = models.CharField(max_length=155)
    novel = models.ForeignKey('Novel', on_delete=models.CASCADE)
    text = models.TextField()


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)
