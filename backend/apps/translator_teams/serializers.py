from rest_framework import serializers
from apps.users.serializers import UserSerializer
from apps.novels.serializers import NovelSerializer


class TranslatorTeamSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=150)
    users = UserSerializer(many=True)
    novels = NovelSerializer(many=True)


class TranslatorTeamDTOSerializer(TranslatorTeamSerializer):
    users = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )
    novels = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )
