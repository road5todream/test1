from django.db import models


class Tags(models.Model):
    """Model for tags of tasks"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Tags'
