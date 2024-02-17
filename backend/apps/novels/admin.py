from django.contrib import admin
from .models import Novel, Tag, Genre

# Register your models here.

admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(Novel)
