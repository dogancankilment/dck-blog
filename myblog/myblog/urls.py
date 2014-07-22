from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    url(r'^user/', include('user_place.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'blog_workshop.views.my_custom_404'
handler500 = 'blog_workshop.views.my_custom_500'