from rest_framework import permissions


class IsTeamUser(permissions.BasePermission):
    code = 403

    def has_permission(self, request, view):
        IsTeamUser.message = "You are not participationg the team"

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated \
                and len(request.user.teams.all()) != 0:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        IsTeamUser.message = f"You are not allowed to edit this {
            obj.__class__.__name__}"

        if obj.__class__.__name__ == "Novel":
            for team in obj.teams.all():
                if team in request.user.teams.all():
                    return True

        if obj.__class__.__name__ == "Team" \
                and request.user in obj.users.all():
            return True

        return False
