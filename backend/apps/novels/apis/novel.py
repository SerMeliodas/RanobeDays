from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from apps.common.exceptions import AlreadyExistError

from apps.novels.services import (
    create_novel,
    update_novel,
)
from apps.novels.selectors import (
    novel_list,
    get_novel
)

from apps.novels.models import Novel
from apps.novels.types import NovelDTO
from apps.novels.serializers import NovelSerializer, NovelDTOSerializer
from apps.common.services import delete_model


class NovelListApi(APIView):
    """Api view to get the Novel list"""

    def get(self, request) -> Response:
        novels = novel_list()

        data = NovelSerializer(novels, many=True).data

        return Response(data)


class NovelGetApi(APIView):
    """Api for getting novel by slug field"""

    def get(self, request, slug: str) -> Response:
        try:
            novel = get_novel(slug=slug)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = NovelSerializer(novel).data

        return Response(data)


class NovelCreatApi(APIView):
    """Api for creating Novel"""

    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        serializer = NovelDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = create_novel(NovelDTO(**serializer.validated_data))
        except AlreadyExistError as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = NovelSerializer(obj).data

        return Response(data=data,
                        status=status.HTTP_201_CREATED)


class NovelUpdateApi(APIView):
    """Api for updating an instance of Novel"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, pk: int) -> Response:
        serializer = NovelDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = update_novel(pk, NovelDTO(**serializer.validated_data))
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = NovelSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)


class NovelDeleteApi(APIView):
    """Api for deleting novels from db"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk: int) -> Response:
        try:
            delete_model(model=Novel, pk=pk)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            "message": f"The novel with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)
