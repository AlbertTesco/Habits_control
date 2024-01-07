from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from habits.permissions import IsSuperUser, IsOwner
from ..models import User
from ..serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for handling User model CRUD operations.

    Attributes:
    queryset (QuerySet): The queryset of User instances.
    serializer_class (UserSerializer): The serializer class for User instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Returns the appropriate permissions depending on the action.

        Returns:
        list: A list of permission classes.

        Raises:
        KeyError: If the action does not match any permission class.
        """
        permission_classes = {
            'list': [IsAuthenticated],
            'update': [IsSuperUser | IsOwner],
            'partial_update': [IsSuperUser | IsOwner],
            'destroy': [IsSuperUser | IsOwner],
            'retrieve': [IsSuperUser | IsOwner],
        }
        return [permission() for permission in permission_classes.get(self.action, [IsAuthenticated])]
