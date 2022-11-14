from django.urls import path
from . import views

urlpatterns = [
    path('',  views.users_list, name='users'),
    path('create/', views.register, name='create_user')
]
