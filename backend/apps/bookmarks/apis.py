from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.core.utils import get_response_data

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.core.permissions import IsOwner

from .types import (
    BookmarkObject,
)

from .services import create_bookmark

from .selectors import (
    get_bookmark,
    get_bookmarks
)

from .serializers import (
    BookmarkBaseSerializer,
    BookmarkCreateSerializer,
)


class BookmarkAPI(APIView):
    """API for getting list of bookmarks or creating instances"""

    permission_classes = ((IsAuthenticated & IsOwner) | IsAdminUser,)

    def get(self, request) -> Response:
        bookmarks = get_bookmarks(request.user)

        data = BookmarkBaseSerializer(bookmarks, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = BookmarkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bookmark_object = BookmarkObject(
            **serializer.validated_data, user=request.user)

        bookmark = create_bookmark(bookmark_object)

        data = BookmarkBaseSerializer(bookmark).data
        data = get_response_data(status.HTTP_201_CREATED, data)

        return Response(data=data, status=status.HTTP_201_CREATED)


class BookmarkDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Bookmark"""

    permission_classes = ((IsAuthenticated & IsOwner) | IsAdminUser,)

    def get(self, request, pk: int) -> Response:
        bookmark = get_bookmark(pk)

        data = BookmarkBaseSerializer(bookmark).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        bookmark = get_bookmark(pk)
        self.check_object_permissions(request, bookmark)

        data = BookmarkBaseSerializer(bookmark).data

        bookmark.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)
