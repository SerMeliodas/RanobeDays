from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


from apps.common.services import delete_model

from .models import Bookmark

from .types import (
    BookmarkObject,
    BookmarkUpdateObject
)

from .services import (
    create_bookmark,
    update_bookmark
)

from .selectors import (
    get_bookmark,
    get_bookmarks
)

from .serializers import (
    BookmarkBaseSerializer,
    BookmarkCreateSerializer,
    BookmarkUpdateSerializer
)


class BookmarkAPI(APIView):
    """API for getting list of bookmarks or creating instances"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(self.__class__, self).get_permissions()

    def get(self, request):
        bookmarks = get_bookmarks()

        data = BookmarkBaseSerializer(bookmarks, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookmarkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bookmark_object = BookmarkObject(
            **serializer.validated_data, user=request.user)

        bookmark = create_bookmark(bookmark_object)

        data = BookmarkBaseSerializer(bookmark).data

        return Response(data=data, status=status.HTTP_200_OK)


class BookmarkDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Bookmark"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "DELETE", "PATCH":
                self.permission_classes = (IsAuthenticated,)

        return super(self.__class__, self).get_permissions()

    def get(self, request, pk: int):
        bookmark = get_bookmark(pk)

        data = BookmarkBaseSerializer(bookmark).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        delete_model(model=Bookmark, pk=pk)

        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        serializer = BookmarkUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bookmark_object = BookmarkUpdateObject(**serializer.validated_data)
        bookmark = update_bookmark(pk, bookmark_object)

        data = BookmarkBaseSerializer(bookmark).data
        return Response(data=data, status=status.HTTP_200_OK)
