from django.core.exceptions import ObjectDoesNotExist
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

from .types import TranslatorTeamDTO

from .services import (
    create_translator_team,
    update_translator_team,
)

from .selectors import (
    get_translator_teams_list,
    get_translator_team_by_id,
)


class TranslatorTeamsListOrCreateAPI(APIView):

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(TranslatorTeamsListOrCreateAPI, self).get_permissions()

    def get(self, request):
        teams_list = get_translator_teams_list()
        data = TranslatorTeamSerializer(teams_list, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TranslatorTeamCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_translator_team(
            TranslatorTeamDTO(**serializer.validated_data))

        data = TranslatorTeamSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TranslatorTeamsGetDeleteUpdateAPI(APIView):

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "PATCH", "DELETE":
                self.permission_classes = (IsAuthenticated,)

        return super(TranslatorTeamsGetDeleteUpdateAPI, self).get_permissions()

    def get(self, request, pk: int):
        try:
            team = get_translator_team_by_id(pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Translator team with id {pk} does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        data = TranslatorTeamSerializer(team)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        try:
            delete_model(model=TranslatorTeam, pk=pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Translator team with id {pk} does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response(data={
            "message": f"The translators team with id {pk} \
was successfuly deleted"
        }, status=status.HTTP_200_OK)

    def post(self, request, pk: int):
        serializer = TranslatorTeamUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            team = update_translator_team(
                pk, TranslatorTeamDTO(**serializer.validated_data))

        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_404_NOT_FOUND)

        data = TranslatorTeamSerializer(team).data

        return Response(data=data, status=status.HTTP_200_OK)


class TranslatorTeamsDeleteNovelAPI(APIView):
    """API endpoint for deleting from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        ...


class TranslatorTeamsAddNovelAPI(APIView):
    """API endpoint for adding from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        ...


class TranslatorTeamsDeleteUserAPI(APIView):
    """API endpoint for deleting from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        ...


class TranslatorTeamsAddUserlAPI(APIView):
    """API endpoint for adding from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        ...
