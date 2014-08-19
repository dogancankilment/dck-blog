from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    which_user = models.ForeignKey(User)
    # image = models.ImageField()

    comments = GenericRelation('Comments')


class Comments(models.Model):
    which_user = models.ForeignKey(User)
    content = models.CharField(max_length=200)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    parent_object = GenericForeignKey('content_type', 'object_id')

    # comment's comment's comment's comment..
    comments = GenericRelation('Comments')