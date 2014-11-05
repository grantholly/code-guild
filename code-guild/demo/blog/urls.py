from django.conf.urls import patterns, url

from .blog import views

urlpatterns = patterns('',
    #blog urls
    url(r'^$', views.blog_index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^(?P<pk>\d+)', views.detail, name='detail'),
)
