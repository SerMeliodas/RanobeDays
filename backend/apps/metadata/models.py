from django.db import models
from apps.common.exceptions import AlreadyExistError


class BaseMetadataModel(models.Model):
    name = models.CharField(max_length=100)


class Tag(BaseMetadataModel):
    class Meta:
        db_table = "tags"

    def clean(self):
        instance = Tag.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Genre(BaseMetadataModel):
    class Meta:
        db_table = "genres"

    def clean(self):
        instance = Genre.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Country(BaseMetadataModel):
    class Meta:
        db_table = "countries"

    def clean(self):
        instance = Country.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Language(BaseMetadataModel):
    abbreviation = models.CharField(max_length=5)

    class Meta:
        db_table = "language"

    def clean(self):
        instance = Language.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)
