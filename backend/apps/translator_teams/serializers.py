from rest_framework import serializers
from apps.users.serializers import UserSerializer
from apps.novels.serializers import NovelSerializer
from apps.novels.models import Novel
from apps.users.models import User
from .models import TranslatorTeam


class TranslatorTeamSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=150)
    users = UserSerializer(many=True)
    novels = NovelSerializer(many=True)

    def validate_name(self, data):
        if TranslatorTeam.objects.filter(name=data).exists():
            raise serializers.ValidationError(
                "Team with this name already exist"
            )

        return data

    def validate_users(self, data):
        users = User.objects.filter(pk__in=data)
        ids_list = users.values_list('pk', flat=True)

        non_existing_users = list(set(data) - set(ids_list))

        if non_existing_users:
            raise serializers.ValidationError(
                f'User(\'s) with id(\'s) does not exist(\'s):\
{non_existing_users}')

        return data

    def validate_novels(self, data):
        novels = Novel.objects.filter(pk__in=data)
        ids_list = novels.values_list('pk', flat=True)

        non_existing_novels = list(set(data) - set(ids_list))

        if non_existing_novels:
            raise serializers.ValidationError(
                f'Novel(\'s) with id(\'s) does not exist(\'s):\
{non_existing_novels}')

        return data


class TranslatorTeamCreateSerializer(TranslatorTeamSerializer):
    users = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )
    novels = serializers.ListField(
        child=serializers.IntegerField(min_value=0), required=False
    )


class TranslatorTeamUpdateSerializer(TranslatorTeamCreateSerializer):
    name = serializers.CharField(max_length=150, required=False)
    users = serializers.ListField(
        child=serializers.IntegerField(min_value=0),
        required=False
    )
    novels = serializers.ListField(
        child=serializers.IntegerField(min_value=0),
        required=False
    )

    def validate_name(self, data):
        return data
