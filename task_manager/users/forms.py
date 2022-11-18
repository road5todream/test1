from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
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
        }


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class': 'form-control'
    })
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': 'form-control',
        }),
    )
