from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
