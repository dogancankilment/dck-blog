from django.conf.urls import patterns, url
# from django.conf import settings

urlpatterns = patterns('',
                       url(r'^test_view$',
                           'user_place.views.test_view',
                           name='test_view'),

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

                       url(r'^activation/(?P<token_id>.*)',
                           'user_place.views.activation',
                           name='activation'),
                       )