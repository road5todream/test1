from django import forms
from .models import Statuses


class CreateStatusForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'name'}),
        }


class ChangeStatusForm(CreateStatusForm):
    pass
