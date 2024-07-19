from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status


from apps.metadata.services import (
    update_genre,
    create_genre
)
from apps.metadata.selectors import (
    get_genre,
    genre_list
)

from apps.metadata.models import Genre
from apps.metadata.types import GenreObject
from apps.metadata.serializers import GenreSerializer
from apps.common.services import delete_model


class GenreAPI(APIView):
    """API for getting list of genres or creating instances"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        genres = genre_list()

        data = GenreSerializer(genres, many=True).data

        return Response(data=data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        obj = create_genre(GenreObject(**serializer.validated_data))

        data = GenreSerializer(obj).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class GenreDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk: int):
        genre = get_genre(pk=pk)

        data = GenreSerializer(genre).data

        return Response(data=data)

    def delete(self, request, pk: int):
        delete_model(model=Genre, pk=pk)

        return Response(data={}, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        obj = update_genre(pk, GenreObject(**serializer.validated_data))

        data = GenreSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)
