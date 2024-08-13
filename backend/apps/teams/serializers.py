from rest_framework import serializers
from apps.users.serializers import UserSerializer
from apps.novels.models import Novel
from apps.users.models import User
from .models import Team


class TeamSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    team_type = serializers.IntegerField()
    name = serializers.CharField(max_length=150)
    users = UserSerializer(many=True)
    novels = serializers.SerializerMethodField()
    description = serializers.CharField(required=False)

    def get_novels(self, instance):
        from apps.novels.serializers import NovelShortenedSerializer
        novels = Novel.objects.filter(teams=instance)
        return NovelShortenedSerializer(novels, many=True).data

    def validate_name(self, data):
        if Team.objects.filter(name=data).exists():
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

    def validate_team_type(self, data):
        if data not in range(1, len(Team.TEAM_TYPES)+1):
            raise serializers.ValidationError("Invalid Team Type")

        return data


class TeamCreateSerializer(TeamSerializer):
    users = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )
    novels = serializers.ListField(
        child=serializers.IntegerField(min_value=0), required=False
    )


class TeamUpdateSerializer(TeamCreateSerializer):
    name = serializers.CharField(max_length=150, required=False)
    team_type = serializers.IntegerField(required=False)
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


class TeamFilterSerializer(serializers.Serializer):
    team_type = serializers.IntegerField(required=False)

    users = serializers.ListField(
        child=serializers.IntegerField(min_value=0), required=False
    )
    novels = serializers.ListField(
        child=serializers.IntegerField(min_value=0), required=False
    )


class TeamShortenedSerializer(TeamSerializer):
    users = None
    novels = None
    description = None
