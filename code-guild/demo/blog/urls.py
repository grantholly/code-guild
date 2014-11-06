from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    #blog urls
    url(r'^$', views.BlogIndex.as_view(), name='index'),
)
