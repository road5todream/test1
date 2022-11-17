from django.contrib.auth.forms import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    repeat_password = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['repeat_password']


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

