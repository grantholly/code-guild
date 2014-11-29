from django.conf.urls import patterns, url

from blog.views import BlogIndex
from . import views

urlpatterns = patterns('',
    #blog urls
    url(r'^$', BlogIndex.as_view(), name='index'),
    url(r'(?P<pk>\d+)/$', views.blog_post_detail, name='detail'),
    url(r'vote/$', views.vote, name='vote'),
    url(r'add_comment/$', views.add_comment, name='add_comment'),
    url(r'get_comments/$', views.get_comments, name='get_comments'),
    url(r'search/$', views.search, name='search'),
)
