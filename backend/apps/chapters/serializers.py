from rest_framework import serializers
from apps.novels.serializers import NovelSerializer


class ChapterSerializer(serializers.Serializer):
    title = serializers.CharField()
    novel = NovelSerializer()
    text = serializers.CharField()


class ChapterDTOSerializer(ChapterSerializer):
    novel = serializers.IntegerField()
