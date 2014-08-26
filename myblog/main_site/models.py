from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    which_user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/images/blog_posts/',
                              default='static/images/blog_posts/default.jpg')

    comments = GenericRelation('Comments')

    class Meta:
        ordering = ['-updated_at']


class Comments(models.Model):
    which_user = models.ForeignKey(User)
    content = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    parent_object = GenericForeignKey('content_type', 'object_id')

    # comment's comment's comment's comment..
    comments = GenericRelation('Comments')

    class Meta:
        ordering = ['-created_at']