from django.conf.urls import patterns, url

from blog.views import BlogIndex

urlpatterns = patterns('',
    #blog urls
    url(r'^$', BlogIndex.as_view(), name='index'),
)
