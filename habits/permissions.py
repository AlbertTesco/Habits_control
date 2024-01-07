from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Custom permission to allow access only to superusers.

    Attributes:
        message (str): Message displayed when permission is denied.
    """

    message = "You aren't a superuser"

    def has_permission(self, request, view):
        """
        Check whether the user is a superuser.

        Args:
            request: Request object.
            view: View requesting permission.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        if request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    """
    Custom permission to allow access only to the owner of an object.

    Attributes:
        message (str): Message displayed when permission is denied.
    """

    message = "You aren't an owner"

    def has_object_permission(self, request, view, obj):
        """
        Check whether the requesting user is the owner of the object.

        Args:
            request: Request object.
            view: View requesting permission.
            obj: Object for which permission is checked.

        Returns:
            bool: True if the user is the owner, False otherwise.
        """
        if request.user == obj:
            return True
        return False
