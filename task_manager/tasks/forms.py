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
                  'labels'
                  )
        widgets = {
            'description': forms.Textarea(),
            'creator': forms.HiddenInput(),
            'labels': forms.SelectMultiple(attrs={'multiple': ''})
        }


class UpdateTaskForm(CreateTaskForm):
    pass
