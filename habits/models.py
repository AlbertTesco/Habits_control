from django.db import models
from django.utils import timezone

from config import settings
from users.models import NULLABLE


class Award(models.Model):
    """
    Model representing an award given to a user for a particular achievement or habit.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    reward = models.TextField(verbose_name='Reward')

    def __str__(self):
        """
        String representation of the Award object.
        """
        return f'{self.user} - {self.reward}'

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'


class Habit(models.Model):
    """
    Model representing a habit or task associated with a user.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User',
                             related_name='habits')
    award = models.ForeignKey(Award, on_delete=models.SET_NULL, verbose_name='Reward', **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='Location of habit execution')
    execution_time = models.DateTimeField(verbose_name='Date and time of habit execution')
    action = models.TextField(verbose_name='Action')
    is_pleasant = models.BooleanField(default=False, verbose_name='Flag indicating a pleasant habit')
    related_habit = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL, verbose_name='Related habit',
                                      related_name='related_habits')
    frequency = models.PositiveIntegerField(default=1, verbose_name='Frequency in days')
    time_to_complete = models.PositiveIntegerField(verbose_name='Time to complete (in seconds)')
    is_public = models.BooleanField(default=False, verbose_name='Public habit flag')

    def should_execute_today(self):
        """
        Determines if the habit should be executed today based on the defined frequency.
        :return: True if the habit should be executed today, False otherwise
        """
        today = timezone.now()
        days_passed = (today - self.execution_time).days
        return days_passed % self.frequency == 0 and self.execution_time.date() <= today.date()

    def __str__(self):
        """
        String representation of the Habit object.
        """
        return f'{self.user} will {self.action} at {self.execution_time} in {self.place}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
