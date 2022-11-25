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
import task_manager as tm
from task_manager.settings import REDIRECT_TO_LOGIN


class UserChangeAccessMixin:

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            tm.messages.error(
                request,
                tm.FlashMessages.NO_AUTHENTICATION.value,
            )

            return self.handle_no_permission()

        elif not self.has_permission():
            tm.messages.error(
                request,
                tm.FlashMessages.NO_PERMIT_TO_CHANGE_USER.value,
            )
            return tm.redirect('users')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteAccessMixin(UserChangeAccessMixin):

    def form_valid(self, form):
        try:
            self.object.delete()
            tm.messages.success(
                self.request, tm.FlashMessages.USER_SUCCESSFULLY_DELETE.value
            )
            return tm.redirect('users')

        except tm.ProtectedError:
            tm.messages.error(self.request,
                              tm.FlashMessages.USER_IS_USING.value)
            return tm.redirect('users')


class PermissionMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            tm.messages.error(
                self.request, tm.FlashMessages.NO_AUTHENTICATION.value
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)