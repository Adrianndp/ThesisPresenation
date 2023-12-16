from typing import Any
from django.db.models.fields import DateTimeField


class PredefinedFunctions:
    """Rules: 1) Define the typing of the arguments."""

    @staticmethod
    def reset_field_after_10_seconds(field: Any):
        return field

    @staticmethod
    def example_with_time(start_time: DateTimeField):
        return start_time
