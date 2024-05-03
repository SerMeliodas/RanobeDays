from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from apps.common.exceptions import AlreadyExistError
from apps.common.services import delete_model

from .models import Library

from .types import (
    LibraryItemObject,
    LibraryObject
)

from .serializers import (
    LibrarySerializer,
    LibraryCreateUpdateSerializer
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
    get_library_item
)


class LibraryAPI(APIView):
    """API thats return list of Library instances or creates the instance"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)

            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(self.__class__, self).get_permissions()

    def get(self, request) -> Response:
        libraries = get_libraries()

        data = LibrarySerializer(libraries, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        library_object = LibraryObject(
            name=serializer.validated_data["name"], user=request.user)

        try:
            library = create_library(library_object)
        except AlreadyExistError as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = LibrarySerializer(library).data
        return Response(data=data, status=status.HTTP_200_OK)


class LibraryDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Library"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)

            case "DELETE", "PATCH":
                self.permission_classes = (IsAuthenticated,)

        return super(self.__class__, self).get_permissions()

    def get(self, request, pk: int) -> Response:
        try:
            library = get_library(pk)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_404_NOT_FOUND)

        data = LibrarySerializer(library).data

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int) -> Response:
        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            library_object = LibraryObject(
                name=serializer.validated_data['name'], user=request.user)

            library = update_library(pk, library_object)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_404_NOT_FOUND)

        data = LibrarySerializer(library).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        try:
            delete_model(model=Library, pk=pk)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(data={}, status=status.HTTP_200_OK)
