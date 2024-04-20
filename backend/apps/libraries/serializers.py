from rest_framework import serializers
from apps.novels.serializers import NovelBaseSerializer
from apps.users.serializers import UserSerializer


class LibrarySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    user = UserSerializer()


class LibraryItemSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    library = LibrarySerializer()
    novel = NovelBaseSerializer()
