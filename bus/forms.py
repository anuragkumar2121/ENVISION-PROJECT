from django import forms
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NameForms(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='email', max_length=50)
    subject = forms.CharField(label='subject', max_length=100)
    message = forms. CharField(label='message', max_length=500)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

