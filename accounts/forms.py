from django import forms
from .models import Account

class LoginForm(forms.Form):
    username = forms.CharField(label='Account username', max_length=255)
    password = forms.CharField(label='Account password', max_length=255, widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=255)
    password1 = forms.CharField(label='password', max_length=255, widget=forms.PasswordInput())
    password2 = forms.CharField(label='retype password', max_length=255, widget=forms.PasswordInput())

    def validate_password(self):
        if self.data['password1'] == self.data['password2']:
            return True
        else:
            return False

    def save(self):
        Account.objects.create(
            username=self.data['username'],
            password=self.data['password1']
        )
        print('${self.username} has been added!')