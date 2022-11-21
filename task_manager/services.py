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


class PermissionMixin:

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(request, 'You haven\'t permission')
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)

