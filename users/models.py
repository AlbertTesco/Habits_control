from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Custom user model representing a user of the system.

    Inherits from Django's AbstractUser class and adds additional fields:

    Attributes:
        email (EmailField): Email of the user (unique).
        avatar (ImageField): User's avatar image.
        phone (CharField): User's phone number.
        country (CharField): User's country.
        telegram_id (PositiveIntegerField): User's Telegram ID.

    Constants:
        NULLABLE (dict): Specifies the settings for nullable fields.

    Class Attributes:
        USERNAME_FIELD (str): Specifies the field to use for authenticating users (email).
        REQUIRED_FIELDS (list): Specifies any other required fields.

    """
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users_avatar/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=40, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    telegram_id = models.PositiveIntegerField(default=None, verbose_name='telegram id', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
