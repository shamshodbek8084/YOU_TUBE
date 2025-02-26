from rest_framework.permissions import BasePermission

class IsHasChannel(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.channel:
                return True
        return False