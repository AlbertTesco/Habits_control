from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User


class UserTestCase(APITestCase):
    """
    Test case for User model API endpoints.

    This test case covers various aspects of your API related to the User model.
    """

    def setUp(self):
        """
        Set up initial data and authentication credentials for testing.

        Creates a User object and generates an access token for authorization.
        """
        self.user = User.objects.create(
            email="user@example.com",
            first_name="string",
            last_name="string",
            phone="string",
            country="string",
            telegram_id=2147483647
        )
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_user_create(self):
        """
        Test the creation of a User object through the API.

        Sends a POST request with user data and checks if the response code is 201 (HTTP_201_CREATED).
        """

        data = {
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "phone": "123456789",
            "country": "Country",
            "telegram_id": 1234567890
        }
        response = self.client.post('/users/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list(self):
        """
        Test the retrieval of a list of User objects through the API.

        Sends a GET request and checks if the response code is 200 (HTTP_200_OK).
        Also verifies the retrieved data against the expected list of users.
        """

        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "pk": self.user.pk,
                    "email": self.user.email,
                    "first_name": self.user.first_name,
                    "last_name": self.user.last_name,
                    "phone": self.user.phone,
                    "country": self.user.country,
                    "avatar": None,
                    "telegram_id": self.user.telegram_id
                }
            ]
        )

    def test_user_update(self):
        """
        Test the update of a User object through the API.

        Sends a PUT request with updated user data and checks if the response code is 200 (HTTP_200_OK).
        """

        updated_data = {
            "email": self.user.email,
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "phone": "+123456789",
            "country": "test_country",
            "telegram_id": self.user.telegram_id
        }
        response = self.client.put(f'/users/{self.user.pk}/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        """
        Test the deletion of a User object through the API.

        Sends a DELETE request and checks if the response code is 204 (HTTP_204_NO_CONTENT).
        """

        response = self.client.delete(f'/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
