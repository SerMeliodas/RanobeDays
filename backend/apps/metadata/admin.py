from django.contrib import admin
from .models import Tag, Country, Language, Genre


admin.site.register(Tag)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Genre)
