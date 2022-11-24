from task_manager import services as svs
from .models import Labels
from .forms import CreateLabelForm, UpdateLabelForm


class LabelsListView(svs.LoginRequiredMixin,
                     svs.ListView,
                     ):
    model = Labels
    login_url = '/login/'
    template_name = 'labels/labels_list.html'


class CreateLabelView(svs.LoginRequiredMixin,
                      svs.SuccessMessageMixin,
                      svs.CreateView,
                      ):
    model = Labels
    form_class = CreateLabelForm
    template_name = 'labels/create_label.html'
    login_url = '/login/'
    success_message = 'Label was create successfully'
    success_url = '/labels/'


class UpdateLabelView(svs.LoginRequiredMixin,
                      svs.SuccessMessageMixin,
                      svs.UpdateView,
                      ):
    model = Labels
    form_class = UpdateLabelForm
    template_name = 'labels/update_label.html'
    login_url = '/login/'
    success_message = 'Label was successfully changes'
    success_url = '/labels/'


class DeleteLabelView(svs.LoginRequiredMixin,
                      svs.SuccessMessageMixin,
                      svs.DeleteView,
                      ):
    model = Labels
    template_name = 'labels/delete_label.html'
    login_url = '/login/'
    success_url = '/labels/'
    success_message = 'Label has been deleted'

    def form_valid(self, form):
        try:
            self.object.delete()
        except svs.ProtectedError:
            svs.messages.error(self.request, 'error')
        finally:
            return svs.redirect(self.success_url)
