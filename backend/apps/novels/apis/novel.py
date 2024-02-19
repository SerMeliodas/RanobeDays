from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.novels.types import NovelDTO
from apps.novels.serializers import NovelSerializer, NovelDTOSerializer


from apps.novels.services import (
    create_novel,
    update_novel
)
from apps.novels.selectors import (
    novel_list,
    get_novel
)


class NovelListApi(APIView):
    """Api view to get the Novel list"""

    def get(self, request) -> Response:
        novels = novel_list()

        data = NovelSerializer(novels, many=True).data

        return Response(data)


class NovelGetApi(APIView):
    """Api for getting novel by slug field"""

    def get(self, request, slug: str) -> Response:
        novel = get_novel(slug=slug)

        data = NovelSerializer(novel).data

        return Response(data)


class NovelCreatApi(APIView):
    """Api for creating Novel"""

    def post(self, request) -> Response:
        serializer = NovelDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = create_novel(NovelDTO(**serializer.validated_data))
        data = NovelSerializer(obj).data

        return Response(data=data,
                        status=status.HTTP_201_CREATED)


class NovelUpdateApi(APIView):
    """Api for updating an instance of Novel"""

    def post(self, request, pk: int) -> Response:
        serializer = NovelDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = update_novel(pk, NovelDTO(**serializer.validated_data))
        data = NovelSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)