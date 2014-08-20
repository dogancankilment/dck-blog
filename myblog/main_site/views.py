from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from .forms import *
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from forms import *
# from django.core.urlresolvers import reverse


def index(request):  # blog_id
    blog_list = Post.objects.all()
    comment_list = Comments.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')

    try:
        post_count = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_count = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_count = paginator.page(paginator.num_pages)

    return render_to_response("index/blog_index.html",
                              {"blogs": blog_list,
                               "comments": comment_list,
                               "request": request,
                               "post_count": post_count})


def single_post(request, id):
    post = Post.objects.get(id=id)
    return render_to_response("post/single_post.html",
                              {"post": post,
                               "request": request})


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.POST:
        form = New_Post(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data.get('title')
            post.content = form.cleaned_data.get('content')
            post.which_user = post.which_user
            post.save()

            return redirect(reverse(index))

    else:
        form = New_Post(initial={'title': post.title,
                                 'content': post.content,
                                 'which_user': post.which_user})

    c = {"form": form, "id": post.id}
    c.update(csrf(request))
    return render_to_response('post/edit_post.html',c)


@login_required()
def new_post(request):
    if request.POST:
        form = New_Post(request.POST, request.FILES)

        if form.is_valid():
            form.save(request.user)
            return HttpResponse("Success")

        else:
            return HttpResponse("form is not valid")

    else:
        form = New_Post()
        c = {"form": form, "request": request}
        c.update(csrf(request))

        return render_to_response("post/new_post.html",
                                  c)


def my_custom_404(request, template_name='404.html'):
    #  404 error handler. Templates: `404.html' Context: None
    return render_to_response(template_name,
                              context_instance=RequestContext(request))


def my_custom_500(request, template_name='500.html'):
    #  500 error handler. Templates: `500.html' Context: None
    return render_to_response(template_name,
                              context_instance=RequestContext(request))
