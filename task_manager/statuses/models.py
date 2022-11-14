from django.db import models


class Statuses(models.Model):
    """Model for statuses of tasks"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Statuses'
