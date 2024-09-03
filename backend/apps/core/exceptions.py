from rest_framework.views import exception_handler
from rest_framework.response import Response
from apps.core.utils import get_response_data
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db.models import ObjectDoesNotExist
from rest_framework import status


import logging


logger = logging.getLogger(__name__)


class AlreadyExistError(Exception):
    ...


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    logger.debug(str(exc))

    if isinstance(exc, ObjectDoesNotExist):
        return Response(get_response_data(status.HTTP_400_BAD_REQUEST, str(exc)),
                        status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, DjangoValidationError):
        return Response(get_response_data(status.HTTP_400_BAD_REQUEST, str(exc)),
                        status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, ValidationError):
        return Response(data=get_response_data(exc.status_code, exc.detail),
                        status=exc.status_code)

    if response is not None:
        return Response(get_response_data(response.status_code, str(exc)),
                        response.status_code)

    return response
