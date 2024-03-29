from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)


class NovelSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    slug = serializers.SlugField(required=False)
    title = serializers.CharField()
    tags = TagSerializer(many=True)
    genres = GenreSerializer(many=True)


class NovelDTOSerializer(NovelSerializer):
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )
