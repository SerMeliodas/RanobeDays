from rest_framework import serializers
from django.contrib.auth import password_validation


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    public_username = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    public_username = serializers.CharField(required=False)

    def validate_username(self, value):
        if ' ' in value:
            raise serializers.ValidationError('username cant contain spaces')
        return value


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError('passwords dont match')
        password_validation.validate_password(
            data['new_password1'], self.context["user"])

        if self.context['user'].check_password(data['new_password1']):
            raise serializers.ValidationError(
                'new password  cannot be the same as old password')

        return data

    def validate_old_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError(
                'Your old password was entered incorrectly. Please enter it again.')

        return value


class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError('passwords dont match')
        return data
