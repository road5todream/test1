from task_manager.users.models import Users
from task_manager import forms as rf
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


def add_user_in_db(user_form: rf.UserRegistrationForm) -> None:
    user = Users()
    user.first_name = user_form.cleaned_data['first_name']
    user.last_name = user_form.cleaned_data['last_name']
    user.password = make_password(user_form.cleaned_data['password'])
    user.username = user_form.cleaned_data['username']
    user.save()


def auth_validate(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'],
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Completed')
                    return redirect('main_page', permanent=True)
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Don\'t valid data')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_user(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            add_user_in_db(user_form)
            messages.success(request, 'Registration successfully')
            new_user.save()
        return redirect('login')
    else:
        user_form = UserRegistrationForm()
        return render(
            request,
            'users/create_user.html',
            {'form': user_form}
        )
