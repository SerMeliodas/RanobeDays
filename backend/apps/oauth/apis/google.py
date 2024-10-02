from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import redirect
from apps.core.utils import get_response_data

from ..types import GoogleLoginObject
from ..services import GoogleLoginRegisterService
from ..serializers import GoogleLoginSerializer


class GoogleLoginRedirectAPI(APIView):
    def get(self, request):
        google_service = GoogleLoginRegisterService()

        auth_url, state = google_service.get_auth_url()

        request.session['google_oauth2_state'] = state

        return redirect(auth_url)


class GoogleLoginAPI(APIView):
    def get(self, request):
        serializer = GoogleLoginSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        # TODO: Make request validating in service

        login_object = GoogleLoginObject(**serializer.validated_data)

        if login_object.error is not None:
            return Response(get_response_data(
                status.HTTP_400_BAD_REQUEST, detail=login_object.error
            ), status.HTTP_400_BAD_REQUEST)

        if login_object.code is None or \
                login_object.state is None:
            return Response(get_response_data(
                status.HTTP_400_BAD_REQUEST, detail="Code and state are required"
            ), status.HTTP_400_BAD_REQUEST)

        session_state = request.session.get('google_oauth2_state')

        if session_state is None:
            return Response(get_response_data(
                status.HTTP_400_BAD_REQUEST, detail='CSRF check failes'
            ), status.HTTP_400_BAD_REQUEST)

        del request.session['google_oauth2_state']

        if login_object.state != session_state:
            return Response()

        google_service = GoogleLoginRegisterService()
        token = google_service.proced_user(login_object.code)

        return Response(get_response_data(status.HTTP_200_OK, {"token": token.key}),)
