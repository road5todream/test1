import loguru
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
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from .dataclasses import FlashMessages


class PermissionMixin:

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(request,
                           FlashMessages.NO_PERMIT_TO_CHANGE_USER.value)

            return redirect('users')
        return super().dispatch(request, *args, **kwargs)

