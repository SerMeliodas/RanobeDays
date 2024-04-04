from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from apps.common.services import delete_model

from .models import Chapter
from .types import ChapterDTO

from .serializers import (
    ChapterSerializer,
)

from .services import (
    create_chapter,
    update_chapter
)

from .selectors import (
    get_chapter_by_id,
    get_chapters_list_by_novel
)


class ChapterGetAPI(APIView):
    """API for getting the chapter by id"""

    def get(self, request, pk: int):
        try:
            chapter = get_chapter_by_id(pk=pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Chapter with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        data = ChapterSerializer(chapter).data

        return Response(data=data)


class ChapterGetListByNovelAPI(APIView):
    """API for getting the chapters filtered by novel"""

    def get(self, request, novel_id: int):
        try:
            chapters = get_chapters_list_by_novel(novel_id=novel_id)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Novel with id {novel_id} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        data = ChapterSerializer(chapters, many=True).data

        return Response(data)


class ChapterCreateAPI(APIView):
    """API for creating the chapter instances"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ChapterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chapter = create_chapter(ChapterDTO(**serializer.data))
        data = ChapterSerializer(chapter).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class ChapterUpdateAPI(APIView):
    """API for updating the chapter instances"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, pk: int):
        serializer = ChapterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            chapter = update_chapter(ChapterDTO(
                **serializer.validated_data), pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Chapter with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        data = ChapterSerializer(chapter).data

        return Response(data, status=status.HTTP_200_OK)


class ChapterDeleteAPI(APIView):
    """API for deleting the chapter instances"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk: int):
        try:
            delete_model(model=Chapter, pk=pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Chapter with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)
