from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import HttpResponse


def main_page(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def login(request):
    return render(request, 'login.html')


def create_user(request):
    return render(request, 'create_user.html')
