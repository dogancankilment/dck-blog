from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="for_index")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    which_user = models.ForeignKey(User)


class Comments(models.Model):
    content = models.CharField(max_length=200)
    which_user = models.ForeignKey(User)
    which_post = models.ForeignKey(Post)