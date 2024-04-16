from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from apps.common.exceptions import AlreadyExistError

from apps.novels.services import (
    create_novel,
    update_novel,
)
from apps.novels.selectors import (
    novel_list,
    get_novel
)

from apps.novels.models import Novel
from apps.novels.types import NovelObject
from apps.novels.serializers import (
    NovelBaseSerializer,
    NovelCreateSerializer,
    NovelUpdateSerializer
)
from apps.common.services import delete_model


class NovelAPI(APIView):
    """API for getting list of novels or creating novel instance"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)
            case "POST":
                self.permission_classes = (IsAuthenticated,)

        return super(NovelAPI, self).get_permissions()

    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        serializer = NovelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = create_novel(NovelObject(**serializer.validated_data))
        except AlreadyExistError as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = NovelBaseSerializer(obj).data

        return Response(data=data,
                        status=status.HTTP_201_CREATED)

    def get(self, request) -> Response:
        novels = novel_list()

        data = NovelBaseSerializer(novels, many=True).data

        return Response(data)


class NovelDetailAPI(APIView):
    """API for getting, deletin, updating the instance of novel"""

    def get_permissions(self):
        match self.request.method:
            case "GET":
                self.permission_classes = (AllowAny,)

            case "DELETE", "PATCH":
                self.permission_classes = (IsAuthenticated,)

        return super(NovelDetailAPI, self).get_permissions()

    def get(self, request, slug: str) -> Response:
        try:
            novel = get_novel(slug=slug)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = NovelBaseSerializer(novel).data

        return Response(data)

    def delete(self, request, slug: str) -> Response:

        try:
            delete_model(model=Novel, slug=slug)
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            "message": f"The novel with slug {slug} was successfuly deleted"
        },
            status=status.HTTP_200_OK)

    def patch(self, request, slug: str) -> Response:
        serializer = NovelUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            obj = update_novel(slug, NovelObject(
                **serializer.validated_data)
            )
        except ObjectDoesNotExist as e:
            return Response(data={"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        data = NovelBaseSerializer(obj).data

        return Response(data=data, status=status.HTTP_200_OK)
