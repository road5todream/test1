from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from task_manager.services import register_user


def users_list(request):
    return render(request, 'users/users.html')


def register(request: HttpRequest) -> HttpResponse:
    return register_user(request)
