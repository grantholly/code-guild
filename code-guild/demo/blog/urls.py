from django.conf.urls import patterns, url

from blog.views import BlogIndex

urlpatterns = patterns('',
    #blog urls
    url(r'^$', BlogIndex.as_view(), name='index'),
    url(r'vote/$', 'blog.views.vote', name='vote'),
    url(r'add_comment/$', 'blog.views.add_comment', name='add_comment'),
    url(r'get_comments/$', 'blog.views.get_comments', name='get_comments'),
    url(r'search/$', 'blog.views.search', name='search'),
)
