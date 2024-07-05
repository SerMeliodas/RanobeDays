from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.common.services import delete_model
from .models import TranslatorTeam
from .serializers import (
    TranslatorTeamSerializer,
    TranslatorTeamCreateSerializer,
    TranslatorTeamUpdateSerializer
)

from .types import TranslatorTeamObject

from .services import (
    create_translator_team,
    update_translator_team,
)

from .selectors import (
    get_translator_teams,
    get_translator_team,
)


class TranslatorTeamsAPI(APIView):
    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(TranslatorTeamsAPI, self).get_permissions()

    def get(self, request):
        teams_list = get_translator_teams()
        data = TranslatorTeamSerializer(teams_list, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TranslatorTeamCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_translator_team(
            TranslatorTeamObject(**serializer.validated_data))

        data = TranslatorTeamSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TranslatorTeamsDetailAPI(APIView):
    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "PATCH", "DELETE":
                self.permission_classes = (IsAuthenticated,)

        return super(TranslatorTeamsDetailAPI, self).get_permissions()

    def get(self, request, pk: int):
        team = get_translator_team(pk)

        data = TranslatorTeamSerializer(team).data

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        delete_model(model=TranslatorTeam, pk=pk)

        return Response(data={}, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        serializer = TranslatorTeamUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        team = update_translator_team(
            pk, TranslatorTeamObject(**serializer.validated_data))

        data = TranslatorTeamSerializer(team).data

        return Response(data=data, status=status.HTTP_200_OK)
