from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class TranslatorTeamsListApi(APIView):
    """Api endpoint for getting list of all teams"""

    def get(self, request):
        ...


class TranslatorTeamsCreateApi(APIView):
    """Api endpoint for creating translators teams"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ...


class TranslatorTeamsDeleteApi(APIView):
    """Api endpoint for creating translators teams"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        ...


class TranslatorTeamsUpdateApi(APIView):
    """Api endpoint for creating translators teams"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ...
