from task_manager.users.models import Users
from .users import forms as rf
from django.contrib.auth.hashers import make_password


def add_data_in_db(user: Users, user_form: rf.UserRegistrationForm) -> None:
    """Add data in database"""
    user.first_name = user_form.cleaned_data['first_name']
    user.last_name = user_form.cleaned_data['last_name']
    user.password = make_password(user_form.cleaned_data['password'])
    user.username = user_form.cleaned_data['username']
    user.save()
