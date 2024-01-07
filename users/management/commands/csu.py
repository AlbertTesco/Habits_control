from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Management command for creating a superuser.
    """

    def handle(self, *args, **options):
        """
        Handle the command execution.
        """

        user = User.objects.create(
            email=input('Enter your email address: '),
            first_name=input('First Name: '),
            last_name=input('Last Name: '),
            is_staff=True,
            is_superuser=True,
        )
        password = input('Password: ')

        user.set_password(password)
        user.save()
