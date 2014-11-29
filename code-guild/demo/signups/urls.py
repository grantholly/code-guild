from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    #signup urls
    url(r'^$', views.signup, name='index'),
)
