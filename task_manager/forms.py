from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    repeat_password = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['repeat_password']


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput
    )
