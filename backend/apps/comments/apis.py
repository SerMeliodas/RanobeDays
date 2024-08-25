from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.core.permissions import IsOwner, ReadOnly

from apps.core.utils import get_response_data
from apps.core.pagination import get_paginated_response

from .serializers import (
    CommentSerializer,
    CommentFilterSerializer,
    CommentCreateSerializer
)

from .services import create_comment
from .types import CommentObject
from .selectors import get_comments, get_comment


class CommentAPI(APIView):
    permission_classes = (IsAuthenticated | ReadOnly,)

    def get(self, request) -> Response:
        filter_serializer = CommentFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        comments = get_comments(filters=filter_serializer.validated_data)

        return get_paginated_response(
            serializer_class=CommentSerializer,
            queryset=comments,
            view=self,
            request=request
        )

    def post(self, request) -> Response:
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = create_comment(CommentObject(
            **serializer.data, user=request.user))

        data = CommentSerializer(comment).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data, status.HTTP_200_OK)


class CommentDetailAPI(APIView):
    permission_classes = (IsAuthenticated, IsOwner | IsAdminUser,)

    def delete(self, request, pk: int) -> Response:
        comment = get_comment(pk)
        self.check_object_permissions(request, comment)

        data = CommentSerializer(comment).data

        comment.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data, status.HTTP_200_OK)
