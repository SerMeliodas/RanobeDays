from rest_framework import serializers
from apps.novels.serializers import NovelBaseSerializer
from apps.chapters.serializers import ChapterSerializer
from apps.users.serializers import UserSerializer


class BookmarkSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user = UserSerializer()
    novel = NovelBaseSerializer()
    chapter = ChapterSerializer()


class BookmrakCreateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    novel = serializers.IntegerField()
    chapter = serializers.IntegerField()
