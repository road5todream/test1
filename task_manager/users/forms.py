from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Users


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'first name',
                                                 }),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'last name',
                                                }),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'username',
                                               }),
            'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                'placeholder': 'username',
                                                    }),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder': 'username',
                                                    }),
        }


class ChangeProfileForm(UserRegistrationForm):
    pass
