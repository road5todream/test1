import loguru
from task_manager import services as svs
from .models import Tasks
from .forms import CreateTaskForm, UpdateTaskForm
from .filters import TaskFilter
from django_filters.views import FilterView


class TasksFilterView(svs.LoginRequiredMixin,
                      FilterView,
                      ):

    login_url = '/login/'
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'


class CreateTaskView(svs.LoginRequiredMixin,
                     svs.SuccessMessageMixin,
                     svs.CreateView,
                     ):

    model = Tasks
    form_class = CreateTaskForm
    login_url = '/login/'
    template_name = 'tasks/create_task.html'
    success_url = '/tasks/'
    success_message = 'The task was successfully created'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['creator'].initial = self.request.user.pk
        loguru.logger.info(context['form'].fields['label'].choices)
        return context


class TaskView(svs.LoginRequiredMixin,
               svs.DetailView,
               ):
    model = Tasks
    login_url = '/login/'
    template_name = 'tasks/view_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loguru.logger.info(context)
        return context


class UpdateTaskView(svs.LoginRequiredMixin,
                     svs.SuccessMessageMixin,
                     svs.UpdateView,
                     ):
    model = Tasks
    form_class = UpdateTaskForm
    login_url = '/login/'
    template_name = 'tasks/update_task.html'
    success_url = '/tasks/'
    success_message = 'Task has been updated!'


class DeleteTaskView(svs.LoginRequiredMixin,
                     svs.PermissionMixin,
                     svs.SuccessMessageMixin,
                     svs.DeleteView,
                     ):
    login_url = '/login/'
    model = Tasks
    success_url = '/tasks/'
    success_message = 'Task has been deleted'
    template_name = 'tasks/delete_task.html'

    def has_permission(self) -> bool:
        return self.get_object().creator.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            svs.messages.error(request, 'You haven\'t permission')
            return svs.redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
