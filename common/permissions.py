from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Any Permission are not allowed to request except SAFE_METHOD.
    If request user and current user is different.
    """

    def has_object_permission(self, request: Request, view, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj


class IsOwnerOnly(permissions.BasePermission):
    """
    Any Permission are not allowed to request.
    If request user and current user is different.
    """

    def has_object_permission(self, request: Request, view, obj: User):
        return request.user == obj
