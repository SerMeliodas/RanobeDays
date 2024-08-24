from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Model
from apps.core.utils import get_response_data

from rest_framework.exceptions import (
    AuthenticationFailed, NotAuthenticated, PermissionDenied
)
from django.core.exceptions import ObjectDoesNotExist
from apps.users.exceptions import TokenError
from apps.teams.exceptions import TeamIsCreator
from django.db import IntegrityError
from django.core.exceptions import ValidationError


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

    exceptions_to_check = (
        (ValidationError, status.HTTP_400_BAD_REQUEST),
        (NotAuthenticated, status.HTTP_401_UNAUTHORIZED),
        (AuthenticationFailed, status.HTTP_401_UNAUTHORIZED),
        (IntegrityError, status.HTTP_422_UNPROCESSABLE_ENTITY),
        (AlreadyExistError, status.HTTP_400_BAD_REQUEST),
        (ObjectDoesNotExist, status.HTTP_400_BAD_REQUEST),
        (PermissionDenied, status.HTTP_403_FORBIDDEN),
        (TokenError, status.HTTP_400_BAD_REQUEST),
        (TeamIsCreator, status.HTTP_400_BAD_REQUEST)
    )

    for error, status_code in exceptions_to_check:
        if isinstance(exc, error):
            logger.debug(str(exc))
            return Response(get_response_data(status_code, str(exc)),
                            status_code)
        return response
