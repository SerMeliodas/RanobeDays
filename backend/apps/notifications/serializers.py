from rest_framework import serializers
from apps.novels.serializers import NovelShortenedSerializer
from apps.users.serializers import UserSerializer
from .models import Notification


class NotificationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    notification_type = serializers.ChoiceField(Notification.TYPES)
    novel = NovelShortenedSerializer()
    user = UserSerializer()
    message = serializers.CharField()
