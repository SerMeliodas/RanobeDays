from django.db import models
from django.contrib.auth import get_user_model


class Library(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'libraries'


class LibraryItem(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    novel = models.ForeignKey('novels.Novel', on_delete=models.CASCADE)

    class Meta:
        db_table = 'libraries_items'
