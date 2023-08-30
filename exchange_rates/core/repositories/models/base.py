"""Django Base Model Abstraction
"""
from django.db import models


class BaseModel(models.Model):
    """
    An abstract base model class that provides common fields for
    tracking creation and update times.

    Attributes:
        created (DateTimeField): A field that stores the date and
        time when the instance was created.
        Automatically set to the current date and time when a
        new instance is created.
        updated (DateTimeField): A field that stores the date and
        time when the instance was last updated.
        Automatically updated to the current date and time
        whenever the instance is modified.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta:
            abstract (bool): Specifies that this is an abstract model,
            not meant to create database tables.
        """

        abstract = True
