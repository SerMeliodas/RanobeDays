from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from apps.core.utils import get_response_data

from .types import ChapterObject
from .permissions import IsChapterOwner

from .serializers import (
    ChapterSerializer,
    ChapterUpdateSerializer,
    ChapterCreateSerializer
)

from .services import (
    create_chapter,
    update_chapter
)

from .selectors import (
    get_chapter_by_id,
    get_chapters_list
)


class ChapterDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Chapter"""

    permission_classes = (IsChapterOwner | IsAdminUser, )

    def get(self, request, slug: str, pk: int) -> Response:
        chapter = get_chapter_by_id(pk=pk)

        data = ChapterSerializer(chapter).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data)

    def delete(self, request, slug: str, pk: int) -> Response:
        chapter = get_chapter_by_id(pk)
        self.check_object_permissions(request, chapter)

        data = ChapterSerializer(chapter).data

        chapter.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, slug: str, pk: int) -> Response:
        chapter = get_chapter_by_id(pk)
        self.check_object_permissions(request, chapter)

        serializer = ChapterUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        chapter = update_chapter(chapter, ChapterObject(
            **serializer.validated_data))

        data = ChapterSerializer(chapter).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data, status=status.HTTP_200_OK)


class ChapterAPI(APIView):
    """API for getting list of chapters or creating instances"""

    permission_classes = (IsChapterOwner | IsAdminUser, )

    def get(self, request, slug: str) -> Response:
        queryset = get_chapters_list(novel_slug=slug)

        data = ChapterSerializer(queryset, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, slug: str) -> Response:
        serializer = ChapterCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chapter_object = ChapterObject(**serializer.data, novel=slug)

        chapter = create_chapter(chapter_object)

        data = ChapterSerializer(chapter).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_201_CREATED)
