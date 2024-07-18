from rest_framework import serializers


class LanguageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(required=False)
    abbreviation = serializers.CharField()


class CountrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()


class TagSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(required=False)


class GenreSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(required=False)
