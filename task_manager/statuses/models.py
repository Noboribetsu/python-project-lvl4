from django.db import models


class Status(models.Model):
    """
        Model for status:
        Fields:
        name - a status name.
        createad_at - automaticly add date of creation.
    """
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
