from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.conf import settings

#class LoginForm():

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        return self.cleaned_data

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
          raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data