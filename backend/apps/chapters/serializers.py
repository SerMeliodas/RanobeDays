from rest_framework import serializers


class ChapterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(required=False)
    novel = serializers.IntegerField(source='novel.id', required=False)
    text = serializers.CharField(required=False)


class ChapterUpdateSerializer(ChapterSerializer):
    novel = serializers.IntegerField(required=False)
