# from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           'main_site.views.index',
                           name='index'),

                       url(r'^user/',
                           include('user_place.urls')),

                       url(r'^blog/',
                           include('main_site.urls')),

                       url(r'^admin/',
                           include(admin.site.urls)),
                       )

handler404 = 'main_site.views.my_custom_404'
handler500 = 'main_site.views.my_custom_500'