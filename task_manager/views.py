from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import HttpResponse, HttpRequest
from .services import auth_validate


def main_page(request):
    return render(request, 'index.html')


def user_login(request: HttpRequest) -> HttpResponse:
    return auth_validate(request)
