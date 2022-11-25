import loguru
from task_manager.settings import REDIRECT_TO_LOGIN
from .models import Tasks
from .forms import CreateTaskForm, UpdateTaskForm
from .filters import TaskFilter
from django_filters.views import FilterView
import task_manager as tm


class TasksFilterView(tm.PermissionMixin,
                      tm.LoginRequiredMixin,
                      FilterView,
                      ):

    login_url = REDIRECT_TO_LOGIN
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'


class CreateTaskView(tm.PermissionMixin,
                     tm.LoginRequiredMixin,
                     tm.SuccessMessageMixin,
                     tm.CreateView,
                     ):

    model = Tasks
    form_class = CreateTaskForm
    login_url = REDIRECT_TO_LOGIN
    template_name = 'tasks/create_task.html'
    success_url = tm.reverse_lazy('tasks')
    success_message = tm.FlashMessages.TASK_CREATED.value

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['creator'].initial = self.request.user.pk
        return context


class TaskView(tm.PermissionMixin,
               tm.LoginRequiredMixin,
               tm.DetailView,
               ):
    model = Tasks
    login_url = REDIRECT_TO_LOGIN
    template_name = 'tasks/view_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class UpdateTaskView(tm.PermissionMixin,
                     tm.LoginRequiredMixin,
                     tm.SuccessMessageMixin,
                     tm.UpdateView,
                     ):
    model = Tasks
    form_class = UpdateTaskForm
    login_url = REDIRECT_TO_LOGIN
    template_name = 'tasks/update_task.html'
    success_url = tm.reverse_lazy('tasks')
    success_message = tm.FlashMessages.TASK_SUCCESSFULLY_CHANGED.value


class DeleteTaskView(tm.LoginRequiredMixin,
                     tm.PermissionRequiredMixin,
                     tm.SuccessMessageMixin,
                     tm.DeleteView,
                     ):
    login_url = REDIRECT_TO_LOGIN
    model = Tasks
    success_url = tm.reverse_lazy('tasks')
    success_message = tm.FlashMessages.TASK_SUCCESSFULLY_DELETE.value
    template_name = 'tasks/delete_task.html'

    def has_permission(self) -> bool:
        return self.get_object().creator.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            tm.messages.error(
                self.request, tm.FlashMessages.NO_AUTHENTICATION.value
            )
            return self.handle_no_permission()

        elif not self.has_permission():
            tm.messages.error(
                request, tm.FlashMessages.NO_PERMIT_TO_DELETE_TASK.value
            )
            return tm.redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
