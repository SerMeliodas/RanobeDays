from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)


class NovelSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.SlugField(required=False)
    title = serializers.CharField()
    tags = TagSerializer(many=True)
    genres = GenreSerializer(many=True)
