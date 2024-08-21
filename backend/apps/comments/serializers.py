from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()

    comment_type = serializers.ChoiceField(Comment.TYPES)
    message = serializers.CharField()

    novel = serializers.CharField(source='novel.slug', required=False)
    chapter = serializers.IntegerField(source='chapter.pk', required=False)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), required=False)
    user = serializers.CharField(source='user.username')


class CommentCreateSerializer(CommentSerializer):
    user = None


class CommentFilterSerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
    novel = serializers.CharField(required=False)
    chapter = serializers.IntegerField(required=False)
