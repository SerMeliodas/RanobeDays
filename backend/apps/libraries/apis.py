from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.core.permissions import ReadOnly, IsOwner

from apps.core.utils import get_response_data

from .types import (
    LibraryItemObject,
    LibraryObject
)

from .permissions import (
    IsLibraryItemOwner
)

from .serializers import (
    LibrarySerializer,
    LibraryCreateUpdateSerializer,
    LibraryItemSerializer,
    LibraryItemCreateUpdateSerializer,
    LibraryFilterSerializer
)

from .services import (
    create_library,
    update_library,
    create_library_item,
    update_library_item
)

from .selectors import (
    get_library,
    get_libraries,
    get_library_item,
    get_library_items
)


class LibraryAPI(APIView):
    """API thats return list of Library instances or creates the instance"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request) -> Response:
        filter_serializer = LibraryFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        libraries = get_libraries(filters=filter_serializer.validated_data)

        data = LibrarySerializer(libraries, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        library_object = LibraryObject(
            name=serializer.validated_data["name"], user=request.user)

        library = create_library(library_object)

        data = LibrarySerializer(library).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)


class LibraryDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Library"""

    permission_classes = (
        IsAuthenticated | ReadOnly,
        IsOwner | IsAdminUser
    )

    def get(self, request, library_id: int) -> Response:
        library = get_library(library_id)

        data = LibrarySerializer(library).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, library_id: int) -> Response:
        library = get_library(library_id)
        self.check_object_permissions(request, library)

        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        library_object = LibraryObject(
            name=serializer.validated_data['name']
        )

        library = update_library(library, library_object)

        data = LibrarySerializer(library).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, library_id: int) -> Response:
        library = get_library(library_id)
        self.check_object_permissions(request, library)

        data = LibrarySerializer(library).data

        library.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, detail='Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)


class LibraryItemAPI(APIView):
    """API thats return list of LibraryItem instances or
    creates the instance"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request, library_id: int):
        items = get_library_items(library_id)

        data = LibraryItemSerializer(items, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, library_id: int):
        serializer = LibraryItemCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_object = LibraryItemObject(**serializer.validated_data)
        item_object.library = library_id

        item = create_library_item(item_object)

        data = LibraryItemSerializer(item).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)


class LibraryItemDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Library"""

    permission_classes = (
        IsAuthenticated | ReadOnly,
        IsLibraryItemOwner | IsAdminUser
    )

    def get(self, request, library_id: int, library_item_id: int):
        item = get_library_item(library_item_id)

        data = LibraryItemSerializer(item).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, library_id: int, library_item_id: int):
        item = get_library_item(library_item_id)
        self.check_object_permissions(request, item)

        serializer = LibraryItemCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_object = LibraryItemObject(**serializer.validated_data)
        item = update_library_item(item, item_object)

        data = LibraryItemSerializer(item).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, library_id: int, library_item_id: int):
        item = get_library_item(library_item_id)
        self.check_object_permissions(request, item)

        data = LibraryItemSerializer(item).data

        item.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)
