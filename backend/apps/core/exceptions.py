from rest_framework.views import exception_handler
from rest_framework.response import Response
from apps.core.utils import get_response_data


import logging


logger = logging.getLogger(__name__)


class AllreadyExists(Exception):
    ...


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response(get_response_data(response.status_code, str(exc)),
                        response.status_code)

    return response
