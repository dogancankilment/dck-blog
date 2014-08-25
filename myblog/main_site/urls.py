from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^index$',
                           'main_site.views.index',
                           name='main_site.index'),

                       url(r'^new_post$',
                           'main_site.views.new_post',
                           name='new_post'),

                       url(r'^single_post/(?P<id>\w+)',
                           'main_site.views.single_post',
                            name='single_post'),

                       url(r'^edit_post/(?P<id>\w+)',
                           'main_site.views.edit_post',
                            name='edit_post'),

                       url(r'^new_comment/(?P<post_id>\w+)/(?P<comment_id>\w+)$',
                           'main_site.views.new_comment',
                           name='new_comment'),

)