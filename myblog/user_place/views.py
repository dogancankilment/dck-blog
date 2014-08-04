from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from forms import *
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib import messages
from django.utils.translation import ugettext as _
from main_site.views import *

import smtplib
import os


@login_required(login_url='/user/login')
def test_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
    # return HttpResponse("hello_world")


def mail_sender_test(request):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # take password variable from .bashrc file
    mail_pass = str(os.getenv("MAIL_PASS"))
    server.login('surveydck@gmail.com', mail_pass)

    server.sendmail('surveydck@gmail.com',
                    'dogancankilment@gmail.com',
                    'my mail content is DCK was here')

    return HttpResponse("Mailiniz gonderildi")


def login(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect(reverse(index))  # Redirect to a success page

        else:
            messages.error(request, 'Hatali yerler var')

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

        return redirect(reverse(index))


@login_required(login_url='/user/login')
def logout(request):
    auth.logout(request)
    return redirect(reverse(login))