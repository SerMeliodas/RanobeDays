from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    TranslatorTeamSerializer,
    TranslatorTeamDTOSerializer
)

from .types import TranslatorTeamDTO

from .services import (
    create_translator_team,
    update_translator_team,
    add_user_to_translator_team,
    delete_user_from_translator_team,
    add_novel_to_translator_team,
    delete_novel_from_translator_team
)

from .selectors import (
    get_translator_teams_list,
    get_translator_team_by_id,
    get_translator_teams_by_novel_id
)


class TranslatorTeamsListApi(APIView):
    """Api endpoint for getting list of all teams"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        teams_list = get_translator_teams_list()

        data = TranslatorTeamSerializer(teams_list, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)


class TranslatorTeamsCreateApi(APIView):
    """Api endpoint for creating translators teams"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TranslatorTeamDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_translator_team(
            TranslatorTeamDTO(**serializer.validated_data))

        data = TranslatorTeamSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TranslatorTeamsGetApi(APIView):
    """Api endpoint that returns team instance by id"""

    def get(self, request, pk: int):
        try:
            team = get_translator_team_by_id(pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Translator team with id {pk} does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        data = TranslatorTeamSerializer(team)

        return Response(data=data, status=status.HTTP_200_OK)


class TranslatorTeamsDeleteApi(APIView):
    """Api endpoint for creating translators teams"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk: int):
        ...


class TranslatorTeamsUpdateApi(APIView):
    """Api endpoint for creating translators teams"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ...


class TranslatorTeamsDeleteNovelApi(APIView):
    """Api endpoint for deleting from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        ...


class TranslatorTeamsAddNovelApi(APIView):
    """Api endpoint for adding from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ...


class TranslatorTeamsDeleteUserApi(APIView):
    """Api endpoint for deleting from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        ...


class TranslatorTeamsAddUserlApi(APIView):
    """Api endpoint for adding from list of translator team"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ...
