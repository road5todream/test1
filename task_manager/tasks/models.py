from django.db import models
from task_manager.users.models import Users
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Labels


class Tasks(models.Model):
    """Models for tasks"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000,
                                   default='')
    creator = models.ForeignKey(Users,
                                on_delete=models.PROTECT,
                                related_name='creator',
                                default=True,
                                blank=True
                                )
    status = models.ForeignKey(Statuses,
                               on_delete=models.PROTECT,
                               )
    label = models.ManyToManyField(Labels,
                                   through='RelationLink',
                                   through_fields=('task', 'label'),
                                   blank=True)
    performer = models.ForeignKey(Users,
                                  on_delete=models.PROTECT,
                                  related_name='performer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Tasks'


class RelationLink(models.Model):
    """An intermediate model for man-to-many communication between tasks and
    labels. Needed to prohibit deletion of labels that are used"""
    task = models.ForeignKey(to='tasks.Tasks',
                             on_delete=models.CASCADE,
                             default=0,
                             null=True
                             )
    label = models.ForeignKey(to='labels.Labels', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Relations'
