from rest_framework import serializers
from apps.users.serializers import UserSerializer


class BookmarkBaseSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user = UserSerializer()
    chapter = serializers.IntegerField(source='chapter.id')


class BookmarkCreateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    chapter = serializers.IntegerField()
