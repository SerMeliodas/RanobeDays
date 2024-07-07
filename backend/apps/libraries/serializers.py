from rest_framework import serializers
from apps.novels.serializers import NovelSerializer
from apps.users.serializers import UserSerializer


class LibrarySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    user = UserSerializer()


class LibraryCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    # user = serializers.IntegerField()


class LibraryItemSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    library = LibrarySerializer()
    novel = NovelSerializer()


class LibraryItemCreateUpdateSerializer(serializers.Serializer):
    library = serializers.IntegerField()
    novel = serializers.IntegerField()
