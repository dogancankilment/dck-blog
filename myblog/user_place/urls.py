from django.conf.urls import patterns, url
# from django.conf import settings

urlpatterns = patterns('',

    url(r'^test_view$',
        'user_place.views.test_view',
        name='test_view'),

    url(r'^login$',
        'user_place.views.login',
        name='login'),

    url(r'^signup$',
        'user_place.views.signup',
        name='signup'),

    url(r'^logout$',
        'user_place.views.logout',
        name='logout'),

    url(r'^sendmail$',
        'user_place.views.mail_sender_test',
        name='sendmail'),

)