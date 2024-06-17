from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from apps.common.services import delete_model

from .models import Chapter
from .types import ChapterObject

from .serializers import (
    ChapterSerializer,
    ChapterUpdateSerializer,
    ChapterFilterSerializer
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

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "DELETE", "PATCH":
                self.permission_classes = (IsAuthenticated,)

        return super(ChapterDetailAPI, self).get_permissions()

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

    def delete(self, request, pk: int):
        try:
            delete_model(model=Chapter, pk=pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Chapter with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        serializer = ChapterUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            chapter = update_chapter(ChapterObject(
                **serializer.validated_data), pk)
        except ObjectDoesNotExist as e:
            return Response(data={
                "message": f"{e}"
            },
                status=status.HTTP_404_NOT_FOUND)

        data = ChapterSerializer(chapter).data

        return Response(data, status=status.HTTP_200_OK)


class ChapterAPI(APIView):
    """API for getting list of chapters or creating instances"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(ChapterAPI, self).get_permissions()

    def get(self, request):
        filter_serializer = ChapterFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        queryset = get_chapters_list(filters=filter_serializer.validated_data)

        data = ChapterSerializer(queryset, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ChapterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chapter = create_chapter(ChapterObject(**serializer.data))
        data = ChapterSerializer(chapter).data

        return Response(data=data, status=status.HTTP_201_CREATED)
