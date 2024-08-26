from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from apps.metadata.types import CountryObject
from apps.metadata.serializers import CountrySerializer
from apps.core.utils import get_response_data

from apps.core.permissions import ReadOnly

from apps.metadata.selectors import (
    country_list,
    get_country
)


from apps.metadata.services import (
    update_country,
    create_country
)


class CountryAPI(APIView):
    """API for getting list of country or creating instances"""

    permission_classes = (IsAuthenticated | ReadOnly, )

    def get(self, request) -> Response:
        queryset = country_list()

        data = CountrySerializer(queryset, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data)

    def post(self, request) -> Response:
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_country(CountryObject(**serializer.validated_data))

        data = CountrySerializer(instance).data
        data = get_response_data(status.HTTP_201_CREATED, data)

        return Response(data=data, status=status.HTTP_201_CREATED)


class CountryDetailAPI(APIView):
    """API for getting, deleting, updating the instance of country"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request, pk: int) -> Response:
        tag = get_country(pk=pk)

        data = CountrySerializer(tag).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data)

    def patch(self, request, pk: int) -> Response:
        country = get_country(pk)
        self.check_object_permissions(request, country)

        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        country = update_country(country, data=CountryObject(
            **serializer.validated_data))

        data = CountrySerializer(country).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        country = get_country(pk)
        self.check_object_permissions(request, country)

        data = CountrySerializer(country).data

        country.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)
