from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from apps.metadata.services import (
    update_genre,
    create_genre
)
from apps.metadata.selectors import (
    get_genre,
    genre_list
)

from apps.metadata.types import GenreObject
from apps.metadata.serializers import GenreSerializer
from apps.core.utils import get_response_data
from apps.core.permissions import ReadOnly


class GenreAPI(APIView):
    """API for getting list of genres or creating instances"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request):
        genres = genre_list()

        data = GenreSerializer(genres, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        genre = create_genre(GenreObject(**serializer.validated_data))

        data = GenreSerializer(genre).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_201_CREATED)


class GenreDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request, pk: int):
        genre = get_genre(pk=pk)

        data = GenreSerializer(genre).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data)

    def delete(self, request, pk: int):
        genre = get_genre(pk)
        self.check_object_permissions(request, genre)

        data = GenreSerializer(genre).data

        genre.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data={}, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        genre = get_genre(pk)
        self.check_object_permissions(request, genre)

        serializer = GenreSerializer(data=request.data)
        serializer.is_valid()

        genre = update_genre(genre, GenreObject(**serializer.validated_data))

        data = GenreSerializer(genre).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)
