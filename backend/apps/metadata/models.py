from django.db import models
from apps.core.exceptions import AlreadyExistError


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def clean(self):
        instance = Tag.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genres"

    def clean(self):
        instance = Genre.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "countries"

    def clean(self):
        instance = Country.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=5)

    class Meta:
        db_table = "language"

    def clean(self):
        instance = Language.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)

    def __str__(self):
        return f"{self.name} - {self.abbreviation}"
