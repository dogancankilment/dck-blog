from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

from .util_mail_sender import mail_sender


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="email")
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_form(self):
        return self.cleaned_data


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        mail_sender.delay(user.email)
        user.is_active = False

        if commit:
            user.save()
        return user


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")