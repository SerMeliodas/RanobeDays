from rest_framework import serializers
from apps.chapters.serializers import ChapterShortenedSerializer
from apps.teams.serializers import TeamShortenedSerializer
from apps.metadata.serializers import (
    TagSerializer,
    CountrySerializer,
    LanguageSerializer,
    GenreSerializer
)

from .models import Novel


class NovelSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.SlugField(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    title = serializers.CharField()
    original_title = serializers.CharField(required=False)

    language = LanguageSerializer()
    translated_language = LanguageSerializer(required=False)

    status = serializers.ChoiceField(Novel.STATUS)

    chapters = ChapterShortenedSerializer(many=True, read_only=True)
    country = CountrySerializer()
    tags = TagSerializer(many=True)
    genres = GenreSerializer(many=True)

    teams = TeamShortenedSerializer(many=True, read_only=True)
    creator = TeamShortenedSerializer(read_only=True)

    synopsys = serializers.CharField(required=False)


class NovelFilterSerializer(serializers.Serializer):
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    order_by = serializers.CharField(required=False)


class NovelCreateSerializer(NovelSerializer):
    country = serializers.IntegerField()
    creator = serializers.IntegerField()
    language = serializers.IntegerField()
    translated_language = serializers.IntegerField(required=False)
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )


class NovelUpdateSerializer(NovelSerializer):
    title = serializers.CharField(required=False)
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )


class NovelListSerializer(NovelSerializer):
    chapters = None
    updated_at = None
    original_title = None
    synopsys = None


class NovelShortenedSerializer(NovelSerializer):
    id = None
    chapters = None
    updated_at = None
    created_at = None
    original_title = None
    synopsys = None
    language = None
    tags = None
    genres = None
    country = None
    teams = None
