from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from forms import *
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib import messages
from django.utils.translation import ugettext as _
from main_site.views import index
from user_place.mail_sender import mail_sender
from token_generator import *

import datetime


@login_required(login_url='/user/login')
def test_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)


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


def activation(request, token_id):
    if token_id:
        email_in_token = tokens_email(token_id)
        result = User.objects.filter(email=email_in_token).exists()

        if result:
            expire_date_in_token = tokens_expire_date(token_id)

            if str(expire_date_in_token) > str(datetime.datetime.today()):
                return HttpResponse(_("Basarili bir sekilde aktif ettiniz"))

            else:
                mail_sender(email_in_token)

                return HttpResponse(_("Eski aktivasyon mailinin suresi bitmistir,"
                                    "yeni bir email yolladik,"
                                    "lutfen posta kutunuzu ziyaret ediniz."))

        else:
            return HttpResponse(_("Eslesen email bulunamadi"))
    else:

        return HttpResponse(_("Boyle bir token yoktur"))


@login_required(login_url='/user/login')
def logout(request):
    auth.logout(request)
    return redirect(reverse(login))