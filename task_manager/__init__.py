import django

django.setup()

from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from .dataclasses import FlashMessages
from task_manager.services import UserChangeAccessMixin, \
    UserDeleteAccessMixin, PermissionMixin

__all__ = [
    'ListView',
    'SuccessMessageMixin',
    'CreateView',
    'UserChangeAccessMixin',
    'UserDeleteAccessMixin',
    'PermissionMixin',
]