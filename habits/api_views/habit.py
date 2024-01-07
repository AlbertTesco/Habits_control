from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from ..models import Habit
from ..paginators import HabitPaginator
from ..permissions import IsOwner, IsSuperUser
from ..serializers.habit import HabitSerializer


class HabitPublicListAPIView(generics.ListAPIView):
    """
    API endpoint to retrieve a list of public Habit objects.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator


class HabitListAPIView(generics.ListAPIView):
    """
    API endpoint to retrieve a list of Habit objects based on permissions.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated | IsOwner | IsSuperUser]

    def get_queryset(self):
        """
        Retrieve the queryset of habits based on the requesting user's permissions.
        """
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return Habit.objects.all()
        elif user.is_authenticated:
            return Habit.objects.filter(user=user)
        else:
            raise PermissionDenied("You are not authenticated.")


class HabitCreateAPIView(generics.CreateAPIView):
    """
    API endpoint to create a new Habit object.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Create a new habit and associate it with the requesting user.
        """
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint to update an existing Habit object.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    API endpoint to delete an existing Habit object.
    """

    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
