from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from apps.common.services import delete_model
from apps.common.exceptions import AlreadyExistError

from .types import (
    BookmarkObject
)

from .services import (
    create_bookmark
)

from .selectors import (
    get_bookmark,
    get_bookmarks
)

from .serializers import (
    BookmarkSerializer,
    BookmrakCreateSerializer
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

        data = BookmarkSerializer(bookmarks, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookmrakCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bookmark_object = BookmarkObject(
            **serializer.validated_data, user=request.user)

        try:
            bookmark = create_bookmark(bookmark_object)
        except AlreadyExistError as e:
            return Response(data={'message': f'{e}'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = BookmarkSerializer(bookmark).data

        return Response(data=data, status=status.HTTP_200_OK)
