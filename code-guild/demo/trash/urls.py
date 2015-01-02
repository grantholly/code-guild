from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.trash_index, name='index'),
)

