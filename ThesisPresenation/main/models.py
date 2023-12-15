from django.db import models


class Task(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=None, null=True, blank=True)
    deadline = models.DateTimeField()
    description = models.TextField()
    __doc__ = "Task using DEADLINE"


class Employee(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    __doc__ = "Employee with a role of 3 options"


class AnotherTask(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=None, null=True, blank=True)
    limit = models.DateTimeField()
    description = models.TextField()
    __doc__ = "Task using LIMIT"
