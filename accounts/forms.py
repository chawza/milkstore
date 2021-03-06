from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Account username', max_length=255)
    password = forms.CharField(label='Account password', max_length=255, widget=forms.PasswordInput())

    def user_is_exist(self):
        try:
            User.objects.get(username=self.data['username'])
            return True
        except User.DoesNotExist:
            return False

    def login_correct(self):
        user = User.objects.get(username=self.data["username"])
        if user.password == self.data["password"]:
            return True
        else:
            # print(user.password, self.data["password"])
            return False

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def is_exist(self):
        try:
            User.objects.get(username=self.data['username'])
            return True
        except User.DoesNotExist:
            return False

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
        user = User.objects.create(
            username=self.data['username']
        )
        user.set_password(self.data['password1'])
        user.save()
        print('${user.username} has been added!')

class EditProfile(forms.Form):
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Address')
    cardnumber = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Cardnumber')
    email = forms.CharField(required=False, widget=forms.EmailInput(attrs={'class' : 'form-control'}), label='Email')