from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from habits import validators
from habits.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer to convert Habit model instances into Python data types and vice versa.

    Serializer Fields:
        - pk: Primary key of the Habit.
        - user: SlugRelatedField to represent the associated User by email.
        - award: The Award associated with the Habit.
        - place: The place where the Habit is to be executed.
        - execution_time: Date and time when the Habit is scheduled for execution.
        - action: The action related to the Habit.
        - is_pleasant: Boolean indicating whether the Habit is pleasant or not.
        - related_habit: PrimaryKeyRelatedField linked to other Habit objects.
        - frequency: Integer representing the frequency of the Habit.
        - time_to_complete: Integer representing the time required to complete the Habit.
        - is_public: Boolean indicating if the Habit is public or not.
        - telegram_id: SerializerMethodField to retrieve the telegram_id of the associated User.

    Attributes:
        time_to_complete: IntegerField with a custom validator for time_to_complete.
        frequency: IntegerField with a custom validator for frequency.
        related_habit: PrimaryKeyRelatedField linked to Habit objects with custom validators.
        user: SlugRelatedField linked to the 'email' field of the User model for retrieval and representation.
        telegram_id: SerializerMethodField to retrieve the telegram_id of the User associated with the Habit.
    """

    time_to_complete = serializers.IntegerField(validators=[validators.time_to_complete_validator])
    frequency = serializers.IntegerField(validators=[validators.frequency_validator])

    related_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(),
        validators=[validators.related_habit_validator],
        allow_null=True,
        required=False,
    )
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all(), required=False)

    telegram_id = serializers.SerializerMethodField()

    def get_telegram_id(self, obj):
        return obj.user.telegram_id if obj.user else None

    class Meta:
        model = Habit
        fields = (
            'pk', 'user', 'award', 'place', 'execution_time', 'action', 'is_pleasant', 'related_habit', 'frequency',
            'time_to_complete', 'is_public', 'telegram_id',
        )

        validators = [
            UniqueTogetherValidator(
                queryset=Habit.objects.all(),
                fields=['award', 'is_pleasant'],
            ),
            validators.exclude_award_and_related_habit_validator,
            validators.not_award_or_related_habit_validator
        ]
