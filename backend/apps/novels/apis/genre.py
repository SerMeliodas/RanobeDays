from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from apps.novels.services import (
    update_genre,
    create_genre
)
from apps.novels.selectors import (
    get_genre,
    genre_list
)

from apps.novels.models import Genre
from apps.novels.types import GenreDTO
from apps.novels.serializers import GenreSerializer
from apps.common.services import delete_model


class GenreListApi(APIView):
    """Api for getting list of genres"""

    def get(self, request):
        genres = genre_list()

        data = GenreSerializer(genres, many=True).data

        return Response(data=data)


class GenreGetApi(APIView):
    """Api for getting genre by id"""

    def get(self, request, pk: int):
        genre = get_genre(pk=pk)

        try:
            data = GenreSerializer(genre).data
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"The genre with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        return Response(data=data)


class GenreCreateApi(APIView):
    """Api for creating genre"""

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        obj = create_genre(GenreDTO(**serializer.validated_data))
        data = GenreSerializer(obj).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class GenreUpdateApi(APIView):
    """Api for updating genre"""

    def post(self, request, pk: int):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        try:
            obj = update_genre(pk, GenreDTO(**serializer.validated_data))
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"The genre with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        data = GenreSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)


class GenreDeleteApi(APIView):
    """Api for deleting genre"""

    def delete(self, request, pk: int):
        try:
            delete_model(model=Genre, pk=pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"The genre with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        return Response(data={
            "message": f"The novel with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)
