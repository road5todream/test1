from .models import Labels
from .forms import CreateLabelForm, UpdateLabelForm
from task_manager.settings import REDIRECT_TO_LOGIN
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


class LabelsListView(PermissionMixin,
                     LoginRequiredMixin,
                     ListView,
                     ):
    model = Labels
    login_url = REDIRECT_TO_LOGIN
    template_name = 'labels/labels_list.html'


class CreateLabelView(PermissionMixin,
                      LoginRequiredMixin,
                      SuccessMessageMixin,
                      CreateView,
                      ):
    model = Labels
    form_class = CreateLabelForm
    template_name = 'labels/create_label.html'
    login_url = REDIRECT_TO_LOGIN
    success_message = FlashMessages.LABEL_CREATED.value
    success_url = reverse_lazy('labels')


class UpdateLabelView(PermissionMixin,
                      LoginRequiredMixin,
                      SuccessMessageMixin,
                      UpdateView,
                      ):
    model = Labels
    form_class = UpdateLabelForm
    template_name = 'labels/update_label.html'
    login_url = REDIRECT_TO_LOGIN
    success_message = FlashMessages.LABEL_SUCCESSFULLY_CHANGED.value
    success_url = reverse_lazy('labels')


class DeleteLabelView(PermissionMixin,
                      LoginRequiredMixin,
                      DeleteView,
                      ):
    model = Labels
    template_name = 'labels/delete_label.html'
    login_url = REDIRECT_TO_LOGIN
    success_url = 'labels'

    def form_valid(self, form):
        try:
            self.object.delete()
            messages.success(
                self.request,
                FlashMessages.LABEL_SUCCESSFULLY_DELETE.value
            )
            return redirect('labels')

        except ProtectedError:
            messages.error(self.request,
                           FlashMessages.LABEL_IS_USING.value)
            return redirect('labels')
