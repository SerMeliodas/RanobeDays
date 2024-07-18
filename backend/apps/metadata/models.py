from django.db import models
from apps.common.exceptions import AlreadyExistError


class BaseMetadataModel(models.Model):
    name = models.CharField(max_length=100)

    def clean(self):
        instance = self.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Tag(BaseMetadataModel):
    class Meta:
        db_table = "tags"


class Genre(BaseMetadataModel):
    class Meta:
        db_table = "genres"


class Country(BaseMetadataModel):
    class Meta:
        db_table = "countries"


class Language(BaseMetadataModel):
    abbreviation = models.CharField(max_length=5)

    class Meta:
        db_table = "language"
