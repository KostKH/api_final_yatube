from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthentAndAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Верификация для классов, где есть поле автора.Проверяем
    в небезопасных методах с постами, что юзер - это автор."""

    def has_object_permission(self, request, view, obj):
        if obj.author != request.user:
            return request.method in permissions.SAFE_METHODS
        return True


class IsAuthenticatedUser(permissions.IsAuthenticated):
    """Верификация для классов, где есть поле юзера.Проверяем
    в небезопасных методах с постами, что юзер - это автор."""

    def has_object_permission(self, request, view, obj):
        if obj.user != request.user:
            return request.method in permissions.SAFE_METHODS
        return True
