from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from models import *
# from django.core.context_processors import csrf
# from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from forms import *
from django.core.urlresolvers import reverse


@login_required(login_url='/user/login')
# @login_required(reverse(login))
def index(request):  # blog_id

    blog_list = Post.objects.all()
    comment_list = Comments.objects.all()
    return render_to_response("index/blog_index.html",
                              {"blogs": blog_list,
                               "comments": comment_list,
                               "request": request})


def my_custom_404(request, template_name='404.html'):

    #404 error handler. Templates: `404.html' Context: None
    return render_to_response(template_name,
                              context_instance=RequestContext(request))


def my_custom_500(request, template_name='500.html'):

    #500 error handler. Templates: `500.html' Context: None
    return render_to_response(template_name,
                              context_instance=RequestContext(request))
