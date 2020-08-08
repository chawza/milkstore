from django import forms

class DateInput(forms.DateInput):   #modify the date input widget so we can pick the date than input on text field
    input_type = 'date'

class LoginForm(forms.Form):
    username = forms.CharField(label='Account username', max_length=32)
    password = forms.CharField(label='Account password', max_length=32, widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(label='Account username', max_length=32)
    password = forms.CharField(label='Account password', max_length=32, widget=forms.PasswordInput())