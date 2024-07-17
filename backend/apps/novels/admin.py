from django.contrib import admin
from .models import Novel, Tag, Genre, Language, Country

# Register your models here.

admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(Novel)
admin.site.register(Language)
admin.site.register(Country)
