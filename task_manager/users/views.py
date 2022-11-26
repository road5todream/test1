from .forms import UserRegistrationForm, ChangeProfileForm
from .models import Users
from task_manager.settings import REDIRECT_TO_LOGIN
import task_manager as tm


class UsersView(tm.ListView):

    model = Users


class RegisterUser(tm.SuccessMessageMixin,
                   tm.CreateView
                   ):

    model = Users
    form_class = UserRegistrationForm
    template_name = 'users/create_user.html'
    success_url = REDIRECT_TO_LOGIN
    success_message = tm.FlashMessages.REGISTER_SUCCESS.value


class UpdateUserView(tm.UserChangeAccessMixin,
                     tm.LoginRequiredMixin,
                     tm.SuccessMessageMixin,
                     tm.UpdateView,
                     ):
    model = Users
    form_class = ChangeProfileForm
    template_name = 'users/update_user.html'
    login_url = REDIRECT_TO_LOGIN
    success_url = tm.reverse_lazy('users')
    success_message = tm.FlashMessages.USER_SUCCESSFULLY_CHANGED.value


class DeleteUserView(tm.UserDeleteAccessMixin,
                     tm.LoginRequiredMixin,
                     tm.DeleteView
                     ):
    login_url = REDIRECT_TO_LOGIN
    model = Users
    success_url = tm.reverse_lazy('users')
    template_name = 'users/delete_user.html'
