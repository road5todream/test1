from .models import Tasks
from django import forms
from django.utils.translation import gettext as _


class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Tasks
        fields = ('name',
                  'description',
                  'status',
                  'creator',
                  'executor',
                  'label'
                  )
        widgets = {
            'description': forms.Textarea(),
            'creator': forms.HiddenInput(),
        }


class UpdateTaskForm(CreateTaskForm):
    pass
