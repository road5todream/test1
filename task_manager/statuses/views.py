from task_manager.settings import REDIRECT_TO_LOGIN
from .models import Statuses
from .forms import CreateStatusForm, ChangeStatusForm
from task_manager.services import PermissionMixin
from task_manager.dataclasses import FlashMessages
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, \
    UpdateView


class StatusesView(PermissionMixin,
                   LoginRequiredMixin,
                   ListView,
                   ):

    login_url = REDIRECT_TO_LOGIN
    model = Statuses
    template_name = 'statuses/statuses_list.html'


class CreateStatus(PermissionMixin,
                   LoginRequiredMixin,
                   SuccessMessageMixin,
                   CreateView
                   ):

    model = Statuses
    form_class = CreateStatusForm
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('statuses')
    success_message = FlashMessages.STATUS_CREATED.value
    login_url = REDIRECT_TO_LOGIN


class UpdateStatus(PermissionMixin,
                   LoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView
                   ):
    model = Statuses
    form_class = ChangeStatusForm
    template_name = 'statuses/update_status.html'
    success_message = FlashMessages.STATUS_SUCCESSFULLY_CHANGED.value
    login_url = REDIRECT_TO_LOGIN
    success_url = reverse_lazy('statuses')


class DeleteStatus(PermissionMixin,
                   LoginRequiredMixin,
                   DeleteView):

    model = Statuses
    login_url = REDIRECT_TO_LOGIN
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/delete_status.html'

    def form_valid(self, form):
        try:
            self.object.delete()
            messages.success(
                self.request, FlashMessages.STATUS_SUCCESSFULLY_DELETE.value
            )
            return redirect('statuses')

        except ProtectedError:
            messages.error(self.request,
                           FlashMessages.STATUS_IS_USING.value)
            return redirect('statuses')
