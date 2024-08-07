from rest_framework import serializers
from apps.novels.serializers import NovelShortenedSerializer
from apps.users.serializers import UserSerializer


class LibrarySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    user = UserSerializer()


class LibraryCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()


class LibraryItemSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    library = LibrarySerializer()
    novel = NovelShortenedSerializer()


class LibraryItemCreateUpdateSerializer(serializers.Serializer):
    # library = serializers.IntegerField()
    novel = serializers.IntegerField()


class LibraryFilterSerializer(serializers.Serializer):
    user = serializers.IntegerField(min_value=1, required=False)
