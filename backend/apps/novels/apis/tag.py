from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from apps.novels.types import TagDTO
from apps.novels.serializers import TagSerializer

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

    def get(self, request):
        queryset = tag_list()

        data = TagSerializer(queryset, many=True).data

        return Response(data)


class TagGetApi(APIView):
    """Api for getting the tag by primary key"""

    def get(self, request, pk: int):
        tag = get_tag(pk=pk)

        data = TagSerializer(tag).data

        return Response(data)


class TagCreateApi(APIView):
    """Api for creating tag instance"""

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_tag(TagDTO(**serializer.validated_data))
        data = TagSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TagUpdateApi(APIView):
    """Api for updating an instance of tag"""

    def post(self, request, pk: int):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = update_tag(pk=pk, dto=TagDTO(**serializer.validated_data))
        data = TagSerializer(instance).data

        return Response(data=data, status=status.HTTP_200_OK)
