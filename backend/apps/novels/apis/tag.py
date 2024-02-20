from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from apps.novels.models import Tag
from apps.novels.types import TagDTO
from apps.novels.serializers import TagSerializer
from apps.common.services import delete_model

from apps.novels.selectors import (
    tag_list,
    get_tag
)


from apps.novels.services import (
    update_tag,
    create_tag
)


class TagListApi(APIView):
    """Api for getting list of tags"""

    def get(self, request) -> Response:
        queryset = tag_list()

        data = TagSerializer(queryset, many=True).data

        return Response(data)


class TagGetApi(APIView):
    """Api for getting the tag by primary key"""

    def get(self, request, pk: int) -> Response:

        try:
            tag = get_tag(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = TagSerializer(tag).data

        return Response(data)


class TagCreateApi(APIView):
    """Api for creating tag instance"""

    def post(self, request) -> Response:
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_tag(TagDTO(**serializer.validated_data))
        data = TagSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TagUpdateApi(APIView):
    """Api for updating an instance of tag"""

    def post(self, request, pk: int) -> Response:
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = update_tag(pk=pk, dto=TagDTO(**serializer.validated_data))
        data = TagSerializer(instance).data

        return Response(data=data, status=status.HTTP_200_OK)


class TagDeleteApi(APIView):
    """Api for deleting an instance of tag"""

    def delete(self, request, pk: int) -> Response:
        try:
            delete_model(model=Tag, pk=pk)
        except ObjectDoesNotExist:
            return Response(data={
                "message": f"Tag with id {pk} does not exist"
            },
                status=status.HTTP_404_NOT_FOUND)

        return Response(data={
            "message": f"The tag with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)
