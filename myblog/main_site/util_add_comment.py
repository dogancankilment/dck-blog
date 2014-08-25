from django.shortcuts import get_object_or_404
from .models import Post, Comments


def post_comments(request, post_id):
    # this comment making to post
    current_post = get_object_or_404(Post.objects.select_related(), pk=post_id)

    return current_post


def comments_comment(request, comment_id):
    # this comment making to comment
    count = 0
    current_comment = get_object_or_404(
        Comments.objects.select_related(),
        pk=comment_id)

    current_post = current_comment.parent_object

    # end the while loop
    # post's, first comment found.
    # like reverse finder node -> root
    while current_post.content_type.name != "post":
        current_post = current_post.parent_object
        count += count  # for tree view in template.

    current_post = current_post.parent_object  # this line find which_post

    return current_comment