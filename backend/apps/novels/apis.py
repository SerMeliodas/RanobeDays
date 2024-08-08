from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status

from apps.core.utils import get_response_data

from apps.novels.services import (
    create_novel,
    update_novel,
)
from apps.novels.selectors import (
    novel_list,
    get_novel
)

from apps.core.pagination import (
    get_paginated_response
)
from apps.teams.permissions import IsTeamUser
from apps.novels.types import NovelObject
from apps.novels.serializers import (
    NovelSerializer,
    NovelCreateSerializer,
    NovelUpdateSerializer,
    NovelFilterSerializer,
    NovelListSerializer
)


class NovelAPI(APIView):
    """API for getting list of novels or creating novel instance"""

    permission_classes = (IsAuthenticatedOrReadOnly,
                          (IsAdminUser | IsTeamUser))

    def post(self, request) -> Response:
        serializer = NovelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        novel = create_novel(NovelObject(**serializer.validated_data))

        data = NovelSerializer(novel).data

        return Response(data=get_response_data(status.HTTP_201_CREATED, data),
                        status=status.HTTP_201_CREATED)

    def get(self, request) -> Response:
        filter_serializer = NovelFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        novels = novel_list(filters=filter_serializer.validated_data)

        return get_paginated_response(
            serializer_class=NovelListSerializer,
            queryset=novels,
            view=self,
            request=request
        )


class NovelDetailAPI(APIView):
    """API for getting, deletin, updating the instance of novel"""

    permission_classes = (IsAuthenticatedOrReadOnly,
                          (IsAdminUser | IsTeamUser))

    def get(self, request, slug: str) -> Response:
        novel = get_novel(slug=slug)

        data = NovelSerializer(novel).data

        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data)

    def delete(self, request, slug: str) -> Response:
        novel = get_novel(slug)
        self.check_object_permissions(request, novel)

        novel.delete()

        return Response(data={}, status=status.HTTP_200_OK)

    def patch(self, request, slug: str) -> Response:
        novel = get_novel(slug)
        self.check_object_permissions(request, novel)

        serializer = NovelUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        novel = update_novel(novel, NovelObject(**serializer.validated_data))

        data = NovelSerializer(novel).data

        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)
