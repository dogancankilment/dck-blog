from django.conf.urls import patterns, include, url
# from django.conf import settings

urlpatterns = patterns('',

    url(r'^index$',
        'main_site.views.index',
        name='main_site.index'),

    url(r'^new_post$',
        'main_site.views.new_post'),
)