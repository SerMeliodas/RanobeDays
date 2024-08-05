from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(source="user.public_id")
    public_id = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()


class UserUpdateSerializer(serializers.Serializer):
    public_id = serializers.CharField(required=False)
    username = serializers.CharField(required=False)


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, data):
        if data["new_password1"] != data["new_password2"]:
            raise serializers.ValidationError("passwords don't match")
        return data
