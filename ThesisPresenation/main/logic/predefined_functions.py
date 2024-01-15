from typing import Any
from django.db.models.fields import DateTimeField


class PredefinedFunctions:

    @staticmethod
    def reset_field(field: Any):
        return field

    @staticmethod
    def is_valid(deadline: DateTimeField, end:DateTimeField):
        return True
