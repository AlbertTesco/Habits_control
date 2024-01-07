from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Custom pagination class for the Habit List API view.

    Attributes:
        page_size (int): Number of items displayed per page.
        page_size_query_param (str): URL query parameter to control the page size.
        max_page_size (int): Maximum limit for page size allowed.
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
