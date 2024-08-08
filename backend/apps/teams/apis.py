from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from apps.core.utils import get_response_data

from .permissions import IsTeamUser
from .serializers import (
    TeamSerializer,
    TeamCreateSerializer,
    TeamUpdateSerializer,
    TeamFilterSerializer
)

from .types import TeamObject

from .services import (
    create_team,
    update_team,
)

from .selectors import (
    get_teams,
    get_team,
)


class TeamsAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,
                          (IsAdminUser | IsTeamUser))

    def get(self, request):
        filter_serializer = TeamFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        team_list = get_teams(filters=filter_serializer.validated_data)

        data = TeamSerializer(team_list, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeamCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_team(
            TeamObject(**serializer.validated_data))

        data = TeamSerializer(instance).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_201_CREATED)


class TeamsDetailAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,
                          (IsAdminUser | IsTeamUser))

    def get(self, request, pk: int):
        team = get_team(pk)

        data = TeamSerializer(team).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        team = get_team(pk)
        self.check_object_permissions(request, team)

        data = TeamSerializer(team).data

        team.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        team = get_team(pk)
        self.check_object_permissions(request, team)

        serializer = TeamUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        team = update_team(
            team, TeamObject(**serializer.validated_data))

        data = TeamSerializer(team).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)
