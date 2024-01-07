from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import Award
from users.models import User


class AwardSerializer(serializers.ModelSerializer):
    """
    Serializer to convert Award model instances into Python data types and vice versa.

    Serializer Fields:
        - pk: Primary key of the Award.
        - user: SlugRelatedField to represent the associated User by email.
        - reward: The reward associated with the Award.

    Attributes:
        user: SlugRelatedField linked to the 'email' field of the User model, allowing retrieval and
              representation of User objects through email.
    """

    user = SlugRelatedField(slug_field='email', queryset=User.objects.all(), required=False)

    class Meta:
        model = Award
        fields = ('pk', 'user', 'reward',)
