from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied

from django.db.models import Model
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from apps.core.utils import get_response_data

import logging


logger = logging.getLogger(__name__)


class AlreadyExistError(Exception):
    """Raised when the instance of model is already exist in data base"""

    def __init__(self, instance: Model):
        self.message = f"{instance.__class__.__name__} already have \
the same instance in db"

        super().__init__(self.message)


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        print(11)
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_401_UNAUTHORIZED,
                                               detail=str(exc)),
                        status=status.HTTP_401_UNAUTHORIZED)

    if isinstance(exc, NotAuthenticated):
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_401_UNAUTHORIZED,
                                               detail=str(exc)),
                        status=status.HTTP_401_UNAUTHORIZED)

    if isinstance(exc, IntegrityError):
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_422_UNPROCESSABLE_ENTITY,
                                               detail=str(exc)),
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if isinstance(exc, AlreadyExistError):
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_400_BAD_REQUEST,
                                               detail=str(exc)),
                        status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, ObjectDoesNotExist):
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_404_NOT_FOUND,
                                               detail=str(exc)),
                        status=status.HTTP_404_NOT_FOUND)

    if isinstance(exc, ValidationError):
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_400_BAD_REQUEST,
                                               detail=exc),
                        status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, PermissionDenied):
        logger.debug(str(exc))
        return Response(data=get_response_data(status.HTTP_403_FORBIDDEN,
                                               detail=str(exc)),
                        status=status.HTTP_403_FORBIDDEN)
    return response
