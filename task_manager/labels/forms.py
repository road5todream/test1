from django import forms
from .models import Labels


class CreateLabelForm(forms.ModelForm):

    class Meta:

        model = Labels
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'name'}),
        }


class UpdateLabelForm(CreateLabelForm):
    pass
