from rest_framework import serializers


class ChapterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    novel = serializers.IntegerField(source='novel.id')
    text = serializers.CharField()
