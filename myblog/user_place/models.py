from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="created_by_user")
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images/user_profile/',
                              default='static/images/user_profile/default_profile.jpg')

    def __unicode__(self):
        return self.user