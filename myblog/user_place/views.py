from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from models import *
from forms import *
# from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth

@login_required(login_url='/user/login')
def test_view(request):
    return HttpResponse("hello_world")

def login(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/blog/index")  # Redirect to a success page
    return render(request, 'Authentication/login.html', {'login_form': form})

# geri gelinecek kullanici girisi kismina
def signup(request):
    if request.method != "POST":
        c = {}
        c.update(csrf(request))
        return render_to_response('Authentication/signup.html',c)
    else:
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/blog/index')

@login_required(login_url='/user/login')
def logout(request):
    auth.logout(request)
    return redirect('/user/login')