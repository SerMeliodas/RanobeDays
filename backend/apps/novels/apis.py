from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from apps.novels.services import (
    create_novel,
    update_novel,
)
from apps.novels.selectors import (
    novel_list,
    get_novel
)

from apps.teams.permissions import IsInTeam
from apps.novels.models import Novel
from apps.novels.types import NovelObject
from apps.novels.serializers import (
    NovelSerializer,
    NovelCreateSerializer,
    NovelUpdateSerializer,
    NovelFilterSerializer
)
from apps.common.services import delete_model


class NovelAPI(APIView):
    """API for getting list of novels or creating novel instance"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request) -> Response:
        serializer = NovelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = create_novel(NovelObject(**serializer.validated_data))

        data = NovelSerializer(obj).data

        return Response(data=data,
                        status=status.HTTP_201_CREATED)

    def get(self, request) -> Response:
        filter_serializer = NovelFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        novels = novel_list(filters=filter_serializer.validated_data)

        data = NovelSerializer(novels, many=True).data

        return Response(data)


class NovelDetailAPI(APIView):
    """API for getting, deletin, updating the instance of novel"""

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, slug: str) -> Response:
        novel = get_novel(slug=slug)

        data = NovelSerializer(novel).data

        return Response(data)

    def delete(self, request, slug: str) -> Response:
        delete_model(model=Novel, slug=slug)

        return Response(data={}, status=status.HTTP_200_OK)

    def patch(self, request, slug: str) -> Response:
        novel = get_novel(slug)
        self.check_object_permissions(request, novel)

        serializer = NovelUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        obj = update_novel(slug, NovelObject(**serializer.validated_data))

        data = NovelSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)
