from rest_framework.permissions import BasePermission

class IsHasChannel(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if getattr(request.user, "channel", None):
                return True
        return False
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.channel == obj.author