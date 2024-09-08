from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from apps.core.utils import get_response_data

from apps.users.serializers import UserSerializer

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    SendVerificationEmailSerializer,
    VerifyEmailSerializer,
)

from .services import (
    register,
    login,
    send_verification_email,
    verify_email
)

from .types import (
    RegisterObject,
    LoginObject,
    SendVerificationEmailObject,
    VerifyEmailObject
)


class AuthRegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = register(RegisterObject(**serializer.validated_data))

        data = UserSerializer(user).data
        data = get_response_data(
            status.HTTP_201_CREATED, data, 'User was succesfuly registered')

        return Response(data, status.HTTP_201_CREATED)


class AuthLoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = login(LoginObject(**serializer.validated_data))

        data = get_response_data(status.HTTP_200_OK, {'token': token.key},
                                 'User was succesfuly loged in')

        return Response(data, status.HTTP_200_OK)


class AuthLogoutAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()

        return Response(get_response_data(status=status.HTTP_200_OK,
                                          detail=f"user {request.user.username}  was loged out"),
                        status.HTTP_200_OK)


class SendEmailVerificationAPI(APIView):
    def post(self, request):
        ...


class VerifyEmailAPI(APIView):
    def post(self, request):
        ...
