from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAccountOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                request.user and
                request.user.is_active):
            return True
        return False