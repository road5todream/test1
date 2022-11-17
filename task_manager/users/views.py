import loguru
from django.http import HttpRequest, HttpResponse
from .forms import UserRegistrationForm
from django.views.generic import ListView, View, DeleteView
from task_manager.users.models import Users
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from task_manager.services import add_data_in_db
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import UpdateView
from django.contrib.auth import models


class UsersView(ListView):
    model = Users
    template_name = 'users/users.html'


class RegisterUser(View):

    def get(self, request, *args, **kwargs) -> HttpResponse:
        form = UserRegistrationForm()
        return render(request, 'users/create_user.html', {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user_form = form.save(commit=False)
            new_user_form.set_password(form.cleaned_data['password'])
            messages.success(request, 'Registration successfully')
            new_user = Users()
            add_data_in_db(new_user, form)
            new_user_form.save()
            return redirect('login')
        return render(request, 'users/create_user.html', {'form': form})


class UserProfileEdit(UpdateView):

    def get(self, request: HttpRequest, *args, **kwargs):
        user_id = kwargs.get('pk')
        _user = Users.objects.get(id=user_id)
        form = UserRegistrationForm(request.POST, instance=_user)
        return render(request,
                      'users/users_update_form.html',
                      {'form': form,
                       'user_id': user_id}
                      )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        _user_in_db = Users.objects.get(id=user_id)
        user = request.user
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            update_user = form.save(commit=False)
            add_data_in_db(_user_in_db, form)
            update_user.set_password(form.cleaned_data['password'])
            messages.success(request, 'Data was updated successfully!')
            update_user.save()
            return redirect('users')
        return render(request,
                      'users/users_update_form.html',
                      {'form': form,
                       'user_id': user_id}
                      )


class DeleteUser(DeleteView):
    model = Users
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('main_page')


