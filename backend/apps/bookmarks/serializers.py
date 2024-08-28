from rest_framework import serializers
from apps.users.serializers import UserSerializer


class BookmarkBaseSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user = UserSerializer()
    novel = serializers.IntegerField(source='novel.id')
    chapter = serializers.IntegerField(source='chapter.id')


class BookmarkCreateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    novel = serializers.IntegerField()
    chapter = serializers.IntegerField()
