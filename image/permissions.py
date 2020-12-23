from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # object permission will not be called for list and other operations
        # where more than one instance is returned. for them we filter in
        # get_queryset
        return obj.user == request.user

class CheckLoggedIn(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
