from .models import Labels
from .forms import CreateLabelForm, UpdateLabelForm
from task_manager.settings import REDIRECT_TO_LOGIN
import task_manager as tm


class LabelsListView(tm.PermissionMixin,
                     tm.LoginRequiredMixin,
                     tm.ListView,
                     ):
    model = Labels
    login_url = REDIRECT_TO_LOGIN
    template_name = 'labels/labels_list.html'


class CreateLabelView(tm.PermissionMixin,
                      tm.LoginRequiredMixin,
                      tm.SuccessMessageMixin,
                      tm.CreateView,
                      ):
    model = Labels
    form_class = CreateLabelForm
    template_name = 'labels/create_label.html'
    login_url = REDIRECT_TO_LOGIN
    success_message = tm.FlashMessages.LABEL_CREATED.value
    success_url = tm.reverse_lazy('labels')


class UpdateLabelView(tm.PermissionMixin,
                      tm.LoginRequiredMixin,
                      tm.SuccessMessageMixin,
                      tm.UpdateView,
                      ):
    model = Labels
    form_class = UpdateLabelForm
    template_name = 'labels/update_label.html'
    login_url = REDIRECT_TO_LOGIN
    success_message = tm.FlashMessages.LABEL_SUCCESSFULLY_CHANGED.value
    success_url = tm.reverse_lazy('labels')


class DeleteLabelView(tm.PermissionMixin,
                      tm.LoginRequiredMixin,
                      tm.DeleteView,
                      ):
    model = Labels
    template_name = 'labels/delete_label.html'
    login_url = REDIRECT_TO_LOGIN
    success_url = 'labels'

    def form_valid(self, form):
        try:
            self.object.delete()
            tm.messages.success(
                self.request,
                tm.FlashMessages.LABEL_SUCCESSFULLY_DELETE.value
            )
            return tm.redirect('labels')

        except tm.ProtectedError:
            tm.messages.error(self.request,
                              tm.FlashMessages.LABEL_IS_USING.value)
            return tm.redirect('labels')
