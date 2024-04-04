from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseManageAPI(APIView):
    """
    The base class for ManageAPI
        A ManageAPI is a API which is used to dispatch the requests to the
        appropriate API's
    """

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception(
                'VIEWS_BY_METHOD static dictionary variable must be defined \
on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request,
                                                          *args,
                                                          **kwargs)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
