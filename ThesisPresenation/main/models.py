from django.db import models


class Task(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=None, null=True, blank=True)
    deadline = models.DateTimeField()
    isTaskExpired = models.BooleanField()
    __doc__ = "Task with some times to get a boolean"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    hours_worked = models.IntegerField()
    total_hours = models.IntegerField()
    remaining_hours = models.IntegerField()
    __doc__ = "Employee to do some calculations"
