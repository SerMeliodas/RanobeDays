from rest_framework import permissions


class IsChapterOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated \
                and len(request.user.team_set.all()) > 0:
            return True

        if not request.user.is_authenticated \
                and request.method in permissions.SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return request.user in obj.team.users.all()
