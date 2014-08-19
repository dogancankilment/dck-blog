from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from .forms import *
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.context_processors import csrf
# from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from forms import *
# from django.core.urlresolvers import reverse


def index(request):  # blog_id

    blog_list = Post.objects.all()
    comment_list = Comments.objects.all()
    return render_to_response("index/blog_index.html",
                              {"blogs": blog_list,
                               "comments": comment_list,
                               "request": request})

@login_required(login_url='/user/login')
def new_post(request):
    # which_user = User.objects.filter(email=request.POST['username'])
    form = New_Post()
    if request.POST:
        form = New_Post(request.POST)

        if form.is_valid():
            post = Post(title=form.cleaned_data.get('title'),
                        content=form.cleaned_data.get('content'),
                        which_user=request.user)
            post.save()
            return HttpResponse("Basarili")
        else:
            return HttpResponse("Amk")

    c = {"form": form}
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
