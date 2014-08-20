from django import forms
from django.contrib.admindocs.tests import fields
from django.forms import ModelForm
from .models import Post


class New_Post(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()