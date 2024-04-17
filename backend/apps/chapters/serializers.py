from rest_framework import serializers


class ChapterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    novel = serializers.IntegerField(source='novel.id', required=False)
    text = serializers.CharField()


class ChapterUpdateSerializer(ChapterSerializer):
    title = serializers.CharField(required=False)
    novel = serializers.IntegerField(required=False)
    text = serializers.CharField(required=False)
