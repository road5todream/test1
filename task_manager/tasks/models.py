from django.db import models
from task_manager.users.models import Users
from task_manager.statuses.models import Statuses
from task_manager.tags.models import Tags


class Tasks(models.Model):
    """Models for tasks"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000,
                                   default='')
    creator_id = models.ForeignKey(Users,
                                   on_delete=models.PROTECT,
                                   related_name='creator')
    status_id = models.ForeignKey(Statuses,
                                  on_delete=models.PROTECT,
                                  )
    tag_id = models.ManyToManyField(Tags)
    performer_id = models.ForeignKey(Users,
                                     on_delete=models.PROTECT,
                                     related_name='performer')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tasks'
