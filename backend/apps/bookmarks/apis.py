from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status


from apps.common.services import delete_model
from apps.core.utils import get_response_data

from .permissions import IsBookmarkOwner
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

    permission_classes = (IsBookmarkOwner | IsAdminUser, )

    def get(self, request):
        bookmarks = get_bookmarks(request.user)

        data = BookmarkBaseSerializer(bookmarks, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookmarkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bookmark_object = BookmarkObject(
            **serializer.validated_data, user=request.user)

        bookmark = create_bookmark(bookmark_object)

        data = BookmarkBaseSerializer(bookmark).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)


class BookmarkDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Bookmark"""

    permission_classes = (IsBookmarkOwner | IsAdminUser, )

    def get(self, request, pk: int):
        bookmark = get_bookmark(pk)

        data = BookmarkBaseSerializer(bookmark).data
        data = get_response_data(status.HTTP_200_OK, data)

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
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)
