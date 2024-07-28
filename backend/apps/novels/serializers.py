from rest_framework import serializers
from apps.chapters.serializers import ChapterShortenedSerializer
from apps.metadata.serializers import (
    TagSerializer,
    CountrySerializer,
    LanguageSerializer,
    GenreSerializer
)


class NovelSerializer(serializers.Serializer):
    STATUS = (
        (1, "Continues"),
        (2, "Finished"),
        (3, "Frozen")
    )

    id = serializers.ReadOnlyField()
    slug = serializers.SlugField(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    title = serializers.CharField()
    original_title = serializers.CharField(required=False)

    language = LanguageSerializer()
    translate_language = LanguageSerializer()

    status = serializers.ChoiceField(STATUS)

    chapters = ChapterShortenedSerializer(many=True, read_only=True)
    country = CountrySerializer()
    tags = TagSerializer(many=True)
    genres = GenreSerializer(many=True)

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
    language = serializers.IntegerField()
    translate_language = serializers.IntegerField()
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
