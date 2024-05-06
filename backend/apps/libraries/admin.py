from django.contrib import admin
from .models import LibraryItem, Library


admin.site.register(Library)
admin.site.register(LibraryItem)
