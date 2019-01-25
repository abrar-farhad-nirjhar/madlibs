

from rest_framework import permissions



actions = ('GET',)


class madlibsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in actions:
            return True
        else:
             return False