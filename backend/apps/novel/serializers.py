from rest_framework import serializers
from .models import Novel, Chapter, Genre, Tag


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ["id", "title", "chapter_set", "genres", "tags"]
