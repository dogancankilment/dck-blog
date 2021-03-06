from django.forms import ModelForm, forms
from .models import Post, Comments
from utils.util_image_resizer import image_resizer
from utils.util_mail_sender import mail_sender
from user_place.models import User

import uuid


class New_Post(ModelForm):
    class Meta:
        model = Post
        exclude = ['which_user']

    def save(self, user):
        post = Post()
        post.title = self.cleaned_data.get('title')
        post.content = self.cleaned_data.get('content')
        post.which_user = user
        post.image = self.cleaned_data.get('image')
        post.save()
        image_resizer.delay(post.image.url)


class New_Comment(ModelForm):
    class Meta:
        model = Comments
        exclude = ['created_at',
                   'which_user',
                   'content_type',
                   'object_id',
                   'email']

    def save(self, root, user):
        comment = Comments(content=self.cleaned_data["content"],
                           which_user=user,
                           parent_object=root,
                           email=user.email)
        comment.is_visible = True
        comment.save()


class New_Comment_Anonymous(ModelForm):
    class Meta:
        model = Comments
        exclude = ['creatad_at',
                   'which_user',
                   'content_type',
                   'object_id']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def save(self, root):
        comment = Comments(content=self.cleaned_data["content"],
                           parent_object=root,
                           which_user=User.objects.create_user(uuid.uuid4(),
                                                               self.cleaned_data["email"]),
                           email=self.cleaned_data["email"])

        comment.is_visible = False
        comment.save()
        mail_sender.delay(comment.email, "comment_activation")


