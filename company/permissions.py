
from rest_framework.permissions import BasePermission


class IsAdminOrHR(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        profile = getattr(user, 'user_profile', None)

        if profile is None:
            return False

        return profile.role in ['ADMIN', 'HR']


class IsAdmin(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        profile = getattr(user, 'user_profile', None)

        if profile is None:
            return False

        return profile.role == 'ADMIN'


class IsAdminHRReadOnly(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        profile = getattr(user, 'user_profile', None)

        if profile is None:
            return False

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if request.method in ['POST', 'PUT', 'PATCH']:
            return profile.role in ['ADMIN', 'HR']

        if request.method == 'DELETE':
            return profile.role == 'ADMIN'

        return False
