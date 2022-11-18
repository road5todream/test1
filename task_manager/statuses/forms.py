from django import forms
from .models import Statuses


class StatusForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'name'}),
        }