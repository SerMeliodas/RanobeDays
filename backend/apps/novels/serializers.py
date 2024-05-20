from rest_framework import serializers
from apps.chapters.serializers import ChapterNovelSerializer


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


# Novel serializers
class NovelBaseSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    slug = serializers.SlugField(required=False)
    chapters = ChapterNovelSerializer(many=True, required=False)
    title = serializers.CharField()
    tags = TagSerializer(many=True)
    genres = GenreSerializer(many=True)


class NovelCreateSerializer(NovelBaseSerializer):
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )


class NovelUpdateSerializer(NovelBaseSerializer):
    title = serializers.CharField(required=False)
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
