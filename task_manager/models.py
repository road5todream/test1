from django.db import models


class Users(models.Model):
    """Model of users"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Tasks(models.Model):
    """Models for tasks"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000,
                                   default='')
    creator_id = models.ForeignKey('Users',
                                   on_delete=models.PROTECT,
                                   related_name='creator')
    status_id = models.ForeignKey('Stats',
                                  on_delete=models.PROTECT,
                                  )
    tag_id = models.ManyToManyField('Tags')
    performer_id = models.ForeignKey('Users',
                                     on_delete=models.PROTECT,
                                     related_name='performer')
    created_at = models.DateTimeField(auto_now_add=True)


class Stats(models.Model):
    """Model for statuses of tasks"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Tags(models.Model):
    """Model for tags of tasks"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
