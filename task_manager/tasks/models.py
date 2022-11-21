from django.urls import reverse
from django.db import models
from task_manager.users.models import Users
from task_manager.statuses.models import Statuses
from task_manager.tags.models import Tags


class Tasks(models.Model):
    """Models for tasks"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000,
                                   default='')
    creator = models.ForeignKey(Users,
                                on_delete=models.PROTECT,
                                related_name='creator',
                                default=None,
                                blank=True
                                )
    status = models.ForeignKey(Statuses,
                               on_delete=models.PROTECT,
                               )
    tag_id = models.ManyToManyField(Tags)
    performer = models.ForeignKey(Users,
                                  on_delete=models.PROTECT,
                                  related_name='performer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Tasks'
