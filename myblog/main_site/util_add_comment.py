from django.shortcuts import get_object_or_404
from .models import Post, Comments
from celery import shared_task


@shared_task
def post_comments(request, post_id):
    # this comment making to post
    current_post = get_object_or_404(Post.objects.select_related(), pk=post_id)
    current_comment = None

    d = [current_post, current_comment]
    return d


@shared_task
def comments_comment(request, post_id):
    # this comment making to comment
    count = 0

    current_comment = get_object_or_404(Comments.objects.select_related(), pk=post_id)
    current_post = current_comment.content_object

    # end the while loop
    # post's, first comment found.
    # like reverse finder node -> root
    while current_post.content_type.name != "post":
        current_post = current_post.content_object
        count += count  # for tree view in template.

    current_post = current_post.content_object  # this line find which_post

    d = [current_post, current_comment, count]
    return d