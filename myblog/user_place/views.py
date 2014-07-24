from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from models import *
from forms import *
# from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.contrib import messages
# from collections import Counter


@login_required(login_url='/user/login')
def test_view(request):
    return HttpResponse("hello_world")


def login(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect("/blog/index")  # Redirect to a success page

        else:
            message = messages.error(request, 'Hatali yerler var')

    return render(request, 'Authentication/login.html',
                  {'login_form': form})


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