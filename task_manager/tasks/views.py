from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.settings import REDIRECT_TO_LOGIN
from .models import Tasks
from .forms import CreateTaskForm, UpdateTaskForm
from .filters import TaskFilter
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from task_manager.services import PermissionMixin
from task_manager.dataclasses import FlashMessages
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, UpdateView, \
    DetailView
from django.contrib.messages.views import SuccessMessageMixin


class TasksFilterView(PermissionMixin,
                      LoginRequiredMixin,
                      FilterView,
                      ):

    login_url = REDIRECT_TO_LOGIN
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'


class CreateTaskView(PermissionMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView,
                     ):

    model = Tasks
    form_class = CreateTaskForm
    login_url = REDIRECT_TO_LOGIN
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks')
    success_message = FlashMessages.TASK_CREATED.value

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['creator'].initial = self.request.user.pk
        return context


class TaskView(PermissionMixin,
               LoginRequiredMixin,
               DetailView,
               ):
    model = Tasks
    login_url = REDIRECT_TO_LOGIN
    template_name = 'tasks/view_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class UpdateTaskView(PermissionMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView,
                     ):
    model = Tasks
    form_class = UpdateTaskForm
    login_url = REDIRECT_TO_LOGIN
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy('tasks')
    success_message = FlashMessages.TASK_SUCCESSFULLY_CHANGED.value


class DeleteTaskView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     SuccessMessageMixin,
                     DeleteView,
                     ):
    login_url = REDIRECT_TO_LOGIN
    model = Tasks
    success_url = reverse_lazy('tasks')
    success_message = FlashMessages.TASK_SUCCESSFULLY_DELETE.value
    template_name = 'tasks/delete_task.html'
    redirect_field_name = None

    def has_permission(self) -> bool:
        return self.get_object().creator.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request, FlashMessages.NO_AUTHENTICATION.value
            )
            return self.handle_no_permission()

        elif not self.has_permission():
            messages.error(
                request, FlashMessages.NO_PERMIT_TO_DELETE_TASK.value
            )
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
