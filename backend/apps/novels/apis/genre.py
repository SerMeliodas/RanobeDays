from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from apps.common.exceptions import AlreadyExistError

from apps.novels.services import (
    update_genre,
    create_genre
)
from apps.novels.selectors import (
    get_genre,
    genre_list
)

from apps.novels.models import Genre
from apps.novels.types import GenreObject
from apps.novels.serializers import GenreSerializer
from apps.common.services import delete_model


class GenreAPI(APIView):
    """API for getting list of genres or creating instances"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(GenreAPI, self).get_permissions()

    def get(self, request):
        genres = genre_list()

        data = GenreSerializer(genres, many=True).data

        return Response(data=data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        try:
            obj = create_genre(GenreObject(**serializer.validated_data))
        except AlreadyExistError as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = GenreSerializer(obj).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class GenreDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)

            case "DELETE", "PATCH":
                self.permission_classes = (IsAuthenticated,)

        return super(GenreDetailAPI, self).get_permissions()

    def get(self, request, pk: int):
        try:
            genre = get_genre(pk=pk)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = GenreSerializer(genre).data

        return Response(data=data)

    def delete(self, request, pk: int):
        try:
            delete_model(model=Genre, pk=pk)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            "message": f"The novel with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        try:
            obj = update_genre(pk, GenreObject(**serializer.validated_data))
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = GenreSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)
