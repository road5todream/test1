from task_manager import services as svs
from .models import Statuses
from .forms import CreateStatusForm, ChangeStatusForm


class StatusesView(svs.LoginRequiredMixin,
                   svs.ListView,
                   ):

    login_url = '/login/'
    model = Statuses
    template_name = 'statuses/statuses_list.html'


class CreateStatus(svs.LoginRequiredMixin,
                   svs.SuccessMessageMixin,
                   svs.CreateView
                   ):

    model = Statuses
    form_class = CreateStatusForm
    template_name = 'statuses/create_status.html'
    success_url = svs.reverse_lazy('statuses')
    success_message = 'Status successfully created'
    login_url = '/login/'


class UpdateStatus(svs.LoginRequiredMixin,
                   svs.SuccessMessageMixin,
                   svs.UpdateView
                   ):

    model = Statuses
    form_class = ChangeStatusForm
    template_name = 'statuses/update_status.html'
    success_message = 'Status successfully changed'
    login_url = '/login/'
    success_url = svs.reverse_lazy('statuses')


class DeleteStatus(svs.LoginRequiredMixin,
                   svs.SuccessMessageMixin,
                   svs.DeleteView):

    model = Statuses
    login_url = '/login/'
    success_url = svs.reverse_lazy('statuses')
    success_message = 'Status has been deleted'
    template_name = 'statuses/delete_status.html'
