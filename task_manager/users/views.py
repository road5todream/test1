from django.http import HttpRequest, HttpResponse
from .forms import UserRegistrationForm
from django.views.generic import ListView, View, DeleteView
from .models import Users
from django.shortcuts import render, redirect
from task_manager.services import add_user_in_db, check_user_permission
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


class UsersView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        return render(request,
                      'users/users.html',
                      context={'users': users,
                               })


class RegisterUser(View):

    def get(self, request, *args, **kwargs) -> HttpResponse:
        form = UserRegistrationForm()
        return render(request, 'users/create_user.html', {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successfully')
            form.save()
            return redirect('login')
        return render(request, 'users/create_user.html', {'form': form})


class UserProfileEdit(LoginRequiredMixin, UpdateView):

    login_url = '/login/'

    def get(self, request: HttpRequest, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Users.objects.get(id=user_id)
        form = UserRegistrationForm(request.POST, instance=user)
        if not check_user_permission(user, request):
            messages.error(request,
                           'You have no permission to change user profile')
            return redirect('users')
        return render(request,
                      'users/users_update.html',
                      {'form': form,
                       'user_id': user_id}
                      )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user_in_db = Users.objects.get(id=user_id)
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            update_user = form.save(commit=False)
            add_user_in_db(user_in_db, form)
            update_user.set_password(form.cleaned_data['password'])
            messages.success(request, 'Data was updated successfully!')
            update_user.save()
            return redirect('users')
        return render(request,
                      'users/users_update.html',
                      {'form': form,
                       'user_id': user_id}
                      )


class DeleteUser(LoginRequiredMixin, DeleteView):

    login_url = '/login/'
    model = Users
    success_url = reverse_lazy('login')
    success_message = 'User has been deleted'
    template_name = 'users/delete_user.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Users.objects.get(id=user_id)
        if not check_user_permission(user, request):
            messages.error(request,
                           'You have no permission to delete user profile')
            return redirect('users')
        return render(request, 'users/delete_user.html')


