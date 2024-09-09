from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import password_validation, get_user_model

User = get_user_model()


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

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {'email': 'User with provided email does not exists'})

        return value


class VerifyEmailSerializer(serializers.Serializer):
    token = serializers.CharField()
