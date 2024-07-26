from django.db import models
from django.contrib.auth import get_user_model

from apps.common.models import BaseModel
from apps.core.exceptions import AlreadyExistError


class Library(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def clean(self):
        instance = Library.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)

    class Meta:
        db_table = 'libraries'
        ordering = ['user']


class LibraryItem(BaseModel):
    library = models.ForeignKey(
        Library, on_delete=models.CASCADE, related_name='items'
    )
    novel = models.ForeignKey('novels.Novel', on_delete=models.CASCADE)

    def clean(self):
        instance = LibraryItem.objects.filter(name=self.name)

        if instance.exists():
            raise AlreadyExistError(self)

    class Meta:
        db_table = 'libraries_items'
        ordering = ['library', '-created_at']
