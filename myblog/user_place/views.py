import datetime

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate
from django.template import RequestContext

from main_site.views import index
from .util_token_generator import tokens_email, tokens_expire_date
from user_place.util_mail_sender import mail_sender
from user_place.forms import LoginForm, UserCreateForm
from .tasks import print_hello
from .models import User


@login_required()
def test_view(request):
    output = _("Welcome to my site.")
    print_hello.delay()  # trying tasks.py
    return HttpResponse(output)


@login_required()
def show_profile(request, template_name="user/user_profile.html"):
    user_profile = User.objects.get(id=request.user.id)

    return render_to_response(template_name,
                              {"user_profile": user_profile,
                               "request": request},
                              context_instance=RequestContext(request))


@login_required()
def edit_profile(request):
    return render_to_response('user/edit_profile.html',
                              {"request": request},
                              context_instance=RequestContext(request))


def my_login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user:
            if user.is_active:
                auth.login(request, user)

                return HttpResponseRedirect(reverse(index))  # Redirect to a success page

            else:
                messages.error(request,
                               'Lutfen Hesabinizi aktif ediniz.')
        else:
            messages.error(request,
                           'Boyle bir kullanici sistemde kayitli degil')

    return render(request, 'Authentication/login.html',
                  {'login_form': form})


def signup(request, template_name="Authentication/signup.html"):
    form = UserCreateForm(request.POST or None)

    if form.is_valid():
        if form.save():
            return HttpResponseRedirect(reverse(my_login))

        # like form validation error
        # but it's more short
        else:
            messages.error(request,
                           (_('Bu email adresi daha onceden alinmistir.')))

    return render(request, template_name,
                  {'form': form})


def activation(request, token_id, template_name="Authentication/activation.html"):
    if token_id:
        try:
            email_in_token = tokens_email(token_id)
        except TypeError:
            messages.error(request,
                           (_('Hatali aktivasyon kodu')))
            return render(request,
                          template_name)

        result = User.objects.filter(email=email_in_token).exists()

        if result:
            expire_date_in_token = tokens_expire_date(token_id)

            if str(expire_date_in_token) > str(datetime.datetime.today()):
                user = User.objects.get(email=email_in_token)
                user.is_active = True
                user.save()

                messages.success(request,
                                 (_('Hesabiniz aktif edilmistir. Lutfen giris yapiniz.')))

                return render(request,
                              template_name)

            else:
                mail_sender(email_in_token)
                messages.success(request, (_('Eski aktivasyon mailinin suresi bitmistir,'
                                             'yeni bir email yolladik,'
                                             'lutfen posta kutunuzu ziyaret ediniz.')))
                return render(request,
                              template_name)
        else:
            messages.success(request, (_('Eslesen email bulunamadi.')))
            return render(request,
                          template_name)
    else:
        messages.success(request, (_('Boyle bir token yoktur')))
        return render(request,
                      template_name)


@login_required()
def logout(request):
    auth.logout(request)
    return redirect(reverse(my_login))
