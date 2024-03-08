from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()
