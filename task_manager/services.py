import loguru
from django.contrib.auth.models import User
from .users.forms import UserRegistrationForm
from .statuses.forms import StatusForm
from django.contrib.auth.hashers import make_password
from typing import Union
from django.db.models import QuerySet
from task_manager.statuses.models import Statuses
from django.http import HttpRequest


def add_user_in_db(user: User, user_form: UserRegistrationForm) -> None:
    """Add user in database"""
    user.first_name = user_form.cleaned_data['first_name']
    user.last_name = user_form.cleaned_data['last_name']
    user.password = make_password(user_form.cleaned_data['password'])
    user.username = user_form.cleaned_data['username']
    user.save()


def add_status_in_db(status: Statuses, status_form: StatusForm) -> None:
    """Add status in database"""
    status.name = status_form.cleaned_data['name']
    status.save()


def get_user_data_from_db(user: Union[QuerySet, User],
                          filters: dict) -> User:
    if len(filters) == 0:
        return user[0]

    for field, value in filters.items():
        user_query_set = user.objects.filter(field=value)
        filters.pop(field)
        get_user_data_from_db(user_query_set, filters)


def check_user_permission(user: User, request) -> bool:
    if user.pk != request.user.id:
        loguru.logger.error(user.pk)
        loguru.logger.error(request.user.id)
        return False
    return True
