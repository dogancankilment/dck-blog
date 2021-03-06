from django.conf.urls import patterns, url
# from django.conf import settings

urlpatterns = patterns('',
                       url(r'^login$',
                           'user_place.views.my_login',
                           name='my_login'),

                       url(r'^signup$',
                           'user_place.views.signup',
                           name='signup'),

                       url(r'^logout$',
                           'user_place.views.logout',
                           name='logout'),

                       url(r'^show_profile$',
                           'user_place.views.show_profile',
                           name='show_profile'),

                       url(r'^edit_profile$',
                           'user_place.views.edit_profile',
                           name='edit_profile'),

                       url(r'^activation/(?P<token_id>.*)',
                           'user_place.views.activation',
                           name='activation'),

                       url(r'^freeze_success',
                           'user_place.views.freeze_account',
                           name='freeze_account'),

                       )