from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .dataclasses import NovelDTO
from .serializers import NovelSerializer


from .services import (
    create_novel
)
from .selectors import (
    novel_list,
    get_novel
)


class NovelListApi(APIView):
    """Api view to get the Novel list"""

    def get(self, request):
        novels = novel_list()

        data = NovelSerializer(novels, many=True).data

        return Response(data)


class NovelGetApi(APIView):

    def get(self, request, slug):
        novel = get_novel(slug=slug)

        data = NovelSerializer(novel).data

        return Response(data)


class NovelCreatApi(APIView):
    """Api for creating Novel"""

    def post(self, request):
        serializer = NovelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = create_novel(NovelDTO(**serializer.validated_data))
        data = NovelSerializer(obj).data

        return Response(data=data,
                        status=status.HTTP_201_CREATED)
