from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from forms import *
from models import *
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib import messages
from django.utils.translation import ugettext as _
from main_site.views import index
from user_place.util_mail_sender import mail_sender
from util_token_generator import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from user_place.forms import *
from django.template import RequestContext


import datetime


@login_required(login_url='/user/login')
def test_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)


def my_login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user:
            auth.login(request, user)

            return HttpResponseRedirect(reverse(index))  # Redirect to a success page

        else:
            messages.error(request, 'Hatali yerler var')

    return render(request, 'Authentication/login.html',
                  {'login_form': form})


def signup(request, template_name="Authentication/signup.html"):
    form = UserCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(my_login))

    return render_to_response(template_name,
                              {"form": form},
                              context_instance=RequestContext(request))


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
    return redirect(reverse(my_login))
