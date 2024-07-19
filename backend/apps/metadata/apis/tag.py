from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.views import APIView
from rest_framework import status

from apps.metadata.models import Tag
from apps.metadata.types import TagObject
from apps.metadata.serializers import TagSerializer
from apps.common.services import delete_model

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

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request) -> Response:
        queryset = tag_list()

        data = TagSerializer(queryset, many=True).data

        return Response(data)

    def post(self, request) -> Response:
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_tag(TagObject(**serializer.validated_data))

        data = TagSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TagDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, pk: int) -> Response:
        tag = get_tag(pk=pk)

        data = TagSerializer(tag).data

        return Response(data)

    def patch(self, request, pk: int) -> Response:

        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = update_tag(pk=pk, data=TagObject(
            **serializer.validated_data))

        data = TagSerializer(instance).data

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        delete_model(model=Tag, pk=pk)

        return Response(data={
            "message": f"The tag with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)
