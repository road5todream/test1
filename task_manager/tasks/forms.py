from .models import Tasks
from django import forms


class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Tasks
        fields = ('name',
                  'description',
                  'status',
                  'creator',
                  'performer',
                  'label'
                  )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'description'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'performer': forms.Select(attrs={'class': 'form-control'}),
            'creator': forms.HiddenInput(),
            'tag_id': forms.SelectMultiple(attrs={'class': 'form-control',
                                                  })
        }


class UpdateTaskForm(CreateTaskForm):
    pass
