from django.shortcuts import render
from django.utils.translation import gettext as _


def main_page(request):
    return render(request, 'index.html')
