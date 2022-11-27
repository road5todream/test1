from .forms import UserRegistrationForm, ChangeProfileForm
from .models import Users
from task_manager.settings import REDIRECT_TO_LOGIN
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.dataclasses import FlashMessages
from task_manager.services import UserChangeAccessMixin, UserDeleteAccessMixin
from django.urls import reverse_lazy


class UsersView(ListView):

    model = Users


class RegisterUser(SuccessMessageMixin,
                   CreateView
                   ):

    model = Users
    form_class = UserRegistrationForm
    template_name = 'users/create_user.html'
    success_url = REDIRECT_TO_LOGIN
    success_message = FlashMessages.REGISTER_SUCCESS.value


class UpdateUserView(UserChangeAccessMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView,
                     ):
    model = Users
    form_class = ChangeProfileForm
    template_name = 'users/update_user.html'
    login_url = REDIRECT_TO_LOGIN
    success_url = reverse_lazy('users')
    success_message = FlashMessages.USER_SUCCESSFULLY_CHANGED.value


class DeleteUserView(UserDeleteAccessMixin,
                     LoginRequiredMixin,
                     DeleteView
                     ):
    login_url = REDIRECT_TO_LOGIN
    model = Users
    success_url = reverse_lazy('users')
    template_name = 'users/delete_user.html'
