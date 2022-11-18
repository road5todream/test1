from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Statuses
from .forms import StatusForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from task_manager.services import add_status_in_db
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


class StatusesView(ListView):

    model = Statuses
    template_name = 'statuses/statuses.html'


class CreateStatus(View):

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = StatusForm()
        return render(request, 'statuses/create_status.html', {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            new_statuses_form = form.save(commit=False)
            messages.success(request, 'Status wa create')
            new_statuses_form.save()
            return redirect('statuses')
        return render(request, 'users/create_user.html', {'form': form})


class UpdateStatus(LoginRequiredMixin, UpdateView):

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        status_id = kwargs.get('pk')
        status = Statuses.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        return render(request,
                      'statuses/status_update.html',
                      {'form': form,
                       'status_id': status_id}
                      )

    def post(self, request, *args, **kwargs) -> HttpResponse:
        status_id = kwargs.get('pk')
        # status_in_db = Statuses.objects.get(id=status_id)
        status = request.user
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            update_status = form.save(commit=False)
            # add_status_in_db(status_in_db, form)
            messages.success(request, 'Data was updated successfully!')
            update_status.save()
            return redirect('statuses')
        return render(request,
                      'statuses/status_update.html',
                      {'form': form,
                       'user_id': status_id}
                      )


class DeleteStatus(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pass
