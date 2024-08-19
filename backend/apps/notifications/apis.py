from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from apps.core.utils import get_response_data

from apps.core.permissions import IsOwner

from .serializers import NotificationSerializer

from .selectors import (
    get_notification,
    get_notifications
)


class NotificationAPI(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        notifications = get_notifications(user=request.user)

        data = NotificationSerializer(notifications, many=True).data
        data = get_response_data(status.HTTP_200_OK, data)

        return Response(data, status.HTTP_200_OK)


class NotificationDetailAPI(APIView):
    permission_classes = ((IsAuthenticated & IsOwner) | IsAdminUser,)

    def delete(self, request, pk):
        notification = get_notification(pk)
        print(notification)
        self.check_object_permissions(request, notification)

        data = NotificationSerializer(notification).data

        notification.delete()

        data = get_response_data(
            status.HTTP_200_OK, data, 'Was successfully deleted')

        return Response(data, status.HTTP_200_OK)
