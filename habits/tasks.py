from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import TelegramNotificationBot


@shared_task
def task_send_notification():
    """
    A Celery task to send notifications/reminders for habits scheduled within the next two hours.

    Fetches habits due for execution within the next two hours and sends a notification to the respective users
    via TelegramNotificationBot if the habit should be executed today.

    - Fetches habits with execution times between current time and the next two hours.
    - Checks if the habit should be executed today using the `should_execute_today()` method from the Habit model.
    - Constructs a notification message with habit details and sends it to the associated Telegram user.

    Usage:
    This task should be executed periodically to send timely reminders for scheduled habits.
    """
    current_datetime = timezone.now()

    habits = Habit.objects.filter(
        execution_time__gte=current_datetime,
        execution_time__lte=current_datetime + timedelta(hours=2),
        frequency__gt=0
    )

    for habit in habits:
        if habit.should_execute_today():
            text_to_send = (
                f'Reminder\n'
                f'To Do: {habit.action}\n'
                f'At: {habit.execution_time}\n'
                f'Place: {habit.place}\n'
                f'Time to Complete: {habit.time_to_complete} sec.'
            )
            if habit.award:
                text_to_send += f'\nYou can get {habit.award.reward} as a reward.'

            TelegramNotificationBot.send_telegram_message(text_to_send, habit.user.telegram_id)
