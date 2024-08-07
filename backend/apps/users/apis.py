from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.core.utils import get_response_data


from .selectors import get_user
from .types import UserObject, UserNewPassObject

from .services import (
    update_user,
    new_password
)

from .serializers import (
    UserSerializer,
    UserUpdateSerializer,
    UserChangePasswordSerializer
)

from .permissions import IsUser


class UserDetailAPI(APIView):
    permission_classes = (IsUser,)

    def get(self, request, username: str):
        user = get_user(username=username)

        data = get_response_data(
            status.HTTP_200_OK, data=UserSerializer(user).data)

        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, username: str):
        user = get_user(username)
        self.check_object_permissions(request, user)

        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = update_user(username, UserObject(**serializer.validated_data))

        data = UserSerializer(user).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)


class UserPasswordDetailAPI(APIView):
    def patch(self, request, username: str):
        user = get_user(username)
        self.check_object_permissions(request, user)

        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)

        user = new_password(username, UserNewPassObject(
            **serializer.validated_data))

        data = UserSerializer(user).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data=data, status=status.HTTP_200_OK)
