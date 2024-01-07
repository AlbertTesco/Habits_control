from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.

    Attributes:
        list_display (tuple): Fields to be displayed in the list view of the User model in the admin interface.

    """

    list_display = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country',)