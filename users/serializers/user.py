from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Attributes:
    Meta (class): Holds metadata configurations for the serializer.
        model (User): Specifies the User model to serialize.
        fields (tuple): Specifies the fields to include in the serialization.
    """
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar', 'telegram_id',)
