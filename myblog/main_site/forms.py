from django.forms import ModelForm
from .models import Post, Comments
from user_place.util_image_resizer import image_resizer



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
        exclude = ['created_at', 'which_user']

    def save(self, root, user):
        comment = Comments(content=self.cleaned_data["name"],
                           which_user=user,
                           content_object=root)
        comment.save()
