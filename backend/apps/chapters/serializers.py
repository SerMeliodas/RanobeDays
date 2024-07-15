from rest_framework import serializers


class ChapterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    novel = serializers.IntegerField(source="novel.id", required=False)
    team = serializers.IntegerField(source="team.id", required=False)
    text = serializers.CharField()


class ChapterFilterSerializer(serializers.Serializer):
    novel = serializers.IntegerField(min_value=1, required=False)
    order_by = serializers.CharField(required=False)


class ChapterUpdateSerializer(ChapterSerializer):
    title = serializers.CharField(required=False)
    novel = serializers.IntegerField(required=False)
    text = serializers.CharField(required=False)
