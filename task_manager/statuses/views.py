from task_manager.settings import REDIRECT_TO_LOGIN
from .models import Statuses
from .forms import CreateStatusForm, ChangeStatusForm
import task_manager as tm


class StatusesView(tm.PermissionMixin,
                   tm.LoginRequiredMixin,
                   tm.ListView,
                   ):

    login_url = REDIRECT_TO_LOGIN
    model = Statuses
    template_name = 'statuses/statuses_list.html'


class CreateStatus(tm.PermissionMixin,
                   tm.LoginRequiredMixin,
                   tm.SuccessMessageMixin,
                   tm.CreateView
                   ):

    model = Statuses
    form_class = CreateStatusForm
    template_name = 'statuses/create_status.html'
    success_url = tm.reverse_lazy('statuses')
    success_message = tm.FlashMessages.STATUS_CREATED.value
    login_url = REDIRECT_TO_LOGIN


class UpdateStatus(tm.PermissionMixin,
                   tm.LoginRequiredMixin,
                   tm.SuccessMessageMixin,
                   tm.UpdateView
                   ):
    model = Statuses
    form_class = ChangeStatusForm
    template_name = 'statuses/update_status.html'
    success_message = tm.FlashMessages.STATUS_SUCCESSFULLY_CHANGED.value
    login_url = REDIRECT_TO_LOGIN
    success_url = tm.reverse_lazy('statuses')


class DeleteStatus(tm.PermissionMixin,
                   tm.LoginRequiredMixin,
                   tm.DeleteView):

    model = Statuses
    login_url = REDIRECT_TO_LOGIN
    success_url = tm.reverse_lazy('statuses')
    template_name = 'statuses/delete_status.html'

    def form_valid(self, form):
        try:
            self.object.delete()
            tm.messages.success(
                self.request, tm.FlashMessages.STATUS_SUCCESSFULLY_DELETE.value
            )
            return tm.redirect('statuses')

        except tm.ProtectedError:
            tm.messages.error(self.request,
                              tm.FlashMessages.STATUS_IS_USING.value)
            return tm.redirect('statuses')
