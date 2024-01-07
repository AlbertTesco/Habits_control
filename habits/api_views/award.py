"""
Award API Views

Provides API endpoints for Award model operations.
"""

from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from habits.models import Award
from habits.permissions import IsOwner, IsSuperUser
from habits.serializers.award import AwardSerializer


class AwardListAPIView(generics.ListAPIView):
    """
    API endpoint that allows listing awards.
    """

    serializer_class = AwardSerializer
    queryset = Award.objects.none()
    permission_classes = [IsAuthenticated | IsOwner | IsSuperUser]

    def get_queryset(self):
        """
        Retrieve the queryset of awards based on the requesting user's permissions.
        """
        user = self.request.user

        if user.is_authenticated and user.is_superuser:
            return Award.objects.all()
        elif user.is_authenticated:
            return Award.objects.filter(user=user)
        else:
            raise PermissionDenied("You do not have permission to access this page")


class AwardCreateAPIView(generics.CreateAPIView):
    """
    API endpoint that allows creating new awards.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = AwardSerializer

    def perform_create(self, serializer):
        """
        Create a new award and associate it with the requesting user.
        """
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class AwardUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint that allows updating an existing award.
    """

    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class AwardDestroyAPIView(generics.DestroyAPIView):
    """
    API endpoint that allows deleting an existing award.
    """

    queryset = Award.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
