from django.conf.urls import patterns, include, url
# from django.conf import settings

urlpatterns = patterns('',

    url(r'^test_view/$', 'user_place.views.test_view', name='test_view'),


)