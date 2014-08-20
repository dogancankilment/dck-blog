from django import forms
from django.contrib.admindocs.tests import fields
from django.forms import ModelForm
from .models import Post


class New_Post(ModelForm):
    class Meta:
        model = Post