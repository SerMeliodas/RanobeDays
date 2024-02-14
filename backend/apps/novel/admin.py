from django.contrib import admin
from .models import Novel, Genre, Tag, Chapter


admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Tag)
admin.site.register(Genre)
