from rest_framework import permissions


class IsLibraryItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.library.user == request.user
