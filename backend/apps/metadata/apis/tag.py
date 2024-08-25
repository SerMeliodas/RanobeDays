from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework import status

from apps.metadata.types import TagObject
from apps.metadata.serializers import TagSerializer
from apps.core.utils import get_response_data
from apps.core.permissions import ReadOnly

from apps.metadata.selectors import (
    tag_list,
    get_tag
)


from apps.metadata.services import (
    update_tag,
    create_tag
)


class TagAPI(APIView):
    """API for getting list of tags or creating instances"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request) -> Response:
        queryset = tag_list()

        data = TagSerializer(queryset, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data)

    def post(self, request) -> Response:
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_tag(TagObject(**serializer.validated_data))

        data = TagSerializer(instance).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_201_CREATED)


class TagDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request, pk: int) -> Response:
        tag = get_tag(pk=pk)

        data = TagSerializer(tag).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data)

    def patch(self, request, pk: int) -> Response:
        tag = get_tag(pk)
        self.check_object_permissions(request, tag)

        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tag = update_tag(tag, data=TagObject(
            **serializer.validated_data))

        data = TagSerializer(tag).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        tag = get_tag(pk)
        self.check_object_permissions(request, tag)

        data = TagSerializer(tag).data

        tag.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data=data, status=status.HTTP_200_OK)
