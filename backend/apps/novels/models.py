from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from apps.common.exceptions import AlreadyExistError


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    class Meta:
        abstract = True


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


class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    novel = models.ForeignKey("Novel", on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = "chapters"
        default_related_name = "chapters"
        ordering = ["novel"]


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
