from .forms import UserRegistrationForm, ChangeProfileForm
from .models import Users
from task_manager import services as svs


class UsersView(svs.ListView):

    model = Users


class RegisterUser(svs.SuccessMessageMixin,
                   svs.CreateView
                   ):

    model = Users
    form_class = UserRegistrationForm
    template_name = 'users/create_user.html'
    success_url = '/login/'
    success_message = svs.FlashMessages.REGISTER_SUCCESS.value


class UpdateUserView(svs.LoginRequiredMixin,
                     svs.PermissionMixin,
                     svs.SuccessMessageMixin,
                     svs.UpdateView,
                     ):

    model = Users
    form_class = ChangeProfileForm
    template_name = 'users/update_user.html'
    login_url = '/login/'
    success_url = svs.reverse_lazy('users')
    success_message = svs.FlashMessages.USER_SUCCESSFULLY_CHANGED.value


class DeleteUserView(svs.LoginRequiredMixin,
                     svs.PermissionMixin,
                     svs.SuccessMessageMixin,
                     svs.DeleteView
                     ):

    login_url = '/login/'
    model = Users
    success_url = svs.reverse_lazy('login')
    success_message = 'User has been deleted'
    template_name = 'users/delete_user.html'
