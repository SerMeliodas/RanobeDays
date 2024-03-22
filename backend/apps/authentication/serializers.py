from dj_rest_auth.registration.serializers import RegisterSerializer as BaseSerializer


class RegisterSerializer(BaseSerializer):
    def validate_username(self, username):
        ...

# class RegisterSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password1 = serializers.CharField()
#     password2 = serializers.CharField()
#
#     def validate(self, instance):
#         if instance['password1'] != instance['password2']:
#             raise serializers.ValidationError(
#                 'Passwords must match'
#             )
#         return instance
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError(
#                 'User with this email already exists'
#             )
#         return value
#
#     def save(self, request):
#         ...
