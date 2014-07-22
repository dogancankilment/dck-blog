from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    which_user = models.ForeignKey(User)

class UserProfile(models.Model):
    user = models.OneToOneField(User)