from rest_framework import serializers


def time_to_complete_validator(value):
    """
    Validates the time required to complete a habit.

    Args:
    value (int): The time taken to complete a habit.

    Raises:
    serializers.ValidationError: If the execution time exceeds the maximum limit of 120 seconds.
    """
    max_time = 120
    if value > max_time:
        raise serializers.ValidationError(f'The execution time should be no more than {max_time} seconds')


def related_habit_validator(value):
    """
    Validates a related habit.

    Args:
    value (Habit): The related habit instance.

    Raises:
    serializers.ValidationError: If the related habit is set and it's not marked as pleasant.
    """
    if value is not None:
        if not value.is_pleasant:
            raise serializers.ValidationError('A related habit should have the hallmark of a pleasant habit')


def frequency_validator(value):
    """
    Validates the frequency of a habit.

    Args:
    value (int): The frequency of the habit in days.

    Raises:
    serializers.ValidationError: If the frequency is set to more than 7 days.
    """
    max_frequency = 7
    if value > max_frequency:
        raise serializers.ValidationError(f'You should not perform the habit less than once every {max_frequency} days')


def exclude_award_and_related_habit_validator(data):
    """
    Validates the exclusion between an award and a related habit.

    Args:
    data (dict): Dictionary containing the award and related habit data.

    Raises:
    serializers.ValidationError: If both an award and a related habit are selected simultaneously.
    """
    award = data.get('award')
    related_habit = data.get('related_habit')

    if award and related_habit:
        raise serializers.ValidationError(
            'Simultaneous selection of a related habit and indication of a reward is prohibited')


def not_award_or_related_habit_validator(data):
    """
    Validates whether a habit marked as pleasant can have an award or a related habit.

    Args:
    data (dict): Dictionary containing habit data.

    Raises:
    serializers.ValidationError: If a habit marked as pleasant has an award or a related habit.
    """
    is_pleasant = data.get('is_pleasant', False)
    award = data.get('award')
    related_habit = data.get('related_habit')

    if is_pleasant and (award or related_habit):
        raise serializers.ValidationError("Pleasant habit cannot have an award or a related habit.")
