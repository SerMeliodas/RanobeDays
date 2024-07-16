from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.exceptions import AlreadyExistError
from apps.common.models import BaseModel


class Novel(BaseModel):
    STATUS = (
        (1, _("Continues")),
        (2, _("Finished")),
        (3, _("Frozen"))
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=title, db_index=True)
    original_title = models.CharField(max_length=255, null=True)
    languages = models.ForeignKey("Languages", db_index=True,
                                  on_delete=models.DO_NOTHING,
                                  related_name="novels",
                                  default=None)
    translate_language = models.ForeignKey("Languages", db_index=True,
                                           on_delete=models.DO_NOTHING,
                                           related_name="translated_novels",
                                           default=None)
    status = models.IntegerField(choices=STATUS, default=1)
    tags = models.ManyToManyField("Tag", db_index=True)
    genres = models.ManyToManyField("Genre", db_index=True)
    synopsys = models.TextField(null=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "novels"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        instance = Novel.objects.filter(title=self.title)

        if instance.exists():
            raise AlreadyExistError(self)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tags"

    def clean(self):
        instance = Tag.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genres"

    def clean(self):
        instance = Genre.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "countries"

    def clean(self):
        instance = Country.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)


class Languages(models.Model):
    name = models.CharField(max_length=50)
    abbrevation = models.CharField(max_length=5)

    class Meta:
        db_table = "languages"

    def clean(self):
        instance = Languages.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)
