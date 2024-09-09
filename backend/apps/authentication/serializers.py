from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import password_validation


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    public_username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('passwords must be equal')

        return data

    def validate_password1(self, value):
        errors = dict()
        try:
            password_validation.validate_password(value)
        except DjangoValidationError as err:
            errors['passoword'] = list(err.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class SendVerificationEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyEmailSerializer(serializers.Serializer):
    token = serializers.CharField()
