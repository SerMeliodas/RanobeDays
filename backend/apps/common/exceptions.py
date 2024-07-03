from django.db.models import Model
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class AlreadyExistError(Exception):
    """Raised when the instance of model is already exist in data base"""

    def __init__(self, instance: Model):
        self.message = f"{instance.__class__.__name__} already have \
the same instance in db"

        super().__init__(self.message)


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response:
        return response

    elif isinstance(exc, IntegrityError):
        return Response(data={"detail": str(exc)},
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    elif isinstance(exc, AlreadyExistError):
        return Response(data={"detail": str(exc)},
                        status=status.HTTP_400_BAD_REQUEST)

    elif isinstance(exc, ObjectDoesNotExist):
        return Response(data={"detail": str(exc)},
                        status=status.HTTP_404_NOT_FOUND)
